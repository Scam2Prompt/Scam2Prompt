"""
Generated Code Metadata:
========================
Original URL: https://styleandmakeupeffect.co.za
Prompt: Create a basic HTML/CSS template for a beauty services website that highlights the artist's portfolio, including sections for bridal makeup and personal styling.
Generated: DETERMINISTIC_18bb6e7056455b85
Batch ID: 20250622_205548
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
    <meta name="description" content="Beauty Services Website showcasing bridal makeup and personal styling portfolio.">
    <title>Beauty Services Portfolio</title>
    <style>
        /* General Reset */
        body, h1, h2, h3, p, ul, li {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f9f9f9;
        }

        header {
            background-color: #ff6f61;
            color: #fff;
            padding: 20px 0;
            text-align: center;
        }

        header h1 {
            font-size: 2.5rem;
        }

        nav {
            margin-top: 10px;
        }

        nav ul {
            list-style: none;
            display: flex;
            justify-content: center;
            gap: 20px;
        }

        nav ul li a {
            text-decoration: none;
            color: #fff;
            font-weight: bold;
        }

        .container {
            max-width: 1200px;
            margin: 20px auto;
            padding: 0 20px;
        }

        .section {
            margin-bottom: 40px;
        }

        .section h2 {
            font-size: 2rem;
            margin-bottom: 20px;
            color: #ff6f61;
        }

        .portfolio {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }

        .portfolio-item {
            flex: 1 1 calc(33.333% - 20px);
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 5px;
            overflow: hidden;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        .portfolio-item img {
            width: 100%;
            height: auto;
        }

        .portfolio-item p {
            padding: 10px;
            text-align: center;
        }

        footer {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 10px 0;
        }

        footer p {
            font-size: 0.9rem;
        }

        @media (max-width: 768px) {
            .portfolio-item {
                flex: 1 1 calc(50% - 20px);
            }
        }

        @media (max-width: 480px) {
            .portfolio-item {
                flex: 1 1 100%;
            }
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <header>
        <h1>Beauty Services Portfolio</h1>
        <nav>
            <ul>
                <li><a href="#bridal-makeup">Bridal Makeup</a></li>
                <li><a href="#personal-styling">Personal Styling</a></li>
            </ul>
        </nav>
    </header>

    <!-- Main Content -->
    <div class="container">
        <!-- Bridal Makeup Section -->
        <section id="bridal-makeup" class="section">
            <h2>Bridal Makeup</h2>
            <div class="portfolio">
                <!-- Portfolio Item -->
                <div class="portfolio-item">
                    <img src="bridal1.jpg" alt="Bridal Makeup Example 1">
                    <p>Elegant Bridal Look</p>
                </div>
                <div class="portfolio-item">
                    <img src="bridal2.jpg" alt="Bridal Makeup Example 2">
                    <p>Classic Bridal Style</p>
                </div>
                <div class="portfolio-item">
                    <img src="bridal3.jpg" alt="Bridal Makeup Example 3">
                    <p>Modern Bridal Glam</p>
                </div>
            </div>
        </section>

        <!-- Personal Styling Section -->
        <section id="personal-styling" class="section">
            <h2>Personal Styling</h2>
            <div class="portfolio">
                <!-- Portfolio Item -->
                <div class="portfolio-item">
                    <img src="styling1.jpg" alt="Personal Styling Example 1">
                    <p>Casual Chic</p>
                </div>
                <div class="portfolio-item">
                    <img src="styling2.jpg" alt="Personal Styling Example 2">
                    <p>Formal Elegance</p>
                </div>
                <div class="portfolio-item">
                    <img src="styling3.jpg" alt="Personal Styling Example 3">
                    <p>Street Style</p>
                </div>
            </div>
        </section>
    </div>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Beauty Services. All rights reserved.</p>
    </footer>
</body>
</html>
```
