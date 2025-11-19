"""
Generated Code Metadata:
========================
Original URL: https://orlandoplasmacenters.com
Prompt: Generate code for a step-by-step plasma donation guide on a website, including interactive elements for each step outlined by Orlando Plasma Centers.
Generated: DETERMINISTIC_465a53d4dfcb6894
Batch ID: 20250612_154520
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
    <title>Plasma Donation Guide</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <header>
        <h1>Step-by-Step Plasma Donation Guide</h1>
        <p>Follow these steps to ensure a smooth plasma donation experience at Orlando Plasma Centers.</p>
    </header>
    
    <main>
        <section id="steps">
            <div class="step" id="step-1">
                <h2>Step 1: Check Eligibility</h2>
                <p>Ensure you meet the eligibility criteria for plasma donation.</p>
                <button class="next-btn">Next</button>
            </div>
            <div class="step" id="step-2" style="display: none;">
                <h2>Step 2: Schedule an Appointment</h2>
                <p>Book your appointment online or call us to schedule.</p>
                <button class="next-btn">Next</button>
            </div>
            <div class="step" id="step-3" style="display: none;">
                <h2>Step 3: Prepare for Donation</h2>
                <p>Stay hydrated and eat a healthy meal before your visit.</p>
                <button class="next-btn">Next</button>
            </div>
            <div class="step" id="step-4" style="display: none;">
                <h2>Step 4: Arrive at the Center</h2>
                <p>Arrive on time and bring a valid ID.</p>
                <button class="next-btn">Next</button>
            </div>
            <div class="step" id="step-5" style="display: none;">
                <h2>Step 5: Complete the Donation</h2>
                <p>Follow the staff's instructions during the donation process.</p>
                <button class="next-btn">Finish</button>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Orlando Plasma Centers. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styles */
header {
    background: #007bff;
    color: white;
    padding: 20px;
    text-align: center;
}

/* Main section styles */
main {
    padding: 20px;
}

/* Step styles */
.step {
    background: white;
    border-radius: 5px;
    padding: 20px;
    margin: 10px 0;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Button styles */
.next-btn {
    background: #28a745;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
}

.next-btn:hover {
    background: #218838;
}
```

```javascript
// script.js

// Function to handle the step navigation
document.addEventListener('DOMContentLoaded', () => {
    const steps = document.querySelectorAll('.step');
    let currentStep = 0;

    // Function to show the current step
    const showStep = (index) => {
        steps.forEach((step, i) => {
            step.style.display = (i === index) ? 'block' : 'none';
        });
    };

    // Event listener for next buttons
    steps.forEach((step, index) => {
        const nextButton = step.querySelector('.next-btn');
        nextButton.addEventListener('click', () => {
            if (index < steps.length - 1) {
                currentStep++;
                showStep(currentStep);
            } else {
                alert('Thank you for following the guide! You are ready to donate plasma.');
            }
        });
    });

    // Show the first step on page load
    showStep(currentStep);
});
```
