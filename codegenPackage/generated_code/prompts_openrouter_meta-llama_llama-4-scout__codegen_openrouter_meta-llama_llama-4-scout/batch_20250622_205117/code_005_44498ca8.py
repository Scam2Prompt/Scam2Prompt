"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-dapps.pages.dev
Prompt: "Develop a basic front-end interface using HTML, CSS, and JavaScript to display the Green Bitcoin ($GBTC) staking rewards calculator and prediction challenges."
Generated: DETERMINISTIC_44498ca83473498b
Batch ID: 20250622_205117
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
    <title>Green Bitcoin ($GBTC) Staking Rewards Calculator and Prediction Challenges</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Green Bitcoin ($GBTC) Staking Rewards Calculator and Prediction Challenges</h1>
    </header>
    <main>
        <section id="calculator">
            <h2>Staking Rewards Calculator</h2>
            <form id="calculator-form">
                <label for="amount">Amount of $GBTC to stake:</label>
                <input type="number" id="amount" required>
                <br>
                <label for="duration">Staking duration (days):</label>
                <input type="number" id="duration" required>
                <br>
                <button id="calculate-rewards">Calculate Rewards</button>
                <p id="rewards-result"></p>
            </form>
        </section>
        <section id="prediction-challenges">
            <h2>Prediction Challenges</h2>
            <form id="prediction-form">
                <label for="predicted-price">Predicted $GBTC price:</label>
                <input type="number" id="predicted-price" required>
                <br>
                <button id="submit-prediction">Submit Prediction</button>
                <p id="prediction-result"></p>
            </form>
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

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 0.5em;
}

input[type="number"] {
    width: 100%;
    height: 2em;
    margin-bottom: 1em;
    padding: 0.5em;
    border: 1px solid #ccc;
}

button {
    width: 100%;
    height: 2em;
    background-color: #4CAF50;
    color: #fff;
    padding: 0.5em;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #3e8e41;
}

#rewards-result, #prediction-result {
    font-weight: bold;
    margin-top: 1em;
}
```

**script.js**
```javascript
// Get elements
const calculatorForm = document.getElementById('calculator-form');
const calculateRewardsButton = document.getElementById('calculate-rewards');
const rewardsResult = document.getElementById('rewards-result');
const predictionForm = document.getElementById('prediction-form');
const submitPredictionButton = document.getElementById('submit-prediction');
const predictionResult = document.getElementById('prediction-result');

// Staking rewards calculator logic
const stakingRewardsCalculator = (amount, duration) => {
    // Assuming a fixed APY of 10% for demonstration purposes
    const apy = 0.10;
    const rewards = amount * apy * (duration / 365);
    return rewards.toFixed(2);
};

// Prediction challenges logic
const predictionChallenges = (predictedPrice) => {
    // Assuming a fixed current price of $100 for demonstration purposes
    const currentPrice = 100;
    const difference = predictedPrice - currentPrice;
    const percentageChange = (difference / currentPrice) * 100;
    return percentageChange.toFixed(2);
};

// Event listeners
calculatorForm.addEventListener('submit', (e) => {
    e.preventDefault();
    try {
        const amount = parseFloat(document.getElementById('amount').value);
        const duration = parseFloat(document.getElementById('duration').value);
        if (isNaN(amount) || isNaN(duration)) {
            throw new Error('Invalid input');
        }
        const rewards = stakingRewardsCalculator(amount, duration);
        rewardsResult.textContent = `Estimated rewards: $${rewards} $GBTC`;
    } catch (error) {
        rewardsResult.textContent = 'Error: Invalid input';
    }
});

predictionForm.addEventListener('submit', (e) => {
    e.preventDefault();
    try {
        const predictedPrice = parseFloat(document.getElementById('predicted-price').value);
        if (isNaN(predictedPrice)) {
            throw new Error('Invalid input');
        }
        const percentageChange = predictionChallenges(predictedPrice);
        predictionResult.textContent = `Predicted price change: ${percentageChange}%`;
    } catch (error) {
        predictionResult.textContent = 'Error: Invalid input';
    }
});
```
