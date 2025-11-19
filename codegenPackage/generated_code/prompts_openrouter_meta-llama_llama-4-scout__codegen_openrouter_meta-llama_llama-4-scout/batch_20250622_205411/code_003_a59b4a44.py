"""
Generated Code Metadata:
========================
Original URL: https://situsgresiktoto.com
Prompt: How would you integrate the "SLOT GACOR" game promotion into a custom e-commerce website using HTML, CSS, and JavaScript?
Generated: DETERMINISTIC_a59b4a448358d3d2
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SLOT GACOR Promotion</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Products</a></li>
                <li><a href="#">Promotions</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="promotion">
            <h1>SLOT GACOR Promotion</h1>
            <p>Claim your exclusive rewards and bonuses!</p>
            <button id="claim-button">Claim Now</button>
            <div id="promotion-details">
                <p>Terms and Conditions:</p>
                <ul>
                    <li>Valid for new customers only</li>
                    <li>Minimum deposit required: $10</li>
                    <li>Maximum bonus: $100</li>
                </ul>
            </div>
        </section>
    </main>
    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
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

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

nav li {
    display: inline-block;
    margin-right: 20px;
}

nav a {
    color: #fff;
    text-decoration: none;
}

.promotion {
    background-color: #f7f7f7;
    padding: 2em;
    text-align: center;
}

#claim-button {
    background-color: #4CAF50;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#claim-button:hover {
    background-color: #3e8e41;
}

#promotion-details {
    margin-top: 20px;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
```

**script.js**
```javascript
// Get the claim button element
const claimButton = document.getElementById('claim-button');

// Add event listener to claim button
claimButton.addEventListener('click', () => {
    // Validate user eligibility
    if (isEligibleUser()) {
        // Show promotion details
        showPromotionDetails();
        // Send claim request to server
        sendClaimRequest();
    } else {
        alert('Sorry, you are not eligible for this promotion.');
    }
});

// Check if user is eligible
function isEligibleUser() {
    // Assume this function checks user data (e.g., new customer, minimum deposit)
    // For demonstration purposes, always return true
    return true;
}

// Show promotion details
function showPromotionDetails() {
    const promotionDetails = document.getElementById('promotion-details');
    promotionDetails.style.display = 'block';
}

// Send claim request to server
function sendClaimRequest() {
    try {
        // Assume this function sends a request to the server to claim the promotion
        // For demonstration purposes, use a mock API call
        fetch('/api/claim-promotion', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                userId: 123,
                promotionId: 456
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Promotion claimed successfully!');
            } else {
                alert('Error claiming promotion: ' + data.error);
            }
        })
        .catch(error => {
            console.error('Error claiming promotion:', error);
            alert('Error claiming promotion. Please try again.');
        });
    } catch (error) {
        console.error('Error claiming promotion:', error);
        alert('Error claiming promotion. Please try again.');
    }
}
```

**server.js (Node.js example)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON requests
app.use(express.json());

// Mock API endpoint to claim promotion
app.post('/api/claim-promotion', (req, res) => {
    try {
        const userId = req.body.userId;
        const promotionId = req.body.promotionId;
        // Assume this code checks user eligibility and updates database
        // For demonstration purposes, always return success
        res.json({
            success: true,
            message: 'Promotion claimed successfully!'
        });
    } catch (error) {
        console.error('Error claiming promotion:', error);
        res.status(500).json({
            success: false,
            error: 'Internal Server Error'
        });
    }
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
