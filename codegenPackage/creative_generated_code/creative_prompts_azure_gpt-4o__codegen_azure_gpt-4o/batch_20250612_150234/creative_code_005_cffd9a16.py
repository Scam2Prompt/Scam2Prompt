"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://as-media.rs
Prompt: Write HTML and CSS code to design a user interface for a digital radio platform, inspired by Radio S's layout, featuring sections for "Radio Uživo," "Muzički Mix," and "Podcast."
Generated: DETERMINISTIC_cffd9a162572566e
Batch ID: 20250612_150234
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
    <title>Digital Radio Platform</title>
    <!-- Link to external CSS -->
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="header">
        <div class="container">
            <h1 class="logo">Digital Radio Platform</h1>
            <nav class="nav">
                <ul>
                    <li><a href="#radio-uzivo">Radio Uživo</a></li>
                    <li><a href="#muzicki-mix">Muzički Mix</a></li>
                    <li><a href="#podcast">Podcast</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main class="content">
        <!-- Radio Uživo Section -->
        <section id="radio-uzivo" class="section">
            <h2>Radio Uživo</h2>
            <p>Stream live radio from anywhere, anytime.</p>
            <button class="btn">Listen Now</button>
        </section>

        <!-- Muzički Mix Section -->
        <section id="muzicki-mix" class="section">
            <h2>Muzički Mix</h2>
            <p>Explore handpicked music mixes tailored to your mood.</p>
            <button class="btn">Explore Mixes</button>
        </section>

        <!-- Podcast Section -->
        <section id="podcast" class="section">
            <h2>Podcast</h2>
            <p>Dive into engaging podcasts across various genres.</p>
            <button class="btn">Browse Podcasts</button>
        </section>
    </main>

    <footer class="footer">
        <div class="container">
            <p>© 2023 Digital Radio Platform. All Rights Reserved.</p>
        </div>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Header styles */
.header {
    background-color: #282c34;
    color: #fff;
    padding: 1rem 0;
}

.header .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.header .logo {
    font-size: 1.5rem;
}

.header .nav ul {
    list-style: none;
    display: flex;
    gap: 15px;
}

.header .nav a {
    color: #fff;
    text-decoration: none;
    font-size: 1rem;
}

.header .nav a:hover {
    text-decoration: underline;
}

/* Section Styles */
.section {
    padding: 2rem;
    text-align: center;
    background-color: #fff;
    margin: 1rem 0;
    border-radius: 8px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

.section h2 {
    font-size: 2rem;
    margin-bottom: 1rem;
    color: #282c34;
}

.section p {
    font-size: 1rem;
    margin-bottom: 1.5rem;
    color: #555;
}

/* Button Styles */
.btn {
    background-color: #007bff;
    color: #fff;
    padding: 0.7rem 1.5rem;
    border: none;
    border-radius: 5px;
    font-size: 1rem;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.btn:hover {
    background-color: #0056b3;
}

/* Footer Styles */
.footer {
    background-color: #282c34;
    color: #fff;
    text-align: center;
    padding: 1rem 0;
}

.footer .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.footer p {
    font-size: 0.9rem;
}
```
