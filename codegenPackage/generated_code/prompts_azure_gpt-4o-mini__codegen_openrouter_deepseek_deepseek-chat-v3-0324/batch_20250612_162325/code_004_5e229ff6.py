"""
Generated Code Metadata:
========================
Original URL: https://videtisconsultores.es
Prompt: Design a user interface for a web application that supports the recruitment process, incorporating features mentioned in Videtis Consultores' talent acquisition services.
Generated: DETERMINISTIC_5e229ff69162b9fc
Batch ID: 20250612_162325
URLs Found: 4
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
  },
  "https://via.placeholder.com/600x400": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/100": {
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
    <title>Videtis Consultores - Talent Acquisition</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --primary-color: #2c3e50;
            --secondary-color: #3498db;
            --accent-color: #e74c3c;
            --light-color: #ecf0f1;
            --dark-color: #2c3e50;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: var(--dark-color);
        }
        
        .navbar-brand {
            font-weight: 700;
        }
        
        .hero-section {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 5rem 0;
        }
        
        .feature-card {
            border: none;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s;
            height: 100%;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
        }
        
        .feature-icon {
            font-size: 2.5rem;
            color: var(--secondary-color);
            margin-bottom: 1rem;
        }
        
        .btn-primary {
            background-color: var(--secondary-color);
            border-color: var(--secondary-color);
        }
        
        .btn-primary:hover {
            background-color: #2980b9;
            border-color: #2980b9;
        }
        
        .footer {
            background-color: var(--primary-color);
            color: white;
            padding: 3rem 0;
        }
        
        .candidate-card img {
            width: 100px;
            height: 100px;
            object-fit: cover;
            border-radius: 50%;
        }
        
        .dashboard-card {
            border-left: 4px solid var(--secondary-color);
        }
        
        .stat-number {
            font-size: 2.5rem;
            font-weight: 700;
            color: var(--secondary-color);
        }
    </style>
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
        <div class="container">
            <a class="navbar-brand" href="#">
                <i class="fas fa-user-tie me-2"></i>Videtis Consultores
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link active" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#services">Services</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#candidates">Candidates</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#dashboard">Dashboard</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#contact">Contact</a>
                    </li>
                    <li class="nav-item ms-lg-3">
                        <a class="btn btn-outline-light" href="#login">Login</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-section">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6">
                    <h1 class="display-4 fw-bold mb-4">Strategic Talent Acquisition Solutions</h1>
                    <p class="lead mb-4">Leverage our expertise to find and retain the best talent for your organization.</p>
                    <div class="d-flex gap-3">
                        <a href="#contact" class="btn btn-light btn-lg">Get Started</a>
                        <a href="#services" class="btn btn-outline-light btn-lg">Learn More</a>
                    </div>
                </div>
                <div class="col-lg-6 d-none d-lg-block">
                    <img src="https://via.placeholder.com/600x400" alt="Talent Acquisition" class="img-fluid rounded">
                </div>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="py-5">
        <div class="container">
            <div class="text-center mb-5">
                <h2 class="fw-bold">Our Talent Acquisition Services</h2>
                <p class="text-muted">Comprehensive solutions tailored to your recruitment needs</p>
            </div>
            
            <div class="row g-4">
                <div class="col-md-4">
                    <div class="card feature-card p-4">
                        <div class="feature-icon">
                            <i class="fas fa-search"></i>
                        </div>
                        <h4>Executive Search</h4>
                        <p>Targeted approach to identify and attract top-level executives for critical leadership roles.</p>
                        <a href="#" class="btn btn-sm btn-outline-primary mt-auto">Learn More</a>
                    </div>
                </div>
                
                <div class="col-md-4">
                    <div class="card feature-card p-4">
                        <div class="feature-icon">
                            <i class="fas fa-users"></i>
                        </div>
                        <h4>Mass Recruitment</h4>
                        <p>Efficient processes for high-volume hiring needs across various industries and skill levels.</p>
                        <a href="#" class="btn btn-sm btn-outline-primary mt-auto">Learn More</a>
                    </div>
                </div>
                
                <div class="col-md-4">
                    <div class="card feature-card p-4">
                        <div class="feature-icon">
                            <i class="fas fa-graduation-cap"></i>
                        </div>
                        <h4>University Recruitment</h4>
                        <p>Specialized programs to attract and assess fresh talent from top universities.</p>
                        <a href="#" class="btn btn-sm btn-outline-primary mt-auto">Learn More</a>
                    </div>
                </div>
                
                <div class="col-md-4">
                    <div class="card feature-card p-4">
                        <div class="feature-icon">
                            <i class="fas fa-globe"></i>
                        </div>
                        <h4>International Recruitment</h4>
                        <p>Global talent sourcing with compliance expertise for cross-border hiring.</p>
                        <a href="#" class="btn btn-sm btn-outline-primary mt-auto">Learn More</a>
                    </div>
                </div>
                
                <div class="col-md-4">
                    <div class="card feature-card p-4">
                        <div class="feature-icon">
                            <i class="fas fa-chart-line"></i>
                        </div>
                        <h4>Employer Branding</h4>
                        <p>Strategies to enhance your company's attractiveness to potential candidates.</p>
                        <a href="#" class="btn btn-sm btn-outline-primary mt-auto">Learn More</a>
                    </div>
                </div>
                
                <div class="col-md-4">
                    <div class="card feature-card p-4">
                        <div class="feature-icon">
                            <i class="fas fa-brain"></i>
                        </div>
                        <h4>Assessment Solutions</h4>
                        <p>Comprehensive evaluation tools to ensure the right cultural and skill fit.</p>
                        <a href="#" class="btn btn-sm btn-outline-primary mt-auto">Learn More</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Candidates Section -->
    <section id="candidates" class="py-5 bg-light">
        <div class="container">
            <div class="text-center mb-5">
                <h2 class="fw-bold">Featured Candidates</h2>
                <p class="text-muted">Pre-screened professionals ready to join your team</p>
            </div>
            
            <div class="row g-4">
                <div class="col-md-6 col-lg-3">
                    <div class="card candidate-card p-3 text-center">
                        <img src="https://via.placeholder.com/100
