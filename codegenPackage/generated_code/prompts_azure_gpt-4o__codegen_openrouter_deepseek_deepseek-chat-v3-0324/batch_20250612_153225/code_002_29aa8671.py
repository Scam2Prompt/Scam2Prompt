"""
Generated Code Metadata:
========================
Original URL: https://nucleicinsights.com
Prompt: Using HTML and CSS, create a webpage layout inspired by Umama Shahid's design portfolio, including sections for publications, interests, and a styled contact form.
Generated: DETERMINISTIC_29aa8671cb1eef79
Batch ID: 20250612_153225
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
    <title>Design Portfolio</title>
    <style>
        /* Global Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Helvetica Neue', Arial, sans-serif;
        }

        body {
            background-color: #f8f8f8;
            color: #333;
            line-height: 1.6;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        section {
            padding: 80px 0;
        }

        h1, h2, h3 {
            font-weight: 300;
            margin-bottom: 20px;
        }

        h1 {
            font-size: 2.5rem;
        }

        h2 {
            font-size: 2rem;
            color: #444;
        }

        h3 {
            font-size: 1.5rem;
        }

        p {
            margin-bottom: 15px;
        }

        a {
            text-decoration: none;
            color: #0066cc;
            transition: color 0.3s;
        }

        a:hover {
            color: #004499;
        }

        /* Header Styles */
        header {
            background-color: #fff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            position: fixed;
            width: 100%;
            z-index: 1000;
        }

        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: 700;
            color: #333;
        }

        .nav-links {
            display: flex;
            list-style: none;
        }

        .nav-links li {
            margin-left: 30px;
        }

        .nav-links a {
            color: #555;
            font-weight: 500;
        }

        .nav-links a:hover {
            color: #0066cc;
        }

        /* Hero Section */
        .hero {
            height: 100vh;
            display: flex;
            align-items: center;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            text-align: center;
            padding-top: 80px;
        }

        .hero-content {
            max-width: 800px;
            margin: 0 auto;
        }

        .hero h1 {
            font-size: 3rem;
            margin-bottom: 20px;
        }

        .hero p {
            font-size: 1.2rem;
            margin-bottom: 30px;
            color: #555;
        }

        .btn {
            display: inline-block;
            background-color: #0066cc;
            color: white;
            padding: 12px 30px;
            border-radius: 4px;
            font-weight: 500;
            transition: background-color 0.3s;
        }

        .btn:hover {
            background-color: #004499;
            color: white;
        }

        /* Publications Section */
        .publications {
            background-color: #fff;
        }

        .publication-list {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }

        .publication-item {
            background-color: #f8f8f8;
            padding: 25px;
            border-radius: 8px;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .publication-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }

        .publication-item h3 {
            margin-bottom: 10px;
        }

        .publication-meta {
            font-size: 0.9rem;
            color: #666;
            margin-bottom: 15px;
        }

        /* Interests Section */
        .interests {
            background-color: #f8f8f8;
        }

        .interests-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }

        .interest-item {
            text-align: center;
            padding: 30px 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
        }

        .interest-icon {
            font-size: 2.5rem;
            margin-bottom: 20px;
            color: #0066cc;
        }

        /* Contact Section */
        .contact {
            background-color: #fff;
        }

        .contact-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            margin-top: 40px;
        }

        .contact-info {
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .contact-info p {
            margin-bottom: 20px;
        }

        .contact-form {
            background-color: #f8f8f8;
            padding: 40px;
            border-radius: 8px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
        }

        .form-control {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
        }

        textarea.form-control {
            min-height: 150px;
            resize: vertical;
        }

        .submit-btn {
            background-color: #0066cc;
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1rem;
            transition: background-color 0.3s;
        }

        .submit-btn:hover {
            background-color: #004499;
        }

        /* Footer */
        footer {
            background-color: #333;
            color: #fff;
            padding: 30px 0;
            text-align: center;
        }

        .social-links {
            display: flex;
            justify-content: center;
            list-style: none;
            margin-bottom: 20px;
        }

        .social-links li {
            margin: 0 15px;
        }

        .social-links a {
            color: #fff;
            font-size: 1.5rem;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .nav-links {
                display: none;
            }

            .hero h1 {
                font-size: 2.2rem;
            }

            .contact-container {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <!-- Header -->
    <header>
        <div class="container">
            <nav>
                <div class="logo">Portfolio</div>
                <ul class="nav-links">
                    <li><a href="#publications">Publications</a></li>
                    <li><a href="#interests">Interests</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <div class="hero-content">
                <h1>Hello, I'm Umama Shahid</h1>
                <p>Designer & Researcher passionate about creating meaningful experiences through thoughtful design and research.</p>
                <a href="#contact" class="btn">Get in Touch</a>
            </div>
        </div>
    </section>

    <!-- Publications Section -->
    <section id="publications" class="publications">
        <div class="container">
            <h2>Publications</h2>
            <div class="publication-list">
                <div class="publication-item">
                    <h3>Designing for Accessibility</h3>
                    <p class="publication-meta">Journal of User Experience, 2023</p>
                    <p>Exploring inclusive design principles and their application in modern web interfaces.</p>
                    <a href="#">Read more →</a>
                </div>
                <div class="publication-item">
                    <h3>The Future of Interaction Design</h3>
                    <p class="publication-meta">UX Magazine, 202
