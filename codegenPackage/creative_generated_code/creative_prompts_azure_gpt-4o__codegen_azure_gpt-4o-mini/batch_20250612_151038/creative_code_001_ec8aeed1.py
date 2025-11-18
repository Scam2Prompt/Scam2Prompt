"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pacmoon-8ko.pages.dev
Prompt: Generate a script to display a countdown timer for an event, such as "Airdrop Season 3 Ends," using JavaScript.
Generated: DETERMINISTIC_ec8aeed1122bcb91
Batch ID: 20250612_151038
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
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
        }
        #countdown {
            font-size: 2rem;
            padding: 20px;
            border: 2px solid #333;
            border-radius: 10px;
            background-color: #fff;
        }
    </style>
</head>
<body>
    <div id="countdown">Loading...</div>

    <script>
        // Set the date and time for the event
        const eventDate = new Date("2023-12-31T23:59:59").getTime(); // Adjust the date and time as needed

        // Function to update the countdown timer
        function updateCountdown() {
            // Get the current date and time
            const now = new Date().getTime();

            // Calculate the remaining time until the event
            const remainingTime = eventDate - now;

            // Check if the countdown is finished
            if (remainingTime < 0) {
                document.getElementById("countdown").innerHTML = "Airdrop Season 3 has ended!";
                clearInterval(countdownInterval); // Stop the countdown
                return; // Exit the function
            }

            // Calculate days, hours, minutes, and seconds
            const days = Math.floor(remainingTime / (1000 * 60 * 60 * 24));
            const hours = Math.floor((remainingTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

            // Display the result in the countdown element
            document.getElementById("countdown").innerHTML = 
                `${days}d ${hours}h ${minutes}m ${seconds}s`;
        }

        // Update the countdown every second
        const countdownInterval = setInterval(updateCountdown, 1000);

        // Handle potential errors gracefully
        try {
            updateCountdown(); // Initial call to display countdown immediately
        } catch (error) {
            console.error("Error updating countdown:", error);
            document.getElementById("countdown").innerHTML = "Error loading countdown.";
        }
    </script>
</body>
</html>
```
