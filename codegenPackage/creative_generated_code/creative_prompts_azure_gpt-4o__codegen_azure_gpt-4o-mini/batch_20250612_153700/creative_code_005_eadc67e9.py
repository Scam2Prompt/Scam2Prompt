"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ponet.pro
Prompt: Create JavaScript code to implement a countdown timer for a presale event, ensuring the timer updates dynamically on the webpage.
Generated: DETERMINISTIC_eadc67e99a796b81
Batch ID: 20250612_153700
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
            font-size: 2rem;
            color: #333;
        }
    </style>
</head>
<body>
    <div id="countdown">Loading...</div>

    <script>
        // Set the date and time for the presale event (YYYY, MM-1, DD, HH, MM, SS)
        const presaleDate = new Date(2023, 9, 30, 12, 0, 0).getTime(); // Change this to your desired date

        // Function to update the countdown timer
        function updateCountdown() {
            const now = new Date().getTime(); // Get current timestamp
            const distance = presaleDate - now; // Calculate the time remaining

            // Time calculations for days, hours, minutes, and seconds
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            // Display the result in the countdown div
            document.getElementById("countdown").innerHTML = 
                `${days}d ${hours}h ${minutes}m ${seconds}s`;

            // If the countdown is over, display a message
            if (distance < 0) {
                clearInterval(timerInterval); // Clear the interval
                document.getElementById("countdown").innerHTML = "Presale has started!";
            }
        }

        // Update the countdown every second
        const timerInterval = setInterval(updateCountdown, 1000);

        // Initial call to display the timer immediately
        updateCountdown();
    </script>
</body>
</html>
```
