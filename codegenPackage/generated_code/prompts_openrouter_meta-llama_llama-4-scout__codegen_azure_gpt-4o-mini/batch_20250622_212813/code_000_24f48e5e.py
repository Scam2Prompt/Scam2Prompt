"""
Generated Code Metadata:
========================
Original URL: https://putrastarboy.github.io
Prompt: Generate a simple web page menu for a coffee shop named "8 Coffee" with options like "Pesan Sekarang" (Order Now) and highlighting their specialty coffee.
Generated: DETERMINISTIC_24f48e5e4ba9500d
Batch ID: 20250622_212813
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
    <title>8 Coffee - Menu</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to 8 Coffee</h1>
        <nav>
            <ul>
                <li><a href="#order">Pesan Sekarang</a></li>
                <li><a href="#specialty">Specialty Coffee</a></li>
                <li><a href="#about">About Us</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="order">
            <h2>Pesan Sekarang</h2>
            <p>Order your favorite coffee online and enjoy it at home!</p>
            <button onclick="orderNow()">Order Now</button>
        </section>

        <section id="specialty">
            <h2>Specialty Coffee</h2>
            <ul>
                <li>Espresso</li>
                <li>Latte</li>
                <li>Cappuccino</li>
                <li>Cold Brew</li>
                <li>Mocha</li>
            </ul>
        </section>

        <section id="about">
            <h2>About Us</h2>
            <p>At 8 Coffee, we serve the finest coffee sourced from around the world.</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 8 Coffee. All rights reserved.</p>
    </footer>

    <script>
        /**
         * Function to handle the order now button click
         */
        function orderNow() {
            try {
                // Simulate an order process
                alert("Your order has been placed successfully!");
            } catch (error) {
                console.error("Error placing order:", error);
                alert("There was an error placing your order. Please try again.");
            }
        }
    </script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Header styles */
header {
    background: #6f4c3e; /* Coffee color */
    color: #fff;
    padding: 20px 0;
    text-align: center;
}

/* Navigation styles */
nav ul {
    list-style: none;
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
}

/* Section styles */
section {
    margin-bottom: 20px;
    padding: 15px;
    background: #fff;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #6f4c3e;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
