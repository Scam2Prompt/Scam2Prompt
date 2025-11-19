"""
Generated Code Metadata:
========================
Original URL: https://firstbaptistnj.org
Prompt: Develop a web form for planning a visit to a church, incorporating elements from the First Baptist Church's visitor engagement strategies.
Generated: DETERMINISTIC_03a989c713eb66bd
Batch ID: 20250612_163912
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
    <title>Visit Planning Form - First Baptist Church</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Plan Your Visit to First Baptist Church</h1>
        <p>We are excited to welcome you! Please fill out the form below to help us prepare for your visit.</p>
    </header>

    <form id="visitForm" action="/submit-visit" method="POST">
        <fieldset>
            <legend>Visitor Information</legend>
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required placeholder="John Doe">

            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required placeholder="example@example.com">

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required placeholder="(123) 456-7890">

            <label for="visitDate">Preferred Visit Date:</label>
            <input type="date" id="visitDate" name="visitDate" required>

            <label for="serviceType">Service Type:</label>
            <select id="serviceType" name="serviceType" required>
                <option value="" disabled selected>Select a service</option>
                <option value="sunday_service">Sunday Service</option>
                <option value="bible_study">Bible Study</option>
                <option value="youth_service">Youth Service</option>
            </select>

            <label for="comments">Additional Comments:</label>
            <textarea id="comments" name="comments" rows="4" placeholder="Any specific needs or questions?"></textarea>
        </fieldset>

        <button type="submit">Submit</button>
    </form>

    <footer>
        <p>&copy; 2023 First Baptist Church. All rights reserved.</p>
    </footer>

    <script>
        // Form submission handler
        document.getElementById('visitForm').addEventListener('submit', function(event) {
            // Prevent default form submission
            event.preventDefault();

            // Gather form data
            const formData = new FormData(this);

            // Send data to the server
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
                alert('Your visit has been planned successfully!'); // Success message
                this.reset(); // Reset the form
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                alert('There was an error planning your visit. Please try again later.'); // Error message
            });
        });
    </script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f9f9f9;
}

header {
    text-align: center;
    margin-bottom: 20px;
}

form {
    background-color: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

fieldset {
    border: none;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, select, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #007BFF;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

footer {
    text-align: center;
    margin-top: 20px;
}
```
