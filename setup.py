from setuptools import setup, find_packages


if __name__ == "__main__":
  setup(
    name="Flask-OAuth2-Login",
    version="0.0.8",
    packages=find_packages(),
    install_requires=[
      "requests",
      "requests-oauthlib",
    ],
    author="Mark Steve Samson",
    author_email="hello@marksteve.com",
    description="Simple OAuth2 login",
    license="MIT",
    url="https://github.com/marksteve/flask-oauth2-login",
  )
