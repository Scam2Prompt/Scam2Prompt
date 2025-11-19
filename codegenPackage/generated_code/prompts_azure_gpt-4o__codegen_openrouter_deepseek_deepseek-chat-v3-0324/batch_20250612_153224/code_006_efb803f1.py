"""
Generated Code Metadata:
========================
Original URL: https://recuperacionjc.com
Prompt: Generate code for a progress bar to visually represent insurance claim processing stages, as seen in the Recuperación JC website's interactive elements.
Generated: DETERMINISTIC_efb803f11f92f8b6
Batch ID: 20250612_153224
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
    <title>Insurance Claim Processing Progress</title>
    <style>
        /* Progress bar container */
        .progress-container {
            width: 100%;
            max-width: 800px;
            margin: 20px auto;
            font-family: Arial, sans-serif;
        }

        /* Progress bar */
        .progress-bar {
            display: flex;
            justify-content: space-between;
            position: relative;
            margin-bottom: 30px;
        }

        /* Progress bar line */
        .progress-bar::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 0;
            right: 0;
            height: 4px;
            background-color: #e0e0e0;
            z-index: -1;
            transform: translateY(-50%);
        }

        /* Active progress bar line */
        .progress-line {
            position: absolute;
            top: 50%;
            left: 0;
            height: 4px;
            background-color: #4CAF50;
            z-index: -1;
            transform: translateY(-50%);
            transition: width 0.3s ease;
        }

        /* Progress steps */
        .progress-step {
            width: 30px;
            height: 30px;
            background-color: #e0e0e0;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #999;
            font-weight: bold;
            position: relative;
        }

        /* Active progress step */
        .progress-step.active {
            background-color: #4CAF50;
            color: white;
        }

        /* Completed progress step */
        .progress-step.completed {
            background-color: #4CAF50;
            color: white;
        }

        /* Step labels */
        .step-label {
            position: absolute;
            top: 40px;
            left: 50%;
            transform: translateX(-50%);
            white-space: nowrap;
            font-size: 14px;
            color: #666;
        }

        .progress-step.active .step-label,
        .progress-step.completed .step-label {
            color: #333;
            font-weight: bold;
        }

        /* Navigation buttons */
        .navigation-buttons {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 40px;
        }

        .nav-button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
        }

        .nav-button:hover {
            background-color: #45a049;
        }

        .nav-button:disabled {
            background-color: #cccccc;
            cursor: not-allowed;
        }
    </style>
</head>
<body>
    <div class="progress-container">
        <h2>Insurance Claim Processing</h2>
        <div class="progress-bar">
            <div class="progress-line" id="progressLine"></div>
            <div class="progress-step completed" id="step1">
                <span>1</span>
                <span class="step-label">Claim Submitted</span>
            </div>
            <div class="progress-step active" id="step2">
                <span>2</span>
                <span class="step-label">Under Review</span>
            </div>
            <div class="progress-step" id="step3">
                <span>3</span>
                <span class="step-label">Approval</span>
            </div>
            <div class="progress-step" id="step4">
                <span>4</span>
                <span class="step-label">Payment Processing</span>
            </div>
            <div class="progress-step" id="step5">
                <span>5</span>
                <span class="step-label">Completed</span>
            </div>
        </div>

        <div class="navigation-buttons">
            <button class="nav-button" id="prevBtn" disabled>Previous</button>
            <button class="nav-button" id="nextBtn">Next</button>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const steps = document.querySelectorAll('.progress-step');
            const progressLine = document.getElementById('progressLine');
            const prevBtn = document.getElementById('prevBtn');
            const nextBtn = document.getElementById('nextBtn');
            let currentStep = 1;

            // Update the progress bar
            function updateProgressBar() {
                // Update steps
                steps.forEach((step, index) => {
                    if (index < currentStep) {
                        step.classList.add('completed');
                        step.classList.remove('active');
                    } else if (index === currentStep) {
                        step.classList.add('active');
                        step.classList.remove('completed');
                    } else {
                        step.classList.remove('active', 'completed');
                    }
                });

                // Update progress line
                const progressPercentage = ((currentStep) / (steps.length - 1)) * 100;
                progressLine.style.width = `${progressPercentage}%`;

                // Update buttons
                prevBtn.disabled = currentStep === 0;
                nextBtn.disabled = currentStep === steps.length - 1;
            }

            // Next button click handler
            nextBtn.addEventListener('click', () => {
                if (currentStep < steps.length - 1) {
                    currentStep++;
                    updateProgressBar();
                }
            });

            // Previous button click handler
            prevBtn.addEventListener('click', () => {
                if (currentStep > 0) {
                    currentStep--;
                    updateProgressBar();
                }
            });

            // Initialize progress bar
            updateProgressBar();
        });
    </script>
</body>
</html>
```
