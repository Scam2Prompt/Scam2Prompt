"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uembark.org
Prompt: Develop a web form for mentor applications, ensuring applicants can submit their information to join a team like the one described on uEmbark.
Generated: DETERMINISTIC_63b0aa25b52da691
Batch ID: 20250612_154632
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
    <title>Mentor Application Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Mentor Application Form</h1>
        <form id="mentor-application-form" method="POST" action="/submit-application">
            <!-- Applicant's Name -->
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required placeholder="John Doe">
            
            <!-- Applicant's Email -->
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="johndoe@example.com">

            <!-- Applicant's Experience -->
            <label for="experience">Experience Level:</label>
            <select id="experience" name="experience" required>
                <option value="" disabled selected>Select your experience level</option>
                <option value="beginner">Beginner</option>
                <option value="intermediate">Intermediate</option>
                <option value="advanced">Advanced</option>
            </select>

            <!-- Applicant's Bio -->
            <label for="bio">Short Bio:</label>
            <textarea id="bio" name="bio" rows="4" required placeholder="Tell us about yourself"></textarea>

            <!-- Submit Button -->
            <button type="submit">Submit Application</button>
        </form>
        <div id="form-response"></div> <!-- Placeholder for response messages -->
    </div>

    <script>
        // Handle form submission
        document.getElementById("mentor-application-form").addEventListener("submit", async function(event) {
            event.preventDefault(); // Prevent the default form submission

            const formData = new FormData(this); // Collect form data

            try {
                const response = await fetch(this.action, {
                    method: this.method,
                    body: formData,
                });

                // Check if the response is ok (status in range 200-299)
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }

                const data = await response.json(); // Parse JSON response
                document.getElementById("form-response").innerText = data.message; // Show success message

            } catch (error) {
                // Handle any errors during fetch
                document.getElementById("form-response").innerText = 'Error: ' + error.message;
            }
        });
    </script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    padding: 20px;
}

.container {
    background: #fff;
    padding: 20px;
    border-radius: 8px;
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
    background-color: #5cb85c;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #4cae4c;
}

#form-response {
    margin-top: 20px;
    font-weight: bold;
    text-align: center;
}
```

```javascript
// server.js (Node.js/Express.js setup for handling application submission)
const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON and URL-encoded form data
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Endpoint to handle mentor application submissions
app.post('/submit-application', (req, res) => {
    const { name, email, experience, bio } = req.body;

    // Basic validation
    if (!name || !email || !experience || !bio) {
        return res.status(400).json({ message: 'All fields are required.' });
    }

    // Process the application (e.g., save to database)
    // Here we just send a success response for demonstration
    console.log(`Application received from ${name}, Email: ${email}, Experience: ${experience}, Bio: ${bio}`);

    res.status(200).json({ message: 'Application submitted successfully!' });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
