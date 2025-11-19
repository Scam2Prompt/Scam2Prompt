"""
Generated Code Metadata:
========================
Original URL: https://sitechgt.com
Prompt: "Generate a newsletter template using HTML and CSS inspired by Études Newsletter's design insights and case studies."
Generated: DETERMINISTIC_3ae07ce3ce660259
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Études Newsletter Template</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="hero">
            <h1>Études Newsletter</h1>
            <p>Inspired by design insights and case studies</p>
            <button>Learn More</button>
        </section>
        <section class="insights">
            <h2>Design Insights</h2>
            <div class="insight-cards">
                <div class="card">
                    <h3>Case Study 1</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                </div>
                <div class="card">
                    <h3>Case Study 2</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                </div>
                <div class="card">
                    <h3>Case Study 3</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                </div>
            </div>
        </section>
        <section class="newsletter">
            <h2>Stay Up-to-Date</h2>
            <form>
                <input type="email" placeholder="Your Email Address">
                <button>Subscribe</button>
            </form>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Études Newsletter</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

:root {
    --primary-color: #333;
    --secondary-color: #666;
    --background-color: #f9f9f9;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: var(--primary-color);
    background-color: var(--background-color);
}

header {
    background-color: var(--primary-color);
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

header nav ul li {
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

.hero {
    background-image: linear-gradient(to bottom, #333, #555);
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

.hero h1 {
    font-size: 48px;
}

.insights {
    max-width: 800px;
    margin: 40px auto;
}

.insight-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.card {
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin: 20px;
    width: calc(33.33% - 20px);
}

.card h3 {
    font-size: 18px;
    margin-bottom: 10px;
}

.newsletter {
    background-color: var(--primary-color);
    color: #fff;
    padding: 20px;
    text-align: center;
}

.newsletter form {
    display: flex;
    justify-content: center;
}

.newsletter input[type="email"] {
    padding: 10px;
    border: none;
    border-radius: 10px 0 0 10px;
}

.newsletter button {
    padding: 10px;
    border: none;
    border-radius: 0 10px 10px 0;
    background-color: var(--secondary-color);
    color: #fff;
    cursor: pointer;
}

footer {
    background-color: var(--primary-color);
    color: #fff;
    padding: 10px;
    text-align: center;
    clear: both;
}

/* Responsive Design */

@media (max-width: 768px) {
    .card {
        width: calc(50% - 20px);
    }
}

@media (max-width: 480px) {
    .card {
        width: 100%;
    }
    .hero h1 {
        font-size: 24px;
    }
}
```
