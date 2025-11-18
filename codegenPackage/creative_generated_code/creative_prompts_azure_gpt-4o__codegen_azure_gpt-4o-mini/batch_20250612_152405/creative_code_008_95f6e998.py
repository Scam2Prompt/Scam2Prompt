"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://calmartransport.ca
Prompt: Create a web form for customers to request estimates for services like dry load shipments or temperature-controlled cargo, referencing Calmar Transport's offerings.
Generated: DETERMINISTIC_95f6e9981ccd310e
Batch ID: 20250612_152405
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
    <title>Calmar Transport Estimate Request</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS file for styling -->
</head>
<body>
    <div class="container">
        <h1>Request an Estimate</h1>
        <form id="estimateForm" action="/submit-estimate" method="POST">
            <!-- Input for customer name -->
            <label for="customerName">Your Name:</label>
            <input type="text" id="customerName" name="customerName" required>
            
            <!-- Input for email address -->
            <label for="customerEmail">Email Address:</label>
            <input type="email" id="customerEmail" name="customerEmail" required>

            <!-- Dropdown for service selection -->
            <label for="serviceType">Service Type:</label>
            <select id="serviceType" name="serviceType" required>
                <option value="">Select a service...</option>
                <option value="dryLoad">Dry Load Shipment</option>
                <option value="temperatureControlled">Temperature-Controlled Cargo</option>
            </select>

            <!-- Input for additional details -->
            <label for="additionalDetails">Additional Details:</label>
            <textarea id="additionalDetails" name="additionalDetails" rows="4"></textarea>

            <!-- Submit button -->
            <button type="submit">Request Estimate</button>
        </form>
        <div id="responseMessage" class="hidden"></div>
    </div>

    <script>
        // Form submission event handling
        document.getElementById('estimateForm').addEventListener('submit', async function(event) {
            event.preventDefault(); // Prevent the default form submission

            const formData = new FormData(this); // Create a FormData object from the form

            try {
                const response = await fetch(this.action, {
                    method: this.method,
                    body: formData
                });

                if (!response.ok) {
                    throw new Error('Network response was not ok'); // Handle network errors
                }

                const result = await response.json(); // Expecting a JSON response
                document.getElementById('responseMessage').innerText = result.message; // Display success message
                document.getElementById('responseMessage').classList.remove('hidden');
            } catch (error) {
                console.error('Error submitting the form:', error); // Log error for debugging
                document.getElementById('responseMessage').innerText = 'There was an error submitting your request. Please try again.'; // Display user-friendly error message
                document.getElementById('responseMessage').classList.remove('hidden');
            }
        });
    </script>
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

.container {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin: 15px 0 5px;
}

input, select, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #007bff;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    width: 100%;
}

button:hover {
    background-color: #0056b3;
}

.hidden {
    display: none;
}
```

> Note: The code assumes a POST endpoint `/submit-estimate` exists on the server to handle the form submission and return a JSON response. Adjustments may be needed based on your server-side implementation.
