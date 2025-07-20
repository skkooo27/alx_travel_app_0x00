# listings/urls.py
from django.urls import path
from django.http import JsonResponse

def test_view(request):
    return JsonResponse({"message": "Listings API works!"})

urlpatterns = [
    path('', test_view),
]
