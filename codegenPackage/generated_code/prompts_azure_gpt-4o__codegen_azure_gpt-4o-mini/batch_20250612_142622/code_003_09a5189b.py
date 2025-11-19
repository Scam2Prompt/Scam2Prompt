"""
Generated Code Metadata:
========================
Original URL: https://metomousk-logi-in.godaddysites.com
Prompt: Create a countdown timer in JavaScript that displays days, hours, minutes, and seconds, similar to the placeholder design on the webpage.
Generated: DETERMINISTIC_09a5189b3449f667
Batch ID: 20250612_142622
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
    <title>Countdown Timer</title>
    <style>
        #countdown {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 2em;
        }
        .time-unit {
            margin: 0 10px;
        }
    </style>
</head>
<body>
    <div id="countdown">
        <div class="time-unit" id="days">00</div> days
        <div class="time-unit" id="hours">00</div> hours
        <div class="time-unit" id="minutes">00</div> minutes
        <div class="time-unit" id="seconds">00</div> seconds
    </div>

    <script>
        // Set the target date and time for the countdown
        const targetDate = new Date("December 31, 2023 23:59:59").getTime();

        // Function to update the countdown timer
        function updateCountdown() {
            // Get the current date and time
            const now = new Date().getTime();
            // Calculate the time remaining
            const distance = targetDate - now;

            // Check if the countdown is finished
            if (distance < 0) {
                clearInterval(timerInterval);
                document.getElementById("countdown").innerHTML = "Countdown Finished!";
                return;
            }

            // Calculate days, hours, minutes, and seconds
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            // Update the countdown display
            document.getElementById("days").innerText = String(days).padStart(2, '0');
            document.getElementById("hours").innerText = String(hours).padStart(2, '0');
            document.getElementById("minutes").innerText = String(minutes).padStart(2, '0');
            document.getElementById("seconds").innerText = String(seconds).padStart(2, '0');
        }

        // Update the countdown every second
        const timerInterval = setInterval(updateCountdown, 1000);

        // Initial call to display the countdown immediately
        updateCountdown();
    </script>
</body>
</html>
```
