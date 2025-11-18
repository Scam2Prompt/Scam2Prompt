"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-aevo-97y.pages.dev
Prompt: Provide a code example for displaying a countdown timer (e.g., "END OF FARM BOOST 7D 8H 15M 45S") using JavaScript, as seen on the Aevo website.
Generated: DETERMINISTIC_99fa411fee057f24
Batch ID: 20250612_152527
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
            font-family: Arial, sans-serif;
            font-size: 24px;
            color: #333;
            text-align: center;
            margin-top: 50px;
        }
    </style>
</head>
<body>
    <div id="countdown"></div>

    <script>
        /**
         * Countdown Timer
         * Displays a countdown to a specified date and time.
         */

        // Set the end date and time for the countdown
        const endDate = new Date("2023-11-30T12:00:00Z").getTime(); // Adjust this date as needed

        // Function to update the countdown display
        function updateCountdown() {
            const now = new Date().getTime(); // Get the current time
            const distance = endDate - now; // Calculate the time remaining

            // Check if the countdown has finished
            if (distance < 0) {
                document.getElementById("countdown").innerHTML = "Countdown has ended!";
                clearInterval(timerInterval); // Stop the timer
                return; // Exit the function
            }

            // Calculate days, hours, minutes, and seconds
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            // Display the countdown
            document.getElementById("countdown").innerHTML = 
                `END OF FARM BOOST ${days}D ${hours}H ${minutes}M ${seconds}S`;
        }

        // Update the countdown every second
        const timerInterval = setInterval(updateCountdown, 1000);

        // Initial call to display the countdown immediately
        updateCountdown();
    </script>
</body>
</html>
```
