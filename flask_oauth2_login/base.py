from flask import request, session, url_for
from requests_oauthlib import OAuth2Session


class OAuth2Login(object):

  def __init__(self, app=None):
    if app:
      self.init_app(app)
      self.app = app

  def get_config(self, app, name, default_value=None):
    return app.config.get(self.config_prefix + name, default_value)

  def init_app(self, app):
    self.client_id = self.get_config(app, "CLIENT_ID")
    self.client_secret = self.get_config(app, "CLIENT_SECRET")
    self.scope = self.get_config(app, "SCOPE", self.default_scope).split(",")
    self.redirect_scheme = self.get_config(app, "REDIRECT_SCHEME", "https")

    app.add_url_rule(
      self.get_config(app, "REDIRECT_PATH", self.default_redirect_path),
      self.redirect_endpoint,
      self.login,
    )

  @property
  def redirect_uri(self):
    return url_for(
      self.redirect_endpoint,
      _external=True,
      _scheme=self.redirect_scheme,
    )

  def session(self):
    return OAuth2Session(
      self.client_id,
      redirect_uri=self.redirect_uri,
      scope=self.scope,
    )

  def authorization_url(self, **kwargs):
    sess = self.session()
    auth_url, state = sess.authorization_url(self.auth_url, **kwargs)
    session[self.state_session_key] = state
    return auth_url

  def login(self):
    sess = self.session()

    # Get token
    try:
      sess.fetch_token(
        self.token_url,
        code=request.args["code"],
        client_secret=self.client_secret,
      )
      # TODO: Check state
    except Warning:
      # Ignore warnings
      pass
    except Exception as e:
      return self.login_failure_func(e)

    # Get profile
    try:
      profile = self.get_profile(sess)
    except Exception as e:
      return self.login_failure_func(e)

    return self.login_success_func(sess.token, profile)

  def login_success(self, f):
    self.login_success_func = f
    return f

  def login_failure(self, f):
    self.login_failure_func = f
    return f

  def get_profile(self, sess):
    raise NotImplementedError

