"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Design a simple HTML form for users to submit inquiries about tailored horse riding tours at Chile Horse Riding, ensuring it captures essential details like the desired tour and number of participants.
Generated: DETERMINISTIC_f33a334ffee5b248
Batch ID: 20250612_162051
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
    <title>Inquiry Form - Chile Horse Riding</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Chile Horse Riding Tours Inquiry</h1>
    </header>
    
    <main>
        <form id="inquiryForm" action="/submit-inquiry" method="POST">
            <fieldset>
                <legend>Inquiry Details</legend>

                <!-- Input for the user's name -->
                <label for="name">Your Name:</label>
                <input type="text" id="name" name="name" required placeholder="Enter your name">

                <!-- Input for the user's email -->
                <label for="email">Your Email:</label>
                <input type="email" id="email" name="email" required placeholder="Enter your email">

                <!-- Dropdown for selecting the desired tour -->
                <label for="tour">Desired Tour:</label>
                <select id="tour" name="tour" required>
                    <option value="" disabled selected>Select a tour</option>
                    <option value="Andes Adventure">Andes Adventure</option>
                    <option value="Coastal Ride">Coastal Ride</option>
                    <option value="Patagonian Experience">Patagonian Experience</option>
                </select>

                <!-- Input for the number of participants -->
                <label for="participants">Number of Participants:</label>
                <input type="number" id="participants" name="participants" min="1" required placeholder="Enter number of participants">

                <!-- Submit button -->
                <button type="submit">Submit Inquiry</button>
            </fieldset>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Chile Horse Riding. All rights reserved.</p>
    </footer>

    <script>
        // Form submission handler
        document.getElementById('inquiryForm').addEventListener('submit', function(event) {
            // Prevent default form submission
            event.preventDefault();

            // Gather form data
            const formData = new FormData(this);

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
                // Handle success (e.g., show a success message)
                alert('Inquiry submitted successfully!');
            })
            .catch(error => {
                // Handle errors (e.g., show an error message)
                console.error('There was a problem with the fetch operation:', error);
                alert('There was an error submitting your inquiry. Please try again later.');
            });
        });
    </script>
</body>
</html>
```
