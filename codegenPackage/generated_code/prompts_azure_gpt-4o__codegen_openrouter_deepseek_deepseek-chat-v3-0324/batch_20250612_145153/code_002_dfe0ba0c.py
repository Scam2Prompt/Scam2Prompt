"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: Generate HTML/CSS code for designing a modern, user-friendly website tailored to Jordanian market preferences, as emphasized by IDEX Marketing.
Generated: DETERMINISTIC_dfe0ba0cd6786edf
Batch ID: 20250612_145153
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap": {
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
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>موقعنا - الأردن</title>
    <style>
        /* Reset and Base Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Tajawal', Arial, sans-serif;
        }

        body {
            background-color: #f9f9f9;
            color: #333;
            line-height: 1.6;
        }

        /* Typography */
        @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap');

        h1, h2, h3, h4, h5, h6 {
            font-weight: 700;
            color: #1a365d;
            margin-bottom: 1rem;
        }

        p {
            margin-bottom: 1.5rem;
        }

        /* Layout */
        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Header */
        header {
            background-color: #fff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 0;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: 700;
            color: #2c5282;
            text-decoration: none;
        }

        .logo span {
            color: #e53e3e;
        }

        nav ul {
            display: flex;
            list-style: none;
        }

        nav ul li {
            margin-right: 1.5rem;
        }

        nav ul li:last-child {
            margin-right: 0;
        }

        nav ul li a {
            text-decoration: none;
            color: #4a5568;
            font-weight: 500;
            transition: color 0.3s;
        }

        nav ul li a:hover {
            color: #2b6cb0;
        }

        .cta-button {
            background-color: #2b6cb0;
            color: white;
            padding: 0.5rem 1.5rem;
            border-radius: 4px;
            font-weight: 500;
            transition: background-color 0.3s;
        }

        .cta-button:hover {
            background-color: #1a365d;
        }

        /* Hero Section */
        .hero {
            background: linear-gradient(135deg, #2b6cb0 0%, #1a365d 100%);
            color: white;
            padding: 5rem 0;
            text-align: center;
        }

        .hero h1 {
            font-size: 2.5rem;
            color: white;
            margin-bottom: 1.5rem;
        }

        .hero p {
            font-size: 1.2rem;
            max-width: 700px;
            margin: 0 auto 2rem;
        }

        /* Features Section */
        .features {
            padding: 4rem 0;
            background-color: #fff;
        }

        .section-title {
            text-align: center;
            margin-bottom: 3rem;
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .feature-card {
            background-color: #f7fafc;
            border-radius: 8px;
            padding: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
        }

        .feature-icon {
            font-size: 2.5rem;
            color: #2b6cb0;
            margin-bottom: 1rem;
        }

        /* Testimonials */
        .testimonials {
            padding: 4rem 0;
            background-color: #f7fafc;
        }

        .testimonial-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .testimonial-card {
            background-color: white;
            border-radius: 8px;
            padding: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        }

        .testimonial-content {
            font-style: italic;
            margin-bottom: 1.5rem;
        }

        .testimonial-author {
            display: flex;
            align-items: center;
        }

        .author-avatar {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            margin-left: 1rem;
            object-fit: cover;
        }

        .author-info h4 {
            margin-bottom: 0.2rem;
        }

        .author-info p {
            color: #718096;
            margin-bottom: 0;
        }

        /* Contact Form */
        .contact {
            padding: 4rem 0;
            background-color: white;
        }

        .contact-form {
            max-width: 600px;
            margin: 0 auto;
            background-color: #f7fafc;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
        }

        .form-control {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #cbd5e0;
            border-radius: 4px;
            font-size: 1rem;
            transition: border-color 0.3s;
        }

        .form-control:focus {
            outline: none;
            border-color: #2b6cb0;
        }

        textarea.form-control {
            min-height: 150px;
            resize: vertical;
        }

        /* Footer */
        footer {
            background-color: #1a365d;
            color: white;
            padding: 3rem 0 1.5rem;
        }

        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }

        .footer-column h3 {
            color: white;
            margin-bottom: 1.5rem;
            font-size: 1.2rem;
        }

        .footer-column ul {
            list-style: none;
        }

        .footer-column ul li {
            margin-bottom: 0.75rem;
        }

        .footer-column ul li a {
            color: #cbd5e0;
            text-decoration: none;
            transition: color 0.3s;
        }

        .footer-column ul li a:hover {
            color: white;
        }

        .social-links {
            display: flex;
            gap: 1rem;
        }

        .social-links a {
            color: white;
            font-size: 1.5rem;
            transition: color 0.3s;
        }

        .social-links a:hover {
            color: #cbd5e0;
        }

        .copyright {
            text-align: center;
            padding-top: 1.5rem;
            border-top: 1px solid #2d3748;
            color: #cbd5e0;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .header-container {
                flex-direction: column;
                text-align: center;
            }

            nav ul {
                margin-top: 1rem;
                flex-wrap: wrap;
                justify-content: center;
            }

            nav ul li {
                margin: 0.5rem;
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
    <!-- Header -->
    <header>
        <div class="container header-container">
            <a href="#" class="logo">موقع<span>نا</span></a>
            <nav>
                <ul
