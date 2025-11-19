"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chile-horseriding.com
Prompt: Design a simple HTML form for users to submit inquiries about tailored horse riding tours at Chile Horse Riding, ensuring it captures essential details like the desired tour and number of participants.
Generated: DETERMINISTIC_f33a334ffee5b248
Batch ID: 20250612_162051
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
    <title>Inquiry Form - Chile Horse Riding</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Inquiry Form for Tailored Horse Riding Tours</h1>
        <p>Please fill out the form below to inquire about our tours.</p>
    </header>
    
    <main>
        <form id="inquiryForm" action="/submit-inquiry" method="POST">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required placeholder="Enter your full name">

            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email address">

            <label for="tour">Desired Tour:</label>
            <select id="tour" name="tour" required>
                <option value="" disabled selected>Select a tour</option>
                <option value="half-day">Half Day Tour</option>
                <option value="full-day">Full Day Tour</option>
                <option value="multi-day">Multi-day Tour</option>
            </select>

            <label for="participants">Number of Participants:</label>
            <input type="number" id="participants" name="participants" min="1" required placeholder="Enter number of participants">

            <label for="message">Additional Message:</label>
            <textarea id="message" name="message" rows="4" placeholder="Any additional information or requests..."></textarea>

            <button type="submit">Submit Inquiry</button>
        </form>
    </main>
    
    <footer>
        <p>&copy; 2023 Chile Horse Riding. All rights reserved.</p>
    </footer>

    <script>
        // Add an event listener to handle form submission
        document.getElementById('inquiryForm').addEventListener('submit', function(event) {
            // Prevent form submission if there are validation errors
            if (!this.checkValidity()) {
                event.preventDefault(); // Prevent form submission
                alert("Please fill out all required fields correctly."); // Alert user
            }
        });
    </script>
</body>
</html>
```
