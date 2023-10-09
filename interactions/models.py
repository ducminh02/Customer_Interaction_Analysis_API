from django.db import models
from django.utils import timezone


class CustomerInteraction(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    customer_id = models.IntegerField()
    action = models.CharField(max_length=255)

    class Meta:
        app_label = 'interactions'

    def save(self, *args, **kwargs):
        # Ensure the timestamp is in the correct time zone before saving
        self.timestamp = timezone.make_aware(self.timestamp)
        super().save(*args, **kwargs)
