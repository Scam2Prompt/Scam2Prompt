"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpncg.edu.mx
Prompt: Develop a simple HTML form for parents to contact the Colegio Panamericano, ensuring it captures essential details like name, phone number, and message.
Generated: DETERMINISTIC_530564cebc60b72c
Batch ID: 20250612_155153
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
    <title>Contact Us - Colegio Panamericano</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Contact Colegio Panamericano</h1>
    </header>

    <main>
        <form id="contactForm" method="POST" action="/submit-contact">
            <fieldset>
                <legend>Contact Information</legend>
                
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required placeholder="Enter your name">
                
                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required placeholder="Enter your phone number">

                <label for="message">Message:</label>
                <textarea id="message" name="message" required placeholder="Enter your message" rows="4" cols="50"></textarea>
                
                <button type="submit">Submit</button>
            </fieldset>
        </form>
        
        <div id="responseMessage" aria-live="polite"></div> <!-- For displaying responses after form submission -->
    </main>

    <footer>
        <p>&copy; 2023 Colegio Panamericano. All rights reserved.</p>
    </footer>

    <script>
        // Handle form submission
        document.getElementById('contactForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = new FormData(this);

            // Send data to the server
            fetch('/submit-contact', {
                method: 'POST',
                body: formData,
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok.');
                }
                return response.text(); // or response.json() if expecting JSON
            })
            .then(data => {
                // Display success message
                document.getElementById('responseMessage').textContent = 'Thank you for contacting us! We will get back to you shortly.';
                this.reset(); // Clear the form
            })
            .catch(error => {
                // Handle errors
                document.getElementById('responseMessage').textContent = 'There was an error submitting your message. Please try again later.';
                console.error('Error:', error);
            });
        });
    </script>
</body>
</html>
```
