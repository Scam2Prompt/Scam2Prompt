"""
Generated Code Metadata:
========================
Original URL: https://donna-lopez-376.pages.dev
Prompt: Write a JavaScript code snippet to create a simple promotional webpage with a countdown timer for a limited-time offer, similar to the one implied on the given website.
Generated: DETERMINISTIC_0d3692beb43b6d55
Batch ID: 20250622_205230
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
    <title>Limited Time Offer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background-color: #f4f4f4;
            margin: 0;
        }
        .countdown {
            font-size: 2em;
            margin: 20px 0;
        }
        .offer {
            background-color: #ffcc00;
            padding: 20px;
            border-radius: 5px;
            text-align: center;
        }
        .expired {
            color: red;
        }
    </style>
</head>
<body>

    <div class="offer">
        <h1>Limited Time Offer!</h1>
        <p>Get 50% off on your first purchase!</p>
        <div id="countdown" class="countdown"></div>
    </div>

    <script>
        // Set the date we're counting down to
        const offerEndDate = new Date("2023-10-31T23:59:59").getTime();

        // Update the countdown every second
        const countdownFunction = setInterval(() => {
            // Get today's date and time
            const now = new Date().getTime();

            // Calculate the distance between now and the offer end date
            const distance = offerEndDate - now;

            // Time calculations for days, hours, minutes and seconds
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            // Display the result in the countdown element
            const countdownElement = document.getElementById("countdown");
            if (distance > 0) {
                countdownElement.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;
            } else {
                // If the countdown is over, display expired message
                clearInterval(countdownFunction);
                countdownElement.innerHTML = "Offer has expired!";
                countdownElement.classList.add("expired");
            }
        }, 1000);
    </script>

</body>
</html>
```
