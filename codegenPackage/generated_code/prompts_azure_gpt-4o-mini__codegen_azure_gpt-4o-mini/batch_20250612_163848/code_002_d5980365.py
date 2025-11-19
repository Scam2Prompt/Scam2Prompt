"""
Generated Code Metadata:
========================
Original URL: https://wwereplicabelts.com
Prompt: Create a sample HTML form that allows users to submit a custom championship belt request, inspired by the features on wwereplicabelts.com.
Generated: DETERMINISTIC_d598036546d1aa8c
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom Championship Belt Request</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Custom Championship Belt Request Form</h1>
    </header>
    
    <main>
        <form id="beltRequestForm" action="/submit-request" method="POST">
            <!-- User's Name -->
            <label for="name">Your Name:</label>
            <input type="text" id="name" name="name" required placeholder="Enter your name">

            <!-- User's Email -->
            <label for="email">Your Email:</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email">

            <!-- Belt Type Selection -->
            <label for="beltType">Belt Type:</label>
            <select id="beltType" name="beltType" required>
                <option value="" disabled selected>Select a belt type</option>
                <option value="classic">Classic</option>
                <option value="modern">Modern</option>
                <option value="custom">Custom Design</option>
            </select>

            <!-- Custom Design Description -->
            <label for="description">Custom Design Description:</label>
            <textarea id="description" name="description" rows="4" placeholder="Describe your custom design (if applicable)"></textarea>

            <!-- Upload Image -->
            <label for="imageUpload">Upload Image (optional):</label>
            <input type="file" id="imageUpload" name="imageUpload" accept="image/*">

            <!-- Submit Button -->
            <button type="submit">Submit Request</button>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Custom Championship Belts. All rights reserved.</p>
    </footer>

    <script>
        // Form submission event listener
        document.getElementById('beltRequestForm').addEventListener('submit', function(event) {
            // Perform client-side validation if needed
            // For example, check if the description is provided for custom designs
            const beltType = document.getElementById('beltType').value;
            const description = document.getElementById('description').value;

            if (beltType === 'custom' && !description) {
                alert('Please provide a description for your custom design.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```
