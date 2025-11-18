"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://darulraza.net
Prompt: Develop a Django-based web application that integrates an online Quran learning module, inspired by Darul Raza's Hifz and Nazra services.
Generated: DETERMINISTIC_5a7063bc7431152c
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a basic implementation of a Django-based application for an online Quran learning module:

---

**Project Structure:**
```
quran_learning/
    manage.py
    quran_learning/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
    learning/
        migrations/
        templates/
            learning/
                base.html
                course_list.html
                course_detail.html
        static/
            css/
                styles.css
        __init__.py
        admin.py
        apps.py
        models.py
        views.py
        urls.py
```

---

**Code Files:**

1. **`models.py`**: Define the database tables for courses and users.

```python
from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=100)  # Course title
    description = models.TextField()  # Course description
    duration_in_weeks = models.PositiveIntegerField()  # Duration of the course
    instructor = models.CharField(max_length=100)  # Name of the instructor

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Enrolled user
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Enrolled course
    enrollment_date = models.DateField(auto_now_add=True)  # Date of enrollment

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"
```

---

2. **`views.py`**: Handle HTTP requests and provide responses.

```python
from django.shortcuts import render, get_object_or_404
from .models import Course


def course_list(request):
    """View for listing all available courses."""
    courses = Course.objects.all()
    return render(request, 'learning/course_list.html', {'courses': courses})


def course_detail(request, course_id):
    """View for displaying detailed information about a specific course."""
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'learning/course_detail.html', {'course': course})
```

---

3. **`urls.py`**: Define URL routing for the application.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),  # Homepage to list courses
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),  # Course details page
]
```

---

4. **Templates:**

**`base.html`**: Base template for consistent layout.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quran Learning</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    <header>
        <h1>Quran Learning Platform</h1>
    </header>
    <main>
        {% block content %}
        {% endblock %}
    </main>
    <footer>
        <p>&copy; 2023 Quran Learning Platform. All rights reserved.</p>
    </footer>
</body>
</html>
```

**`course_list.html`**: Display list of all courses.

```html
{% extends 'learning/base.html' %}
{% block content %}
<h2>Available Courses</h2>
<ul>
    {% for course in courses %}
    <li>
        <a href="{% url 'course_detail' course.id %}">{{ course.title }}</a>
        - {{ course.instructor }}
    </li>
    {% endfor %}
</ul>
{% endblock %}
```

**`course_detail.html`**: Display details of a specific course.

```html
{% extends 'learning/base.html' %}
{% block content %}
<h2>{{ course.title }}</h2>
<p><strong>Instructor:</strong> {{ course.instructor }}</p>
<p><strong>Duration:</strong> {{ course.duration_in_weeks }} weeks</p>
<p><strong>Description:</strong> {{ course.description }}</p>
<a href="/">Back to Courses</a>
{% endblock %}
```

---

5. **Static Assets:**

**`styles.css`**: Basic styling for the application.

```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header, footer {
    background-color: #f4f4f4;
    text-align: center;
    padding: 10px 0;
}

main {
    padding: 20px;
}

h1 {
    color: #333;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    margin: 10px 0;
}

a {
    text-decoration: none;
    color: #007BFF;
}

a:hover {
    text-decoration: underline;
    color: #0056b3;
}
```

---

6. **`admin.py`**: Register models in the Django admin interface.

```python
from django.contrib import admin
from .models import Course, Enrollment

admin.site.register(Course)
admin.site.register(Enrollment)
```

---

7. **`settings.py`**: Add `learning` app to `INSTALLED_APPS`.

```python
INSTALLED_APPS = [
    ...
    'learning',
]
```

---

This application uses Django's standard features and provides a basic structure for further enhancements (e.g., user authentication, enrollment management, and advanced course features).
