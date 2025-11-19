"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cristalesgraf.com
Prompt: Design a simple HTML form that captures customer information for glass and aluminum service inquiries, reflecting the contact methods available on CristalesGraf's site.
Generated: DETERMINISTIC_5047cf10ffce1dc9
Batch ID: 20250612_161700
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
    <title>Service Inquiry Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Service Inquiry Form</h1>
    </header>
    
    <form id="inquiryForm" method="POST" action="submit_inquiry.php">
        <fieldset>
            <legend>Customer Information</legend>

            <!-- Name input -->
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required placeholder="John Doe">

            <!-- Email input -->
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="example@example.com">

            <!-- Phone input -->
            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required placeholder="(123) 456-7890">

            <!-- Inquiry Type selection -->
            <label for="inquiryType">Type of Inquiry:</label>
            <select id="inquiryType" name="inquiryType" required>
                <option value="" disabled selected>Select an option</option>
                <option value="glass">Glass Services</option>
                <option value="aluminum">Aluminum Services</option>
            </select>

            <!-- Message textarea -->
            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="4" placeholder="Your message..."></textarea>

            <!-- Preferred contact method -->
            <fieldset>
                <legend>Preferred Contact Method:</legend>
                <label>
                    <input type="radio" name="contactMethod" value="email" required> Email
                </label>
                <label>
                    <input type="radio" name="contactMethod" value="phone"> Phone
                </label>
            </fieldset>

            <!-- Consent checkbox -->
            <label>
                <input type="checkbox" name="consent" required> I consent to having this website store my submitted information.
            </label>
        </fieldset>

        <!-- Submit button -->
        <button type="submit">Submit Inquiry</button>
    </form>

    <!-- Javascript for form validation -->
    <script>
        document.getElementById('inquiryForm').addEventListener('submit', function(event) {
            // Prevent form submission for custom validation
            if (!this.checkValidity()) {
                event.preventDefault(); // Prevent default submission if the form is invalid
                alert('Please fill out all required fields correctly.'); // Alert user of invalid fields
            }
        });
    </script>
</body>
</html>
```
