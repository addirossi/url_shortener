from string import ascii_letters, digits

from django.utils.crypto import get_random_string
from django.db import models


class Shortener(models.Model):
    full_url = models.URLField()
    short_url = models.CharField(max_length=20, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.full_url} to {self.short_url}'

    @staticmethod
    def create_random_code():
        available_chars = ascii_letters + digits
        code = get_random_string(7, available_chars)
        return code

    def create_shortened_url(self):
        random_code = self.create_random_code()
        if self.__class__.objects.filter(short_url=random_code).exists():
            return self.create_shortened_url()
        return random_code

    def save(self, *args, **kwargs) -> None:
        if not self.short_url:
            self.short_url = self.create_shortened_url()
        return super().save(*args, **kwargs)
