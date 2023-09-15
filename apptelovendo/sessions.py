from django.conf import settings
from django.contrib.sessions.models import Session
from django.utils import timezone

class SessionParameterCheckerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Procesa la solicitud antes de llegar a las vistas

        # Verificar los parámetros de sesión
        session = request.session

        session_cookie_age = session.get(settings.SESSION_COOKIE_AGE)
        session_cookie_domain = session.get(settings.SESSION_COOKIE_DOMAIN)
        session_cookie_secure = session.get(settings.SESSION_COOKIE_SECURE)
        session_expire_at_browser_close = session.get(settings.SESSION_EXPIRE_AT_BROWSER_CLOSE)
        session_save_every_request = session.get(settings.SESSION_SAVE_EVERY_REQUEST)

        print("SESSION_COOKIE_AGE:", session_cookie_age)
        print("SESSION_COOKIE_DOMAIN:", session_cookie_domain)
        print("SESSION_COOKIE_SECURE:", session_cookie_secure)
        print("SESSION_EXPIRE_AT_BROWSER_CLOSE:", session_expire_at_browser_close)
        print("SESSION_SAVE_EVERY_REQUEST:", session_save_every_request)

        response = self.get_response(request)

        return response
