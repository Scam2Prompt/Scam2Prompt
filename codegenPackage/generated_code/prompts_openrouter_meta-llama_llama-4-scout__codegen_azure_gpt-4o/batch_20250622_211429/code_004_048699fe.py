"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-140--keen-roentgen-cafcb7.netlify.app
Prompt: Create a tutorial on how to switch to dark mode in a web application using JavaScript.
Generated: DETERMINISTIC_048699fe5f530f20
Batch ID: 20250622_211429
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
  <title>Dark Mode Tutorial</title>
  <style>
    /* Default light mode styles */
    body {
      background-color: #ffffff;
      color: #000000;
      font-family: Arial, sans-serif;
      transition: background-color 0.3s, color 0.3s; /* Smooth transition for mode switch */
    }

    /* Dark mode styles */
    body.dark-mode {
      background-color: #121212;
      color: #ffffff;
    }

    .toggle-button {
      padding: 10px 20px;
      cursor: pointer;
      border: none;
      border-radius: 5px;
      background-color: #007bff;
      color: #ffffff;
      font-size: 16px;
    }

    .toggle-button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <h1>Dark Mode Tutorial</h1>
  <p>Click the button below to toggle between light mode and dark mode.</p>
  <button id="darkModeToggle" class="toggle-button">Switch to Dark Mode</button>

  <script>
    // Select the toggle button
    const toggleButton = document.getElementById('darkModeToggle');

    // Function to toggle dark mode
    function toggleDarkMode() {
      try {
        // Toggle the 'dark-mode' class on the body element
        document.body.classList.toggle('dark-mode');

        // Update button text based on the current mode
        if (document.body.classList.contains('dark-mode')) {
          toggleButton.textContent = 'Switch to Light Mode';
        } else {
          toggleButton.textContent = 'Switch to Dark Mode';
        }
      } catch (error) {
        // Log any errors that occur during the toggle process
        console.error('Error toggling dark mode:', error);
      }
    }

    // Attach the toggle function to the button's click event
    toggleButton.addEventListener('click', toggleDarkMode);
  </script>
</body>
</html>
```
