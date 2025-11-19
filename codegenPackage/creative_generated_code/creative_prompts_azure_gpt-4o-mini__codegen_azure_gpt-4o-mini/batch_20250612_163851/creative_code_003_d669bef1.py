"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mercatura.co.id
Prompt: Create a JavaScript example that implements a user feedback form similar to the "What People Say" section on Mercatura's site.
Generated: DETERMINISTIC_d669bef1f324d041
Batch ID: 20250612_163851
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
    <title>User Feedback Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .feedback {
            margin-top: 20px;
            border-top: 1px solid #eaeaea;
            padding-top: 20px;
        }
        .feedback-item {
            margin-bottom: 10px;
            padding: 10px;
            border: 1px solid #eaeaea;
            border-radius: 5px;
            background: #f9f9f9;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>User Feedback</h1>
    <form id="feedbackForm">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required /><br /><br />
        
        <label for="message">Feedback:</label><br />
        <textarea id="message" name="message" rows="4" required></textarea><br /><br />
        
        <button type="submit">Submit</button>
    </form>

    <div class="feedback" id="feedbackList">
        <h2>What People Say</h2>
    </div>
</div>

<script>
    // Function to handle form submission
    document.getElementById('feedbackForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent page refresh on submit

        // Get input values
        const name = document.getElementById('name').value.trim();
        const message = document.getElementById('message').value.trim();

        // Validate inputs
        if (!name || !message) {
            alert("Please fill out all fields.");
            return;
        }

        // Create feedback element
        const feedbackItem = document.createElement('div');
        feedbackItem.classList.add('feedback-item');
        feedbackItem.innerHTML = `<strong>${escapeHtml(name)}</strong><p>${escapeHtml(message)}</p>`;

        // Append feedback to the list
        document.getElementById('feedbackList').appendChild(feedbackItem);

        // Reset the form
        document.getElementById('feedbackForm').reset();
    });

    // Function to escape HTML to prevent XSS attacks
    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
</script>

</body>
</html>
```
