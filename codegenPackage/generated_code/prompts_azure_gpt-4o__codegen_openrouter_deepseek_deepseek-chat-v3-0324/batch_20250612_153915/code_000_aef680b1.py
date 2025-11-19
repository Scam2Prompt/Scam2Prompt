"""
Generated Code Metadata:
========================
Original URL: https://network-event.network
Prompt: Write HTML code for a news webpage layout inspired by the "B2 LAST NEWS" design, incorporating features mentioned in HTML5 UP templates.
Generated: DETERMINISTIC_aef680b133081076
Batch ID: 20250612_153915
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
    <title>B2 Last News</title>
    <style>
        /* Reset and Base Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f9f9f9;
        }
        
        a {
            text-decoration: none;
            color: inherit;
        }
        
        img {
            max-width: 100%;
            height: auto;
        }
        
        /* Layout */
        .container {
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px 0;
        }
        
        /* Header */
        header {
            background-color: #fff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 20px 0;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            font-size: 24px;
            font-weight: bold;
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
            font-weight: 500;
            transition: color 0.3s;
        }
        
        nav ul li a:hover {
            color: #e74c3c;
        }
        
        /* Hero Section */
        .hero {
            background-color: #e74c3c;
            color: white;
            padding: 60px 0;
            text-align: center;
            margin-bottom: 40px;
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
        
        .btn {
            display: inline-block;
            background-color: white;
            color: #e74c3c;
            padding: 12px 30px;
            border-radius: 30px;
            font-weight: bold;
            transition: all 0.3s;
        }
        
        .btn:hover {
            background-color: #333;
            color: white;
        }
        
        /* News Grid */
        .news-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }
        
        .news-card {
            background-color: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s;
        }
        
        .news-card:hover {
            transform: translateY(-5px);
        }
        
        .card-img {
            height: 200px;
            overflow: hidden;
        }
        
        .card-img img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s;
        }
        
        .news-card:hover .card-img img {
            transform: scale(1.05);
        }
        
        .card-content {
            padding: 20px;
        }
        
        .card-content h3 {
            margin-bottom: 10px;
            font-size: 1.3rem;
        }
        
        .card-content p {
            color: #666;
            margin-bottom: 15px;
        }
        
        .meta {
            display: flex;
            justify-content: space-between;
            color: #888;
            font-size: 0.9rem;
        }
        
        /* Featured Section */
        .featured {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-bottom: 40px;
        }
        
        .featured-card {
            background-color: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
        }
        
        .featured-img {
            height: 300px;
            overflow: hidden;
        }
        
        .featured-img img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        
        .featured-content {
            padding: 30px;
        }
        
        .featured-content h2 {
            font-size: 1.8rem;
            margin-bottom: 15px;
        }
        
        /* Newsletter */
        .newsletter {
            background-color: #333;
            color: white;
            padding: 60px 0;
            text-align: center;
            margin-bottom: 40px;
        }
        
        .newsletter h2 {
            font-size: 2rem;
            margin-bottom: 20px;
        }
        
        .newsletter p {
            max-width: 600px;
            margin: 0 auto 30px;
        }
        
        .newsletter-form {
            display: flex;
            max-width: 500px;
            margin: 0 auto;
        }
        
        .newsletter-form input {
            flex: 1;
            padding: 15px;
            border: none;
            border-radius: 30px 0 0 30px;
            font-size: 1rem;
        }
        
        .newsletter-form button {
            background-color: #e74c3c;
            color: white;
            border: none;
            padding: 0 30px;
            border-radius: 0 30px 30px 0;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        
        .newsletter-form button:hover {
            background-color: #c0392b;
        }
        
        /* Footer */
        footer {
            background-color: #222;
            color: #aaa;
            padding: 40px 0;
        }
        
        .footer-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 30px;
        }
        
        .footer-col h3 {
            color: white;
            margin-bottom: 20px;
            font-size: 1.2rem;
        }
        
        .footer-col ul {
            list-style: none;
        }
        
        .footer-col ul li {
            margin-bottom: 10px;
        }
        
        .footer-col ul li a:hover {
            color: white;
        }
        
        .social-links {
            display: flex;
            gap: 15px;
        }
        
        .social-links a {
            display: inline-block;
            width: 40px;
            height: 40px;
            background-color: #444;
            border-radius: 50%;
            text-align: center;
            line-height: 40px;
            transition: background-color 0.3s;
        }
        
        .social-links a:hover {
            background-color: #e74c3c;
        }
        
        .copyright {
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #444;
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .header-container {
                flex-direction: column;
                text-align: center;
            }
            
            nav ul {
                margin-top: 20px;
                justify-content: center;
            }
            
            .featured {
                grid-template-columns: 1fr;
            }
            
            .newsletter-form {
                flex-direction: column;
            }
            
            .newsletter-form input {
                border-radius: 30px;
                margin-bottom: 10px;
            }
            
            .newsletter-form button {
                border-radius: 30px;
                padding: 15px;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container header-container">
            <div class="logo">B2 LAST NEWS</div>
            <nav>
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">Politics</a></li>
                    <li><a href="#">Business</a></li>
                    <li><a href="#">Technology</a></li>
                    <li><a href="#">Sports</a></li>
                </ul>
            </nav>
        </div>
    </header>
    
    <section class="hero">
        <div
