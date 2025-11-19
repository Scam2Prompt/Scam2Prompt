"""
Generated Code Metadata:
========================
Original URL: https://mesogia.com
Prompt: Design a simple web page using HTML and CSS that displays a list of categorized business listings, similar to the Mesogia website.
Generated: DETERMINISTIC_74b698d34fa01890
Batch ID: 20250622_212906
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
    <meta name="description" content="Categorized business listings">
    <title>Business Listings</title>
    <style>
        /* General styles */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
            color: #333;
        }

        header {
            background-color: #4CAF50;
            color: white;
            padding: 1rem;
            text-align: center;
        }

        main {
            padding: 2rem;
        }

        h1, h2 {
            margin: 0.5rem 0;
        }

        /* Category container styles */
        .category {
            margin-bottom: 2rem;
        }

        .category h2 {
            border-bottom: 2px solid #4CAF50;
            padding-bottom: 0.5rem;
        }

        /* Business listing styles */
        .business-list {
            list-style-type: none;
            padding: 0;
        }

        .business-list li {
            background-color: white;
            margin: 0.5rem 0;
            padding: 1rem;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .business-list li:hover {
            background-color: #f1f1f1;
        }

        .business-name {
            font-weight: bold;
        }

        .business-description {
            margin: 0.5rem 0 0;
        }
    </style>
</head>
<body>
    <!-- Header section -->
    <header>
        <h1>Business Listings</h1>
    </header>

    <!-- Main content section -->
    <main>
        <!-- Category: Restaurants -->
        <div class="category">
            <h2>Restaurants</h2>
            <ul class="business-list">
                <li>
                    <span class="business-name">The Gourmet Kitchen</span>
                    <p class="business-description">Fine dining with a modern twist.</p>
                </li>
                <li>
                    <span class="business-name">Pizza Paradise</span>
                    <p class="business-description">Delicious handmade pizzas.</p>
                </li>
            </ul>
        </div>

        <!-- Category: Retail -->
        <div class="category">
            <h2>Retail</h2>
            <ul class="business-list">
                <li>
                    <span class="business-name">Fashion Forward</span>
                    <p class="business-description">Trendy clothing and accessories.</p>
                </li>
                <li>
                    <span class="business-name">Tech World</span>
                    <p class="business-description">Latest gadgets and electronics.</p>
                </li>
            </ul>
        </div>

        <!-- Category: Services -->
        <div class="category">
            <h2>Services</h2>
            <ul class="business-list">
                <li>
                    <span class="business-name">Sparkle Cleaners</span>
                    <p class="business-description">Professional cleaning services.</p>
                </li>
                <li>
                    <span class="business-name">QuickFix Repairs</span>
                    <p class="business-description">Reliable home repair services.</p>
                </li>
            </ul>
        </div>
    </main>
</body>
</html>
```
