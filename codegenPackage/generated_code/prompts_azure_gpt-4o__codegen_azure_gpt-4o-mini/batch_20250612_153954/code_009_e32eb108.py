"""
Generated Code Metadata:
========================
Original URL: https://millymally.pl
Prompt: Generate HTML and CSS code for a product showcase page featuring items like "Milly Mally Zabawka pluszowa z Projektorem Szumiś Milly Bear Blue" and "Hulajnoga trójkołowa balansowa Scooter Sparky Red."
Generated: DETERMINISTIC_e32eb108f51e0afd
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Showcase</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Product Showcase</h1>
    </header>
    <main>
        <section class="product">
            <h2>Milly Mally Zabawka pluszowa z Projektorem Szumiś Milly Bear Blue</h2>
            <img src="milly-bear.jpg" alt="Milly Bear Blue" class="product-image">
            <p class="product-description">Urocza pluszowa zabawka z projektorem, idealna dla dzieci.</p>
            <span class="product-price">Cena: 99,99 zł</span>
            <button class="buy-button">Kup teraz</button>
        </section>
        <section class="product">
            <h2>Hulajnoga trójkołowa balansowa Scooter Sparky Red</h2>
            <img src="scooter-sparky.jpg" alt="Scooter Sparky Red" class="product-image">
            <p class="product-description">Bezpieczna hulajnoga trójkołowa, idealna dla małych dzieci.</p>
            <span class="product-price">Cena: 199,99 zł</span>
            <button class="buy-button">Kup teraz</button>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Product Showcase. Wszelkie prawa zastrzeżone.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default browser styles */
body, h1, h2, p {
    margin: 0;
    padding: 0;
}

/* Set a basic font and background color */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

/* Style the header */
header {
    background: #007BFF;
    color: white;
    padding: 20px;
    text-align: center;
}

/* Main content styling */
main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
}

/* Individual product styling */
.product {
    background: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    margin: 15px;
    padding: 20px;
    width: 300px;
    text-align: center;
}

/* Image styling */
.product-image {
    max-width: 100%;
    height: auto;
}

/* Button styling */
.buy-button {
    background-color: #28a745;
    border: none;
    border-radius: 5px;
    color: white;
    cursor: pointer;
    padding: 10px 15px;
    text-align: center;
    text-decoration: none;
    transition: background-color 0.3s;
}

/* Button hover effect */
.buy-button:hover {
    background-color: #218838;
}

/* Footer styling */
footer {
    text-align: center;
    padding: 10px;
    background: #007BFF;
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
