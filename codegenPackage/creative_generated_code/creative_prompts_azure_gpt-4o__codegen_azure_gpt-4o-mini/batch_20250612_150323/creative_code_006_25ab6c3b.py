"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamark.lt
Prompt: Create a JavaScript snippet for integrating a "Get a Commercial Offer" form into a website, similar to the forms used on Metamark's site.
Generated: DETERMINISTIC_25ab6c3bdbf9bce0
Batch ID: 20250612_150323
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
    <title>Get a Commercial Offer</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
        }
        #offerForm {
            max-width: 500px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        input[type="text"], input[type="email"], textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>

    <h2>Get a Commercial Offer</h2>
    <form id="offerForm" action="#" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="company">Company:</label>
        <input type="text" id="company" name="company" required>

        <label for="details">Details:</label>
        <textarea id="details" name="details" rows="4"></textarea>

        <input type="submit" value="Submit">
    </form>

    <div id="responseMessage" style="margin-top: 20px;"></div>

    <script>
        // Listen for the form submission
        document.getElementById('offerForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            // Gather form data
            const formData = new FormData(this);
            const data = {};
            formData.forEach((value, key) => {
                data[key] = value;
            });

            // Send the data to the server
            fetch('/submit-offer', { // Replace with your server endpoint
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => {
                // Check if the response is okay
                if (!response.ok) {
                    throw new Error('Network response was not ok: ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                // Display success message
                document.getElementById('responseMessage').innerText = 'Offer submitted successfully!';
                document.getElementById('offerForm').reset(); // Reset the form
            })
            .catch(error => {
                // Display error message
                document.getElementById('responseMessage').innerText = 'Error submitting offer: ' + error.message;
            });
        });
    </script>

</body>
</html>
```
