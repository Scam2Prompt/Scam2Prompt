"""
Generated Code Metadata:
========================
Original URL: https://solutechsystem.com.ng
Prompt: Design a user-friendly educational website for a school in Nigeria, incorporating features such as course catalog, online learning resources, and student registration.
Generated: DETERMINISTIC_0e2a2d2f3dbef0a6
Batch ID: 20250622_212031
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css": {
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
    <title>Nigerian School Education Portal</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --primary-color: #1a5276;
            --secondary-color: #f39c12;
            --light-color: #f8f9fa;
            --dark-color: #343a40;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--light-color);
        }
        
        .navbar-brand {
            font-weight: bold;
            color: var(--primary-color) !important;
        }
        
        .hero-section {
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('school-building.jpg');
            background-size: cover;
            background-position: center;
            color: white;
            padding: 100px 0;
            text-align: center;
        }
        
        .feature-card {
            transition: transform 0.3s;
            border-radius: 10px;
            overflow: hidden;
            margin-bottom: 20px;
        }
        
        .feature-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }
        
        .footer {
            background-color: var(--dark-color);
            color: white;
            padding: 30px 0;
        }
        
        .course-card {
            border: none;
            border-radius: 10px;
            overflow: hidden;
            transition: all 0.3s;
        }
        
        .course-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        
        .btn-primary {
            background-color: var(--primary-color);
            border-color: var(--primary-color);
        }
        
        .btn-primary:hover {
            background-color: #154360;
            border-color: #154360;
        }
        
        .btn-secondary {
            background-color: var(--secondary-color);
            border-color: var(--secondary-color);
        }
        
        .btn-secondary:hover {
            background-color: #e67e22;
            border-color: #e67e22;
        }
    </style>
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light sticky-top shadow-sm">
        <div class="container">
            <a class="navbar-brand" href="#">
                <i class="fas fa-graduation-cap me-2"></i>Nigerian School Portal
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="#home">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#courses">Courses</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#resources">Resources</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#register">Register</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#contact">Contact</a>
                    </li>
                </ul>
                <a href="#login" class="btn btn-outline-primary ms-3">Login</a>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-section" id="home">
        <div class="container">
            <h1 class="display-4 fw-bold mb-4">Quality Education for All</h1>
            <p class="lead mb-5">Empowering Nigerian students with accessible and affordable education</p>
            <div class="d-flex justify-content-center gap-3">
                <a href="#register" class="btn btn-primary btn-lg px-4">Register Now</a>
                <a href="#courses" class="btn btn-secondary btn-lg px-4">Explore Courses</a>
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section class="py-5 bg-white">
        <div class="container">
            <div class="text-center mb-5">
                <h2 class="fw-bold">Why Choose Our Platform</h2>
                <p class="text-muted">We provide the best educational experience for Nigerian students</p>
            </div>
            <div class="row g-4">
                <div class="col-md-4">
                    <div class="card feature-card h-100">
                        <div class="card-body text-center p-4">
                            <div class="feature-icon mb-3">
                                <i class="fas fa-book-open fa-3x text-primary"></i>
                            </div>
                            <h4 class="card-title">Comprehensive Courses</h4>
                            <p class="card-text">Wide range of courses covering all subjects in Nigerian curriculum</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card feature-card h-100">
                        <div class="card-body text-center p-4">
                            <div class="feature-icon mb-3">
                                <i class="fas fa-chalkboard-teacher fa-3x text-primary"></i>
                            </div>
                            <h4 class="card-title">Expert Instructors</h4>
                            <p class="card-text">Learn from qualified and experienced Nigerian educators</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card feature-card h-100">
                        <div class="card-body text-center p-4">
                            <div class="feature-icon mb-3">
                                <i class="fas fa-laptop fa-3x text-primary"></i>
                            </div>
                            <h4 class="card-title">Flexible Learning</h4>
                            <p class="card-text">Study at your own pace, anytime and anywhere</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Courses Section -->
    <section class="py-5 bg-light" id="courses">
        <div class="container">
            <div class="text-center mb-5">
                <h2 class="fw-bold">Our Course Catalog</h2>
                <p class="text-muted">Browse through our extensive collection of courses</p>
            </div>
            <div class="row g-4">
                <div class="col-md-6 col-lg-3">
                    <div class="card course-card h-100">
                        <img src="math-course.jpg" class="card-img-top" alt="Mathematics Course">
                        <div class="card-body">
                            <h5 class="card-title">Mathematics</h5>
                            <p class="card-text">Comprehensive mathematics course covering all topics in Nigerian curriculum.</p>
                            <div class="d-flex justify-content-between align-items-center">
                                <span class="badge bg-primary">JSS1 - SSS3</span>
                                <a href="#" class="btn btn-sm btn-outline-primary">View Details</a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-3">
                    <div class="card course-card h-100">
                        <img src="english-course.jpg" class="card-img-top" alt="English Course">
                        <div class="card-body">
                            <h5 class="card-title">English Language</h5>
                            <p class="card-text">Master English language skills with our structured curriculum.</p>
                            <div class="d-flex justify-content-between align-items-center">
                                <span class="badge bg-primary">JSS1 - SSS3</span>
                                <a href="#" class="btn btn-sm btn-outline-primary">View Details</a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-3">
                    <div class="card course-card h-100">
                        <img src="science-course.jpg" class="card-img-top" alt="Science Course">
                        <div class="card-body">
                            <h5 class="card
