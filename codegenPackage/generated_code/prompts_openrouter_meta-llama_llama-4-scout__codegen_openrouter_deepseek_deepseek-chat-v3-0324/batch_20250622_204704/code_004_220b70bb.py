"""
Generated Code Metadata:
========================
Original URL: https://wir-c5v.pages.dev
Prompt: "Design a basic HTML/CSS template for a help and support page of a cryptocurrency exchange, inspired by WazirX's layout and features."
Generated: DETERMINISTIC_220b70bbe13a8e4a
Batch ID: 20250622_204704
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
    <title>CryptoExchange | Help & Support</title>
    <style>
        /* Reset and Base Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f8f9fa;
            color: #333;
            line-height: 1.6;
        }

        /* Header Styles */
        header {
            background-color: #1a1a2e;
            color: white;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: #4cc9f0;
        }

        nav ul {
            display: flex;
            list-style: none;
        }

        nav ul li {
            margin-left: 1.5rem;
        }

        nav ul li a {
            color: white;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s;
        }

        nav ul li a:hover {
            color: #4cc9f0;
        }

        .auth-buttons button {
            padding: 0.5rem 1rem;
            margin-left: 0.5rem;
            border: none;
            border-radius: 4px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s;
        }

        .login-btn {
            background-color: transparent;
            color: white;
            border: 1px solid white;
        }

        .login-btn:hover {
            background-color: rgba(255, 255, 255, 0.1);
        }

        .signup-btn {
            background-color: #4cc9f0;
            color: #1a1a2e;
        }

        .signup-btn:hover {
            background-color: #3aa8d8;
        }

        /* Main Content Styles */
        main {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 2rem;
        }

        .help-header {
            text-align: center;
            margin-bottom: 3rem;
        }

        .help-header h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: #1a1a2e;
        }

        .help-header p {
            color: #666;
            max-width: 700px;
            margin: 0 auto;
        }

        .search-container {
            max-width: 600px;
            margin: 0 auto 3rem;
            position: relative;
        }

        .search-container input {
            width: 100%;
            padding: 1rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
            padding-left: 3rem;
        }

        .search-container::before {
            content: "🔍";
            position: absolute;
            left: 1rem;
            top: 50%;
            transform: translateY(-50%);
            font-size: 1rem;
        }

        .categories {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }

        .category-card {
            background-color: white;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .category-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        .category-card h3 {
            margin-bottom: 1rem;
            color: #1a1a2e;
        }

        .category-card ul {
            list-style: none;
        }

        .category-card ul li {
            margin-bottom: 0.5rem;
        }

        .category-card ul li a {
            color: #4cc9f0;
            text-decoration: none;
        }

        .category-card ul li a:hover {
            text-decoration: underline;
        }

        .faq-section h2 {
            margin-bottom: 1.5rem;
            color: #1a1a2e;
        }

        .faq-item {
            background-color: white;
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        }

        .faq-question {
            font-weight: 600;
            margin-bottom: 0.5rem;
            color: #1a1a2e;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .faq-answer {
            color: #666;
            padding-top: 0.5rem;
            display: none;
        }

        .faq-item.active .faq-answer {
            display: block;
        }

        .contact-section {
            background-color: white;
            border-radius: 8px;
            padding: 2rem;
            margin-top: 3rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        }

        .contact-section h2 {
            margin-bottom: 1.5rem;
            color: #1a1a2e;
        }

        .contact-methods {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 2rem;
        }

        .contact-method {
            display: flex;
            align-items: center;
        }

        .contact-icon {
            font-size: 1.5rem;
            margin-right: 1rem;
            color: #4cc9f0;
        }

        .contact-info h4 {
            margin-bottom: 0.3rem;
            color: #1a1a2e;
        }

        .contact-info p {
            color: #666;
        }

        /* Footer Styles */
        footer {
            background-color: #1a1a2e;
            color: white;
            padding: 3rem 2rem;
            margin-top: 3rem;
        }

        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 2rem;
        }

        .footer-column h3 {
            color: #4cc9f0;
            margin-bottom: 1rem;
            font-size: 1.1rem;
        }

        .footer-column ul {
            list-style: none;
        }

        .footer-column ul li {
            margin-bottom: 0.5rem;
        }

        .footer-column ul li a {
            color: #ddd;
            text-decoration: none;
            transition: color 0.3s;
        }

        .footer-column ul li a:hover {
            color: #4cc9f0;
        }

        .social-links {
            display: flex;
            gap: 1rem;
            margin-top: 1rem;
        }

        .social-links a {
            color: white;
            font-size: 1.2rem;
            transition: color 0.3s;
        }

        .social-links a:hover {
            color: #4cc9f0;
        }

        .copyright {
            text-align: center;
            margin-top: 3rem;
            padding-top: 1.5rem;
            border-top: 1px solid #333;
            color: #999;
            font-size: 0.9rem;
        }

        /* Responsive Styles */
        @media (max-width: 768px) {
            header {
                flex-direction: column;
                padding: 1rem;
            }

            nav ul {
                margin-top: 1rem;
            }

            .auth-buttons {
                margin-top: 1rem;
            }

            .help-header h1 {
                font-size: 2rem;
            }

            .categories {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">CryptoExchange</div>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li
