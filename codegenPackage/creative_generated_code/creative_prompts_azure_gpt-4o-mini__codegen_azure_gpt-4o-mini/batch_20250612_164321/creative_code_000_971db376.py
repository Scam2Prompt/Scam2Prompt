"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gyvseguros.com
Prompt: Generate a code snippet for a web form that allows users to request a quote for different types of insurance policies such as auto, health, and life insurance as described on the GYV Seguros website.
Generated: DETERMINISTIC_971db376c3c26dfc
Batch ID: 20250612_164321
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
    <title>Insurance Quote Request Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Request a Quote</h1>
        <form id="quoteForm" action="/submit-quote" method="POST">
            <!-- User's name input -->
            <label for="fullName">Full Name:</label>
            <input type="text" id="fullName" name="fullName" required>

            <!-- User's email input -->
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="insuranceType">Select Insurance Type:</label>
            <select id="insuranceType" name="insuranceType" required>
                <option value="" disabled selected>Select a type</option>
                <option value="auto">Auto Insurance</option>
                <option value="health">Health Insurance</option>
                <option value="life">Life Insurance</option>
            </select>

            <!-- User's additional information input -->
            <label for="additionalInfo">Additional Information:</label>
            <textarea id="additionalInfo" name="additionalInfo" rows="4"></textarea>

            <button type="submit">Request Quote</button>
        </form>
        
        <div id="responseMessage" aria-live="polite"></div> <!-- Container for response message -->
    </div>

    <script>
        // Attach event listener to the form
        document.getElementById('quoteForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission
            
            // Gather form data
            const formData = new FormData(this);
            const url = this.action;

            // Send the form data using fetch API
            fetch(url, {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json(); // Parse JSON response
            })
            .then(data => {
                // Display success message
                document.getElementById('responseMessage').innerText = 'Quote request submitted successfully!';
            })
            .catch(error => {
                // Handle errors gracefully
                console.error('There was a problem with the fetch operation:', error);
                document.getElementById('responseMessage').innerText = 'Error submitting your request. Please try again later.';
            });
        });
    </script>
</body>
</html>
```
