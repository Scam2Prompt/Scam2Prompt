"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loyalnft6.web.app
Prompt: Generate code to display a countdown timer for the $LOYAL airdrop closing time, updating in real-time using JavaScript.
Generated: DETERMINISTIC_d96240a9ceb019e1
Batch ID: 20250612_150557
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
    <title>Countdown Timer for $LOYAL Airdrop</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        #countdown {
            font-size: 2em;
            color: #2c3e50;
        }
    </style>
</head>
<body>

    <h1>Countdown to $LOYAL Airdrop Closing</h1>
    <div id="countdown"></div>

    <script>
        // Set the date we're counting down to
        const airdropEndDate = new Date("2023-12-31T23:59:59Z").getTime(); // Replace with actual end time

        // Update the countdown every second
        const countdownInterval = setInterval(() => {
            // Get the current date and time
            const now = new Date().getTime();

            // Calculate the distance between now and the airdrop end date
            const distance = airdropEndDate - now;

            // Time calculations for days, hours, minutes, and seconds
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            // Display the result in the countdown element
            document.getElementById("countdown").innerHTML = 
                days + "d " + hours + "h " + minutes + "m " + seconds + "s ";

            // If the countdown is over, display a message and clear the interval
            if (distance < 0) {
                clearInterval(countdownInterval);
                document.getElementById("countdown").innerHTML = "Airdrop has ended!";
            }
        }, 1000); // Update every second
    </script>
</body>
</html>
```
