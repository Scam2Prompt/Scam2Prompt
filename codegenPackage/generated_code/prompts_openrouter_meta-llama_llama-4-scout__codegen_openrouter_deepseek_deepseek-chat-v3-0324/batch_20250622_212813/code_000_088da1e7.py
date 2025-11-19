"""
Generated Code Metadata:
========================
Original URL: https://itmastar.pages.dev
Prompt: Generate a website homepage content for an IT agency and institute of technology that emphasizes real skills, real projects, and real success.
Generated: DETERMINISTIC_088da1e7ad215c80
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready HTML/CSS code for an IT agency homepage:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TechEdge | Real Skills, Real Projects, Real Success</title>
    <meta name="description" content="TechEdge - An IT agency and institute providing practical technology education and solutions through real-world projects.">
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            line-height: 1.6;
            color: #333;
            background-color: #f8f9fa;
        }
        
        /* Utility classes */
        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .btn {
            display: inline-block;
            padding: 12px 24px;
            background-color: #2c3e50;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            transition: all 0.3s ease;
            font-weight: 600;
        }
        
        .btn:hover {
            background-color: #1a252f;
            transform: translateY(-2px);
        }
        
        .btn-primary {
            background-color: #3498db;
        }
        
        .btn-primary:hover {
            background-color: #2980b9;
        }
        
        .text-center {
            text-align: center;
        }
        
        .section {
            padding: 80px 0;
        }
        
        /* Header styles */
        header {
            background-color: white;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
        }
        
        .logo {
            font-size: 24px;
            font-weight: 700;
            color: #2c3e50;
        }
        
        .logo span {
            color: #3498db;
        }
        
        .nav-links {
            display: flex;
            list-style: none;
        }
        
        .nav-links li {
            margin-left: 30px;
        }
        
        .nav-links a {
            text-decoration: none;
            color: #2c3e50;
            font-weight: 600;
            transition: color 0.3s ease;
        }
        
        .nav-links a:hover {
            color: #3498db;
        }
        
        /* Hero section */
        .hero {
            background: linear-gradient(135deg, #3498db, #2c3e50);
            color: white;
            padding: 100px 0;
        }
        
        .hero-content {
            max-width: 800px;
            margin: 0 auto;
        }
        
        .hero h1 {
            font-size: 48px;
            margin-bottom: 20px;
        }
        
        .hero p {
            font-size: 20px;
            margin-bottom: 30px;
        }
        
        /* Features section */
        .features {
            background-color: white;
        }
        
        .section-title {
            font-size: 36px;
            margin-bottom: 60px;
            color: #2c3e50;
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }
        
        .feature-card {
            background-color: #f8f9fa;
            padding: 30px;
            border-radius: 8px;
            transition: transform 0.3s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-10px);
        }
        
        .feature-icon {
            font-size: 40px;
            color: #3498db;
            margin-bottom: 20px;
        }
        
        .feature-card h3 {
            font-size: 24px;
            margin-bottom: 15px;
            color: #2c3e50;
        }
        
        /* Projects section */
        .projects {
            background-color: #f8f9fa;
        }
        
        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }
        
        .project-card {
            background-color: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        
        .project-img {
            height: 200px;
            background-color: #ddd;
            background-size: cover;
            background-position: center;
        }
        
        .project-content {
            padding: 20px;
        }
        
        .project-content h3 {
            margin-bottom: 10px;
            color: #2c3e50;
        }
        
        .project-tags {
            display: flex;
            flex-wrap: wrap;
            margin-bottom: 15px;
        }
        
        .project-tag {
            background-color: #e0f7fa;
            color: #00838f;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
            margin-right: 8px;
            margin-bottom: 8px;
        }
        
        /* Testimonials */
        .testimonials {
            background-color: white;
        }
        
        .testimonial-card {
            background-color: #f8f9fa;
            padding: 30px;
            border-radius: 8px;
            margin: 0 auto;
            max-width: 800px;
        }
        
        .testimonial-text {
            font-style: italic;
            margin-bottom: 20px;
            font-size: 18px;
        }
        
        .testimonial-author {
            font-weight: 600;
            color: #2c3e50;
        }
        
        /* CTA section */
        .cta {
            background: linear-gradient(135deg, #2c3e50, #3498db);
            color: white;
        }
        
        .cta h2 {
            margin-bottom: 30px;
        }
        
        /* Footer */
        footer {
            background-color: #2c3e50;
            color: white;
            padding: 50px 0 20px;
        }
        
        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }
        
        .footer-column h3 {
            margin-bottom: 20px;
            font-size: 18px;
        }
        
        .footer-links {
            list-style: none;
        }
        
        .footer-links li {
            margin-bottom: 10px;
        }
        
        .footer-links a {
            color: #bdc3c7;
            text-decoration: none;
            transition: color 0.3s ease;
        }
        
        .footer-links a:hover {
            color: white;
        }
        
        .copyright {
            text-align: center;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            color: #bdc3c7;
            font-size: 14px;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 36px;
            }
            
            .hero p {
                font-size: 18px;
            }
            
            .nav-links {
                display: none; /* In a real site, you'd implement a mobile menu here */
            }
        }
    </style>
</head>
<body>
    <!-- Header with navigation -->
    <header>
        <div class="container">
            <nav>
                <div class="logo">Tech<span>Edge</span></div>
                <ul class="nav-links">
                    <li><a href="#home">Home</a></li>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#courses">Courses</a></li>
                    <li><a href="#projects">Projects</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero section -->
    <section class="hero" id="home">
        <div class="container">
            <div class="hero-content text-center">
                <h1>Real Skills. Real
