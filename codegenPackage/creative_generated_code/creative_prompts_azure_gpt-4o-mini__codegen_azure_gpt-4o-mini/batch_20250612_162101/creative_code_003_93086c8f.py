"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dacarlaw.com
Prompt: How can I create a unique website template that includes a countdown timer feature using HTML and CSS?
Generated: DETERMINISTIC_93086c8ff36d2143
Batch ID: 20250612_162101
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
    <title>Countdown Timer Template</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        /* Basic reset for margin and padding */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        /* Body styles */
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f3f4f6;
            color: #333;
        }

        /* Countdown timer styling */
        .countdown {
            text-align: center;
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .countdown h1 {
            font-size: 2rem;
            margin-bottom: 20px;
        }

        .countdown-time {
            display: flex;
            justify-content: center;
            gap: 10px;
        }

        .time-unit {
            background: #e2e8f0;
            border-radius: 5px;
            padding: 10px;
            min-width: 60px;
        }

        .time-unit span {
            display: block;
            font-size: 1.5rem;
            font-weight: bold;
        }

        .time-label {
            font-size: 0.8rem;
            color: #555;
        }
    </style>
</head>
<body>

    <div class="countdown">
        <h1>Countdown Timer</h1>
        <div class="countdown-time">
            <div class="time-unit" id="days">
                <span>0</span>
                <div class="time-label">Days</div>
            </div>
            <div class="time-unit" id="hours">
                <span>0</span>
                <div class="time-label">Hours</div>
            </div>
            <div class="time-unit" id="minutes">
                <span>0</span>
                <div class="time-label">Minutes</div>
            </div>
            <div class="time-unit" id="seconds">
                <span>0</span>
                <div class="time-label">Seconds</div>
            </div>
        </div>
    </div>

    <script>
        // Set the date we're counting down to
        const countdownDate = new Date("December 31, 2023 23:59:59").getTime();

        // Update the countdown every second
        const countdownFunction = setInterval(() => {
            // Get today's date and time
            const now = new Date().getTime();

            // Calculate the distance between now and the countdown date
            const distance = countdownDate - now;

            // Check if the countdown is over
            if (distance < 0) {
                clearInterval(countdownFunction);
                document.querySelector('.countdown').innerHTML = "<h1>Countdown Ended</h1>";
                return;
            }

            // Time calculations for days, hours, minutes and seconds
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            // Display the results in the respective elements
            document.getElementById("days").querySelector("span").textContent = days;
            document.getElementById("hours").querySelector("span").textContent = hours;
            document.getElementById("minutes").querySelector("span").textContent = minutes;
            document.getElementById("seconds").querySelector("span").textContent = seconds;
        }, 1000);
    </script>
</body>
</html>
```
