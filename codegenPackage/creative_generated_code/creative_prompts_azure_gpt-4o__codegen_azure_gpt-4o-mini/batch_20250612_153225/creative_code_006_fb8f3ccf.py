"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://efeitoharmonie.com.br
Prompt: Suggest tools or libraries for creating a virtual consultation form for hair transplant clinics, inspired by the contact form on the Efeito Harmonie website.
Generated: DETERMINISTIC_fb8f3ccf29509ad6
Batch ID: 20250612_153225
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
    <title>Virtual Consultation Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Virtual Consultation Form</h1>
        <form id="consultationForm" method="POST" action="/submit-form">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required>

            <label for="consultationType">Type of Consultation:</label>
            <select id="consultationType" name="consultationType" required>
                <option value="">Select</option>
                <option value="initial">Initial Consultation</option>
                <option value="follow-up">Follow-Up Consultation</option>
            </select>

            <label for="message">Additional Information:</label>
            <textarea id="message" name="message" rows="4" placeholder="Any specific questions or concerns..."></textarea>

            <button type="submit">Submit</button>
        </form>
        <div id="formResponse"></div>
    </div>

    <script>
        // Function to handle form submission
        document.getElementById('consultationForm').addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent default form submission

            const formData = new FormData(this); // Gather form data

            fetch(this.action, {
                method: this.method,
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.json(); 
            })
            .then(data => {
                document.getElementById('formResponse').innerHTML = 'Thank you for your submission!';
                this.reset(); // Reset the form
            })
            .catch(error => {
                document.getElementById('formResponse').innerHTML = 'Error: ' + error.message;
            });
        });
    </script>
</body>
</html>
```

```css
/* styles.css file */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: auto;
    background: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, select, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #28a745;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    width: 100%;
}

button:hover {
    background-color: #218838;
}

#formResponse {
    margin-top: 20px;
    text-align: center;
    color: #d9534f;
}
```
