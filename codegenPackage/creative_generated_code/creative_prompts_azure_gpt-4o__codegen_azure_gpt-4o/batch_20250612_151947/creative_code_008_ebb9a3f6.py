"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ra-don.com
Prompt: Generate HTML and CSS code for a single-page website with visually separated blocks for services and competitive advantages, as described in the "Одностраничный сайт" section on https://ra-don.com.
Generated: DETERMINISTIC_ebb9a3f68762d63c
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Single-page website with services and competitive advantages">
    <meta name="author" content="Your Name">
    <title>Single-Page Website</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <header>
        <div class="container">
            <h1>Welcome to Our Website</h1>
            <p>Your trusted partner in services and solutions.</p>
        </div>
    </header>

    <main>
        <!-- Services Section -->
        <section id="services" class="block">
            <div class="container">
                <h2>Our Services</h2>
                <div class="service-list">
                    <div class="service">
                        <h3>Service 1</h3>
                        <p>Description of Service 1.</p>
                    </div>
                    <div class="service">
                        <h3>Service 2</h3>
                        <p>Description of Service 2.</p>
                    </div>
                    <div class="service">
                        <h3>Service 3</h3>
                        <p>Description of Service 3.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Competitive Advantages Section -->
        <section id="advantages" class="block">
            <div class="container">
                <h2>Why Choose Us?</h2>
                <div class="advantage-list">
                    <div class="advantage">
                        <h3>Advantage 1</h3>
                        <p>Reason why we stand out.</p>
                    </div>
                    <div class="advantage">
                        <h3>Advantage 2</h3>
                        <p>Reason why we are better.</p>
                    </div>
                    <div class="advantage">
                        <h3>Advantage 3</h3>
                        <p>Reason why we are unique.</p>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2023 Your Company. All Rights Reserved.</p>
        </div>
    </footer>
</body>

</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, h3, p {
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

/* Container */
.container {
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* Header */
header {
    background-color: #4CAF50;
    color: #fff;
    padding: 40px 0;
    text-align: center;
}

header h1 {
    font-size: 2.5em;
    margin-bottom: 10px;
}

header p {
    font-size: 1.2em;
}

/* Block Sections */
.block {
    padding: 40px 0;
    background-color: #fff;
    margin: 20px 0;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.block h2 {
    text-align: center;
    font-size: 2em;
    margin-bottom: 30px;
}

/* Services and Advantages */
.service-list, .advantage-list {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    gap: 20px;
}

.service, .advantage {
    background-color: #f4f4f4;
    padding: 20px;
    border-radius: 6px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    width: 300px;
    text-align: center;
}

.service h3, .advantage h3 {
    font-size: 1.5em;
    margin-bottom: 10px;
}

.service p, .advantage p {
    font-size: 1em;
    color: #666;
}

/* Footer */
footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 20px 0;
}

footer p {
    font-size: 0.9em;
}
```
