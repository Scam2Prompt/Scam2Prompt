"""
Generated Code Metadata:
========================
Original URL: https://birafurniture.com
Prompt: Develop a simple HTML/CSS template for a furniture shop homepage that includes sections for exploring different furniture categories, similar to Bira Furniture's design.
Generated: DETERMINISTIC_c75af3d7fd0d9c54
Batch ID: 20250612_162051
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
    <meta name="description" content="Furniture Shop Homepage - Explore various furniture categories">
    <title>Furniture Shop</title>
    <style>
        /* General Reset */
        body, h1, h2, p, ul, li {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f9f9f9;
            color: #333;
        }

        /* Header Section */
        header {
            background-color: #4CAF50;
            color: white;
            padding: 20px 0;
            text-align: center;
        }

        header h1 {
            font-size: 2.5rem;
        }

        /* Navigation Bar */
        nav {
            background-color: #333;
            color: white;
            display: flex;
            justify-content: center;
            padding: 10px 0;
        }

        nav ul {
            list-style: none;
            display: flex;
        }

        nav ul li {
            margin: 0 15px;
        }

        nav ul li a {
            color: white;
            text-decoration: none;
            font-size: 1rem;
        }

        nav ul li a:hover {
            text-decoration: underline;
        }

        /* Main Content */
        main {
            padding: 20px;
        }

        .category-section {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: center;
        }

        .category-card {
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 5px;
            width: 300px;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        .category-card:hover {
            transform: scale(1.05);
        }

        .category-card img {
            width: 100%;
            border-top-left-radius: 5px;
            border-top-right-radius: 5px;
        }

        .category-card h2 {
            font-size: 1.5rem;
            margin: 15px 0;
        }

        .category-card p {
            padding: 0 15px;
            font-size: 1rem;
            color: #666;
        }

        .category-card a {
            display: inline-block;
            margin: 15px 0;
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-size: 1rem;
        }

        .category-card a:hover {
            background-color: #45a049;
        }

        /* Footer Section */
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 10px 0;
            margin-top: 20px;
        }

        footer p {
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <header>
        <h1>Welcome to Furniture Shop</h1>
        <p>Explore our wide range of furniture categories</p>
    </header>

    <!-- Navigation Bar -->
    <nav>
        <ul>
            <li><a href="#living-room">Living Room</a></li>
            <li><a href="#bedroom">Bedroom</a></li>
            <li><a href="#office">Office</a></li>
            <li><a href="#outdoor">Outdoor</a></li>
        </ul>
    </nav>

    <!-- Main Content -->
    <main>
        <section class="category-section">
            <!-- Living Room Category -->
            <div class="category-card" id="living-room">
                <img src="living-room.jpg" alt="Living Room Furniture">
                <h2>Living Room</h2>
                <p>Discover comfortable and stylish furniture for your living room.</p>
                <a href="#">Explore Living Room</a>
            </div>

            <!-- Bedroom Category -->
            <div class="category-card" id="bedroom">
                <img src="bedroom.jpg" alt="Bedroom Furniture">
                <h2>Bedroom</h2>
                <p>Find cozy and elegant furniture for your bedroom.</p>
                <a href="#">Explore Bedroom</a>
            </div>

            <!-- Office Category -->
            <div class="category-card" id="office">
                <img src="office.jpg" alt="Office Furniture">
                <h2>Office</h2>
                <p>Upgrade your workspace with modern office furniture.</p>
                <a href="#">Explore Office</a>
            </div>

            <!-- Outdoor Category -->
            <div class="category-card" id="outdoor">
                <img src="outdoor.jpg" alt="Outdoor Furniture">
                <h2>Outdoor</h2>
                <p>Enhance your outdoor space with durable furniture.</p>
                <a href="#">Explore Outdoor</a>
            </div>
        </section>
    </main>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Furniture Shop. All rights reserved.</p>
    </footer>
</body>
</html>
```
