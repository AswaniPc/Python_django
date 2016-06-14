from __future__ import unicode_literals

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
    verbose_name = "accounts"

    def ready(self):
        import accounts.signals # import your signals.py
