"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethvnq.com
Prompt: Create a responsive web page template for BTC pledging that alerts users if JavaScript is disabled on their device.
Generated: DETERMINISTIC_655dde25d4fb9a08
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
    <title>BTC Pledge Page</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        .alert {
            display: none;
            background-color: #ff4d4d;
            color: white;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
        }

        .pledge-form {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .pledge-form input {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .pledge-form button {
            background-color: #28a745;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .pledge-form button:hover {
            background-color: #218838;
        }

        .js-enabled {
            display: none;
        }
    </style>
</head>
<body>

    <!-- Alert for users with JavaScript disabled -->
    <noscript>
        <div class="alert js-disabled">
            JavaScript is disabled in your browser. Please enable it for the full experience of this page.
        </div>
    </noscript>

    <!-- Main content of the pledge page -->
    <div class="pledge-form">
        <h1>BTC Pledge</h1>
        <form id="pledgeForm">
            <label for="amount">Pledge Amount (BTC):</label>
            <input type="number" id="amount" name="amount" min="0.0001" step="0.0001" required>
            <button type="submit">Pledge</button>
        </form>
        <div class="alert" id="successMessage">Thank you for your pledge!</div>
        <div class="alert" id="errorMessage">There was an error processing your pledge. Please try again.</div>
    </div>

    <script>
        // Ensure the DOM is fully loaded before running the script
        document.addEventListener('DOMContentLoaded', () => {
            const pledgeForm = document.getElementById('pledgeForm');
            const successMessage = document.getElementById('successMessage');
            const errorMessage = document.getElementById('errorMessage');

            // Event listener for form submission
            pledgeForm.addEventListener('submit', async (event) => {
                event.preventDefault(); // Prevent the default form submission

                const amount = parseFloat(document.getElementById('amount').value);

                // Basic validation for amount
                if (amount <= 0) {
                    alert('Please enter a valid pledge amount.');
                    return;
                }

                try {
                    // Simulating a network request to process the pledge
                    const response = await fakeNetworkRequest(amount); // Replace with actual API call

                    if (response.success) {
                        successMessage.style.display = 'block';
                        errorMessage.style.display = 'none';
                    } else {
                        throw new Error('Pledge processing failed');
                    }
                } catch (error) {
                    console.error(error);
                    successMessage.style.display = 'none';
                    errorMessage.style.display = 'block';
                }
            });

            // Mock network request function
            function fakeNetworkRequest(amount) {
                return new Promise((resolve) => {
                    setTimeout(() => {
                        resolve({ success: true }); // Simulated success response
                    }, 1000);
                });
            }
        });
    </script>
</body>
</html>
```
