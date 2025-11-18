"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imtaoekecn.com
Prompt: Create a JavaScript-based user interface for an Ethereum pledge system that alerts users if JavaScript is disabled, inspired by the ETH Pledge website's functionality.
Generated: DETERMINISTIC_68ac1d8192f9a797
Batch ID: 20250612_145619
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
    <title>Ethereum Pledge System</title>
    <style>
        /* Basic styles for the pledge form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
        }
        .pledge-form {
            display: flex;
            flex-direction: column;
        }
        .pledge-form input, .pledge-form button {
            margin: 10px 0;
            padding: 10px;
            font-size: 16px;
        }
        .alert {
            color: red;
            text-align: center;
        }
    </style>
</head>
<body>

    <noscript>
        <div class="alert">
            <strong>JavaScript is disabled in your browser.</strong> Please enable JavaScript to use the Ethereum Pledge System.
        </div>
    </noscript>

    <div class="container">
        <h1>Ethereum Pledge System</h1>
        <form class="pledge-form" id="pledgeForm">
            <input type="text" id="name" placeholder="Your Name" required>
            <input type="number" id="amount" placeholder="Pledge Amount (in ETH)" required min="0.01" step="0.01">
            <button type="submit">Pledge</button>
        </form>
        <div id="message" class="alert"></div>
    </div>

    <script>
        // Wait for the document to be fully loaded
        document.addEventListener("DOMContentLoaded", function () {
            const pledgeForm = document.getElementById('pledgeForm');
            const messageDiv = document.getElementById('message');

            // Handle form submission
            pledgeForm.addEventListener('submit', async function (event) {
                event.preventDefault(); // Prevent the form from submitting traditionally

                // Get the input values
                const name = document.getElementById('name').value;
                const amount = document.getElementById('amount').value;

                // Validate inputs
                if (amount <= 0) {
                    displayMessage("Pledge amount must be greater than zero.", true);
                    return;
                }

                // Simulate sending the pledge to the Ethereum smart contract
                try {
                    // Placeholder for the actual pledge function
                    await sendPledgeToBlockchain(name, amount);
                    displayMessage(`Thank you, ${name}! You have pledged ${amount} ETH.`, false);
                } catch (error) {
                    console.error("Error during pledge:", error);
                    displayMessage("There was an error processing your pledge. Please try again later.", true);
                }
            });

            // Display message to the user
            function displayMessage(message, isError) {
                messageDiv.textContent = message;
                messageDiv.style.color = isError ? 'red' : 'green';
            }

            // Placeholder for the pledge function (to be integrated with actual blockchain interaction)
            async function sendPledgeToBlockchain(name, amount) {
                // Simulate request delay
                return new Promise((resolve, reject) => {
                    setTimeout(() => {
                        // Simulate success or failure
                        Math.random() > 0.1 ? resolve() : reject(new Error("Pledge failed"));
                    }, 1000);
                });
            }
        });
    </script>
</body>
</html>
```
