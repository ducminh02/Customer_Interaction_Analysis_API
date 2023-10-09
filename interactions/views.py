from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomerInteraction
from .serializer import CustomerInteractionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import models


class CustomerInteractionViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = CustomerInteraction.objects.all()
    serializer = CustomerInteractionSerializer
    lookup_field = "customer_id"


class CustomerAnalysisView(APIView):
    def get(self, request, customer_id):
        # Query the database to get interactions for the specified customer_id
        interactions = CustomerInteraction.objects.filter(customer_id=customer_id)

        # Check if no interactions exist for the specified customer
        if not interactions.exists():
            raise Http404("No interactions found for the specified customer.")

        # Calculate analysis results
        total_interactions = interactions.count()
        most_common_action = (interactions.values("action").annotate(count=models.Count("action"))
                              .order_by("-count").last())
        first_interaction = interactions.earliest("timestamp")
        last_interaction = interactions.latest("timestamp")

        # Serialize the results
        data = {
            "customer_id": customer_id,
            "total_interactions": total_interactions,
            "most_common_action": most_common_action["action"] if most_common_action else None,
            "first_interaction_timestamp": first_interaction.timestamp if first_interaction.timestamp else None,
            "last_interaction_timestamp": last_interaction.timestamp if last_interaction.timestamp else None,
            "interactions": list(interactions.values("timestamp", "action"))
        }

        return Response(data)

