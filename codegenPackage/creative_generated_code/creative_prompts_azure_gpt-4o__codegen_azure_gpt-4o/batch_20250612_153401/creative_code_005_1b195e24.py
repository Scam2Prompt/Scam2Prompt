"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lending-ui-beta.vercel.app
Prompt: Provide an example of a JavaScript-based beta web application that requires user interaction and is hosted on Vercel.
Generated: DETERMINISTIC_1b195e2495d79f22
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Beta Web Application</title>
  <link rel="stylesheet" href="styles.css">
  <script defer src="script.js"></script>
</head>
<body>
  <div class="app-container">
    <h1>Beta Web Application</h1>
    <p>Enter your name below and click 'Submit' to interact with the application.</p>
    <form id="user-form">
      <input type="text" id="user-name" placeholder="Your name" required />
      <button type="submit">Submit</button>
    </form>
    <div id="output"></div>
  </div>
</body>
</html>
```

```javascript
// File: script.js

// Wait for the DOM to load before executing the script
document.addEventListener("DOMContentLoaded", () => {
  // Form and Output DOM elements
  const userForm = document.getElementById("user-form");
  const userNameInput = document.getElementById("user-name");
  const outputDiv = document.getElementById("output");
  
  /**
   * Handles form submission and updates the output with the user's input.
   * @param {Event} event - The event object from the form submission.
   */
  const handleFormSubmit = (event) => {
    event.preventDefault(); // Prevent the form from reloading the page

    const userName = userNameInput.value.trim(); // Get and sanitize user input

    // Validate the input
    if (!userName) {
      outputDiv.textContent = "Error: Name cannot be empty.";
      outputDiv.style.color = "red";
      return;
    }

    // Display the personalized greeting
    outputDiv.textContent = `Hello, ${userName}! Welcome to our beta web application.`;
    outputDiv.style.color = "green";

    // Clear the input field
    userNameInput.value = "";
  };

  // Attach the submit event listener to the form
  userForm.addEventListener("submit", handleFormSubmit);
});
```

```css
/* File: styles.css */

body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
}

.app-container {
  text-align: center;
  background: #ffffff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

h1 {
  font-size: 1.8rem;
  margin-bottom: 10px;
}

form {
  margin-bottom: 20px;
}

input {
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 200px;
}

button {
  padding: 10px 15px;
  font-size: 1rem;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

#output {
  font-size: 1.2rem;
}
```

---

To deploy this application to Vercel:

1. Create a new project folder and place the `index.html`, `script.js`, and `styles.css` files inside it.
2. Install the Vercel CLI if not already installed (`npm install -g vercel`).
3. Run `vercel` in the project folder to deploy the application.
4. Follow the CLI instructions to complete the deployment.
