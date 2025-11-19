"""
Generated Code Metadata:
========================
Original URL: https://moonbirds-9g2.pages.dev
Prompt: Create a web application that includes a "Begin" button for a token-gated survey, with a timer feature that limits completion time to 3 minutes.
Generated: DETERMINISTIC_6444776131a632da
Batch ID: 20250612_153225
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
    <title>Token-Gated Survey</title>
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
        #survey {
            display: none;
            text-align: center;
        }
        #timer {
            font-size: 24px;
            margin: 20px 0;
        }
        #error {
            color: red;
            display: none;
        }
    </style>
</head>
<body>

    <h1>Welcome to the Token-Gated Survey</h1>
    <button id="beginButton">Begin</button>
    <div id="error">Invalid token. Please try again.</div>
    <div id="survey">
        <div id="timer">Time left: <span id="timeLeft">180</span> seconds</div>
        <form id="surveyForm">
            <label for="response">Your response:</label><br>
            <textarea id="response" required></textarea><br>
            <button type="submit">Submit</button>
        </form>
    </div>

    <script>
        // Function to start the survey
        function startSurvey() {
            const token = prompt("Please enter your access token:");
            if (validateToken(token)) {
                document.getElementById('beginButton').style.display = 'none';
                document.getElementById('survey').style.display = 'block';
                startTimer(180); // Start timer for 3 minutes
            } else {
                document.getElementById('error').style.display = 'block';
            }
        }

        // Function to validate the token
        function validateToken(token) {
            // Replace with actual token validation logic
            return token === "valid-token"; // Example valid token
        }

        // Function to start the countdown timer
        function startTimer(duration) {
            let timeLeft = duration;
            const timerDisplay = document.getElementById('timeLeft');

            const timerInterval = setInterval(() => {
                if (timeLeft <= 0) {
                    clearInterval(timerInterval);
                    alert("Time is up! Please submit your response.");
                    document.getElementById('surveyForm').submit();
                } else {
                    timeLeft--;
                    timerDisplay.textContent = timeLeft;
                }
            }, 1000);
        }

        // Event listener for the Begin button
        document.getElementById('beginButton').addEventListener('click', startSurvey);

        // Event listener for the survey form submission
        document.getElementById('surveyForm').addEventListener('submit', (event) => {
            event.preventDefault(); // Prevent default form submission
            alert("Thank you for your response!");
            // Here you can add logic to send the response to the server
            document.getElementById('survey').style.display = 'none';
            document.getElementById('beginButton').style.display = 'block';
            document.getElementById('error').style.display = 'none';
        });
    </script>

</body>
</html>
```
