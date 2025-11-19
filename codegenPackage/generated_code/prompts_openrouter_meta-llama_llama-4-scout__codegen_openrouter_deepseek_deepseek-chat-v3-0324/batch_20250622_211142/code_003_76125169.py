"""
Generated Code Metadata:
========================
Original URL: https://marinendtbd.com
Prompt: "What are the key features of a company profile page for a NDT service provider in Bangladesh, and how can it be implemented using HTML and CSS?"
Generated: DETERMINISTIC_761251695d08ec95
Batch ID: 20250622_211142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation of an NDT service provider company profile page using HTML and CSS:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Precision NDT Services | Bangladesh</title>
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
            background-color: #1a5276;
            color: white;
            padding: 1rem 0;
            text-align: center;
        }

        .logo-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 1rem;
        }

        .logo {
            height: 60px;
            margin-right: 15px;
        }

        /* Navigation */
        nav {
            background-color: #2874a6;
            padding: 0.5rem 0;
        }

        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
        }

        nav ul li {
            margin: 0 15px;
        }

        nav ul li a {
            color: white;
            text-decoration: none;
            font-weight: 500;
            padding: 5px 10px;
            border-radius: 4px;
            transition: background-color 0.3s;
        }

        nav ul li a:hover {
            background-color: #3498db;
        }

        /* Main content */
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 20px;
        }

        section {
            margin-bottom: 2rem;
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        h1, h2, h3 {
            color: #1a5276;
            margin-bottom: 1rem;
        }

        /* Services section */
        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 1.5rem;
        }

        .service-card {
            border: 1px solid #ddd;
            padding: 1.5rem;
            border-radius: 8px;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .service-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .service-card h3 {
            color: #2874a6;
        }

        /* Certification badges */
        .certifications {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 1rem;
        }

        .cert-badge {
            background-color: #f1f1f1;
            padding: 10px 15px;
            border-radius: 20px;
            font-size: 0.9rem;
            display: flex;
            align-items: center;
        }

        .cert-badge img {
            height: 20px;
            margin-right: 8px;
        }

        /* Contact section */
        .contact-info {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }

        .contact-card {
            padding: 1rem;
            background-color: #eaf2f8;
            border-radius: 8px;
        }

        /* Footer */
        footer {
            background-color: #1a5276;
            color: white;
            text-align: center;
            padding: 1.5rem 0;
            margin-top: 2rem;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            nav ul {
                flex-direction: column;
                align-items: center;
            }

            nav ul li {
                margin: 5px 0;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="logo-container">
            <img src="logo.png" alt="Precision NDT Logo" class="logo">
            <h1>Precision NDT Services</h1>
        </div>
        <p>Your trusted NDT partner in Bangladesh since 2010</p>
    </header>

    <nav>
        <ul>
            <li><a href="#about">About Us</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#certifications">Certifications</a></li>
            <li><a href="#clients">Our Clients</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <div class="container">
        <section id="about">
            <h2>About Our Company</h2>
            <p>Precision NDT Services is a leading non-destructive testing provider in Bangladesh, offering comprehensive inspection solutions for industrial and construction sectors. With a team of ASNT Level III certified professionals, we ensure the highest quality standards in all our services.</p>
            <p>Our mission is to provide reliable, accurate, and efficient NDT services that help our clients maintain the integrity of their assets while complying with international safety standards.</p>
        </section>

        <section id="services">
            <h2>Our NDT Services</h2>
            <div class="services-grid">
                <div class="service-card">
                    <h3>Ultrasonic Testing (UT)</h3>
                    <p>High-frequency sound waves to detect internal flaws in materials and measure thickness.</p>
                </div>
                <div class="service-card">
                    <h3>Radiographic Testing (RT)</h3>
                    <p>X-ray or gamma-ray imaging to examine internal structures of components.</p>
                </div>
                <div class="service-card">
                    <h3>Magnetic Particle Testing (MT)</h3>
                    <p>Detection of surface and near-surface discontinuities in ferromagnetic materials.</p>
                </div>
                <div class="service-card">
                    <h3>Liquid Penetrant Testing (PT)</h3>
                    <p>Identification of surface-breaking defects in non-porous materials.</p>
                </div>
                <div class="service-card">
                    <h3>Visual Inspection (VT)</h3>
                    <p>Direct or remote visual examination of components and structures.</p>
                </div>
                <div class="service-card">
                    <h3>Pipeline Inspection</h3>
                    <p>Comprehensive inspection solutions for oil, gas, and water pipelines.</p>
                </div>
            </div>
        </section>

        <section id="certifications">
            <h2>Our Certifications</h2>
            <p>We maintain the highest industry standards with the following certifications:</p>
            <div class="certifications">
                <div class="cert-badge">
                    <img src="asnt-icon.png" alt="ASNT">
                    <span>ASNT Level III Certified</span>
                </div>
                <div class="cert-badge">
                    <img src="iso-icon.png" alt="ISO">
                    <span>ISO 9001:2015 Certified</span>
                </div>
                <div class="cert-badge">
                    <img src="bangladesh-icon.png" alt="BSTI">
                    <span>BSTI Approved</span>
                </div>
            </div>
        </section>

        <section id="clients">
            <h2>Our Clients</h2>
            <p>We proudly serve leading organizations across various industries in Bangladesh:</p>
            <ul>
                <li>Power generation plants</li>
                <li>Oil & gas refineries</li>
                <li>Shipbuilding and marine industries</li>
                <li>Construction and infrastructure projects</li>
                <li>Manufacturing facilities</li>
            </ul>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <div class="contact-info">
                <div class="contact-card">
                    <h3>Head Office</h3>
                    <p>123 Industrial Area, Dhaka-1205</p>
                    <p>Bangladesh</p>
                </div>
                <div class="contact-card">
                    <h3>Contact Details</h3>
                    <p>Phone: +880 2 9876543</p>
                    <p>Mobile: +880 1711 123456</p>
