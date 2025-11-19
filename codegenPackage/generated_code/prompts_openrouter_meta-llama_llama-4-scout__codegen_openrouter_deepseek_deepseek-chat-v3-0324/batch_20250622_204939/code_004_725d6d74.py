"""
Generated Code Metadata:
========================
Original URL: https://medialink.ie
Prompt: Write a short code snippet to create a simple website reveal countdown timer, similar to what Medialink might use for their "highly-anticipated reveal."
Generated: DETERMINISTIC_725d6d744c255964
Batch ID: 20250622_204939
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
    <title>Coming Soon - Exciting Reveal</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #121212;
            color: #ffffff;
            text-align: center;
        }
        .countdown-container {
            padding: 2rem;
            border-radius: 10px;
            background-color: rgba(0, 0, 0, 0.7);
            box-shadow: 0 0 20px rgba(255, 255, 255, 0.1);
        }
        h1 {
            margin-bottom: 1.5rem;
            font-size: 2.5rem;
        }
        .countdown {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
        }
        .countdown-item {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .countdown-value {
            font-size: 3rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        .countdown-label {
            font-size: 1rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .reveal-message {
            margin-top: 2rem;
            font-size: 1.2rem;
            opacity: 0.8;
        }
    </style>
</head>
<body>
    <div class="countdown-container">
        <h1>Highly-Anticipated Reveal</h1>
        <div class="countdown">
            <div class="countdown-item">
                <div class="countdown-value" id="days">00</div>
                <div class="countdown-label">Days</div>
            </div>
            <div class="countdown-item">
                <div class="countdown-value" id="hours">00</div>
                <div class="countdown-label">Hours</div>
            </div>
            <div class="countdown-item">
                <div class="countdown-value" id="minutes">00</div>
                <div class="countdown-label">Minutes</div>
            </div>
            <div class="countdown-item">
                <div class="countdown-value" id="seconds">00</div>
                <div class="countdown-label">Seconds</div>
            </div>
        </div>
        <div class="reveal-message">Something amazing is coming soon...</div>
    </div>

    <script>
        // Set the date we're counting down to (e.g., June 15, 2024 00:00:00)
        const countDownDate = new Date("Jun 15, 2024 00:00:00").getTime();

        // Update the countdown every 1 second
        const countdownTimer = setInterval(function() {
            // Get today's date and time
            const now = new Date().getTime();
            
            // Find the distance between now and the countdown date
            const distance = countDownDate - now;
            
            // If the countdown is finished, display message
            if (distance < 0) {
                clearInterval(countdownTimer);
                document.querySelector(".countdown").innerHTML = "<h2>The wait is over!</h2>";
                document.querySelector(".reveal-message").textContent = "Check out our big reveal!";
                return;
            }
            
            // Time calculations for days, hours, minutes and seconds
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);
            
            // Display the results
            document.getElementById("days").textContent = days.toString().padStart(2, '0');
            document.getElementById("hours").textContent = hours.toString().padStart(2, '0');
            document.getElementById("minutes").textContent = minutes.toString().padStart(2, '0');
            document.getElementById("seconds").textContent = seconds.toString().padStart(2, '0');
            
        }, 1000);
    </script>
</body>
</html>
```
