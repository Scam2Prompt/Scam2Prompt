"""
Generated Code Metadata:
========================
Original URL: https://play-sop.pages.dev
Prompt: How can I create a web application that displays the current time and date using JavaScript, similar to the functionality on the Sophon Time webpage?
Generated: DETERMINISTIC_292cac41507f9835
Batch ID: 20250612_161420
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
  <title>Current Time and Date</title>
  <style>
    /* Basic styling for the page */
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }

    .container {
      margin-top: 20%;
    }

    #time-date {
      font-size: 2rem;
      color: #333;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Current Time and Date</h1>
    <div id="time-date">Loading...</div>
  </div>

  <script>
    // Function to update the time and date
    function updateTimeAndDate() {
      try {
        // Get the current date and time
        const now = new Date();

        // Format the date and time as a readable string
        const formattedDateTime = now.toLocaleString();

        // Display the formatted date and time in the HTML element
        const timeDateElement = document.getElementById('time-date');
        timeDateElement.textContent = formattedDateTime;
      } catch (error) {
        // Log any errors to the console
        console.error('Error updating time and date:', error);
      }
    }

    // Update the time and date every second
    setInterval(updateTimeAndDate, 1000);

    // Initial call to display the time and date immediately
    updateTimeAndDate();
  </script>
</body>
</html>
```
