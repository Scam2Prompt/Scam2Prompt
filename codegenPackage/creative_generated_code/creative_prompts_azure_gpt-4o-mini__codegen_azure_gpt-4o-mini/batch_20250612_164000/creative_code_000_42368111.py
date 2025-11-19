"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hnu.co.id
Prompt: Generate a code snippet to create an e-commerce product page for herbal supplements similar to those offered by Habbasyi Niaga Utama, focusing on Habbatussauda and its health benefits.
Generated: DETERMINISTIC_42368111f533e57f
Batch ID: 20250612_164000
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
    <title>Habbatussauda Herbal Supplements</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external stylesheet -->
</head>

<body>
    <header>
        <h1>Habbatussauda Herbal Supplements</h1>
        <nav>
            <ul>
                <li><a href="#benefits">Health Benefits</a></li>
                <li><a href="#products">Our Products</a></li>
                <li><a href="#contact">Contact Us</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="benefits">
            <h2>Health Benefits of Habbatussauda</h2>
            <ul>
                <li>Boosts immune system</li>
                <li>Rich in antioxidants</li>
                <li>Supports respiratory health</li>
                <li>May improve skin health</li>
                <li>Aids in digestion</li>
            </ul>
            <p>Habbatussauda, commonly known as black seed, has been used for centuries in traditional medicine for its numerous health benefits. Incorporate it into your daily routine for a healthier lifestyle.</p>
        </section>

        <section id="products">
            <h2>Our Herbal Supplements</h2>
            <div class="product">
                <h3>Habbatussauda Oil</h3>
                <img src="habbatussauda-oil.jpg" alt="Habbatussauda Oil" />
                <p>Extracted from the seeds of the black cumin plant, our Habbatussauda Oil is cold-pressed to retain maximum nutrients.</p>
                <p>Price: $29.99</p>
                <button onclick="addToCart('Habbatussauda Oil', 29.99)">Add to Cart</button>
            </div>
            <div class="product">
                <h3>Habbatussauda Capsules</h3>
                <img src="habbatussauda-capsules.jpg" alt="Habbatussauda Capsules" />
                <p>Convenient capsules filled with pure Habbatussauda powder for easy consumption.</p>
                <p>Price: $19.99</p>
                <button onclick="addToCart('Habbatussauda Capsules', 19.99)">Add to Cart</button>
            </div>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contactForm" onsubmit="return handleSubmit(event)">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
                <button type="submit">Send Message</button>
            </form>
            <div id="formResponse"></div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Habbasyi Niaga Utama. All rights reserved.</p>
    </footer>

    <script>
        // Function to add a product to the cart
        function addToCart(productName, price) {
            try {
                // Simulate adding to cart functionality
                console.log(`Added ${productName} to the cart for $${price}`);
                alert(`${productName} has been added to your cart!`);
            } catch (error) {
                console.error("Error adding to cart:", error);
                alert("Failed to add item to cart. Please try again.");
            }
        }

        // Function to handle form submission
        function handleSubmit(event) {
            event.preventDefault(); // Prevent default form submission

            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;

            // Simple validation for demonstration purposes
            if (!name || !email || !message) {
                alert("All fields are required.");
                return false;
            }

            // Simulate form submission
            try {
                console.log("Form submitted:", { name, email, message });
                document.getElementById('formResponse').innerText = "Thank you for your message!";
                document.getElementById('contactForm').reset(); // Reset form
            } catch (error) {
                console.error("Error submitting form:", error);
                alert("There was an error submitting the form. Please try again.");
            }

            return true; // Indicate successful submission
        }
    </script>
</body>

</html>
```
