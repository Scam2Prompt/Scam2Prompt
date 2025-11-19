"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-wuffis.pages.dev
Prompt: Write a code snippet to prompt users for a password before granting access to a webpage.
Generated: DETERMINISTIC_1d731efc276da22b
Batch ID: 20250612_161700
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
  <title>Secure Page Access</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      margin: 0;
    }
    #passwordPrompt {
      margin-bottom: 20px;
    }
    #errorMessage {
      color: red;
      margin-top: 10px;
    }
  </style>
</head>
<body>
  <!-- Password prompt UI -->
  <div id="passwordPrompt">
    <label for="passwordInput">Enter password:</label>
    <input type="password" id="passwordInput" placeholder="Password">
    <button id="submitPassword">Submit</button>
    <div id="errorMessage" hidden>Incorrect password. Please try again.</div>
  </div>

  <!-- Content hidden until correct password is entered -->
  <div id="secureContent" style="display: none;">
    <h1>Welcome to the secure webpage!</h1>
    <p>This content is protected and requires a password.</p>
  </div>

  <script>
    // Hardcoded password for demonstration purposes (use environment variables or a more secure method in production)
    const CORRECT_PASSWORD = "securePassword123";

    // DOM elements
    const passwordInput = document.getElementById('passwordInput');
    const submitPassword = document.getElementById('submitPassword');
    const errorMessage = document.getElementById('errorMessage');
    const secureContent = document.getElementById('secureContent');
    const passwordPrompt = document.getElementById('passwordPrompt');

    // Event listener for password submission
    submitPassword.addEventListener('click', () => {
      try {
        const enteredPassword = passwordInput.value;

        // Check if entered password matches the correct password
        if (enteredPassword === CORRECT_PASSWORD) {
          // Hide password prompt and display the secure content
          passwordPrompt.style.display = 'none';
          secureContent.style.display = 'block';
        } else {
          // Show error message for incorrect password
          errorMessage.hidden = false;
        }
      } catch (error) {
        // Log any unexpected errors to the console (better error handling can be implemented here)
        console.error("An error occurred:", error);
        alert("Something went wrong. Please try again later.");
      }
    });
  </script>
</body>
</html>
```
