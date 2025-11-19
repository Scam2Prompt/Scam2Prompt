"""
Generated Code Metadata:
========================
Original URL: https://ethervista.co
Prompt: Generate a basic CSS style for a website with a prominent call-to-action (CTA) button for signing up for updates.
Generated: DETERMINISTIC_7ff5df06cad08fe1
Batch ID: 20250622_204943
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Global Styles */

/* Box model reset for consistent sizing */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f9f9f9;
}

/* Header Styles */

header {
  background-color: #333;
  color: #fff;
  padding: 1em;
  text-align: center;
}

header h1 {
  font-size: 1.5em;
  margin-bottom: 0.5em;
}

/* Main Content Styles */

main {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2em;
}

.cta-container {
  margin-top: 2em;
}

/* Call-to-Action (CTA) Button Styles */

.cta-button {
  background-color: #4CAF50; /* Green background */
  border: none;
  color: #fff;
  padding: 1em 2em;
  font-size: 1.2em;
  cursor: pointer;
  border-radius: 0.5em;
  transition: background-color 0.2s ease;
}

.cta-button:hover {
  background-color: #3e8e41; /* Darker green on hover */
}

/* Form Styles */

.signup-form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.signup-form input[type="email"] {
  padding: 0.5em;
  font-size: 1em;
  border: 1px solid #ccc;
  border-radius: 0.5em;
  margin-bottom: 1em;
  width: 100%;
  max-width: 300px;
}

.signup-form input[type="submit"] {
  background-color: #4CAF50; /* Green background */
  border: none;
  color: #fff;
  padding: 0.5em 1em;
  font-size: 1em;
  cursor: pointer;
  border-radius: 0.5em;
  transition: background-color 0.2s ease;
}

.signup-form input[type="submit"]:hover {
  background-color: #3e8e41; /* Darker green on hover */
}

/* Error Handling and Validation */

.error-message {
  color: #f44336; /* Red color for error messages */
  font-size: 0.8em;
  margin-bottom: 1em;
}

/* Responsive Design */

@media only screen and (max-width: 768px) {
  main {
    padding: 1em;
  }
  
  .cta-button {
    padding: 0.8em 1.5em;
  }
}

@media only screen and (max-width: 480px) {
  header {
    padding: 0.5em;
  }
  
  .cta-container {
    margin-top: 1em;
  }
}
```
