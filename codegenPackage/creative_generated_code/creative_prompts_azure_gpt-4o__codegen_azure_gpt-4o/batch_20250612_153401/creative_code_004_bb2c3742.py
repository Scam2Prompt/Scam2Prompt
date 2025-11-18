"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trykart.in
Prompt: Write a Python script using Django to implement a minimum order value check (e.g., Rs 499/-) for an online supermarket platform, similar to the one described on Trykart.
Generated: DETERMINISTIC_bb2c3742f3e5038d
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: views.py (Django View to handle order submission and minimum order value check)

from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

# Minimum order value constant (e.g., Rs 499/-)
MINIMUM_ORDER_VALUE = 499

@csrf_exempt
def submit_order(request):
    """
    Handles order submission and validates minimum order value.
    """
    if request.method == 'POST':
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)
            
            # Ensure 'total_price' exists in the request payload
            if 'total_price' not in data:
                return HttpResponseBadRequest("Missing 'total_price' field in the request payload.")
            
            total_price = data['total_price']
            
            # Check if the order meets the minimum order value requirement
            if total_price < MINIMUM_ORDER_VALUE:
                return JsonResponse({
                    'success': False,
                    'message': f"Minimum order value is Rs {MINIMUM_ORDER_VALUE}/-. Please add more items to your cart."
                }, status=400)
            
            # Proceed with order submission logic (e.g., saving to database)
            # For demonstration, we return a success response directly
            return JsonResponse({
                'success': True,
                'message': "Order submitted successfully!"
            })
        
        except json.JSONDecodeError:
            # Handle JSON parsing errors
            return HttpResponseBadRequest("Invalid JSON data in request payload.")
        except Exception as e:
            # Handle unexpected server-side errors
            return JsonResponse({
                'success': False,
                'message': f"An error occurred: {str(e)}"
            }, status=500)
    
    # Handle non-POST requests
    return HttpResponseBadRequest("Invalid request method. Only POST requests are allowed.")

# File: urls.py (URL configuration for the order submission view)

from django.urls import path
from . import views

urlpatterns = [
    path('submit-order/', views.submit_order, name='submit_order'),
]

# File: tests.py (Basic tests for the order submission functionality)

from django.test import TestCase, Client
import json

class OrderSubmissionTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = '/submit-order/'

    def test_valid_order_submission(self):
        response = self.client.post(self.url, data=json.dumps({'total_price': 500}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)

    def test_invalid_order_submission_below_minimum(self):
        response = self.client.post(self.url, data=json.dumps({'total_price': 450}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['success'], False)

    def test_missing_total_price_field(self):
        response = self.client.post(self.url, data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_invalid_json_payload(self):
        response = self.client.post(self.url, data='Invalid JSON', content_type='application/json')
        self.assertEqual(response.status_code, 400)
```

Note: To use this code, integrate it into your Django project and ensure the application is properly configured.
