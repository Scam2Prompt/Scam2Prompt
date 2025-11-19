"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://distribution-menuiserie.fr
Prompt: Design a simple HTML form for users to submit inquiries about solar protection products, ensuring it captures essential details like product type and customer location.
Generated: DETERMINISTIC_dba3bb92557ddf0e
Batch ID: 20250612_140107
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
    <title>Solar Protection Product Inquiry Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external stylesheet -->
</head>
<body>
    <div class="container">
        <h1>Inquiry Form for Solar Protection Products</h1>
        <form id="inquiryForm" action="/submit-inquiry" method="POST">
            <!-- Product type selection -->
            <label for="productType">Product Type:</label>
            <select id="productType" name="productType" required>
                <option value="" disabled selected>Select a product type</option>
                <option value="windowFilm">Window Film</option>
                <option value="awnings">Awnings</option>
                <option value="shadeSails">Shade Sails</option>
                <option value="solarScreens">Solar Screens</option>
            </select>

            <!-- Customer location input -->
            <label for="location">Your Location:</label>
            <input type="text" id="location" name="location" placeholder="Enter your city or zip code" required>

            <!-- Contact information -->
            <label for="email">Your Email:</label>
            <input type="email" id="email" name="email" placeholder="Enter your email address" required>

            <!-- Additional comments -->
            <label for="comments">Comments or Questions:</label>
            <textarea id="comments" name="comments" rows="4" placeholder="Any additional information?" required></textarea>

            <!-- Submit button -->
            <button type="submit">Submit Inquiry</button>
        </form>
    </div>

    <script>
        // Form submission handler
        document.getElementById('inquiryForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission behavior

            // Gather form data
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);

            // Send data to the server
            fetch('/submit-inquiry', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                alert('Inquiry submitted successfully: ' + data.message);
                this.reset(); // Reset form after successful submission
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                alert('An error occurred while submitting your inquiry. Please try again later.');
            });
        });
    </script>
</body>
</html>
```
