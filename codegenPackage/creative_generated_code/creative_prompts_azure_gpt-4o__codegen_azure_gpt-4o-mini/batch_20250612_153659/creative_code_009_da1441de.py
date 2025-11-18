"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loyalnft3.web.app
Prompt: Develop a web-based countdown timer using JavaScript that syncs with the $LOYAL airdrop closing time, displaying minutes and seconds dynamically.
Generated: DETERMINISTIC_da1441de8cbb5b94
Batch ID: 20250612_153659
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
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
        }
        .timer {
            font-size: 3em;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="timer" id="countdown-timer">Loading...</div>

    <script>
        // Set the closing date and time for the LOYAL airdrop
        const airdropEndTime = new Date('2023-10-31T23:59:59Z').getTime();

        // Function to update the countdown timer
        function updateTimer() {
            const now = new Date().getTime(); // Current date and time
            const distance = airdropEndTime - now; // Calculate time remaining

            // Calculate minutes and seconds
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            // Display the result in the HTML element
            const timerElement = document.getElementById('countdown-timer');
            timerElement.innerHTML = `${minutes}m ${seconds}s`;

            // Check if the countdown is finished
            if (distance < 0) {
                clearInterval(interval);
                timerElement.innerHTML = "Airdrop has ended!";
                console.error("Countdown has ended, no more time left.");
            }
        }

        // Update the timer every second
        const interval = setInterval(updateTimer, 1000);

        // Initial call to display the timer immediately
        updateTimer();
    </script>
</body>
</html>
```
