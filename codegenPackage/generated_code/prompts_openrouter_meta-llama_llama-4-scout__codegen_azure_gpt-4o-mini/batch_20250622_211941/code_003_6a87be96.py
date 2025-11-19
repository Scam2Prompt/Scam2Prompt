"""
Generated Code Metadata:
========================
Original URL: https://capcutpro.ofertatcdigital.shop
Prompt: Design a simple user interface using HTML and CSS to promote the sale of CapCut Pro accounts, including features like discounts, bonuses, and guarantees, as showcased on this webpage.
Generated: DETERMINISTIC_6a87be96c33ca072
Batch ID: 20250622_211941
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
    <title>CapCut Pro Accounts Sale</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Get Your CapCut Pro Account Today!</h1>
        <p>Unlock premium features and enhance your video editing experience.</p>
    </header>

    <main>
        <section class="promo">
            <h2>Exclusive Offers</h2>
            <div class="offer">
                <h3>Discounts</h3>
                <p>Enjoy a 20% discount on your first purchase!</p>
            </div>
            <div class="offer">
                <h3>Bonuses</h3>
                <p>Get 1 month free when you subscribe for 12 months!</p>
            </div>
            <div class="offer">
                <h3>Guarantees</h3>
                <p>30-day money-back guarantee if you're not satisfied!</p>
            </div>
        </section>

        <section class="cta">
            <h2>Ready to Buy?</h2>
            <button id="buyButton">Purchase Now</button>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 CapCut Pro Accounts. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, h3, p {
    margin: 0;
    padding: 0;
}

/* Basic styling for the body */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styling */
header {
    background: #007bff;
    color: #fff;
    padding: 20px;
    text-align: center;
}

/* Main section styling */
main {
    padding: 20px;
}

/* Promotional offers styling */
.promo {
    background: #fff;
    border-radius: 5px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Individual offer styling */
.offer {
    margin-bottom: 15px;
}

/* Call to action section styling */
.cta {
    text-align: center;
}

/* Button styling */
button {
    background: #28a745;
    color: #fff;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
}

button:hover {
    background: #218838;
}
```

```javascript
// script.js

// Function to handle the purchase button click
document.getElementById('buyButton').addEventListener('click', function() {
    try {
        // Simulate a purchase action
        alert('Thank you for your purchase! Your CapCut Pro account will be activated shortly.');
    } catch (error) {
        console.error('Error during purchase:', error);
        alert('An error occurred while processing your purchase. Please try again later.');
    }
});
```
