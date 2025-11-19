"""
Generated Code Metadata:
========================
Original URL: https://mpeppe--dashboard.pages.dev
Prompt: Design a simple webpage for the Mpeppe ($MPEPE) presale using HTML, CSS, and JavaScript, incorporating a countdown timer and a "buy now" button.
Generated: DETERMINISTIC_3a56ec57cf7b08df
Batch ID: 20250622_205435
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
    <title>Mpeppe Presale</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Mpeppe ($MPEPE) Presale</h1>
        <div id="countdown" class="countdown"></div>
        <button id="buyButton" class="buy-button">Buy Now</button>
    </div>

    <script src="script.js"></script>
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

/* Container styling */
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background-color: #f4f4f4;
}

/* Heading styling */
h1 {
    font-size: 2.5rem;
    margin-bottom: 20px;
}

/* Countdown timer styling */
.countdown {
    font-size: 2rem;
    margin-bottom: 30px;
    color: #333;
}

/* Button styling */
.buy-button {
    padding: 15px 30px;
    font-size: 1.2rem;
    color: #fff;
    background-color: #28a745;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.buy-button:hover {
    background-color: #218838;
}
```

```javascript
// script.js

// Set the date for the presale to end
const presaleEndDate = new Date("2023-12-31T23:59:59Z").getTime();

// Function to update the countdown timer
function updateCountdown() {
    const now = new Date().getTime();
    const distance = presaleEndDate - now;

    // Calculate days, hours, minutes, and seconds
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Display the result in the countdown element
    document.getElementById("countdown").innerHTML = 
        `${days}d ${hours}h ${minutes}m ${seconds}s`;

    // If the countdown is over, display a message
    if (distance < 0) {
        clearInterval(countdownInterval);
        document.getElementById("countdown").innerHTML = "Presale has ended";
        document.getElementById("buyButton").disabled = true; // Disable button
    }
}

// Update the countdown every second
const countdownInterval = setInterval(updateCountdown, 1000);

// Event listener for the buy button
document.getElementById("buyButton").addEventListener("click", function() {
    try {
        // Simulate a buy action (replace with actual buy logic)
        alert("You have successfully purchased $MPEPE!");
    } catch (error) {
        console.error("Error during purchase:", error);
        alert("An error occurred while processing your purchase. Please try again.");
    }
});

// Initial call to display the countdown immediately
updateCountdown();
```
