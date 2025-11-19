"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://play-sop.pages.dev
Prompt: How can I create a web application that displays the current time and date using JavaScript, similar to the functionality on the Sophon Time webpage?
Generated: DETERMINISTIC_292cac41507f9835
Batch ID: 20250612_161420
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
  <title>Current Time and Date</title>
  <style>
    /* Basic styling for the page */
    body {
      font-family: Arial, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      background-color: #f4f4f9;
    }
    #time-date {
      text-align: center;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 10px;
      background-color: #fff;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    h1 {
      font-size: 1.5rem;
      margin: 0;
    }
    p {
      font-size: 1.2rem;
      margin: 10px 0;
    }
  </style>
</head>
<body>
  <div id="time-date">
    <h1>Current Time and Date</h1>
    <p id="current-time"></p>
  </div>

  <!-- JavaScript code to update the time and date dynamically -->
  <script>
    /**
     * Function to update the current time and date on the webpage.
     */
    function updateTime() {
      try {
        // Get the current date and time
        const now = new Date();

        // Format the time and date string
        const formattedTime = now.toLocaleString('en-US', {
          weekday: 'long',
          year: 'numeric',
          month: 'long',
          day: 'numeric',
          hour: 'numeric',
          minute: 'numeric',
          second: 'numeric',
          hour12: true
        });

        // Update the DOM element with the formatted time
        const timeElement = document.getElementById('current-time');
        timeElement.textContent = formattedTime;
      } catch (error) {
        // Log any errors to the console
        console.error('An error occurred while updating the time:', error);
      }
    }

    // Initial call to display the time immediately
    updateTime();

    // Set an interval to update the time every second
    setInterval(updateTime, 1000);
  </script>
</body>
</html>
```
