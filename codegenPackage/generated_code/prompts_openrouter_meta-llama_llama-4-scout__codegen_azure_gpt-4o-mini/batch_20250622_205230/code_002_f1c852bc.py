"""
Generated Code Metadata:
========================
Original URL: https://nelson-8-donna-48.pages.dev
Prompt: Write a script that creates a sense of urgency on a webpage by displaying a countdown timer for a promotional offer.
Generated: DETERMINISTIC_f1c852bc02d5bf91
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
    <title>Countdown Timer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
        }
        .countdown {
            font-size: 2rem;
            color: #ff0000;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="countdown" id="countdown"></div>

    <script>
        // Set the date and time for the promotional offer to end
        const offerEndDate = new Date(Date.now() + 3600 * 1000); // 1 hour from now

        // Function to start the countdown
        function startCountdown() {
            const countdownElement = document.getElementById('countdown');

            // Update the countdown every second
            const countdownInterval = setInterval(() => {
                const now = new Date().getTime();
                const distance = offerEndDate - now;

                // Calculate hours, minutes, and seconds
                const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                const seconds = Math.floor((distance % (1000 * 60)) / 1000);

                // Display the result in the countdown element
                countdownElement.innerHTML = `${hours}h ${minutes}m ${seconds}s`;

                // If the countdown is over, display a message and clear the interval
                if (distance < 0) {
                    clearInterval(countdownInterval);
                    countdownElement.innerHTML = "Offer has expired!";
                }
            }, 1000);
        }

        // Start the countdown when the page loads
        window.onload = startCountdown;
    </script>
</body>
</html>
```
