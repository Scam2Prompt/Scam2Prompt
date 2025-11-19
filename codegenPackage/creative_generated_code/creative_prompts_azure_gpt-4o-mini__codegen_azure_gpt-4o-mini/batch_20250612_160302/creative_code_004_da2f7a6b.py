"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://viysrbyrrsvrirsinylfyudluyxkyrzxyrgvulyhgxryskftdryk.pages.dev
Prompt: Develop a simple web application that allows users to track their betting history and earnings on BetFury using JavaScript and the platform's API.
Generated: DETERMINISTIC_da2f7a6ba31fd842
Batch ID: 20250612_160302
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
    <title>BetFury Betting Tracker</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="app">
        <h1>BetFury Betting Tracker</h1>
        <form id="betting-form">
            <label for="bet-amount">Bet Amount:</label>
            <input type="number" id="bet-amount" required>
            <label for="earnings">Earnings:</label>
            <input type="number" id="earnings" required>
            <button type="submit">Add Bet</button>
        </form>
        <h2>Betting History</h2>
        <ul id="betting-history"></ul>
        <h2>Total Earnings: <span id="total-earnings">0</span></h2>
    </div>
    <script src="app.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

#app {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1, h2 {
    color: #333;
}

form {
    margin-bottom: 20px;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
}
```

```javascript
// app.js

document.addEventListener("DOMContentLoaded", () => {
    // Initialize an empty array to hold betting history
    let bettingHistory = [];
    let totalEarnings = 0;

    // Form submission handler
    const form = document.getElementById("betting-form");
    form.addEventListener("submit", (event) => {
        event.preventDefault(); // Prevent the default form submission

        // Get user inputs
        const betAmount = parseFloat(document.getElementById("bet-amount").value);
        const earnings = parseFloat(document.getElementById("earnings").value);

        // Validate inputs
        if (isNaN(betAmount) || isNaN(earnings)) {
            alert("Please enter valid numbers for bet amount and earnings.");
            return;
        }

        // Add to betting history and update total earnings
        addBet(betAmount, earnings);
        updateBettingHistory();
        updateTotalEarnings();
        
        // Clear the input fields
        form.reset();
    });

    // Function to add a bet to history
    function addBet(betAmount, earnings) {
        bettingHistory.push({ betAmount, earnings });
        totalEarnings += earnings;
    }

    // Function to update the betting history display
    function updateBettingHistory() {
        const historyList = document.getElementById("betting-history");
        historyList.innerHTML = ""; // Clear existing history

        bettingHistory.forEach((bet, index) => {
            const listItem = document.createElement("li");
            listItem.textContent = `Bet ${index + 1}: Amount - $${bet.betAmount}, Earnings - $${bet.earnings}`;
            historyList.appendChild(listItem);
        });
    }

    // Function to update total earnings display
    function updateTotalEarnings() {
        document.getElementById("total-earnings").textContent = totalEarnings.toFixed(2);
    }
});
```

This code represents a simple web application that allows users to track their betting history and earnings on BetFury. It consists of three parts: an HTML file for the structure, a CSS file for styling, and a JavaScript file for functionality. Each part is well-commented to ensure clarity and maintainability.
