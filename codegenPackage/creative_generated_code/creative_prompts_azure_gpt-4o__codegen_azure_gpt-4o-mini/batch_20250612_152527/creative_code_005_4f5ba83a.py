"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.depanten-gel.click
Prompt: Create JavaScript code to display a countdown timer for a "limited-time discount" offer, as seen on the Depanten webpage.
Generated: DETERMINISTIC_4f5ba83af95dd784
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
        /* Simple styling for the countdown timer */
        #countdown {
            font-family: 'Arial', sans-serif;
            font-size: 24px;
            color: #ff0000; /* Red color for urgency */
            text-align: center;
            margin-top: 50px;
        }
    </style>
</head>
<body>
    <div id="countdown"></div>

    <script>
        // Set the date we're counting down to
        const countdownDate = new Date("2023-10-31T23:59:59").getTime();

        // Update the countdown every 1 second
        const countdownFunction = setInterval(() => {
            // Get the current date and time
            const now = new Date().getTime();

            // Calculate the distance between now and the countdown date
            const distance = countdownDate - now;

            // Check if the countdown is over
            if (distance < 0) {
                clearInterval(countdownFunction);
                document.getElementById("countdown").innerHTML = "Offer has expired!";
                return;
            }

            // Calculate time components
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            // Display the result in the countdown element
            document.getElementById("countdown").innerHTML = 
                `${days}d ${hours}h ${minutes}m ${seconds}s`;

        }, 1000);
    </script>
</body>
</html>
```
