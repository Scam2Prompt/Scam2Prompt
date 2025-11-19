"""
Generated Code Metadata:
========================
Original URL: https://ashkar2023.github.io
Prompt: Write a code snippet for a responsive webpage using HTML, CSS, and Bootstrap, similar to the Atomic Habits project showcased on Muhammed Ashkar's portfolio.
Generated: DETERMINISTIC_c2c2fc1e41e668d9
Batch ID: 20250612_135442
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://via.placeholder.com/600x400": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/800x450": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://www.w3.org/2000/svg": {
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
    <title>Atomic Habits - Project Showcase</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Custom CSS -->
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
            line-height: 1.6;
        }
        
        .hero-section {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 5rem 0;
            margin-bottom: 3rem;
        }
        
        .project-image {
            border-radius: 8px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
            margin-bottom: 2rem;
        }
        
        .project-image:hover {
            transform: translateY(-5px);
        }
        
        .feature-card {
            border: none;
            border-radius: 8px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s ease;
            margin-bottom: 2rem;
            padding: 1.5rem;
            height: 100%;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
        }
        
        .tech-badge {
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
            font-weight: 500;
        }
        
        .btn-primary {
            background-color: var(--secondary-color);
            border-color: var(--secondary-color);
        }
        
        .btn-primary:hover {
            background-color: #2980b9;
            border-color: #2980b9;
        }
        
        .btn-outline-primary {
            color: var(--secondary-color);
            border-color: var(--secondary-color);
        }
        
        .btn-outline-primary:hover {
            background-color: var(--secondary-color);
            border-color: var(--secondary-color);
        }
        
        footer {
            background-color: var(--primary-color);
            color: white;
            padding: 2rem 0;
            margin-top: 3rem;
        }
        
        @media (max-width: 768px) {
            .hero-section {
                padding: 3rem 0;
            }
            
            .project-image {
                margin-bottom: 1.5rem;
            }
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
        <div class="container">
            <a class="navbar-brand" href="#">Atomic Habits</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="#overview">Overview</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#features">Features</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#technologies">Technologies</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#contact">Contact</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-section" id="home">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6">
                    <h1 class="display-4 fw-bold mb-4">Atomic Habits Tracker</h1>
                    <p class="lead mb-4">A powerful habit-building application inspired by James Clear's best-selling book, designed to help users form good habits and break bad ones.</p>
                    <div class="d-flex gap-3">
                        <a href="#demo" class="btn btn-primary btn-lg px-4">View Demo</a>
                        <a href="#features" class="btn btn-outline-light btn-lg px-4">Learn More</a>
                    </div>
                </div>
                <div class="col-lg-6">
                    <img src="https://via.placeholder.com/600x400" alt="Atomic Habits App Screenshot" class="img-fluid project-image">
                </div>
            </div>
        </div>
    </section>

    <!-- Project Overview -->
    <section class="container mb-5" id="overview">
        <div class="row justify-content-center">
            <div class="col-lg-8 text-center">
                <h2 class="fw-bold mb-4">Project Overview</h2>
                <p class="mb-4">The Atomic Habits Tracker is a comprehensive application that helps users implement the principles from James Clear's book. It provides tools for habit tracking, streak counting, and progress visualization to make habit formation easier and more effective.</p>
                <img src="https://via.placeholder.com/800x450" alt="Atomic Habits Dashboard" class="img-fluid project-image">
            </div>
        </div>
    </section>

    <!-- Key Features -->
    <section class="container mb-5 py-5 bg-light rounded-3" id="features">
        <div class="row text-center mb-5">
            <div class="col">
                <h2 class="fw-bold">Key Features</h2>
                <p class="lead">Designed to help you build better habits</p>
            </div>
        </div>
        <div class="row">
            <div class="col-md-4">
                <div class="feature-card">
                    <div class="feature-icon mb-3">
                        <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="var(--secondary-color)" viewBox="0 0 16 16">
                            <path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4H1z"/>
                            <path d="M8 7a.5.5 0 0 1 .5.5V9H10a.5.5 0 0 1 0 1H8.5v1.5a.5.5 0 0 1-1 0V10H6a.5.5 0 0 1 0-1h1.5V7.5A.5.5 0 0 1 8 7z"/>
                        </svg>
                    </div>
                    <h3>Habit Tracking</h3>
                    <p>Track your daily habits with an intuitive interface that shows your progress and streaks.</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="feature-card">
                    <div class="feature-icon mb-3">
                        <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="var(--secondary-color)" viewBox="0 0 16 16">
                            <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zm.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738
