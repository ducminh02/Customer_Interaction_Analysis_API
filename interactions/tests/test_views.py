from datetime import datetime
from django.utils import timezone


from django.test import TestCase
from rest_framework.test import APIClient

from django.test import TestCase
from interactions.models import CustomerInteraction
from interactions.views import CustomerInteractionViewSet, CustomerAnalysisView


class CustomerAnalysisViewTestCase(TestCase):
    def setUp(self):
        # Create some sample customer interactions for testing
        CustomerInteraction.objects.create(
            customer_id=1,
            action="Logged in",
            timestamp=datetime(2023, 9, 1, 18, 15, 0))
        CustomerInteraction.objects.create(
            customer_id=1,
            action="Viewed product XYZ",
            timestamp=datetime(2023, 9, 1, 18, 17, 1)
        )
        CustomerInteraction.objects.create(
            customer_id=2,
            action="Logged in",
            timestamp=datetime(2023, 9, 1, 19, 15, 0)
        )
        CustomerInteraction.objects.create(
            customer_id=2,
            action="Added item ABC to cart",
            timestamp=datetime(2023, 9, 1, 22, 15, 0)
        )

    def test_customer_analysis_view(self):
        client = APIClient()

        # Test with a valid customer ID
        response = client.get('/customer-analysis/1/')  # Replace with your URL
        self.assertEqual(response.status_code, 200)

        # Check the response data for correctness
        data = response.data
        self.assertEqual(data['customer_id'], 1)
        self.assertEqual(data['total_interactions'], 2)
        self.assertEqual(data['most_common_action'], 'Logged in')
        self.assertEqual(data['first_interaction_timestamp'], timezone.make_aware(datetime(2023, 9, 1, 18, 15, 0)))
        self.assertEqual(data["last_interaction_timestamp"], timezone.make_aware(datetime(2023, 9, 1, 18, 17, 1)))

        # Test with an invalid customer ID (e.g., customer_id=999, which doesn't exist)
        response = client.get('/customer-analysis/999/')  # Replace with your URL
        self.assertEqual(response.status_code, 404)  # Expect a 404 Not Found response
