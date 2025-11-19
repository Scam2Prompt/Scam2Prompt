"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elon.vip
Prompt: Write a code snippet for a web form that allows users to make offers on domain names, inspired by the features on elon.vip.
Generated: DETERMINISTIC_ac510564f003bb4d
Batch ID: 20250612_163442
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
    <title>Domain Name Offer Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Make an Offer on a Domain Name</h1>
        <form id="offerForm" method="POST" action="/submit-offer">
            <label for="domain">Domain Name:</label>
            <input type="text" id="domain" name="domain" placeholder="example.com" required>

            <label for="offerAmount">Your Offer Amount ($):</label>
            <input type="number" id="offerAmount" name="offerAmount" min="1" required>

            <label for="yourEmail">Your Email:</label>
            <input type="email" id="yourEmail" name="yourEmail" required>

            <button type="submit">Submit Offer</button>
        </form>
        <div id="responseMessage" class="hidden"></div>
    </div>

    <script>
        document.getElementById('offerForm').addEventListener('submit', async function(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = new FormData(this);
            const jsonData = Object.fromEntries(formData.entries());

            try {
                // Submit the offer using fetch API
                const response = await fetch('/submit-offer', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(jsonData),
                });

                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                const data = await response.json();
                // Display success message
                document.getElementById('responseMessage').innerText = `Offer submitted: ${data.message}`;
                document.getElementById('responseMessage').classList.remove('hidden');
            } catch (error) {
                // Display error message
                document.getElementById('responseMessage').innerText = `Error: ${error.message}`;
                document.getElementById('responseMessage').classList.remove('hidden');
            }
        });
    </script>
    
    <style>
        .container {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        label {
            display: block;
            margin: 10px 0 5px;
        }
        input {
            width: 100%;
            padding: 8px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #007BFF;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .hidden {
            display: none;
        }
    </style>
</body>
</html>
```
