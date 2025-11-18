"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://farms-sophon.web.app
Prompt: Develop a script to calculate and display the estimated time for Sophon Farming registration (~1 minute) dynamically on a webpage.
Generated: DETERMINISTIC_e24b4776049bddc6
Batch ID: 20250612_145913
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
    <title>Sophon Farming Registration Timer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background-color: #f4f4f4;
        }
        #timer {
            font-size: 2em;
            color: #333;
        }
    </style>
</head>
<body>

    <h1>Sophon Farming Registration</h1>
    <p id="timer">Estimated time: <span id="time">1:00</span></p>
    <button id="startButton">Start Registration</button>

    <script>
        // Function to start the timer
        function startTimer(duration, display) {
            let timer = duration, minutes, seconds;

            const intervalId = setInterval(() => {
                // Calculate minutes and seconds
                minutes = parseInt(timer / 60, 10);
                seconds = parseInt(timer % 60, 10);

                // Format time to always show two digits
                seconds = seconds < 10 ? "0" + seconds : seconds;
                display.textContent = minutes + ":" + seconds;

                // Stop the timer when it reaches zero
                if (--timer < 0) {
                    clearInterval(intervalId);
                    display.textContent = "Time's up!";
                    alert("Sophon Farming Registration is complete!");
                }
            }, 1000); // Update every second
        }

        // Event listener for the start button
        document.getElementById('startButton').addEventListener('click', () => {
            // Get the reference to the time display span
            const timeDisplay = document.getElementById('time');
            
            // Start the timer for 60 seconds
            try {
                startTimer(60, timeDisplay);
            } catch (error) {
                console.error("An error occurred while starting the timer:", error);
                alert("Sorry, an error occurred while starting the registration process.");
            }
        });
    </script>

</body>
</html>
```
