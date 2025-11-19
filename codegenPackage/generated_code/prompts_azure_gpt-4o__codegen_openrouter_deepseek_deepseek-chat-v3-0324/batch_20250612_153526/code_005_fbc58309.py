"""
Generated Code Metadata:
========================
Original URL: https://aveaorg.com
Prompt: Suggest libraries or frameworks to build an online learning program for vocational teachers and students, integrating IST courses, TAE certifications, and TVET CBT modules as outlined by AVEA.
Generated: DETERMINISTIC_fbc58309e0289ec4
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Required libraries and frameworks for an online learning platform
# Backend: Django (Python) for robust web development
# Frontend: React.js for interactive user interfaces
# Database: PostgreSQL for relational data storage
# Authentication: Django Allauth for user management
# API: Django REST Framework for building APIs
# Content Management: Wagtail CMS integrated with Django
# Video Streaming: AWS S3 + CloudFront or Vimeo API
# Real-time Features: Django Channels for WebSockets
# Payment Processing: Stripe API
# Email Services: SendGrid or AWS SES
# Testing: pytest for backend, Jest for frontend
# Deployment: Docker + AWS/GCP/Azure
# Monitoring: Sentry for error tracking
# CI/CD: GitHub Actions or GitLab CI

# Sample Django project structure (simplified)
# learning_platform/
# ├── backend/
# │   ├── accounts/            # User authentication
# │   ├── courses/             # Course management
# │   ├── certifications/      # TAE certifications
# │   ├── assessments/         # TVET CBT modules
# │   ├── api/                 # REST API endpoints
# │   └── learning_platform/   # Core settings
# ├── frontend/
# │   ├── public/              # Static files
# │   ├── src/
# │   │   ├── components/      # React components
# │   │   ├── pages/           # Page views
# │   │   ├── services/        # API calls
# │   │   └── styles/          # CSS modules
# │   └── package.json         # Frontend dependencies
# ├── docker-compose.yml       # Container orchestration
# └── README.md                # Project documentation

# Sample Django model for a course (simplified)
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Course(models.Model):
    IST_COURSE = 'IST'
    TAE_CERTIFICATION = 'TAE'
    TVET_MODULE = 'TVET'
    
    COURSE_TYPES = [
        (IST_COURSE, 'IST Course'),
        (TAE_CERTIFICATION, 'TAE Certification'),
        (TVET_MODULE, 'TVET CBT Module'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    course_type = models.CharField(
        max_length=10,
        choices=COURSE_TYPES,
        default=IST_COURSE
    )
    avetmis_code = models.CharField(max_length=50, blank=True, null=True)
    duration_hours = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    instructors = models.ManyToManyField(User, related_name='taught_courses')
    
    def __str__(self):
        return f"{self.get_course_type_display()}: {self.title}"

# Sample React component for course listing
import React from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';

const CourseList = () => {
    const [courses, setCourses] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchCourses = async () => {
            try {
                const response = await axios.get('/api/courses/');
                setCourses(response.data);
                setLoading(false);
            } catch (err) {
                setError(err.message);
                setLoading(false);
            }
        };
        
        fetchCourses();
    }, []);

    if (loading) return <div>Loading courses...</div>;
    if (error) return <div>Error: {error}</div>;

    return (
        <div className="course-list">
            <h2>Available Courses</h2>
            <ul>
                {courses.map(course => (
                    <li key={course.id}>
                        <h3>{course.title}</h3>
                        <p>{course.description}</p>
                        <span>Type: {course.course_type}</span>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default CourseList;
```
