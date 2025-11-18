"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerionsuzki.pages.dev
Prompt: Write code to create a dynamic countdown timer that updates in real-time, similar to the one used on the Azuki WORLD website.
Generated: DETERMINISTIC_690f5d74c2cd80ce
Batch ID: 20250612_154927
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
    <title>Dynamic Countdown Timer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
        }
        #countdown {
            font-size: 48px;
            color: #333;
        }
    </style>
</head>
<body>
    <div id="countdown"></div>

    <script>
        // Countdown Timer Function
        function startCountdown(targetDate) {
            const countdownElement = document.getElementById('countdown');

            // Update the countdown every second
            const interval = setInterval(() => {
                const now = new Date().getTime(); // Get the current time
                const distance = targetDate - now; // Calculate the distance to the target date

                // Time calculations for days, hours, minutes and seconds
                const days = Math.floor(distance / (1000 * 60 * 60 * 24));
                const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                const seconds = Math.floor((distance % (1000 * 60)) / 1000);

                // Display the countdown in the format: DD:HH:MM:SS
                countdownElement.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;

                // If the countdown is finished, display a message and clear the interval
                if (distance < 0) {
                    clearInterval(interval);
                    countdownElement.innerHTML = "EXPIRED";
                }
            }, 1000); // Update every second
        }

        // Set the target date for the countdown (e.g., December 31, 2023, 23:59:59)
        const targetDate = new Date("December 31, 2023 23:59:59").getTime();

        // Start the countdown
        startCountdown(targetDate);
    </script>
</body>
</html>
```
