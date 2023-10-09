from django.test import TestCase
from django.urls import reverse, resolve
from interactions.views import CustomerInteractionViewSet, CustomerAnalysisView


class TestUrls(TestCase):
    def test_customer_interaction_list_url(self):
        # Get the URL for the customer interaction list view using the router
        url = reverse('customerinteraction-list')

        # Resolve the URL to a view function and check if it's associated with the expected view
        view = resolve(url)
        self.assertEqual(view.func.cls, CustomerInteractionViewSet)

    def test_customer_analysis_url(self):
        # Create a sample customer ID for testing
        customer_id = 1

        # Get the URL for the customer analysis view with the customer ID
        url = reverse('customer-analysis', args=[customer_id])

        view = resolve(url)
        self.assertEqual(view.func.cls, CustomerAnalysisView)