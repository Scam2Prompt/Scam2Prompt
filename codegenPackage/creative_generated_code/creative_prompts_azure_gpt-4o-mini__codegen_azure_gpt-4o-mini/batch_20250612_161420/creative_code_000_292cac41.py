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
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
            margin: 0;
        }
        #time-container {
            text-align: center;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            font-size: 2rem;
            margin: 0;
        }
    </style>
</head>
<body>
    <div id="time-container">
        <h1 id="current-time"></h1>
        <p id="current-date"></p>
    </div>

    <script>
        /**
         * Updates the displayed current time and date.
         */
        function updateTime() {
            try {
                const now = new Date();
                const options = { year: 'numeric', month: 'long', day: 'numeric' };
                const timeString = now.toLocaleTimeString();
                const dateString = now.toLocaleDateString(undefined, options);

                // Update the time and date in the HTML
                document.getElementById('current-time').textContent = timeString;
                document.getElementById('current-date').textContent = dateString;
            } catch (error) {
                console.error("Error updating time and date:", error);
            }
        }

        // Update time and date every second
        setInterval(updateTime, 1000);

        // Initial call to display time and date immediately on page load
        updateTime();
    </script>
</body>
</html>
```
