"""
Generated Code Metadata:
========================
Original URL: https://ashkar2023.github.io
Prompt: Create a clone of a webpage similar to the "ADIDAS clone" described on Muhammed Ashkar's portfolio, using only HTML and CSS. Include transitions and ensure it matches the original design closely.
Generated: DETERMINISTIC_e6c48a681abbc5fa
Batch ID: 20250612_150440
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80": {
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
    <title>ADIDAS Clone</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        /* Reset and Base Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }

        a {
            text-decoration: none;
            color: inherit;
        }

        /* Header Styles */
        header {
            background-color: white;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
        }

        .top-bar {
            background-color: #000;
            color: white;
            padding: 8px 0;
            text-align: center;
            font-size: 12px;
        }

        .main-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 5%;
        }

        .logo {
            font-size: 24px;
            font-weight: bold;
            color: #000;
        }

        .logo span {
            color: #0066cc;
        }

        nav ul {
            display: flex;
            list-style: none;
        }

        nav ul li {
            margin: 0 15px;
            position: relative;
        }

        nav ul li a {
            font-weight: 500;
            transition: color 0.3s ease;
        }

        nav ul li a:hover {
            color: #0066cc;
        }

        .icons {
            display: flex;
            gap: 20px;
        }

        .icons i {
            font-size: 18px;
            cursor: pointer;
            transition: color 0.3s ease;
        }

        .icons i:hover {
            color: #0066cc;
        }

        /* Hero Section */
        .hero {
            margin-top: 80px;
            height: 80vh;
            background: url('https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80') no-repeat center center/cover;
            display: flex;
            align-items: center;
            padding: 0 5%;
            position: relative;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.3);
        }

        .hero-content {
            position: relative;
            z-index: 1;
            color: white;
            max-width: 500px;
        }

        .hero-content h1 {
            font-size: 48px;
            margin-bottom: 20px;
            animation: fadeInUp 1s ease;
        }

        .hero-content p {
            margin-bottom: 30px;
            animation: fadeInUp 1.2s ease;
        }

        .btn {
            display: inline-block;
            padding: 12px 30px;
            background-color: #0066cc;
            color: white;
            border-radius: 30px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: all 0.3s ease;
            animation: fadeInUp 1.4s ease;
        }

        .btn:hover {
            background-color: #0055aa;
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }

        /* Featured Products */
        .featured {
            padding: 80px 5%;
            text-align: center;
        }

        .section-title {
            font-size: 32px;
            margin-bottom: 50px;
            position: relative;
            display: inline-block;
        }

        .section-title::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 50px;
            height: 3px;
            background-color: #0066cc;
        }

        .products {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }

        .product-card {
            background-color: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .product-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
        }

        .product-img {
            height: 250px;
            overflow: hidden;
        }

        .product-img img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }

        .product-card:hover .product-img img {
            transform: scale(1.1);
        }

        .product-info {
            padding: 20px;
        }

        .product-info h3 {
            margin-bottom: 10px;
            font-size: 18px;
        }

        .product-info p {
            color: #666;
            margin-bottom: 15px;
        }

        .price {
            font-weight: bold;
            color: #0066cc;
            font-size: 20px;
        }

        /* Footer */
        footer {
            background-color: #000;
            color: white;
            padding: 50px 5% 20px;
        }

        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
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
            transition: color 0.3s ease;
        }

        .footer-column ul li a:hover {
            color: #0066cc;
        }

        .social-icons {
            display: flex;
            gap: 15px;
            margin-top: 20px;
        }

        .social-icons a {
            color: white;
            font-size: 20px;
            transition: color 0.3s ease;
        }

        .social-icons a:hover {
            color: #0066cc;
        }

        .copyright {
            text-align: center;
            padding-top: 20px;
            border-top: 1px solid #333;
            color: #ccc;
            font-size: 14px;
        }

        /* Animations */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .main-header {
                flex-direction: column;
                padding: 15px;
            }

            nav ul {
                margin: 15px 0;
            }

            .hero {
                height: 60vh;
                text-align: center;
            }

            .hero-content h1 {
                font-size: 36px;
            }

            .products {
                grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
            }
        }

        @media (max-width: 480px) {
            nav ul {
                flex-direction: column;
                align-items: center;
            }

            nav ul li {
                margin: 5px 0;
            }

            .hero {
                height: 50vh;
            }

            .hero-content h1 {
                font-size: 28px;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="
