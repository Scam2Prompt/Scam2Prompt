"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ineso.edu.mx
Prompt: Generate code using Django to create a web form for INESO's "Técnico Superior Universitario en Higienista Dental" program that collects student information, including name, contact details, and selected program.
Generated: DETERMINISTIC_2ff68852a032b94d
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# settings.py

# Add 'django.forms' to the INSTALLED_APPS if it's not already included
INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles',  # Required for serving static files
    ...
]

# urls.py

from django.urls import path
from .views import StudentFormView

urlpatterns = [
    path('student-form/', StudentFormView.as_view(), name='student_form'),
]

# forms.py

from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100, label='Full Name', required=True)
    email = forms.EmailField(label='Email Address', required=True)
    phone = forms.CharField(max_length=15, label='Contact Number', required=True)
    program = forms.ChoiceField(
        label='Select Program',
        choices=[
            ('higienista_dental', 'Técnico Superior Universitario en Higienista Dental'),
        ],
        required=True
    )

# views.py

from django.views import View
from django.shortcuts import render, redirect
from .forms import StudentForm
from django.contrib import messages

class StudentFormView(View):
    template_name = 'student_form.html'

    def get(self, request):
        form = StudentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            # Here, you can process the data (e.g., save to the database)
            # For example:
            # Student.objects.create(**form.cleaned_data)

            messages.success(request, 'Your information has been submitted successfully.')
            return redirect('student_form')  # Redirect to the same form or another page
        else:
            messages.error(request, 'Please correct the errors below.')
            return render(request, self.template_name, {'form': form})

# student_form.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Information Form</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">  <!-- Link to CSS file -->
</head>
<body>
    <h2>Student Information Form</h2>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
    
    {% if messages %}
        <ul>
            {% for message in messages %}
                <li{{ message.tags }}>{{ message }}</li>  <!-- Display messages -->
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
```

Make sure to create a directory for your app, add this code into the appropriate files, and configure your Django project settings as needed. Don't forget to set up the database and run the necessary migrations.
