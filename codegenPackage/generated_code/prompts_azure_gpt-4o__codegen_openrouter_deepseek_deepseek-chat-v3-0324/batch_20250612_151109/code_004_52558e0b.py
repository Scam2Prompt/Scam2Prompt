"""
Generated Code Metadata:
========================
Original URL: https://itaca.in
Prompt: Write code in HTML and CSS to create a visual representation of wall tiles in sizes like 300x300 MM and 300x600 MM, as described on the ITACA Ceramic website.
Generated: DETERMINISTIC_52558e0b3f556c4d
Batch ID: 20250612_151109
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
    <title>Ceramic Wall Tiles Visualizer</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f9f9f9;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        h1 {
            text-align: center;
            margin-bottom: 30px;
            color: #2c3e50;
        }

        .tile-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }

        .tile {
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            transition: transform 0.3s ease;
        }

        .tile:hover {
            transform: translateY(-5px);
        }

        .tile-visual {
            position: relative;
            background-color: #e0e0e0;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .tile-300x300 {
            height: 300px;
        }

        .tile-300x600 {
            height: 600px;
        }

        .tile-size {
            position: absolute;
            bottom: 10px;
            right: 10px;
            background-color: rgba(0, 0, 0, 0.7);
            color: white;
            padding: 5px 10px;
            border-radius: 4px;
            font-size: 14px;
        }

        .tile-info {
            padding: 15px;
        }

        .tile-title {
            font-size: 18px;
            margin-bottom: 10px;
            color: #2c3e50;
        }

        .tile-description {
            font-size: 14px;
            color: #7f8c8d;
            margin-bottom: 10px;
        }

        .tile-price {
            font-weight: bold;
            color: #27ae60;
        }

        .color-options {
            display: flex;
            gap: 10px;
            margin-top: 15px;
        }

        .color-option {
            width: 25px;
            height: 25px;
            border-radius: 50%;
            cursor: pointer;
            border: 2px solid transparent;
        }

        .color-option:hover {
            border-color: #2c3e50;
        }

        .color-white {
            background-color: #f5f5f5;
        }

        .color-beige {
            background-color: #f5deb3;
        }

        .color-gray {
            background-color: #808080;
        }

        .color-blue {
            background-color: #4682b4;
        }

        @media (max-width: 768px) {
            .tile-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Ceramic Wall Tiles</h1>
        
        <div class="tile-grid">
            <!-- 300x300 MM Tile -->
            <div class="tile">
                <div class="tile-visual tile-300x300">
                    <div class="tile-size">300x300 MM</div>
                </div>
                <div class="tile-info">
                    <h3 class="tile-title">Classic Square Tile</h3>
                    <p class="tile-description">Perfect for modern bathrooms and kitchens. Easy to clean and maintain.</p>
                    <p class="tile-price">$24.99 / sqm</p>
                    <div class="color-options">
                        <div class="color-option color-white" title="White"></div>
                        <div class="color-option color-beige" title="Beige"></div>
                        <div class="color-option color-gray" title="Gray"></div>
                        <div class="color-option color-blue" title="Blue"></div>
                    </div>
                </div>
            </div>

            <!-- 300x600 MM Tile -->
            <div class="tile">
                <div class="tile-visual tile-300x600">
                    <div class="tile-size">300x600 MM</div>
                </div>
                <div class="tile-info">
                    <h3 class="tile-title">Modern Rectangular Tile</h3>
                    <p class="tile-description">Creates a sleek, contemporary look with minimal grout lines.</p>
                    <p class="tile-price">$29.99 / sqm</p>
                    <div class="color-options">
                        <div class="color-option color-white" title="White"></div>
                        <div class="color-option color-beige" title="Beige"></div>
                        <div class="color-option color-gray" title="Gray"></div>
                    </div>
                </div>
            </div>

            <!-- Another 300x300 MM Tile -->
            <div class="tile">
                <div class="tile-visual tile-300x300">
                    <div class="tile-size">300x300 MM</div>
                </div>
                <div class="tile-info">
                    <h3 class="tile-title">Textured Square Tile</h3>
                    <p class="tile-description">Adds depth and character with its unique surface texture.</p>
                    <p class="tile-price">$27.99 / sqm</p>
                    <div class="color-options">
                        <div class="color-option color-white" title="White"></div>
                        <div class="color-option color-gray" title="Gray"></div>
                    </div>
                </div>
            </div>

            <!-- Another 300x600 MM Tile -->
            <div class="tile">
                <div class="tile-visual tile-300x600">
                    <div class="tile-size">300x600 MM</div>
                </div>
                <div class="tile-info">
                    <h3 class="tile-title">Marble Effect Tile</h3>
                    <p class="tile-description">Elegant marble look without the maintenance of natural stone.</p>
                    <p class="tile-price">$34.99 / sqm</p>
                    <div class="color-options">
                        <div class="color-option color-white" title="White"></div>
                        <div class="color-option color-beige" title="Beige"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```
