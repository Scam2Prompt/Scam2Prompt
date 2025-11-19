"""
Generated Code Metadata:
========================
Original URL: https://wintron.minibachat.shop
Prompt: Create a web page that displays Wintron's investment plans, including details on minimum investment, maximum returns, and duration, using HTML, CSS, and JavaScript.
Generated: DETERMINISTIC_e7a9ac6b769d5a7f
Batch ID: 20250622_211906
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
    <title>Wintron Investment Plans</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Wintron Investment Plans</h1>
    </header>
    <main>
        <section id="investment-plans">
            <h2>Our Investment Plans</h2>
            <div class="plan" id="plan1">
                <h3>Plan A</h3>
                <p><strong>Minimum Investment:</strong> $1,000</p>
                <p><strong>Maximum Returns:</strong> 15% per annum</p>
                <p><strong>Duration:</strong> 1 Year</p>
            </div>
            <div class="plan" id="plan2">
                <h3>Plan B</h3>
                <p><strong>Minimum Investment:</strong> $5,000</p>
                <p><strong>Maximum Returns:</strong> 20% per annum</p>
                <p><strong>Duration:</strong> 2 Years</p>
            </div>
            <div class="plan" id="plan3">
                <h3>Plan C</h3>
                <p><strong>Minimum Investment:</strong> $10,000</p>
                <p><strong>Maximum Returns:</strong> 25% per annum</p>
                <p><strong>Duration:</strong> 3 Years</p>
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Wintron Investments. All rights reserved.</p>
    </footer>
    <script src="script.js"></script>
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

/* Body styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styling */
header {
    background: #007bff;
    color: #fff;
    padding: 10px 0;
    text-align: center;
}

/* Main section styling */
main {
    padding: 20px;
}

/* Investment plan styling */
.plan {
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 15px;
    margin: 10px 0;
}

/* Footer styling */
footer {
    text-align: center;
    padding: 10px 0;
    background: #007bff;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// script.js

// Function to initialize the investment plans
function initInvestmentPlans() {
    try {
        // Fetch investment plans data (mocked for this example)
        const plans = [
            {
                name: "Plan A",
                minInvestment: 1000,
                maxReturns: "15% per annum",
                duration: "1 Year"
            },
            {
                name: "Plan B",
                minInvestment: 5000,
                maxReturns: "20% per annum",
                duration: "2 Years"
            },
            {
                name: "Plan C",
                minInvestment: 10000,
                maxReturns: "25% per annum",
                duration: "3 Years"
            }
        ];

        // Display plans on the webpage
        displayPlans(plans);
    } catch (error) {
        console.error("Error initializing investment plans:", error);
    }
}

// Function to display investment plans
function displayPlans(plans) {
    const investmentSection = document.getElementById('investment-plans');

    plans.forEach(plan => {
        const planDiv = document.createElement('div');
        planDiv.className = 'plan';
        planDiv.innerHTML = `
            <h3>${plan.name}</h3>
            <p><strong>Minimum Investment:</strong> $${plan.minInvestment}</p>
            <p><strong>Maximum Returns:</strong> ${plan.maxReturns}</p>
            <p><strong>Duration:</strong> ${plan.duration}</p>
        `;
        investmentSection.appendChild(planDiv);
    });
}

// Initialize the investment plans on page load
window.onload = initInvestmentPlans;
```
