"""
Generated Code Metadata:
========================
Original URL: https://linea-7.webflow.io
Prompt: Generate a code snippet for a web application that showcases a portfolio of architectural projects similar to those featured on Linea 7's website, emphasizing user-centric design and functionality.
Generated: DETERMINISTIC_78b90ae3951f3584
Batch ID: 20250612_155944
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1487958449943-2429e8be8625?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80": {
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
    <title>Architectural Portfolio</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        :root {
            --primary-color: #2c3e50;
            --secondary-color: #3498db;
            --light-color: #ecf0f1;
            --dark-color: #2c3e50;
            --text-color: #333;
            --text-light: #fff;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--light-color);
            color: var(--text-color);
            line-height: 1.6;
        }

        header {
            background-color: var(--primary-color);
            color: var(--text-light);
            padding: 1rem 2rem;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--text-light);
            text-decoration: none;
        }

        .nav-links {
            display: flex;
            list-style: none;
        }

        .nav-links li {
            margin-left: 2rem;
        }

        .nav-links a {
            color: var(--text-light);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s;
        }

        .nav-links a:hover {
            color: var(--secondary-color);
        }

        .hero {
            height: 100vh;
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('https://images.unsplash.com/photo-1487958449943-2429e8be8625?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80') no-repeat center center/cover;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            color: var(--text-light);
            padding: 0 2rem;
            margin-top: 60px;
        }

        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 1rem;
        }

        .hero p {
            font-size: 1.2rem;
            max-width: 800px;
            margin-bottom: 2rem;
        }

        .btn {
            display: inline-block;
            background-color: var(--secondary-color);
            color: var(--text-light);
            padding: 0.8rem 2rem;
            border: none;
            border-radius: 5px;
            font-size: 1rem;
            cursor: pointer;
            transition: background-color 0.3s;
            text-decoration: none;
        }

        .btn:hover {
            background-color: #2980b9;
        }

        .portfolio {
            padding: 5rem 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .section-title {
            text-align: center;
            margin-bottom: 3rem;
        }

        .section-title h2 {
            font-size: 2.5rem;
            color: var(--dark-color);
            margin-bottom: 1rem;
        }

        .section-title p {
            color: #666;
            max-width: 700px;
            margin: 0 auto;
        }

        .projects {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 2rem;
        }

        .project-card {
            background-color: #fff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .project-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
        }

        .project-img {
            height: 250px;
            overflow: hidden;
        }

        .project-img img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s;
        }

        .project-card:hover .project-img img {
            transform: scale(1.1);
        }

        .project-info {
            padding: 1.5rem;
        }

        .project-info h3 {
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
            color: var(--dark-color);
        }

        .project-info p {
            color: #666;
            margin-bottom: 1rem;
        }

        .project-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 1rem;
        }

        .tag {
            background-color: var(--light-color);
            color: var(--dark-color);
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 500;
        }

        .project-link {
            display: inline-block;
            color: var(--secondary-color);
            font-weight: 600;
            text-decoration: none;
            transition: color 0.3s;
        }

        .project-link:hover {
            color: #2980b9;
        }

        footer {
            background-color: var(--dark-color);
            color: var(--text-light);
            padding: 3rem 2rem;
            text-align: center;
        }

        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            text-align: left;
        }

        .footer-column h3 {
            font-size: 1.3rem;
            margin-bottom: 1.5rem;
            position: relative;
            padding-bottom: 0.5rem;
        }

        .footer-column h3::after {
            content: '';
            position: absolute;
            left: 0;
            bottom: 0;
            width: 50px;
            height: 2px;
            background-color: var(--secondary-color);
        }

        .footer-column p {
            margin-bottom: 1rem;
        }

        .social-links {
            display: flex;
            gap: 1rem;
        }

        .social-links a {
            color: var(--text-light);
            font-size: 1.2rem;
            transition: color 0.3s;
        }

        .social-links a:hover {
            color: var(--secondary-color);
        }

        .copyright {
            margin-top: 3rem;
            padding-top: 1.5rem;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }

        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2.5rem;
            }

            .hero p {
                font-size: 1rem;
            }

            .nav-links {
                display: none;
            }

            .projects {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <a href="#" class="logo">ARCHISTUDIO</a>
            <ul class="nav-links">
                <li><a href="#">Home</a></li>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <section class="hero">
        <h1>Innovative Architectural Designs</h1>
        <p>We create spaces that inspire, transform, and elevate human experience through thoughtful design and meticulous craftsmanship.</p>
        <a href="#portfolio" class="btn">View Our Work</a>
    </section>

    <section id="portfolio" class="portfolio">
