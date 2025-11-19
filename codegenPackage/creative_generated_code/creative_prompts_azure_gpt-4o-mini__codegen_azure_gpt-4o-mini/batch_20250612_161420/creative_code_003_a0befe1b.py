"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bossasopetroleum.com
Prompt: Create a code snippet for a contact form that captures user inquiries for a petrol company, reflecting the contact methods used by Bosasa Petroleum.
Generated: DETERMINISTIC_a0befe1b226bd101
Batch ID: 20250612_161420
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
    <title>Contact Us - Bosasa Petroleum</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Contact Bosasa Petroleum</h1>
        <p>Your inquiries are important to us. Please fill out the form below to get in touch.</p>
    </header>
    
    <main>
        <form id="contactForm" action="/submit-contact" method="POST" novalidate>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            
            <label for="phone">Phone:</label>
            <input type="tel" id="phone" name="phone" required>
            
            <label for="inquiry">Inquiry:</label>
            <textarea id="inquiry" name="inquiry" required></textarea>
            
            <button type="submit">Submit Inquiry</button>
        </form>
        
        <div id="formFeedback" aria-live="polite"></div> <!-- For displaying feedback to the user -->
    </main>

    <footer>
        <p>Contact us at:</p>
        <p>Email: <a href="mailto:support@bosasa.com">support@bosasa.com</a></p>
        <p>Phone: <a href="tel:+27123456789">+27 12 345 6789</a></p>
    </footer>

    <script>
        document.getElementById('contactForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission
            
            // Gather form data
            const formData = new FormData(this);
            const xhr = new XMLHttpRequest();
            xhr.open('POST', this.action, true);
            
            // Set up error handling
            xhr.onload = function() {
                if (xhr.status >= 200 && xhr.status < 300) {
                    document.getElementById('formFeedback').textContent = 'Your inquiry has been submitted successfully!';
                    document.getElementById('contactForm').reset(); // Reset the form upon success
                } else {
                    document.getElementById('formFeedback').textContent = 'There was an error submitting your inquiry. Please try again.';
                }
            };

            xhr.onerror = function() {
                document.getElementById('formFeedback').textContent = 'An error occurred while processing your request.';
            };

            // Send the form data
            xhr.send(formData);
        });
    </script>
</body>
</html>
```
