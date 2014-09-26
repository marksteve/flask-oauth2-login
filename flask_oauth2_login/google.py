from .base import OAuth2Login


class GoogleLogin(OAuth2Login):

  config_prefix = "GOOGLE_LOGIN_"
  redirect_endpoint = "_google_login"
  state_session_key = "_google_login_state"

  default_scope = (
    "https://www.googleapis.com/auth/userinfo.email,"
    "https://www.googleapis.com/auth/userinfo.profile"
  )
  default_redirect_path = "/login/google"

  auth_url = "https://accounts.google.com/o/oauth2/auth"
  token_url = "https://accounts.google.com/o/oauth2/token"
  profile_url = "https://www.googleapis.com/oauth2/v2/userinfo"

  def get_profile(self, sess):
    resp = sess.get(self.profile_url)
    # FIXME: Check `error` key
    resp.raise_for_status()
    return resp.json()

