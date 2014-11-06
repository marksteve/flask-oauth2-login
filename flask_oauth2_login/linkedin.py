from .base import OAuth2Login


class LinkedIn(OAuth2Login):

  config_prefix = "LINKEDIN_LOGIN"
  redirect_endpoint = "_linkedin_login"
  state_session_key = "_linkedin_login_state"

  default_scope = (
    "r_basicprofile",
    "r_emailaddress",
  )
  default_redirect_path = "/login/linkedin"

  auth_url = "https://www.linkedin.com/uas/oauth2/authorization"
  token_url = "https://www.linkedin.com/uas/oauth2/accessToken"
  profile_url = "https://api.linkedin.com/v1/people/~"

  def get_profile(self, sess):
    resp = sess.get(self.profile_url)
    resp.raise_for_status()
    return resp.json()

