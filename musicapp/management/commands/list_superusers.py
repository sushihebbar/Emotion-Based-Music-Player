# your_app/management/commands/list_superusers.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'List superusers in the system.'

    def handle(self, *args, **options):
        superusers = User.objects.filter(is_superuser=True)

        if superusers:
            self.stdout.write(self.style.SUCCESS("Superusers in the system:"))
            for superuser in superusers:
                self.stdout.write(superuser.username)
        else:
            self.stdout.write(self.style.SUCCESS("No superusers found in the system."))
