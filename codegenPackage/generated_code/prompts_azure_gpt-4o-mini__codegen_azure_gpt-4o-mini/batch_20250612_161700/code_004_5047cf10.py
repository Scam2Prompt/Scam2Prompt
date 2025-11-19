"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: Design a simple HTML form that captures customer information for glass and aluminum service inquiries, reflecting the contact methods available on CristalesGraf's site.
Generated: DETERMINISTIC_5047cf10ffce1dc9
Batch ID: 20250612_161700
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
    <title>Service Inquiry Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Service Inquiry Form</h1>
        <p>Please fill out the form below for inquiries regarding glass and aluminum services.</p>
    </header>

    <form id="inquiryForm" action="/submit-inquiry" method="POST">
        <!-- Customer Name -->
        <label for="name">Full Name:</label>
        <input type="text" id="name" name="name" required placeholder="John Doe">

        <!-- Email Address -->
        <label for="email">Email Address:</label>
        <input type="email" id="email" name="email" required placeholder="example@example.com">

        <!-- Phone Number -->
        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" required placeholder="(123) 456-7890">

        <!-- Inquiry Type -->
        <label for="inquiryType">Type of Inquiry:</label>
        <select id="inquiryType" name="inquiryType" required>
            <option value="" disabled selected>Select an option</option>
            <option value="glass">Glass Services</option>
            <option value="aluminum">Aluminum Services</option>
        </select>

        <!-- Message -->
        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="4" required placeholder="Please describe your inquiry..."></textarea>

        <!-- Preferred Contact Method -->
        <fieldset>
            <legend>Preferred Contact Method:</legend>
            <label>
                <input type="radio" name="contactMethod" value="email" required>
                Email
            </label>
            <label>
                <input type="radio" name="contactMethod" value="phone">
                Phone
            </label>
        </fieldset>

        <!-- Submit Button -->
        <button type="submit">Submit Inquiry</button>
    </form>

    <footer>
        <p>&copy; 2023 CristalesGraf. All rights reserved.</p>
    </footer>

    <script>
        // Form submission handler
        document.getElementById('inquiryForm').addEventListener('submit', function(event) {
            // Prevent default form submission
            event.preventDefault();

            // Perform form validation if necessary
            // Here you can add additional validation logic if needed

            // Submit the form using Fetch API
            fetch(this.action, {
                method: this.method,
                body: new FormData(this)
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // Handle success (e.g., show a success message)
                alert('Inquiry submitted successfully!');
            })
            .catch(error => {
                // Handle error (e.g., show an error message)
                console.error('There was a problem with the fetch operation:', error);
                alert('There was an error submitting your inquiry. Please try again later.');
            });
        });
    </script>
</body>
</html>
```
