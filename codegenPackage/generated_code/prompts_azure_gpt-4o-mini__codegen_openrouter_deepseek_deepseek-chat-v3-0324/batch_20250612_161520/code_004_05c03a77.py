"""
Generated Code Metadata:
========================
Original URL: https://tiburonfishingreels.com
Prompt: Develop a user interface design for a fishing reel product page that highlights the unique features of Tiburon's automatic-shifting reels.
Generated: DETERMINISTIC_05c03a77f7182b2f
Batch ID: 20250612_161520
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://images.unsplash.com/photo-1600267175161-cfaa711b4a81?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css": {
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
    <title>Tiburon Automatic-Shifting Reels | Premium Fishing Gear</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --primary-color: #0056b3;
            --secondary-color: #003366;
            --accent-color: #ff6600;
            --light-color: #f8f9fa;
            --dark-color: #212529;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--light-color);
            color: var(--dark-color);
            line-height: 1.6;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        header {
            background-color: var(--secondary-color);
            color: white;
            padding: 20px 0;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 24px;
            font-weight: bold;
            color: white;
            text-decoration: none;
        }

        .logo span {
            color: var(--accent-color);
        }

        nav ul {
            display: flex;
            list-style: none;
        }

        nav ul li {
            margin-left: 20px;
        }

        nav ul li a {
            color: white;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s;
        }

        nav ul li a:hover {
            color: var(--accent-color);
        }

        .product-hero {
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('https://images.unsplash.com/photo-1600267175161-cfaa711b4a81?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
            background-size: cover;
            background-position: center;
            color: white;
            padding: 100px 0;
            text-align: center;
        }

        .product-hero h1 {
            font-size: 48px;
            margin-bottom: 20px;
        }

        .product-hero p {
            font-size: 20px;
            max-width: 800px;
            margin: 0 auto 30px;
        }

        .btn {
            display: inline-block;
            background-color: var(--accent-color);
            color: white;
            padding: 12px 30px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: bold;
            transition: background-color 0.3s;
            border: none;
            cursor: pointer;
        }

        .btn:hover {
            background-color: #e65c00;
        }

        .product-section {
            padding: 80px 0;
        }

        .section-title {
            text-align: center;
            margin-bottom: 50px;
            color: var(--secondary-color);
        }

        .product-container {
            display: flex;
            flex-wrap: wrap;
            gap: 30px;
            justify-content: center;
        }

        .product-card {
            background: white;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            width: 350px;
            transition: transform 0.3s;
        }

        .product-card:hover {
            transform: translateY(-10px);
        }

        .product-image {
            height: 250px;
            overflow: hidden;
        }

        .product-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s;
        }

        .product-card:hover .product-image img {
            transform: scale(1.1);
        }

        .product-info {
            padding: 20px;
        }

        .product-info h3 {
            font-size: 22px;
            margin-bottom: 10px;
            color: var(--secondary-color);
        }

        .product-info p {
            margin-bottom: 15px;
            color: #666;
        }

        .price {
            font-size: 24px;
            font-weight: bold;
            color: var(--primary-color);
            margin-bottom: 15px;
        }

        .features-section {
            background-color: var(--secondary-color);
            color: white;
            padding: 80px 0;
        }

        .features-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }

        .feature-card {
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            transition: transform 0.3s;
        }

        .feature-card:hover {
            transform: translateY(-5px);
        }

        .feature-icon {
            font-size: 40px;
            margin-bottom: 20px;
            color: var(--accent-color);
        }

        .feature-card h3 {
            margin-bottom: 15px;
            font-size: 22px;
        }

        .testimonials-section {
            padding: 80px 0;
            background-color: white;
        }

        .testimonials-container {
            display: flex;
            flex-wrap: wrap;
            gap: 30px;
            justify-content: center;
        }

        .testimonial-card {
            background: var(--light-color);
            padding: 30px;
            border-radius: 10px;
            width: 350px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
        }

        .testimonial-text {
            font-style: italic;
            margin-bottom: 20px;
        }

        .testimonial-author {
            font-weight: bold;
            color: var(--secondary-color);
        }

        .cta-section {
            background-color: var(--primary-color);
            color: white;
            padding: 80px 0;
            text-align: center;
        }

        .cta-section h2 {
            margin-bottom: 20px;
        }

        .cta-section p {
            max-width: 700px;
            margin: 0 auto 30px;
        }

        footer {
            background-color: var(--dark-color);
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
            font-size: 18px;
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
            color: var(--accent-color);
        }

        .social-links {
            display: flex;
            gap: 15px;
        }

        .social-links a {
            color: white;
            font-size: 20px;
            transition: color 0.3s;
        }

        .social-links a:hover {
            color: var(--accent-color);
        }

        .copyright {
            text-align: center;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            color: #ccc;
            font-size: 14px;
        }

        @media (max-width: 768px) {
            .header-content {
                flex-direction: column;
                text-align: center;
            }

            nav ul {
                margin-top: 20px;
                justify-content: center;
            }

            nav ul li {
                margin: 0 10px;
            }

            .product-hero h1 {
                font-size: 36px;
            }

            .product-hero p {
                font-size: 18px;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container header-content">
            <a href="#"
