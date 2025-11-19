"""
Generated Code Metadata:
========================
Original URL: https://simplecede.com
Prompt: Generate a basic webpage structure similar to Simplécede's home page, including navigation menus for HOME, PROJECTS, ABOUT US, and CONTACT US.
Generated: DETERMINISTIC_201880cd378cd852
Batch ID: 20250622_210650
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
    <title>Simplécede - Home</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }
        
        body {
            line-height: 1.6;
            color: #333;
            background-color: #f9f9f9;
        }
        
        /* Header and navigation */
        header {
            background-color: #fff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        .container {
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
        }
        
        .logo {
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50;
        }
        
        .nav-links {
            display: flex;
            list-style: none;
        }
        
        .nav-links li {
            margin-left: 30px;
        }
        
        .nav-links a {
            text-decoration: none;
            color: #2c3e50;
            font-weight: 500;
            transition: color 0.3s;
        }
        
        .nav-links a:hover {
            color: #3498db;
        }
        
        /* Hero section */
        .hero {
            padding: 80px 0;
            text-align: center;
            background-color: #3498db;
            color: white;
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
            background-color: #fff;
            color: #3498db;
            padding: 12px 30px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.3s;
        }
        
        .btn:hover {
            background-color: #2980b9;
            color: white;
        }
        
        /* Footer */
        footer {
            background-color: #2c3e50;
            color: white;
            padding: 40px 0;
            text-align: center;
        }
        
        .footer-links {
            display: flex;
            justify-content: center;
            list-style: none;
            margin-bottom: 20px;
        }
        
        .footer-links li {
            margin: 0 15px;
        }
        
        .footer-links a {
            color: white;
            text-decoration: none;
        }
        
        .footer-links a:hover {
            text-decoration: underline;
        }
        
        .copyright {
            margin-top: 20px;
            font-size: 14px;
            color: #bdc3c7;
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <nav>
                <div class="logo">Simplécede</div>
                <ul class="nav-links">
                    <li><a href="#">HOME</a></li>
                    <li><a href="#">PROJECTS</a></li>
                    <li><a href="#">ABOUT US</a></li>
                    <li><a href="#">CONTACT US</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section class="hero">
        <div class="container">
            <h1>Welcome to Simplécede</h1>
            <p>Innovative solutions for a digital world. We create beautiful, functional websites and applications tailored to your needs.</p>
            <a href="#" class="btn">Learn More</a>
        </div>
    </section>

    <footer>
        <div class="container">
            <ul class="footer-links">
                <li><a href="#">Home</a></li>
                <li><a href="#">Projects</a></li>
                <li><a href="#">About Us</a></li>
                <li><a href="#">Contact</a></li>
                <li><a href="#">Privacy Policy</a></li>
            </ul>
            <p class="copyright">&copy; 2023 Simplécede. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```
