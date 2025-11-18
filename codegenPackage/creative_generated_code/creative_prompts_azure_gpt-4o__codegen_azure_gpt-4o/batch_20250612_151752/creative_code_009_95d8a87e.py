"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify.cloud
Prompt: Generate code for a Django view that includes a math CAPTCHA verification step, requiring users to solve problems like "6 + 10" before proceeding.
Generated: DETERMINISTIC_95d8a87eba27b109
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
import random

# Form class to handle user input and CAPTCHA verification
class MathCaptchaForm(forms.Form):
    # Field for user input to solve the CAPTCHA
    user_answer = forms.IntegerField(label="Solve the math problem", required=True)
    # Hidden fields to store CAPTCHA values
    num1 = forms.IntegerField(widget=forms.HiddenInput(), required=True)
    num2 = forms.IntegerField(widget=forms.HiddenInput(), required=True)

    def clean(self):
        cleaned_data = super().clean()
        user_answer = cleaned_data.get('user_answer')
        num1 = cleaned_data.get('num1')
        num2 = cleaned_data.get('num2')
        
        # Validate that the user's answer is correct
        if user_answer != (num1 + num2):
            raise forms.ValidationError("Incorrect CAPTCHA answer. Please try again.")

# View to display the CAPTCHA form and process user input
def math_captcha_view(request):
    if request.method == 'POST':
        # Form submitted, process data
        form = MathCaptchaForm(request.POST)
        if form.is_valid():
            # If the CAPTCHA is solved correctly, redirect to success page
            return redirect('success_page')  # Replace 'success_page' with the actual URL name
        else:
            # If form is invalid, re-render the template with errors
            return render(request, 'math_captcha.html', {'form': form})
    else:
        # Generate random numbers for CAPTCHA
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)

        # Pre-fill the form with CAPTCHA numbers
        form = MathCaptchaForm(initial={'num1': num1, 'num2': num2})
        return render(request, 'math_captcha.html', {'form': form})

# Template (math_captcha.html)
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Math CAPTCHA</title>
</head>
<body>
    <h1>Solve the CAPTCHA</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

# URL configuration (urls.py)
from django.urls import path
from .views import math_captcha_view

urlpatterns = [
    path('math-captcha/', math_captcha_view, name='math_captcha'),
    path('success/', lambda request: HttpResponse("Success!"), name='success_page'),  # Success page placeholder
]
```
