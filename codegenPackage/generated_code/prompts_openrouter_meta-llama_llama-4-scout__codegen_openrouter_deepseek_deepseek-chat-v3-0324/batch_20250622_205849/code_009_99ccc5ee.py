"""
Generated Code Metadata:
========================
Original URL: https://rspbharat.com
Prompt: "Outline a basic structure for a career guidance and counseling website, inspired by RSP Bharat's Diploma in Career Guidance & Counseling course."
Generated: DETERMINISTIC_99ccc5ee14a9e2ef
Batch ID: 20250622_205849
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Career Guidance & Counseling</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="#">CareerGuide</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="#home">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#services">Services</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#courses">Courses</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#counselors">Counselors</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#resources">Resources</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#contact">Contact</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="hero-section py-5">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6">
                    <h1 class="display-4 fw-bold mb-4">Your Career Journey Starts Here</h1>
                    <p class="lead mb-4">Professional guidance to help you discover and achieve your career goals.</p>
                    <a href="#services" class="btn btn-primary btn-lg me-2">Explore Services</a>
                    <a href="#contact" class="btn btn-outline-primary btn-lg">Book Consultation</a>
                </div>
                <div class="col-lg-6">
                    <img src="images/hero-image.jpg" alt="Career Guidance" class="img-fluid rounded">
                </div>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="py-5 bg-light">
        <div class="container">
            <h2 class="text-center mb-5">Our Services</h2>
            <div class="row g-4">
                <div class="col-md-4">
                    <div class="card h-100">
                        <div class="card-body text-center">
                            <div class="mb-3">
                                <i class="bi bi-person-badge fs-1 text-primary"></i>
                            </div>
                            <h4 class="card-title">Career Assessment</h4>
                            <p class="card-text">Comprehensive tests to identify your strengths, interests, and career potential.</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card h-100">
                        <div class="card-body text-center">
                            <div class="mb-3">
                                <i class="bi bi-book fs-1 text-primary"></i>
                            </div>
                            <h4 class="card-title">Educational Guidance</h4>
                            <p class="card-text">Help choosing the right courses, colleges, and educational paths.</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card h-100">
                        <div class="card-body text-center">
                            <div class="mb-3">
                                <i class="bi bi-briefcase fs-1 text-primary"></i>
                            </div>
                            <h4 class="card-title">Job Placement</h4>
                            <p class="card-text">Assistance with resume building, interview prep, and job search strategies.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Courses Section -->
    <section id="courses" class="py-5">
        <div class="container">
            <h2 class="text-center mb-5">Career Guidance Courses</h2>
            <div class="row g-4">
                <div class="col-md-6 col-lg-4">
                    <div class="card h-100">
                        <img src="images/diploma-course.jpg" class="card-img-top" alt="Diploma Course">
                        <div class="card-body">
                            <h4 class="card-title">Diploma in Career Guidance</h4>
                            <p class="card-text">Comprehensive training program covering all aspects of career counseling.</p>
                            <ul class="list-group list-group-flush mb-3">
                                <li class="list-group-item">Duration: 6 months</li>
                                <li class="list-group-item">Certification: RSP Bharat</li>
                                <li class="list-group-item">Mode: Online/Offline</li>
                            </ul>
                            <a href="#" class="btn btn-primary">Learn More</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4">
                    <div class="card h-100">
                        <img src="images/certificate-course.jpg" class="card-img-top" alt="Certificate Course">
                        <div class="card-body">
                            <h4 class="card-title">Career Counseling Certification</h4>
                            <p class="card-text">Specialized training for professionals looking to become career counselors.</p>
                            <ul class="list-group list-group-flush mb-3">
                                <li class="list-group-item">Duration: 3 months</li>
                                <li class="list-group-item">Certification: RSP Bharat</li>
                                <li class="list-group-item">Mode: Online</li>
                            </ul>
                            <a href="#" class="btn btn-primary">Learn More</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4">
                    <div class="card h-100">
                        <img src="images/workshop.jpg" class="card-img-top" alt="Workshop">
                        <div class="card-body">
                            <h4 class="card-title">Career Development Workshop</h4>
                            <p class="card-text">Interactive sessions for students and professionals to enhance career skills.</p>
                            <ul class="list-group list-group-flush mb-3">
                                <li class="list-group-item">Duration: 2 days</li>
                                <li class="list-group-item">Certificate: Participation</li>
                                <li class="list-group-item">Mode: In-person</li>
                            </ul>
                            <a href="#" class="btn btn-primary">Learn More</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Counselors Section -->
    <section id="counselors" class="py-5 bg-light">
        <div class="container">
            <h2 class="text-center mb-5">Our Expert Counselors</h2>
            <div class="row g-4">
                <div class="col-md-6 col-lg-3">
                    <div class="card h-100">
                        <img src="images/counselor1.jpg" class="card-img-top" alt="Counselor">
                        <div class="card-body text-center">
                            <h4 class="card-title">Dr. Priya Sharma</h4>
                            <p class="text-muted">Career Psychologist</p>
                            <p class="card-text">15+ years experience in career assessment and guidance.</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-3">
                    <div class="card h-100">
                        <img src="images/counselor2.jpg" class="card-img-top" alt="Counselor">
                        <div class="card-body text-center">
                            <h4 class="card-title">Rajesh Kumar</h4>
                            <p class="text-muted">Educational Consultant</p>
                            <p class="card-text">Specialized in STEM career paths and international education.</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-3">
                    <div class="card h-100">
                        <img src="images/counselor3.jpg" class="card-img-top" alt="Counselor">
                        <div class="card-body text-center
