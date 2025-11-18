"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wonderino.com
Prompt: Generate HTML and ARIA attributes for a gemstone encyclopedia webpage that is optimized for screen-reader users, similar to Wonderino's implementation.
Generated: DETERMINISTIC_fc0ee64df2997e8b
Batch ID: 20250612_151811
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
    <title>Gemstone Encyclopedia</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header role="banner">
        <h1 id="main-title">Gemstone Encyclopedia</h1>
        <nav aria-label="Main navigation">
            <ul>
                <li><a href="#gems" aria-current="page">Gemstones</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main role="main">
        <section id="gems" aria-labelledby="gems-title">
            <h2 id="gems-title">Gemstones</h2>
            <article aria-labelledby="amethyst-title" tabindex="0">
                <h3 id="amethyst-title">Amethyst</h3>
                <p>Amethyst is a purple variety of quartz.</p>
                <p>Color: Purple</p>
                <p>Hardness: 7 on the Mohs scale</p>
                <p>Price Range: $20 - $40 per carat</p>
            </article>

            <article aria-labelledby="emerald-title" tabindex="0">
                <h3 id="emerald-title">Emerald</h3>
                <p>Emerald is a green variety of beryl.</p>
                <p>Color: Green</p>
                <p>Hardness: 7.5-8 on the Mohs scale</p>
                <p>Price Range: $500 - $3000 per carat</p>
            </article>

            <article aria-labelledby="ruby-title" tabindex="0">
                <h3 id="ruby-title">Ruby</h3>
                <p>Ruby is a red variety of corundum.</p>
                <p>Color: Red</p>
                <p>Hardness: 9 on the Mohs scale</p>
                <p>Price Range: $100 - $1000 per carat</p>
            </article>
        </section>

        <section id="about" aria-labelledby="about-title">
            <h2 id="about-title">About This Encyclopedia</h2>
            <p>This encyclopedia provides detailed information about various gemstones.</p>
        </section>

        <section id="contact" aria-labelledby="contact-title">
            <h2 id="contact-title">Contact Us</h2>
            <form aria-labelledby="contact-form-title" onsubmit="return validateForm()" novalidate>
                <h3 id="contact-form-title">Send us a message</h3>
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required aria-required="true">
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required aria-required="true">
                
                <label for="message">Message:</label>
                <textarea id="message" name="message" required aria-required="true"></textarea>
                
                <button type="submit">Submit</button>
            </form>
        </section>
    </main>

    <footer role="contentinfo">
        <p>&copy; 2023 Gemstone Encyclopedia. All rights reserved.</p>
    </footer>

    <script>
        // Function to validate the contact form
        function validateForm() {
            // Basic validation logic can be added here
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();

            if (!name || !email || !message) {
                alert("All fields are required!");
                return false; // Prevent form submission
            }
            return true; // Allow form submission
        }
    </script>
</body>
</html>
```
