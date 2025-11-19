"""
Generated Code Metadata:
========================
Original URL: https://ethcll.com
Prompt: Create a responsive web page using HTML, CSS, and JavaScript that allows users to pledge ETH and displays a warning if JavaScript is disabled.
Generated: DETERMINISTIC_0ac31349fd2eb281
Batch ID: 20250612_152600
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
    <title>ETH Pledge Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>ETH Pledge Page</h1>
    </header>
    <main>
        <section class="pledge-form">
            <h2>Pledge ETH</h2>
            <form id="pledge-form">
                <label for="amount">Amount (ETH):</label>
                <input type="number" id="amount" step="0.01" required>
                <button id="pledge-btn">Pledge</button>
            </form>
            <div id="js-warning" class="js-warning">
                <p>Please enable JavaScript to use this feature.</p>
            </div>
        </section>
    </main>

    <script src="script.js"></script>
    <noscript>
        <style>
            .js-warning {
                display: block;
            }
        </style>
    </noscript>
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

.pledge-form {
    background-color: #f7f7f7;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

#pledge-form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

label {
    margin-bottom: 0.5em;
}

input[type="number"] {
    width: 100%;
    height: 2em;
    padding: 0.5em;
    margin-bottom: 1em;
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

.js-warning {
    display: none;
    background-color: #ffc107;
    color: #333;
    padding: 1em;
    border: 1px solid #ccc;
    border-radius: 5px;
}

@media only screen and (max-width: 768px) {
    main {
        padding: 1em;
    }
    .pledge-form {
        padding: 0.5em;
    }
}
```

**script.js**
```javascript
// Get the pledge form and button elements
const pledgeForm = document.getElementById('pledge-form');
const pledgeBtn = document.getElementById('pledge-btn');
const amountInput = document.getElementById('amount');

// Add event listener to pledge button
pledgeBtn.addEventListener('click', async (e) => {
    e.preventDefault();

    // Get the amount value
    const amount = parseFloat(amountInput.value);

    // Validate amount
    if (isNaN(amount) || amount <= 0) {
        alert('Please enter a valid amount');
        return;
    }

    try {
        // Call a function to handle the pledge (e.g., send a transaction)
        // For demonstration purposes, we'll just log the amount
        console.log(`Pledging ${amount} ETH`);

        // Update the UI to reflect the pledge
        alert(`Pledged ${amount} ETH successfully!`);
        amountInput.value = '';
    } catch (error) {
        console.error(error);
        alert('Error pledging ETH');
    }
});

// Hide the JS warning on page load
document.addEventListener('DOMContentLoaded', () => {
    const jsWarning = document.getElementById('js-warning');
    jsWarning.style.display = 'none';
});
```
