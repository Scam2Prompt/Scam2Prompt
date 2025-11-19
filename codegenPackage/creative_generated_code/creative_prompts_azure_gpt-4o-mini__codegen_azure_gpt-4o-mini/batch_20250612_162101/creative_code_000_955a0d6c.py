"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dacarlaw.com
Prompt: Generate a countdown timer using JavaScript that can be integrated into a website template.
Generated: DETERMINISTIC_955a0d6c083f16f0
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
    <title>Countdown Timer</title>
    <style>
        /* Basic styling for the timer display */
        #countdown {
            font-family: Arial, sans-serif;
            font-size: 2em;
            color: #333;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <div id="countdown">Loading...</div>

    <script>
        /**
         * Countdown Timer Function
         * @param {number} durationInSeconds - The countdown duration in seconds.
         */
        function countdownTimer(durationInSeconds) {
            // Ensure the duration is a positive number
            if (durationInSeconds <= 0) {
                console.error("Duration must be a positive number.");
                return;
            }

            let remainingTime = durationInSeconds; // Store remaining time
            const countdownDisplay = document.getElementById('countdown'); // Get the countdown display element

            // Update the countdown display every second
            const intervalId = setInterval(() => {
                // Calculate minutes and seconds
                const minutes = Math.floor(remainingTime / 60);
                const seconds = remainingTime % 60;

                // Format time string
                countdownDisplay.textContent = `${padZero(minutes)}:${padZero(seconds)}`;

                // Decrease remaining time
                remainingTime--;

                // Stop countdown when time is up
                if (remainingTime < 0) {
                    clearInterval(intervalId);
                    countdownDisplay.textContent = "Time's up!";
                }
            }, 1000);
        }

        /**
         * Pad a number with leading zero if it's less than 10
         * @param {number} number - The number to pad.
         * @returns {string} - The padded number as a string.
         */
        function padZero(number) {
            return number < 10 ? '0' + number : number;
        }

        // Start the countdown timer for 5 minutes (300 seconds)
        countdownTimer(300);
    </script>

</body>
</html>
```
