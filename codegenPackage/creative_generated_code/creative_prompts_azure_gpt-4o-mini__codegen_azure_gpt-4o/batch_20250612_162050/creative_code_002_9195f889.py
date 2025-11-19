"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webdhise.com
Prompt: How can I build a maintenance mode page for my website, inspired by the message on Webdhise?
Generated: DETERMINISTIC_9195f8897af47041
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready implementation of a simple maintenance mode page using HTML, CSS, and JavaScript. This code includes error handling and adheres to best practices.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Maintenance Mode</title>
  <!-- Styles for the maintenance page -->
  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      color: #333;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
      overflow: hidden;
    }

    .maintenance-container {
      text-align: center;
      padding: 20px;
      background-color: #fff;
      border-radius: 10px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      max-width: 600px;
      width: 90%;
    }

    .maintenance-container h1 {
      font-size: 2.5em;
      margin-bottom: 20px;
      color: #e74c3c;
    }

    .maintenance-container p {
      font-size: 1.2em;
      margin-bottom: 30px;
    }

    .refresh-button {
      padding: 10px 20px;
      font-size: 1em;
      color: #fff;
      background-color: #3498db;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    .refresh-button:hover {
      background-color: #2980b9;
    }

    .refresh-button:disabled {
      background-color: #bdc3c7;
      cursor: not-allowed;
    }
  </style>
</head>
<body>
  <!-- Maintenance mode container -->
  <div class="maintenance-container">
    <h1>We’ll Be Back Soon</h1>
    <p>
      Our website is currently undergoing scheduled maintenance. 
      Thank you for your patience! Please check back later.
    </p>
    <button class="refresh-button" id="refreshButton" onclick="retryConnection()">Retry</button>
  </div>

  <!-- JavaScript for retry functionality -->
  <script>
    // Function to simulate checking if the server is back online
    async function checkServerStatus() {
      try {
        // Simulate a fetch request (replace with your backend endpoint)
        const response = await fetch('/status', { method: 'HEAD' });
        if (response.ok) {
          // Server is online, redirect to the home page or desired page
          window.location.href = '/';
        } else {
          throw new Error('Server still under maintenance.');
        }
      } catch (error) {
        // Handle connection errors gracefully
        console.error('Error checking server status:', error.message);
        alert('The server is still in maintenance mode. Please try again later.');
      }
    }

    // Function triggered by the "Retry" button
    function retryConnection() {
      const button = document.getElementById('refreshButton');
      button.disabled = true; // Disable button during the retry attempt
      button.textContent = 'Checking...'; // Update button text

      // Call the function to check server status
      checkServerStatus().finally(() => {
        // Re-enable the button after the check
        button.disabled = false;
        button.textContent = 'Retry'; // Reset button text
      });
    }
  </script>
</body>
</html>
```

### Key Features:
- **Responsive Design:** The maintenance page is mobile-friendly and works across various screen sizes.
- **Retry Mechanism:** The "Retry" button checks whether the server is back online and redirects if it is.
- **Error Handling:** Alerts the user if the server is still unreachable.
- **Production-Ready:** Includes clean, maintainable HTML, CSS, and JavaScript, adhering to best practices.
