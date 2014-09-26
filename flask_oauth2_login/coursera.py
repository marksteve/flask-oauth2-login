from .base import OAuth2Login


class CourseraLogin(OAuth2Login):

  config_prefix = "COURSERA_LOGIN_"
  redirect_endpoint = "_coursera_login"
  state_session_key = "_coursera_login_state"

  default_scope = "view_profile"
  default_redirect_path = "/login/coursera"

  auth_url = "https://accounts.coursera.org/oauth2/v1/auth"
  token_url = "https://accounts.coursera.org/oauth2/v1/token"
  profile_url = "https://api.coursera.org/api/externalBasicProfiles.v1"

  def get_profile(self, sess):
    resp = sess.get(
      self.profile_url,
      params=dict(
        q="me",
        fields=",".join([
          "name",
        ]),
      )
    )
    resp.raise_for_status()
    return resp.json()["elements"][0]

