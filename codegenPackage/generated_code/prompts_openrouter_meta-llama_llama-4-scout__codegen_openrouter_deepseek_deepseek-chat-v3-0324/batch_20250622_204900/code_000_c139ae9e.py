"""
Generated Code Metadata:
========================
Original URL: https://inbetweeners-blue.pages.dev
Prompt: "Write a Shopify-powered e-commerce website for a digital art project called $BLUE by inBetweeners, including sections for shop, artist team, and licensing."
Generated: DETERMINISTIC_c139ae9eeca40f7b
Batch ID: 20250622_204900
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
    <title>$BLUE by inBetweeners | Digital Art Project</title>
    <style>
        /* Global Styles */
        :root {
            --primary-color: #1a73e8;
            --secondary-color: #0d47a1;
            --accent-color: #ff4081;
            --text-color: #333;
            --light-text: #f5f5f5;
            --bg-color: #f9f9f9;
            --dark-bg: #212121;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Helvetica Neue', Arial, sans-serif;
        }
        
        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
        }
        
        a {
            text-decoration: none;
            color: var(--primary-color);
            transition: color 0.3s ease;
        }
        
        a:hover {
            color: var(--secondary-color);
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        /* Header Styles */
        header {
            background-color: var(--dark-bg);
            color: var(--light-text);
            padding: 20px 0;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            font-size: 24px;
            font-weight: bold;
            color: var(--light-text);
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
            color: var(--light-text);
            font-weight: 500;
        }
        
        /* Hero Section */
        .hero {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: var(--light-text);
            padding: 100px 0;
            text-align: center;
        }
        
        .hero h1 {
            font-size: 48px;
            margin-bottom: 20px;
        }
        
        .hero p {
            font-size: 20px;
            max-width: 800px;
            margin: 0 auto 30px;
        }
        
        .btn {
            display: inline-block;
            background-color: var(--accent-color);
            color: var(--light-text);
            padding: 12px 30px;
            border-radius: 30px;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .btn:hover {
            background-color: #e91e63;
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }
        
        /* Shop Section */
        .shop {
            padding: 80px 0;
        }
        
        .section-title {
            text-align: center;
            margin-bottom: 50px;
            font-size: 36px;
        }
        
        .products-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 30px;
        }
        
        .product-card {
            background-color: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        
        .product-card:hover {
            transform: translateY(-10px);
        }
        
        .product-image {
            height: 250px;
            width: 100%;
            object-fit: cover;
        }
        
        .product-info {
            padding: 20px;
        }
        
        .product-title {
            font-size: 18px;
            margin-bottom: 10px;
        }
        
        .product-price {
            font-weight: bold;
            color: var(--primary-color);
            margin-bottom: 15px;
        }
        
        /* Team Section */
        .team {
            padding: 80px 0;
            background-color: var(--dark-bg);
            color: var(--light-text);
        }
        
        .team-members {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 30px;
        }
        
        .team-member {
            text-align: center;
        }
        
        .member-image {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
            margin-bottom: 20px;
            border: 5px solid var(--accent-color);
        }
        
        .member-name {
            font-size: 20px;
            margin-bottom: 10px;
        }
        
        .member-role {
            color: var(--accent-color);
            margin-bottom: 15px;
        }
        
        /* Licensing Section */
        .licensing {
            padding: 80px 0;
        }
        
        .license-options {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 30px;
        }
        
        .license-card {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        
        .license-title {
            font-size: 24px;
            margin-bottom: 15px;
            color: var(--primary-color);
        }
        
        .license-price {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        
        .license-features {
            list-style: none;
            margin-bottom: 25px;
        }
        
        .license-features li {
            margin-bottom: 10px;
            position: relative;
            padding-left: 25px;
        }
        
        .license-features li:before {
            content: "✓";
            color: var(--accent-color);
            position: absolute;
            left: 0;
        }
        
        /* Footer */
        footer {
            background-color: var(--dark-bg);
            color: var(--light-text);
            padding: 50px 0 20px;
        }
        
        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }
        
        .footer-column h3 {
            font-size: 18px;
            margin-bottom: 20px;
            color: var(--accent-color);
        }
        
        .footer-column ul {
            list-style: none;
        }
        
        .footer-column ul li {
            margin-bottom: 10px;
        }
        
        .footer-column ul li a {
            color: var(--light-text);
        }
        
        .copyright {
            text-align: center;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .header-container {
                flex-direction: column;
            }
            
            nav ul {
                margin-top: 20px;
            }
            
            nav ul li {
                margin-left: 15px;
                margin-right: 15px;
            }
            
            .hero h1 {
                font-size: 36px;
            }
            
            .hero p {
                font-size: 18px;
            }
        }
    </style>
</head>
<body>
    <!-- Header -->
    <header>
        <div class="container header-container">
            <div class="logo">$<span>BLUE</span> by inBetweeners</div>
            <nav>
                <ul>
                    <li><a href="#shop">Shop</a></li>
                    <li><a href="#team">Team</a></li>
                    <li><a href="#licensing">Licensing</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h1>Digital Art Redefined</h1>
            <p>$BLUE is a groundbreaking digital art project that
