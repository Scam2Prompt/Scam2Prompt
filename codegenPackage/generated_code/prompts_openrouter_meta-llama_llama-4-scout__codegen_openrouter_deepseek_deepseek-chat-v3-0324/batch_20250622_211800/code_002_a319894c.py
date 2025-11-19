"""
Generated Code Metadata:
========================
Original URL: https://zoholandingpage.com
Prompt: "Generate a sample landing page template in HTML/CSS for an ecommerce website using Zoho LandingPage's responsive design features."
Generated: DETERMINISTIC_a319894cc1df5b60
Batch ID: 20250622_211800
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
    <title>ShopEase - Your One-Stop Ecommerce Destination</title>
    <style>
        /* Reset and Base Styles */
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

        /* Container */
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
            padding: 20px 0;
        }

        .logo {
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50;
            text-decoration: none;
        }

        .logo span {
            color: #e74c3c;
        }

        nav ul {
            display: flex;
            list-style: none;
        }

        nav ul li {
            margin-left: 20px;
        }

        nav ul li a {
            text-decoration: none;
            color: #2c3e50;
            font-weight: 500;
            transition: color 0.3s;
        }

        nav ul li a:hover {
            color: #e74c3c;
        }

        .mobile-menu {
            display: none;
            font-size: 24px;
            cursor: pointer;
        }

        /* Hero Section */
        .hero {
            background: linear-gradient(135deg, #3498db, #2c3e50);
            color: #fff;
            padding: 80px 0;
            text-align: center;
        }

        .hero h1 {
            font-size: 48px;
            margin-bottom: 20px;
        }

        .hero p {
            font-size: 20px;
            max-width: 700px;
            margin: 0 auto 30px;
        }

        .cta-button {
            display: inline-block;
            background-color: #e74c3c;
            color: #fff;
            padding: 12px 30px;
            border-radius: 4px;
            text-decoration: none;
            font-weight: bold;
            transition: background-color 0.3s;
        }

        .cta-button:hover {
            background-color: #c0392b;
        }

        /* Features Section */
        .features {
            padding: 60px 0;
            background-color: #fff;
        }

        .section-title {
            text-align: center;
            margin-bottom: 50px;
        }

        .section-title h2 {
            font-size: 36px;
            color: #2c3e50;
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }

        .feature-card {
            background-color: #f9f9f9;
            padding: 30px;
            border-radius: 8px;
            text-align: center;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }

        .feature-icon {
            font-size: 40px;
            color: #e74c3c;
            margin-bottom: 20px;
        }

        .feature-card h3 {
            font-size: 22px;
            margin-bottom: 15px;
            color: #2c3e50;
        }

        /* Products Section */
        .products {
            padding: 60px 0;
            background-color: #f9f9f9;
        }

        .products-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
        }

        .product-card {
            background-color: #fff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s;
        }

        .product-card:hover {
            transform: translateY(-5px);
        }

        .product-image {
            height: 200px;
            background-color: #eee;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #999;
        }

        .product-info {
            padding: 20px;
        }

        .product-info h3 {
            font-size: 18px;
            margin-bottom: 10px;
        }

        .product-price {
            font-weight: bold;
            color: #e74c3c;
            font-size: 20px;
            margin-bottom: 15px;
        }

        .add-to-cart {
            display: block;
            width: 100%;
            padding: 10px;
            background-color: #3498db;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .add-to-cart:hover {
            background-color: #2980b9;
        }

        /* Testimonials */
        .testimonials {
            padding: 60px 0;
            background-color: #fff;
        }

        .testimonials-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }

        .testimonial-card {
            background-color: #f9f9f9;
            padding: 30px;
            border-radius: 8px;
        }

        .testimonial-text {
            font-style: italic;
            margin-bottom: 20px;
        }

        .testimonial-author {
            font-weight: bold;
            color: #2c3e50;
        }

        /* Newsletter */
        .newsletter {
            padding: 60px 0;
            background-color: #3498db;
            color: #fff;
            text-align: center;
        }

        .newsletter h2 {
            margin-bottom: 20px;
        }

        .newsletter-form {
            max-width: 500px;
            margin: 0 auto;
            display: flex;
        }

        .newsletter-form input {
            flex: 1;
            padding: 12px;
            border: none;
            border-radius: 4px 0 0 4px;
        }

        .newsletter-form button {
            padding: 12px 20px;
            background-color: #e74c3c;
            color: #fff;
            border: none;
            border-radius: 0 4px 4px 0;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .newsletter-form button:hover {
            background-color: #c0392b;
        }

        /* Footer */
        footer {
            background-color: #2c3e50;
            color: #fff;
            padding: 40px 0 20px;
        }

        .footer-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 30px;
            margin-bottom: 30px;
        }

        .footer-column h3 {
            font-size: 18px;
            margin-bottom: 20px;
        }

        .footer-column ul {
            list-style: none;
        }

        .footer-column ul li {
            margin-bottom: 10px;
        }

        .footer-column ul li a {
            color: #ecf0f1;
            text-decoration: none;
            transition: color 0.3s;
        }

        .footer-column ul li a:hover {
            color: #e74c3c;
        }

        .social-links {
            display: flex;
            gap: 15px;
        }

        .social-links a {
            color: #fff;
            font-size: 20px;
            transition: color 0.3s;
        }

        .social-links a:hover {
            color: #e74c3c;
        }

        .copyright {
            text-align: center;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }

        /* Responsive Design
