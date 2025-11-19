"""
Generated Code Metadata:
========================
Original URL: https://mystrikingly.com
Prompt: Generate a simple HTML structure for a landing page using Strikingly's templates and customization options.
Generated: DETERMINISTIC_e866a4312d309bc5
Batch ID: 20250612_161059
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
    <title>Landing Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#features">Features</a></li>
                <li><a href="#pricing">Pricing</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="home">
        <h1>Welcome to our Landing Page</h1>
        <p>This is a sample landing page created using Strikingly's templates and customization options.</p>
        <button>Sign Up</button>
    </section>

    <!-- Features Section -->
    <section id="features">
        <h2>Features</h2>
        <div class="feature-cards">
            <div class="card">
                <h3>Feature 1</h3>
                <p>This is feature 1.</p>
            </div>
            <div class="card">
                <h3>Feature 2</h3>
                <p>This is feature 2.</p>
            </div>
            <div class="card">
                <h3>Feature 3</h3>
                <p>This is feature 3.</p>
            </div>
        </div>
    </section>

    <!-- Pricing Section -->
    <section id="pricing">
        <h2>Pricing</h2>
        <div class="pricing-cards">
            <div class="card">
                <h3>Basic</h3>
                <p>$9.99/month</p>
            </div>
            <div class="card">
                <h3>Premium</h3>
                <p>$19.99/month</p>
            </div>
            <div class="card">
                <h3>Enterprise</h3>
                <p>Custom pricing</p>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <h2>Get in Touch</h2>
        <form>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name"><br><br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email"><br><br>
            <label for="message">Message:</label>
            <textarea id="message" name="message"></textarea><br><br>
            <input type="submit" value="Submit">
        </form>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Landing Page</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

header nav ul li {
    display: inline-block;
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

#home {
    background-image: linear-gradient(to bottom, #f7f7f7, #fff);
    padding: 5em;
    text-align: center;
}

#home button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

#features, #pricing, #contact {
    padding: 5em;
}

.feature-cards, .pricing-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.card {
    background-color: #f7f7f7;
    margin: 20px;
    padding: 20px;
    width: calc(33.33% - 20px);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```
