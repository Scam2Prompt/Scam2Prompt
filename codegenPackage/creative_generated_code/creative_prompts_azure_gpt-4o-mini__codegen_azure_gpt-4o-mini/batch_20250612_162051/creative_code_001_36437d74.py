"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drcelsolemos.com.br
Prompt: Generate a code snippet for a web form that allows users to inquire about orthodontic treatments and schedule an evaluation at Dr. Celso Lemos' clinic.
Generated: DETERMINISTIC_36437d74d1945e4a
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
    <title>Orthodontic Inquiry Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Orthodontic Treatment Inquiry</h1>
        <p>Please fill out the form below to inquire about treatments and schedule your evaluation.</p>
    </header>
    
    <form id="inquiryForm" action="/submit-inquiry" method="POST">
        <label for="name">Full Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" required>

        <label for="treatment">Treatment Inquiry:</label>
        <textarea id="treatment" name="treatment" rows="4" required></textarea>

        <label for="appointmentDate">Preferred Appointment Date:</label>
        <input type="date" id="appointmentDate" name="appointmentDate" required>

        <button type="submit">Submit Inquiry</button>
    </form>

    <footer>
        <p>&copy; 2023 Dr. Celso Lemos Orthodontics. All rights reserved.</p>
    </footer>

    <script>
        // Add an event listener for form submission
        document.getElementById('inquiryForm').addEventListener('submit', function(event) {
            // Prevent form submission if there are validation errors
            if (!this.checkValidity()) {
                event.preventDefault();
                alert('Please fill in all required fields.');
                return;
            }

            // Display a confirmation message
            alert('Thank you for your inquiry! We will get back to you soon.');
        });
    </script>
</body>
</html>
```
