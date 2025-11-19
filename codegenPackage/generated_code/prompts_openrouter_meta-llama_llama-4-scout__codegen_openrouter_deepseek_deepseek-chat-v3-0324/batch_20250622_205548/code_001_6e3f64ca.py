"""
Generated Code Metadata:
========================
Original URL: https://styleandmakeupeffect.co.za
Prompt: Generate a code snippet for a basic website structure that includes sections for Home, Services, Packages, Our Team, Gallery, and Contact, similar to styleandmakeupeffect.co.za.
Generated: DETERMINISTIC_6e3f64cac8786283
Batch ID: 20250622_205548
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
    <title>Style & Makeup Effect</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }
        
        body {
            line-height: 1.6;
            color: #333;
            background-color: #f9f9f9;
        }
        
        /* Header styles */
        header {
            background-color: #fff;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
        }
        
        .container {
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 15px;
        }
        
        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
        }
        
        .logo {
            font-size: 24px;
            font-weight: bold;
            color: #e83e8c;
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
            color: #333;
            font-weight: 500;
            transition: color 0.3s;
        }
        
        .nav-links a:hover {
            color: #e83e8c;
        }
        
        /* Hero section */
        .hero {
            height: 100vh;
            background: url('hero-bg.jpg') no-repeat center center/cover;
            display: flex;
            align-items: center;
            text-align: center;
            color: #fff;
            margin-top: 80px;
        }
        
        .hero-content h1 {
            font-size: 48px;
            margin-bottom: 20px;
        }
        
        .hero-content p {
            font-size: 20px;
            margin-bottom: 30px;
        }
        
        .btn {
            display: inline-block;
            background: #e83e8c;
            color: #fff;
            padding: 12px 30px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: bold;
            transition: background 0.3s;
        }
        
        .btn:hover {
            background: #d42d7b;
        }
        
        /* Section styles */
        section {
            padding: 80px 0;
        }
        
        .section-title {
            text-align: center;
            margin-bottom: 50px;
        }
        
        .section-title h2 {
            font-size: 36px;
            color: #e83e8c;
            margin-bottom: 15px;
        }
        
        .section-title p {
            color: #777;
            max-width: 700px;
            margin: 0 auto;
        }
        
        /* Services section */
        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }
        
        .service-card {
            background: #fff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            text-align: center;
            transition: transform 0.3s;
        }
        
        .service-card:hover {
            transform: translateY(-10px);
        }
        
        .service-card i {
            font-size: 40px;
            color: #e83e8c;
            margin-bottom: 20px;
        }
        
        /* Team section */
        .team-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
        }
        
        .team-member {
            text-align: center;
        }
        
        .team-member img {
            width: 100%;
            border-radius: 50%;
            margin-bottom: 20px;
            border: 5px solid #e83e8c;
        }
        
        /* Gallery section */
        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 15px;
        }
        
        .gallery-item {
            overflow: hidden;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .gallery-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s;
        }
        
        .gallery-item:hover img {
            transform: scale(1.1);
        }
        
        /* Contact section */
        .contact-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }
        
        .contact-info {
            margin-bottom: 30px;
        }
        
        .contact-info h3 {
            margin-bottom: 15px;
            color: #e83e8c;
        }
        
        .contact-form input,
        .contact-form textarea {
            width: 100%;
            padding: 15px;
            margin-bottom: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        
        .contact-form textarea {
            height: 150px;
        }
        
        /* Footer */
        footer {
            background: #333;
            color: #fff;
            padding: 50px 0 20px;
            text-align: center;
        }
        
        .social-links {
            margin-bottom: 20px;
        }
        
        .social-links a {
            color: #fff;
            margin: 0 10px;
            font-size: 20px;
            transition: color 0.3s;
        }
        
        .social-links a:hover {
            color: #e83e8c;
        }
        
        .copyright {
            margin-top: 20px;
            color: #777;
            font-size: 14px;
        }
        
        /* Responsive styles */
        @media (max-width: 768px) {
            .nav-links {
                display: none;
            }
            
            .hero-content h1 {
                font-size: 36px;
            }
            
            .hero-content p {
                font-size: 18px;
            }
        }
    </style>
</head>
<body>
    <!-- Header and Navigation -->
    <header>
        <div class="container">
            <nav>
                <div class="logo">Style & Makeup Effect</div>
                <ul class="nav-links">
                    <li><a href="#home">Home</a></li>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#packages">Packages</a></li>
                    <li><a href="#team">Our Team</a></li>
                    <li><a href="#gallery">Gallery</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section id="home" class="hero">
        <div class="container">
            <div class="hero-content">
                <h1>Enhance Your Natural Beauty</h1>
                <p>Professional makeup and styling services for all occasions</p>
                <a href="#contact" class="btn">Book Now</a>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="section">
        <div class="container">
            <div class="section-title">
                <h2>Our Services</h2>
                <p>We offer a wide range of professional makeup and styling services tailored to your needs.</p>
            </div>
            <div class="services-grid">
                <div class="service-card">
                    <i>💄</i>
                    <h3>Bridal Makeup</h3>
                    <p>Flawless makeup application for your special day with long-lasting results.</p>
                </div>
                <div class="service-card">
                    <i>✨</i>
                    <h3>Special Occasion</h3>
                    <p>Perfect makeup for weddings, parties, photoshoots, and other events.</p>
                </div>
                <div class="service-card">
                    <i>👩‍🎤</i>
                    <h3>Hair Styling</h3>
                    <p>Professional hairstyling to complement your makeup look
