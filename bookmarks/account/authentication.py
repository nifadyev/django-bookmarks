from django.contrib.auth.models import User


class EmailAuthBackend():
    """Authenticate using an e-mail address."""

    def authenticate(self, _request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            return user if user.check_password(password) else None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
