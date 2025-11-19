"""
Generated Code Metadata:
========================
Original URL: https://agenciainside.com
Prompt: "Write a code snippet to create a responsive design for a marketing website, inspired by Agência inSIDE's portfolio, using HTML, CSS, and JavaScript."
Generated: DETERMINISTIC_d1c684028b4838a9
Batch ID: 20250622_210348
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
    <title>Marketing Agency</title>
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
            background-color: #f9f9f9;
        }

        /* Header styles */
        header {
            background-color: #fff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            position: fixed;
            width: 100%;
            z-index: 1000;
        }

        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
        }

        .logo {
            font-size: 24px;
            font-weight: 700;
            color: #2a2a2a;
            text-decoration: none;
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
            color: #2a2a2a;
            font-weight: 500;
            transition: color 0.3s;
        }

        .nav-links a:hover {
            color: #007bff;
        }

        .menu-toggle {
            display: none;
            cursor: pointer;
            font-size: 24px;
        }

        /* Hero section */
        .hero {
            padding: 150px 0 100px;
            text-align: center;
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            color: white;
        }

        .hero h1 {
            font-size: 3rem;
            margin-bottom: 20px;
        }

        .hero p {
            font-size: 1.2rem;
            max-width: 700px;
            margin: 0 auto 30px;
        }

        .cta-button {
            display: inline-block;
            background-color: #fff;
            color: #6e8efb;
            padding: 12px 30px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s;
        }

        .cta-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }

        /* Services section */
        .services {
            padding: 80px 0;
            background-color: #fff;
        }

        .section-title {
            text-align: center;
            margin-bottom: 50px;
        }

        .section-title h2 {
            font-size: 2.5rem;
            color: #2a2a2a;
        }

        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }

        .service-card {
            background-color: #f9f9f9;
            border-radius: 10px;
            padding: 30px;
            text-align: center;
            transition: transform 0.3s;
        }

        .service-card:hover {
            transform: translateY(-10px);
        }

        .service-card i {
            font-size: 3rem;
            color: #6e8efb;
            margin-bottom: 20px;
        }

        .service-card h3 {
            margin-bottom: 15px;
            font-size: 1.5rem;
        }

        /* Portfolio section */
        .portfolio {
            padding: 80px 0;
            background-color: #f9f9f9;
        }

        .portfolio-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }

        .portfolio-item {
            position: relative;
            overflow: hidden;
            border-radius: 10px;
            height: 250px;
        }

        .portfolio-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s;
        }

        .portfolio-item:hover img {
            transform: scale(1.1);
        }

        .portfolio-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(110, 142, 251, 0.8);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            opacity: 0;
            transition: opacity 0.3s;
        }

        .portfolio-item:hover .portfolio-overlay {
            opacity: 1;
        }

        .portfolio-overlay h3 {
            color: white;
            font-size: 1.5rem;
            margin-bottom: 10px;
        }

        /* Footer */
        footer {
            background-color: #2a2a2a;
            color: white;
            padding: 50px 0 20px;
        }

        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 30px;
            margin-bottom: 30px;
        }

        .footer-column h3 {
            margin-bottom: 20px;
            font-size: 1.2rem;
        }

        .footer-column ul {
            list-style: none;
        }

        .footer-column ul li {
            margin-bottom: 10px;
        }

        .footer-column ul li a {
            color: #ccc;
            text-decoration: none;
            transition: color 0.3s;
        }

        .footer-column ul li a:hover {
            color: #6e8efb;
        }

        .copyright {
            text-align: center;
            padding-top: 20px;
            border-top: 1px solid #444;
        }

        /* Responsive styles */
        @media (max-width: 768px) {
            .header-container {
                padding: 15px 0;
            }

            .nav-links {
                position: fixed;
                top: 70px;
                left: -100%;
                width: 100%;
                height: calc(100vh - 70px);
                background-color: #fff;
                flex-direction: column;
                align-items: center;
                padding-top: 30px;
                transition: left 0.3s;
            }

            .nav-links.active {
                left: 0;
            }

            .nav-links li {
                margin: 15px 0;
            }

            .menu-toggle {
                display: block;
            }

            .hero h1 {
                font-size: 2.2rem;
            }

            .hero p {
                font-size: 1rem;
            }
        }

        @media (max-width: 480px) {
            .hero h1 {
                font-size: 1.8rem;
            }

            .section-title h2 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container header-container">
            <a href="#" class="logo">Agency</a>
            <div class="menu-toggle" id="mobile-menu">
                <span>☰</span>
            </div>
            <ul class="nav-links" id="nav-links">
                <li><a href="#">Home</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </header>

    <section class="hero">
        <div class="container">
            <h1>Creative Digital Solutions</h1>
            <p>We help brands grow through innovative design and strategic marketing solutions.</p>
            <a href="#contact" class="cta-button">Get Started</a>
        </div>
    </section>

    <section class="services" id="services">
        <div class="container">
            <div class="section-title">
                <h2>Our Services</h2>
            </div>
            <div class="services-grid">
                <div class="service-card">
                    <i>📱</i>
                    <h3>Web Design</h3>
                    <p>Custom websites that convert visitors into customers.</p>
                </div>
                <div class
