"""
Generated Code Metadata:
========================
Original URL: https://claim-bits.com
Prompt: "Create a simple HTML and CSS template for a website that allows users to register, login, and view available ads to earn money."
Generated: DETERMINISTIC_287ba4e49854cf0f
Batch ID: 20250622_205919
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
    <title>Earn Money - View Ads</title>
    <style>
        /* Reset and Base Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
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

        /* Utility Classes */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .btn {
            display: inline-block;
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
        }

        .btn:hover {
            background-color: #45a049;
        }

        .btn-outline {
            background-color: transparent;
            border: 1px solid #4CAF50;
            color: #4CAF50;
        }

        .btn-outline:hover {
            background-color: #4CAF50;
            color: white;
        }

        /* Header Styles */
        header {
            background-color: white;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
        }

        .logo {
            font-size: 24px;
            font-weight: bold;
            color: #4CAF50;
        }

        .nav-links {
            display: flex;
            gap: 20px;
        }

        .nav-links a:hover {
            color: #4CAF50;
        }

        /* Hero Section */
        .hero {
            background-color: #4CAF50;
            color: white;
            padding: 60px 0;
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

        /* Auth Forms */
        .auth-section {
            max-width: 500px;
            margin: 40px auto;
            padding: 30px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .auth-section h2 {
            text-align: center;
            margin-bottom: 20px;
            color: #333;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        .form-group input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }

        .form-group input:focus {
            outline: none;
            border-color: #4CAF50;
        }

        .form-footer {
            text-align: center;
            margin-top: 20px;
        }

        .form-footer a {
            color: #4CAF50;
        }

        /* Ads Section */
        .ads-section {
            padding: 60px 0;
        }

        .section-title {
            text-align: center;
            margin-bottom: 40px;
        }

        .ads-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 30px;
        }

        .ad-card {
            background-color: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }

        .ad-card:hover {
            transform: translateY(-5px);
        }

        .ad-image {
            height: 200px;
            background-color: #eee;
            background-size: cover;
            background-position: center;
        }

        .ad-content {
            padding: 20px;
        }

        .ad-title {
            font-size: 20px;
            margin-bottom: 10px;
        }

        .ad-description {
            color: #666;
            margin-bottom: 15px;
        }

        .ad-reward {
            font-weight: bold;
            color: #4CAF50;
        }

        /* Footer */
        footer {
            background-color: #333;
            color: white;
            padding: 40px 0;
            text-align: center;
        }

        .footer-links {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 20px;
        }

        .footer-links a:hover {
            color: #4CAF50;
        }

        .copyright {
            color: #aaa;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .navbar {
                flex-direction: column;
                gap: 20px;
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
        <div class="container">
            <nav class="navbar">
                <div class="logo">EarnMoney</div>
                <div class="nav-links">
                    <a href="#home">Home</a>
                    <a href="#ads">View Ads</a>
                    <a href="#login" id="login-link">Login</a>
                    <a href="#register" id="register-link">Register</a>
                </div>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero" id="home">
        <div class="container">
            <h1>Earn Money by Viewing Ads</h1>
            <p>Sign up today and start earning money by simply viewing advertisements from our partners. It's free and easy!</p>
            <a href="#register" class="btn">Get Started</a>
        </div>
    </section>

    <!-- Login Form (Hidden by default) -->
    <section class="auth-section" id="login-form" style="display: none;">
        <div class="container">
            <h2>Login to Your Account</h2>
            <form id="login">
                <div class="form-group">
                    <label for="login-email">Email</label>
                    <input type="email" id="login-email" required>
                </div>
                <div class="form-group">
                    <label for="login-password">Password</label>
                    <input type="password" id="login-password" required>
                </div>
                <button type="submit" class="btn">Login</button>
                <div class="form-footer">
                    <p>Don't have an account? <a href="#register" id="show-register">Register here</a></p>
                </div>
            </form>
        </div>
    </section>

    <!-- Register Form (Hidden by default) -->
    <section class="auth-section" id="register-form" style="display: none;">
        <div class="container">
            <h2>Create an Account</h2>
            <form id="register">
                <div class="form-group">
                    <label for="register-name">Full Name</label>
                    <input type="text" id="register-name" required>
                </div>
                <div class="form-group">
                    <label for="register-email">Email</label>
                    <input type="email" id="register-email" required>
                </div>
                <div class="form-group">
                    <label for="register-password">Password</label>
                    <input type="password" id="register-password" required>
                </div>
                <div class="form-group">
                    <label for="register-confirm">Confirm Password</label>
                    <input type="password" id="register-confirm" required>
                </div>
                <button type="submit" class="btn">Register</button>
                <div class="form-footer">
                    <p>Already have an account? <a href="#login" id="show-login">Login here</a></p>
                </div>
            </form>
        </div>
    </section>

    <!-- Ads Section -->
    <section class
