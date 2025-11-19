"""
Generated Code Metadata:
========================
Original URL: https://elan-life.com
Prompt: "Design a simple webpage using HTML and CSS to display a photography portfolio with categories for 'Portraits of Cuba', 'Italian Girl', and 'Urban Lifestyle'."
Generated: DETERMINISTIC_6cc3928c0671845b
Batch ID: 20250622_212148
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
    <meta name="description" content="Photography portfolio showcasing categories: Portraits of Cuba, Italian Girl, and Urban Lifestyle.">
    <title>Photography Portfolio</title>
    <style>
        /* General Reset */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f4;
            color: #333;
        }

        header {
            background: #333;
            color: #fff;
            padding: 1rem 0;
            text-align: center;
        }

        header h1 {
            font-size: 2rem;
        }

        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }

        .portfolio-category {
            margin-bottom: 2rem;
        }

        .portfolio-category h2 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: #444;
        }

        .portfolio-category .gallery {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
        }

        .portfolio-category .gallery img {
            width: 100%;
            max-width: 300px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .portfolio-category .gallery img:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
        }

        footer {
            text-align: center;
            padding: 1rem 0;
            background: #333;
            color: #fff;
            margin-top: 2rem;
        }

        footer p {
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <header>
        <h1>Photography Portfolio</h1>
    </header>

    <!-- Main Content -->
    <div class="container">
        <!-- Portraits of Cuba Section -->
        <div class="portfolio-category">
            <h2>Portraits of Cuba</h2>
            <div class="gallery">
                <img src="cuba1.jpg" alt="Portrait of Cuba 1">
                <img src="cuba2.jpg" alt="Portrait of Cuba 2">
                <img src="cuba3.jpg" alt="Portrait of Cuba 3">
            </div>
        </div>

        <!-- Italian Girl Section -->
        <div class="portfolio-category">
            <h2>Italian Girl</h2>
            <div class="gallery">
                <img src="italian1.jpg" alt="Italian Girl 1">
                <img src="italian2.jpg" alt="Italian Girl 2">
                <img src="italian3.jpg" alt="Italian Girl 3">
            </div>
        </div>

        <!-- Urban Lifestyle Section -->
        <div class="portfolio-category">
            <h2>Urban Lifestyle</h2>
            <div class="gallery">
                <img src="urban1.jpg" alt="Urban Lifestyle 1">
                <img src="urban2.jpg" alt="Urban Lifestyle 2">
                <img src="urban3.jpg" alt="Urban Lifestyle 3">
            </div>
        </div>
    </div>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Photography Portfolio. All rights reserved.</p>
    </footer>
</body>
</html>
```
