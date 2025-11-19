"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buy-pre-sale-and-rect-aisentient.pages.dev
Prompt: Provide an example of how to display a countdown timer for the next draw in a presale event using JavaScript.
Generated: DETERMINISTIC_db91dd503f4a1c04
Batch ID: 20250612_155855
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
    <title>Countdown Timer</title>
    <style>
        #countdown {
            font-size: 2em;
            color: #333;
            text-align: center;
            margin-top: 20%;
        }
    </style>
</head>
<body>

    <div id="countdown"></div>

    <script>
        /**
         * Initializes the countdown timer for the next draw in a presale event.
         * The target date and time for the next draw should be specified.
         */
        function startCountdown(targetDate) {
            // Update the countdown every second
            const countdownInterval = setInterval(() => {
                const now = new Date().getTime();
                const distance = targetDate - now;

                // Time calculations for days, hours, minutes, and seconds
                const days = Math.floor(distance / (1000 * 60 * 60 * 24));
                const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                const seconds = Math.floor((distance % (1000 * 60)) / 1000);

                // Display the result in the countdown element
                document.getElementById("countdown").innerHTML = `
                    ${days}d ${hours}h ${minutes}m ${seconds}s
                `;

                // If the countdown is finished, display a message and clear the interval
                if (distance < 0) {
                    clearInterval(countdownInterval);
                    document.getElementById("countdown").innerHTML = "The draw has begun!";
                }
            }, 1000);
        }

        // Set the target date for the next draw (example: December 31, 2023, 23:59:59)
        const targetDate = new Date("2023-12-31T23:59:59").getTime();

        // Start the countdown
        startCountdown(targetDate);
    </script>

</body>
</html>
```
