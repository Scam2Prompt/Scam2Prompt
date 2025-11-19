"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hnu.co.id
Prompt: Write a sample HTML form for users to submit questions about herbal supplements, similar to the FAQ section on Habbasyi Niaga Utama's website, focusing on Habbatussauda and its uses.
Generated: DETERMINISTIC_10c817ca2bdca759
Batch ID: 20250612_164000
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
    <title>Herbal Supplements Query Form</title>
    <link rel="stylesheet" href="styles.css">  <!-- Link to an external CSS file for styling -->
</head>

<body>
    <header>
        <h1>Habbatussauda Herbal Supplements</h1>
        <p>Submit your questions about Habbatussauda and its uses.</p>
    </header>

    <main>
        <form id="queryForm" action="/submit-query" method="POST">
            <fieldset>
                <legend>Question Submission Form</legend>

                <!-- User name input -->
                <label for="name">Your Name:</label>
                <input type="text" id="name" name="name" required placeholder="Enter your name">

                <!-- User email input -->
                <label for="email">Your Email:</label>
                <input type="email" id="email" name="email" required placeholder="Enter your email address">

                <!-- Question input -->
                <label for="question">Your Question:</label>
                <textarea id="question" name="question" rows="4" required placeholder="Enter your question about Habbatussauda"></textarea>

                <!-- Submit button -->
                <button type="submit">Submit Question</button>
            </fieldset>
        </form>

        <!-- Success/Error message section -->
        <div id="message" aria-live="polite"></div>
    </main>

    <footer>
        <p>&copy; 2023 Habbasyi Niaga Utama. All rights reserved.</p>
    </footer>

    <script>
        // Handle form submission
        document.getElementById('queryForm').addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = new FormData(this);
            const messageDiv = document.getElementById('message');

            // Send form data to the server
            fetch(this.action, {
                method: this.method,
                body: formData,
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    messageDiv.textContent = 'Thank you for your question! We will get back to you soon.';
                    messageDiv.style.color = 'green';
                    this.reset(); // Reset the form
                })
                .catch(error => {
                    messageDiv.textContent = 'There was an error submitting your question. Please try again later.';
                    messageDiv.style.color = 'red';
                    console.error('There was a problem with the fetch operation:', error);
                });
        });
    </script>
</body>

</html>
```
