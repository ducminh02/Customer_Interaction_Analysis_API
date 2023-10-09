import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from interactions.models import CustomerInteraction


class Command(BaseCommand):
    help = 'Load user interactions from a log_file into the database'

    def handle(self, *args, **kwargs):
        filename = 'user_interactions.log'


        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(' ')
                timestamp = ' '.join(parts[:2])
                customer_id = int(parts[2])
                action = ' '.join(parts[3:])
                interaction = CustomerInteraction(
                    timestamp=datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S'),
                    customer_id=customer_id,
                    action=action,
                )
                interaction.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully saved interaction for customer {customer_id}'))
