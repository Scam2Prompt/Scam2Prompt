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
  <meta name="description" content="Submit your questions about herbal supplements, including Habbatussauda and its uses">
  <title>Herbal Supplement FAQ - Submit Your Question</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
      line-height: 1.6;
    }

    h1 {
      color: #2c3e50;
    }

    form {
      max-width: 600px;
      margin: 0 auto;
    }

    label {
      display: block;
      margin-top: 10px;
      font-weight: bold;
    }

    input,
    textarea,
    button {
      width: 100%;
      padding: 10px;
      margin-top: 5px;
      border: 1px solid #ccc;
      border-radius: 5px;
      box-sizing: border-box;
    }

    button {
      background-color: #2c3e50;
      color: #fff;
      cursor: pointer;
    }

    button:hover {
      background-color: #34495e;
    }

    .error {
      color: red;
      font-size: 0.9em;
    }

    .success {
      color: green;
      font-size: 0.9em;
    }
  </style>
</head>

<body>
  <h1>Submit Your Question About Herbal Supplements</h1>
  <p>Have questions about Habbatussauda and its uses? Fill out the form below and we'll get back to you!</p>

  <form id="questionForm">
    <!-- User's Name -->
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required placeholder="Enter your name">

    <!-- User's Email -->
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required placeholder="Enter your email">

    <!-- Question subject -->
    <label for="subject">Subject:</label>
    <input type="text" id="subject" name="subject" required placeholder="Enter the subject of your question">

    <!-- Question text -->
    <label for="question">Your Question:</label>
    <textarea id="question" name="question" rows="5" required placeholder="Write your question here"></textarea>

    <!-- Submit Button -->
    <button type="submit">Submit Question</button>

    <!-- Feedback section -->
    <div id="feedback" class="success" style="display: none;">
      Thank you for submitting your question. We will get back to you soon!
    </div>
    <div id="feedbackError" class="error" style="display: none;">
      There was an error submitting your question. Please try again later.
    </div>
  </form>

  <script>
    // Add event listener to handle form submission
    document.getElementById('questionForm').addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent default form submission

      // Simulate form submission logic
      try {
        // Example: Validate inputs (basic validation for demonstration purposes)
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const subject = document.getElementById('subject').value.trim();
        const question = document.getElementById('question').value.trim();

        if (!name || !email || !subject || !question) {
          throw new Error('All fields are required.');
        }

        // Simulate successful submission
        document.getElementById('feedback').style.display = 'block';
        document.getElementById('feedbackError').style.display = 'none';
        event.target.reset(); // Reset the form after submission
      } catch (error) {
        // Handle errors
        document.getElementById('feedbackError').style.display = 'block';
        document.getElementById('feedback').style.display = 'none';
        console.error('Form submission error:', error.message);
      }
    });
  </script>
</body>

</html>
```
