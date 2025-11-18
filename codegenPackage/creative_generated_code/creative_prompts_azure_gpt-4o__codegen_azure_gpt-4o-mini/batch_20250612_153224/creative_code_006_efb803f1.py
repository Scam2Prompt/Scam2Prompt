"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://recuperacionjc.com
Prompt: Generate code for a progress bar to visually represent insurance claim processing stages, as seen in the Recuperación JC website's interactive elements.
Generated: DETERMINISTIC_efb803f11f92f8b6
Batch ID: 20250612_153224
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
    <title>Insurance Claim Progress Bar</title>
    <style>
        /* Basic styles for the progress bar container */
        .progress-container {
            width: 100%;
            background-color: #e0e0df;
            border-radius: 25px;
            overflow: hidden;
            position: relative;
            margin: 20px 0;
        }

        /* Styles for the actual progress bar */
        .progress-bar {
            height: 30px;
            width: 0; /* Start width at 0 */
            background-color: #4caf50;
            text-align: center;
            line-height: 30px; /* Center text vertically */
            color: white;
            transition: width 0.4s ease; /* Smooth transition for width change */
        }

        /* Stage labels styles */
        .progress-label {
            position: absolute;
            font-size: 14px;
            color: #333;
            top: 35px; /* Position label below progress bar */
        }
    </style>
</head>
<body>

    <h1>Insurance Claim Processing Stages</h1>
    
    <!-- Progress Bar Container -->
    <div class="progress-container">
        <div class="progress-bar" id="progressBar">0%</        </div>
        <div class="progress-label" id="stageLabel">Stage: Submitted</div>
    </div>

    <script>
        // Define stages of the insurance claim process
        const stages = [
            "Submitted",
            "Under Review",
            "Approved",
            "Payment Processed",
            "Completed"
        ];

        // Initialize progress
        let currentStage = 0;

        /**
         * Function to update the progress bar
         * @param {number} stage - The current stage index
         */
        function updateProgress(stage) {
            // Check if the stage is within the valid range
            if (stage < 0 || stage >= stages.length) {
                console.error("Invalid stage index", stage);
                return;
            }

            // Calculate progress percentage
            const percentage = ((stage + 1) / stages.length) * 100;
            // Update progress bar width and text
            const progressBar = document.getElementById("progressBar");
            const stageLabel = document.getElementById("stageLabel");
            progressBar.style.width = percentage + "%";
            progressBar.textContent = Math.round(percentage) + "%";
            stageLabel.textContent = "Stage: " + stages[stage];
        }

        // Simulate progress through stages every 2 seconds
        const progressInterval = setInterval(() => {
            if (currentStage < stages.length - 1) {
                currentStage++;
                updateProgress(currentStage);
            } else {
                clearInterval(progressInterval); // Stop interval on completion
            }
        }, 2000);

        // Initial call to set starting state
        updateProgress(currentStage);

    </script>

</body>
</html>
```
