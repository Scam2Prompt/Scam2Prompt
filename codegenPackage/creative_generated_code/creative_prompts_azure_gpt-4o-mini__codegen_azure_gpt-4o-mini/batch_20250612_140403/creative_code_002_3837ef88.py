"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ether-pool.org
Prompt: Generate a code snippet for a web form that allows users to submit their own ads, similar to the functionality on Kleinanzeigen.
Generated: DETERMINISTIC_3837ef889f0ca748
Batch ID: 20250612_140403
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
    <title>Submit Your Ad</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>

    <h1>Submit Your Ad</h1>
    <form id="adForm" method="POST" action="/submit-ad">
        <label for="title">Ad Title:</label>
        <input type="text" id="title" name="title" required maxlength="100">
        
        <label for="description">Description:</label>
        <textarea id="description" name="description" required maxlength="1000"></textarea>
        
        <label for="price">Price:</label>
        <input type="number" id="price" name="price" required min="0" step="0.01">
        
        <label for="category">Category:</label>
        <select id="category" name="category" required>
            <option value="">Select a category</option>
            <option value="furniture">Furniture</option>
            <option value="electronics">Electronics</option>
            <option value="vehicles">Vehicles</option>
            <option value="clothing">Clothing</option>
        </select>
        
        <label for="contact">Contact Email:</label>
        <input type="email" id="contact" name="contact" required>

        <button type="submit">Submit Ad</button>
    </form>

    <script>
        // Form submission event handler
        document.getElementById('adForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = new FormData(this);

            // Send data to server using Fetch API
            fetch('/submit-ad', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                alert('Ad submitted successfully!'); // Success message
                this.reset(); // Reset form fields
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                alert('There was an error submitting your ad. Please try again.'); // Error message
            });
        });
    </script>

</body>
</html>
```
