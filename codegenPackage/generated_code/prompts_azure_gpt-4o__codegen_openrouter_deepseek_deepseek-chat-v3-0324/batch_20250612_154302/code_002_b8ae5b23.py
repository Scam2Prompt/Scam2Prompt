"""
Generated Code Metadata:
========================
Original URL: https://vagopros.com
Prompt: Generate code to design a responsive website layout that aligns with Vagopros' web design services and branding strategies.
Generated: DETERMINISTIC_b8ae5b23edda9e64
Batch ID: 20250612_154302
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
    <title>Vagopros - Web Design Services</title>
    <style>
        /* Global Styles */
        :root {
            --primary-color: #2a4365;
            --secondary-color: #4299e1;
            --accent-color: #f6ad55;
            --text-color: #2d3748;
            --light-bg: #f7fafc;
            --white: #ffffff;
            --transition: all 0.3s ease;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--light-bg);
        }

        a {
            text-decoration: none;
            color: var(--primary-color);
            transition: var(--transition);
        }

        a:hover {
            color: var(--accent-color);
        }

        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .btn {
            display: inline-block;
            padding: 10px 20px;
            background-color: var(--primary-color);
            color: var(--white);
            border-radius: 4px;
            transition: var(--transition);
            border: none;
            cursor: pointer;
            font-weight: 600;
        }

        .btn:hover {
            background-color: var(--secondary-color);
            transform: translateY(-2px);
        }

        .btn-accent {
            background-color: var(--accent-color);
            color: var(--text-color);
        }

        .btn-accent:hover {
            background-color: #e69c3e;
        }

        /* Header Styles */
        header {
            background-color: var(--white);
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            position: sticky;
            top: 0;
            z-index: 100;
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
            color: var(--primary-color);
        }

        .logo span {
            color: var(--accent-color);
        }

        nav ul {
            display: flex;
            list-style: none;
        }

        nav ul li {
            margin-left: 30px;
        }

        nav ul li a {
            font-weight: 600;
        }

        .mobile-menu-btn {
            display: none;
            background: none;
            border: none;
            font-size: 24px;
            cursor: pointer;
            color: var(--primary-color);
        }

        /* Hero Section */
        .hero {
            padding: 80px 0;
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: var(--white);
            text-align: center;
        }

        .hero h1 {
            font-size: 2.5rem;
            margin-bottom: 20px;
        }

        .hero p {
            font-size: 1.2rem;
            max-width: 700px;
            margin: 0 auto 30px;
        }

        /* Services Section */
        .services {
            padding: 80px 0;
        }

        .section-title {
            text-align: center;
            margin-bottom: 50px;
        }

        .section-title h2 {
            font-size: 2rem;
            color: var(--primary-color);
            margin-bottom: 15px;
        }

        .section-title p {
            max-width: 700px;
            margin: 0 auto;
        }

        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }

        .service-card {
            background-color: var(--white);
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
            transition: var(--transition);
        }

        .service-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
        }

        .service-img {
            height: 200px;
            background-color: var(--secondary-color);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--white);
            font-size: 3rem;
        }

        .service-content {
            padding: 20px;
        }

        .service-content h3 {
            margin-bottom: 15px;
            color: var(--primary-color);
        }

        /* About Section */
        .about {
            padding: 80px 0;
            background-color: var(--white);
        }

        .about-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            align-items: center;
        }

        .about-text h2 {
            font-size: 2rem;
            color: var(--primary-color);
            margin-bottom: 20px;
        }

        .about-text p {
            margin-bottom: 20px;
        }

        .about-image {
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }

        .about-image img {
            width: 100%;
            height: auto;
            display: block;
        }

        /* Testimonials */
        .testimonials {
            padding: 80px 0;
            background-color: var(--light-bg);
        }

        .testimonials-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }

        .testimonial-card {
            background-color: var(--white);
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
        }

        .testimonial-text {
            font-style: italic;
            margin-bottom: 20px;
        }

        .testimonial-author {
            display: flex;
            align-items: center;
        }

        .author-img {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background-color: var(--secondary-color);
            margin-right: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--white);
            font-weight: bold;
        }

        .author-info h4 {
            color: var(--primary-color);
            margin-bottom: 5px;
        }

        .author-info p {
            font-size: 0.9rem;
            color: #718096;
        }

        /* Contact Section */
        .contact {
            padding: 80px 0;
            background-color: var(--white);
        }

        .contact-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
        }

        .contact-info h3 {
            font-size: 1.5rem;
            color: var(--primary-color);
            margin-bottom: 20px;
        }

        .contact-info p {
            margin-bottom: 30px;
        }

        .contact-details {
            margin-bottom: 30px;
        }

        .contact-item {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
        }

        .contact-icon {
            width: 40px;
            height: 40px;
            background-color: var(--light-bg);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 15px;
            color: var(--primary-color);
        }

        .contact-form input,
        .contact-form textarea {
            width: 100%;
            padding: 12px 15px;
            margin-bottom: 20px;
            border: 1px solid #e2e8f0;
            border-radius: 4px;
            font-family: inherit;
            transition: var(--transition);
        }

        .contact-form input:focus,
        .contact-form textarea:focus {
            outline: none;
            border-color: var(--secondary-color);
            box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.2);
        }

        .contact-form textarea {
            min-height: 150px;
            resize: vertical;
        }

        /* Footer */
