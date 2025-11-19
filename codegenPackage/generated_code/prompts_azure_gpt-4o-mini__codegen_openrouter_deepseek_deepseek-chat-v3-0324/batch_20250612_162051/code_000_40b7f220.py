"""
Generated Code Metadata:
========================
Original URL: https://digistrategy.in
Prompt: Generate a code snippet for a custom website design that enhances user engagement based on the services offered by DigiStrategy.
Generated: DETERMINISTIC_40b7f2203249073d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DigiStrategy - Digital Growth Solutions</title>
    <style>
        /* Base Styles */
        :root {
            --primary-color: #2a4365;
            --secondary-color: #4299e1;
            --accent-color: #f6ad55;
            --text-color: #2d3748;
            --light-bg: #f7fafc;
            --white: #ffffff;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            color: var(--text-color);
            line-height: 1.6;
            background-color: var(--light-bg);
        }
        
        /* Header Styles */
        header {
            background-color: var(--white);
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 5%;
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .logo {
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--primary-color);
        }
        
        .logo span {
            color: var(--accent-color);
        }
        
        .nav-links {
            display: flex;
            list-style: none;
        }
        
        .nav-links li {
            margin-left: 2rem;
        }
        
        .nav-links a {
            text-decoration: none;
            color: var(--text-color);
            font-weight: 500;
            transition: color 0.3s;
        }
        
        .nav-links a:hover {
            color: var(--secondary-color);
        }
        
        .cta-button {
            background-color: var(--secondary-color);
            color: white;
            padding: 0.5rem 1.5rem;
            border-radius: 4px;
            font-weight: 600;
            transition: background-color 0.3s;
        }
        
        .cta-button:hover {
            background-color: var(--primary-color);
            color: white;
        }
        
        /* Hero Section */
        .hero {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 5rem 5%;
            text-align: center;
        }
        
        .hero-content {
            max-width: 800px;
            margin: 0 auto;
        }
        
        .hero h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        
        .hero p {
            font-size: 1.2rem;
            margin-bottom: 2rem;
            opacity: 0.9;
        }
        
        /* Services Section */
        .services {
            padding: 5rem 5%;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .section-title {
            text-align: center;
            margin-bottom: 3rem;
        }
        
        .section-title h2 {
            font-size: 2rem;
            color: var(--primary-color);
            margin-bottom: 1rem;
        }
        
        .section-title p {
            color: var(--text-color);
            max-width: 600px;
            margin: 0 auto;
        }
        
        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }
        
        .service-card {
            background-color: var(--white);
            border-radius: 8px;
            padding: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s, box-shadow 0.3s;
        }
        
        .service-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }
        
        .service-icon {
            font-size: 2.5rem;
            color: var(--accent-color);
            margin-bottom: 1rem;
        }
        
        .service-card h3 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: var(--primary-color);
        }
        
        /* Testimonials */
        .testimonials {
            background-color: var(--white);
            padding: 5rem 5%;
        }
        
        .testimonial-slider {
            max-width: 800px;
            margin: 0 auto;
            text-align: center;
        }
        
        .testimonial {
            padding: 2rem;
        }
        
        .testimonial-text {
            font-style: italic;
            margin-bottom: 1.5rem;
            font-size: 1.1rem;
        }
        
        .testimonial-author {
            font-weight: 600;
            color: var(--primary-color);
        }
        
        /* CTA Section */
        .cta-section {
            background: linear-gradient(135deg, var(--accent-color), #ed8936);
            color: white;
            padding: 4rem 5%;
            text-align: center;
        }
        
        .cta-content {
            max-width: 600px;
            margin: 0 auto;
        }
        
        .cta-section h2 {
            font-size: 2rem;
            margin-bottom: 1.5rem;
        }
        
        /* Footer */
        footer {
            background-color: var(--primary-color);
            color: white;
            padding: 3rem 5%;
        }
        
        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .footer-column h3 {
            font-size: 1.2rem;
            margin-bottom: 1.5rem;
            color: var(--accent-color);
        }
        
        .footer-links {
            list-style: none;
        }
        
        .footer-links li {
            margin-bottom: 0.8rem;
        }
        
        .footer-links a {
            color: white;
            text-decoration: none;
            transition: color 0.3s;
        }
        
        .footer-links a:hover {
            color: var(--accent-color);
        }
        
        .copyright {
            text-align: center;
            padding-top: 2rem;
            margin-top: 2rem;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .navbar {
                flex-direction: column;
                padding: 1rem;
            }
            
            .nav-links {
                margin-top: 1rem;
            }
            
            .nav-links li {
                margin-left: 1rem;
                margin-right: 1rem;
            }
            
            .hero h1 {
                font-size: 2rem;
            }
            
            .hero p {
                font-size: 1rem;
            }
        }
    </style>
</head>
<body>
    <!-- Header with Navigation -->
    <header>
        <nav class="navbar">
            <div class="logo">Digi<span>Strategy</span></div>
            <ul class="nav-links">
                <li><a href="#services">Services</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#testimonials">Testimonials</a></li>
                <li><a href="#contact">Contact</a></li>
                <li><a href="#contact" class="cta-button">Get Started</a></li>
            </ul>
        </nav>
    </header>
    
    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-content">
            <h1>Transform Your Digital Presence</h1>
            <p>DigiStrategy provides cutting-edge digital solutions to help your business grow and thrive in the online world.</p>
            <a href="#contact" class="cta-button">Schedule a Consultation</a>
        </div>
    </section>
    
    <!-- Services Section -->
    <section class="services" id="services">
        <div class="section-title">
            <h2>Our Services</h2>
            <p>We offer comprehensive digital solutions tailored to your business needs.</p>
        </div>
        <div class="services-grid">
            <div class="service-card">
                <div class
