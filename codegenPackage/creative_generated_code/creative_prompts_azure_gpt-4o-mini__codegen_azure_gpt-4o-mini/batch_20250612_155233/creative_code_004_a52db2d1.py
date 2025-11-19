"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amici.nz
Prompt: Construct a simple HTML form that enables customers to submit inquiries to Amici Italian Cafe, ensuring it captures all necessary contact information.
Generated: DETERMINISTIC_a52db2d17d8371e5
Batch ID: 20250612_155233
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
    <title>Inquiry Form - Amici Italian Cafe</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external stylesheet for better styling -->
</head>
<body>
    <header>
        <h1>Contact Us - Amici Italian Cafe</h1>
    </header>
    
    <main>
        <form id="inquiryForm" action="/submit-inquiry" method="POST" novalidate>
            <fieldset>
                <legend>Submit Your Inquiry</legend>

                <!-- Name Input -->
                <label for="name">Full Name <span class="required">*</span></label>
                <input type="text" id="name" name="name" required placeholder="John Doe">

                <!-- Email Input -->
                <label for="email">Email Address <span class="required">*</span></label>
                <input type="email" id="email" name="email" required placeholder="example@example.com">

                <!-- Phone Number Input -->
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" name="phone" placeholder="(123) 456-7890">

                <!-- Inquiry Message -->
                <label for="message">Your Message <span class="required">*</span></label>
                <textarea id="message" name="message" required rows="4" placeholder="Write your inquiry here..."></textarea>

                <!-- Submit Button -->
                <button type="submit">Submit Inquiry</button>
            </fieldset>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Amici Italian Cafe. All rights reserved.</p>
    </footer>

    <script>
        // Form submission handler
        document.getElementById('inquiryForm').addEventListener('submit', function(event) {
            // Prevent default form submission
            event.preventDefault();

            // Basic client-side validation
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;

            if (name && email && message) {
                // Assuming AJAX call or form submission logic here
                alert('Thank you for your inquiry, ' + name + '. We will get back to you shortly!');
                this.submit(); // Proceed to submit the form if validation passes
            } else {
                alert('Please fill out all required fields.');
            }
        });
    </script>
</body>
</html>
```
