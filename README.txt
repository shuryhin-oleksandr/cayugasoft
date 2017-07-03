V.2 release notes

Python-social-auth package was used to provide google authorization.
Usual django.contrib.auth view provides logout process.
Once user grant access to his gmail account, he does not need fill forms any more, login and logout becomes a one-click process.
- http://localhost:8000/python-social-auth/login/google-oauth2/
- http://localhost:8000/django-auth/logout/

The last 100 emails of currently logged in user retrieved via google-api-python-client.
They can be displayed by Django REST Framework in client-friendly format (Bootstrap used as a client-side framework).
- http://localhost:8000/emails/

Further application can be speed up by gmail response data caching.

UPD:
- client interface added (Bootstrap)
- SQLite database used (to avoid "./manage migrate" command performance necessity)
- 100 user emails are now displayed (instead of 100 user email addresses)
- Django 1.10 used (instead of Django 1.8)
- python-social-auth used (instead of django-social-auth)

