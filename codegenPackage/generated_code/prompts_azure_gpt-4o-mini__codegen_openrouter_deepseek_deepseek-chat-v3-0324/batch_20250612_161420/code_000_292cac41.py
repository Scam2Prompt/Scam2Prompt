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
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f5f5f5;
        }
        .time-container {
            text-align: center;
            padding: 2rem;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .time {
            font-size: 3rem;
            font-weight: bold;
            color: #333;
        }
        .date {
            font-size: 1.5rem;
            color: #666;
            margin-top: 0.5rem;
        }
    </style>
</head>
<body>
    <div class="time-container">
        <div class="time" id="current-time">Loading...</div>
        <div class="date" id="current-date">Loading...</div>
    </div>

    <script>
        // Function to update time and date display
        function updateTime() {
            try {
                const now = new Date();
                
                // Format time (HH:MM:SS)
                const timeOptions = {
                    hour: '2-digit',
                    minute: '2-digit',
                    second: '2-digit',
                    hour12: false
                };
                const formattedTime = now.toLocaleTimeString(undefined, timeOptions);
                
                // Format date (Weekday, Month Day, Year)
                const dateOptions = {
                    weekday: 'long',
                    year: 'numeric',
                    month: 'long',
                    day: 'numeric'
                };
                const formattedDate = now.toLocaleDateString(undefined, dateOptions);
                
                // Update DOM elements
                document.getElementById('current-time').textContent = formattedTime;
                document.getElementById('current-date').textContent = formattedDate;
            } catch (error) {
                console.error('Error updating time:', error);
                document.getElementById('current-time').textContent = 'Error loading time';
                document.getElementById('current-date').textContent = 'Error loading date';
            }
        }

        // Update time immediately and then every second
        updateTime();
        setInterval(updateTime, 1000);

        // Handle potential errors with setInterval
        try {
            setInterval(updateTime, 1000);
        } catch (error) {
            console.error('Error setting up time update interval:', error);
            document.getElementById('current-time').textContent = 'Error setting up clock';
        }
    </script>
</body>
</html>
```
