"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ye-8lg.pages.dev
Prompt: Provide an example of how to display a countdown timer for a token presale, similar to the one used on ye-8lg.pages.dev for the $YE Token.
Generated: DETERMINISTIC_97b4ef834f60c96d
Batch ID: 20250612_160220
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
    <title>Token Presale Countdown Timer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
            margin: 0;
        }
        .countdown {
            font-size: 2rem;
            padding: 20px;
            border: 2px solid #007bff;
            border-radius: 10px;
            background-color: #fff;
        }
    </style>
</head>
<body>
    <div class="countdown" id="countdown"></div>

    <script>
        // Set the date and time for the presale to end
        const presaleEndDate = new Date("2023-12-31T23:59:59Z").getTime();

        // Update the countdown every second
        const countdownTimer = setInterval(function() {
            const now = new Date().getTime(); // Get the current time
            const distance = presaleEndDate - now; // Calculate the time remaining

            // Time calculations for days, hours, minutes, and seconds
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            // Display the result in the element with id="countdown"
            document.getElementById("countdown").innerHTML = 
                days + "d " + hours + "h " + minutes + "m " + seconds + "s ";

            // If the countdown is over, display a message
            if (distance < 0) {
                clearInterval(countdownTimer); // Stop the timer
                document.getElementById("countdown").innerHTML = "Presale has ended";
            }
        }, 1000);
    </script>
</body>
</html>
```
