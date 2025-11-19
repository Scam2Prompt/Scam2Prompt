"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tc-harsewinkel.de
Prompt: Generate a membership registration form for a tennis club, incorporating community engagement and benefits of joining as highlighted by TC Harsewinkel.
Generated: DETERMINISTIC_7516e10760da6f10
Batch ID: 20250612_160044
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
    <title>Tennis Club Membership Registration</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Join TC Harsewinkel Tennis Club!</h1>
        <p>Engage with the community and enjoy exclusive benefits!</p>
    </header>
    
    <form id="membershipForm" onsubmit="return handleSubmit(event)">
        <fieldset>
            <legend>Membership Registration</legend>

            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required>

            <label for="dob">Date of Birth:</label>
            <input type="date" id="dob" name="dob" required>

            <label for="membershipType">Membership Type:</label>
            <select id="membershipType" name="membershipType" required>
                <option value="" disabled selected>Select a type</option>
                <option value="individual">Individual</option>
                <option value="family">Family</option>
                <option value="junior">Junior</option>
            </select>

            <label for="comments">Additional Comments:</label>
            <textarea id="comments" name="comments"></textarea>

            <button type="submit">Submit Registration</button>
        </fieldset>
    </form>

    <footer>
        <p>Benefits of joining TC Harsewinkel:</p>
        <ul>
            <li>Access to exclusive tournaments</li>
            <li>Community events and meet-ups</li>
            <li>Discounted coaching and training</li>
            <li>Networking opportunities with fellow players</li>
        </ul>
    </footer>

    <script>
        /**
         * Handles the form submission
         * @param {Event} event - The form submission event
         * @returns {boolean} - false to prevent default form submission
         */
        function handleSubmit(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                phone: document.getElementById('phone').value,
                dob: document.getElementById('dob').value,
                membershipType: document.getElementById('membershipType').value,
                comments: document.getElementById('comments').value,
            };

            // Validate email format
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(formData.email)) {
                alert("Please enter a valid email address.");
                return false;
            }

            // Simulating an API request (this should be replaced with an actual API call)
            console.log("Submitting form data:", formData);
            alert("Registration successful!");

            // Reset the form after submission
            document.getElementById('membershipForm').reset();
            return false; // Prevent default form submission
        }
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
    background-color: #f4f4f4;
}

header, footer {
    text-align: center;
    margin-bottom: 20px;
}

form {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
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
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #28a745;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}
```
