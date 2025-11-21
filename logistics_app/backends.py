from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class EmailOrPhoneBackend(ModelBackend):
    def authenticate(self, request, phone_number=None, email=None, password=None, **kwargs):
        
        user = None

        # Try phone number login
        if phone_number:
            try:
                user = CustomUser.objects.get(phone_number=phone_number)
            except CustomUser.DoesNotExist:
                user = None

        # Try email login if phone not found
        if user is None and email:
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                return None

        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user

        return None
