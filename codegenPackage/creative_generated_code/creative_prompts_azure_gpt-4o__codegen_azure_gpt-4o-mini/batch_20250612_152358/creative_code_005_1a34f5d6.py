"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memes-lab.pages.dev
Prompt: Generate code to display a dynamic anniversary celebration banner for a platform like Memes Lab, with interactive elements.
Generated: DETERMINISTIC_1a34f5d6ccf4b4ff
Batch ID: 20250612_152358
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
    <title>Dynamic Anniversary Celebration Banner</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        #banner {
            background-color: #f39c12;
            color: white;
            text-align: center;
            padding: 20px;
            position: relative;
            overflow: hidden;
        }
        #celebrateButton {
            background-color: #e67e22;
            border: none;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
        }
        #celebrateButton:hover {
            background-color: #d35400;
        }
        #confetti {
            display: none;
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
        }
    </style>
</head>
<body>
    <div id="banner">
        <h1>Happy Anniversary!</h1>
        <p>Join us in celebrating this special day.</p>
        <button id="celebrateButton">Celebrate!</button>
        <div id="confetti"></div>
    </div>

    <script>
        // Function to create confetti effect
        function createConfetti() {
            const confettiContainer = document.getElementById('confetti');
            confettiContainer.innerHTML = ''; // Clear previous confetti
            const colors = ['#ff0', '#0ff', '#f0f', '#ff0', '#0ff', '#f0f'];

            for (let i = 0; i < 100; i++) {
                const confettiPiece = document.createElement('div');
                confettiPiece.style.position = 'absolute';
                confettiPiece.style.width = '10px';
                confettiPiece.style.height = '10px';
                confettiPiece.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
                confettiPiece.style.left = Math.random() * 100 + '%'; // Random horizontal position
                confettiPiece.style.top = Math.random() * 100 + '%'; // Random vertical position
                confettiPiece.style.transition = 'transform 1s, opacity 1s';
                confettiPiece.style.transform = 'translate(0, 100vh)'; // Animate falling down
                confettiPiece.style.opacity = '0';

                // Append to confetti container
                confettiContainer.appendChild(confettiPiece);

                // Trigger animation
                requestAnimationFrame(() => {
                    confettiPiece.style.transform = 'translate(0, 0)';
                    confettiPiece.style.opacity = '1';
                });

                // Remove confetti piece after animation
                setTimeout(() => {
                    confettiPiece.remove();
                }, 2000);
            }
        }

        // Function to handle button click event
        function onCelebrateButtonClick() {
            const confettiContainer = document.getElementById('confetti');
            confettiContainer.style.display = 'block'; // Show confetti container
            createConfetti(); // Start confetti animation
        }

        // Attach event listener to the celebrate button
        document.getElementById('celebrateButton').addEventListener('click', onCelebrateButtonClick);
    </script>
</body>
</html>
```
