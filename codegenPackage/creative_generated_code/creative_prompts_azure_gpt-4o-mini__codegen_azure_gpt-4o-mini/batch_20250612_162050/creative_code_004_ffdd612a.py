"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oromaticas.com
Prompt: Design a simple HTML form that collects user information for contacting a business like Oromáticas, focusing on natural and chemical-free products.
Generated: DETERMINISTIC_ffdd612af87846b0
Batch ID: 20250612_162050
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
    <title>Contact Us - Oromáticas</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Contact Oromáticas</h1>
        <p>We focus on natural and chemical-free products. We would love to hear from you!</p>
    </header>
    
    <main>
        <form id="contact-form" action="/submit_form" method="POST">
            <!-- User Name Input -->
            <label for="name">Your Name:</label>
            <input type="text" id="name" name="name" required placeholder="John Doe">

            <!-- User Email Input -->
            <label for="email">Your Email:</label>
            <input type="email" id="email" name="email" required placeholder="example@example.com">

            <!-- User Message Input -->
            <label for="message">Your Message:</label>
            <textarea id="message" name="message" required placeholder="Type your message here..."></textarea>

            <!-- Submit Button -->
            <button type="submit">Send Message</button>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Oromáticas. All rights reserved.</p>
    </footer>

    <script>
        // Form submission handler
        document.getElementById('contact-form').onsubmit = function(event) {
            // Prevent default form submission
            event.preventDefault();

            // Collect form data
            const formData = new FormData(this);

            // Fetch API POST request to submit the form
            fetch(this.action, {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.json(); // Parse JSON response
            })
            .then(data => {
                alert('Your message has been sent successfully!');
                this.reset(); // Reset the form fields
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                alert('There was an error sending your message. Please try again later.');
            });
        };
    </script>
</body>
</html>
```
