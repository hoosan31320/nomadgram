from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, URLField, TextField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for nomadgram.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not specified')
    )

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    website = URLField(null=True)
    bio = TextField(null=True)
    phone = CharField(max_length=140, null=True)
    gender = CharField(max_length=80, choices=GENDER_CHOICES, null=True)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
