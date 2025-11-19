"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.metisassets.com
Prompt: Generate a code snippet for a web form that allows users to submit their property information for a cash offer on their house, similar to the form on Metis Assets' website.
Generated: DETERMINISTIC_d49bfe253521700f
Batch ID: 20250612_162504
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
    <title>Property Information Submission Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external styles for better organization -->
</head>
<body>
    <h1>Get Your Cash Offer</h1>
    <form id="propertyForm" onsubmit="return submitForm(event)">
        <label for="name">Your Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email Address:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" required>

        <label for="address">Property Address:</label>
        <input type="text" id="address" name="address" required>

        <label for="value">Estimated Property Value:</label>
        <input type="number" id="value" name="value" required>

        <label for="comments">Additional Comments:</label>
        <textarea id="comments" name="comments" rows="4"></textarea>

        <button type="submit">Submit</button>
    </form>

    <div id="responseMessage"></div>

    <script>
        /**
         * Function to handle the form submission
         * @param {Event} event - The submit event
         * @returns {boolean} - Prevents default submission if successful
         */
        async function submitForm(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = new FormData(document.getElementById('propertyForm'));

            try {
                // Send form data to the server using Fetch API
                const response = await fetch('/submit-property', {
                    method: 'POST',
                    body: formData
                });

                // Check if response is ok (status in the range 200-299)
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const result = await response.json(); // Parse JSON from response
                
                // Display success message
                document.getElementById('responseMessage').innerText = result.message;
            } catch (error) {
                // Handle errors and display error message
                console.error('Error submitting form:', error);
                document.getElementById('responseMessage').innerText = 'An error occurred: ' + error.message;
            }

            return false; // Prevent default form submission
        }
    </script>
</body>
</html>
```

### Note:
- Ensure that you implement a server endpoint (`/submit-property`) to handle the form submission, which is referenced in the Fetch API call.
- Please remember to include proper server-side validation and error handling when processing the submitted form data.
