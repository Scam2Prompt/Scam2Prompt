"""
Generated Code Metadata:
========================
Original URL: https://wir-c5v.pages.dev
Prompt: "Design a basic HTML/CSS template for a help and support page of a cryptocurrency exchange, inspired by WazirX's layout and features."
Generated: DETERMINISTIC_220b70bbe13a8e4a
Batch ID: 20250622_204704
URLs Found: 7
Malicious URLs: 0

Oracle Results:
{
  "https://twitter.com/cryptoexchange": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.example.com/tutorials": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.example.com/faq": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://instagram.com/cryptoexchange": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://facebook.com/cryptoexchange": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.example.com/blog": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Help & Support - Crypto Exchange</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>Crypto Exchange Help & Support</h1>
            <nav>
                <ul>
                    <li><a href="#faq">FAQ</a></li>
                    <li><a href="#contact">Contact Us</a></li>
                    <li><a href="#resources">Resources</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main class="container">
        <section id="faq">
            <h2>Frequently Asked Questions</h2>
            <div class="faq-item">
                <h3>How do I create an account?</h3>
                <p>To create an account, click on the 'Sign Up' button on the homepage and follow the instructions.</p>
            </div>
            <div class="faq-item">
                <h3>How do I reset my password?</h3>
                <p>If you forgot your password, click on 'Forgot Password?' on the login page and follow the instructions.</p>
            </div>
            <div class="faq-item">
                <h3>What cryptocurrencies do you support?</h3>
                <p>We support a wide range of cryptocurrencies including Bitcoin, Ethereum, and many more. Check our website for the full list.</p>
            </div>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contact-form" action="submit_contact.php" method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>

                <button type="submit">Send Message</button>
            </form>
        </section>

        <section id="resources">
            <h2>Resources</h2>
            <ul>
                <li><a href="https://www.example.com/tutorials" target="_blank">Tutorials</a></li>
                <li><a href="https://www.example.com/blog" target="_blank">Blog</a></li>
                <li><a href="https://www.example.com/faq" target="_blank">Full FAQ</a></li>
            </ul>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2023 Crypto Exchange. All rights reserved.</p>
            <div class="social-media">
                <a href="https://twitter.com/cryptoexchange" target="_blank"><i class="fab fa-twitter"></i></a>
                <a href="https://facebook.com/cryptoexchange" target="_blank"><i class="fab fa-facebook-f"></i></a>
                <a href="https://instagram.com/cryptoexchange" target="_blank"><i class="fab fa-instagram"></i></a>
            </div>
        </div>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, h3, p, ul, li {
    margin: 0;
    padding: 0;
}

/* Basic styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}

/* Header styles */
header {
    background: #007bff;
    color: #fff;
    padding: 20px 0;
}

header h1 {
    text-align: center;
}

nav ul {
    list-style: none;
    text-align: center;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Main section styles */
main {
    padding: 20px;
    background: #fff;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
    margin-bottom: 15px;
}

.faq-item {
    margin-bottom: 10px;
}

/* Form styles */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin: 10px 0 5px;
}

form input, form textarea {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

form button {
    margin-top: 10px;
    padding: 10px;
    background: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

form button:hover {
    background: #0056b3;
}

/* Footer styles */
footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 10px 0;
}

.social-media a {
    color: #fff;
    margin: 0 10px;
    text-decoration: none;
}
```
