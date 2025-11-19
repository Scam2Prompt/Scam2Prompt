"""
Generated Code Metadata:
========================
Original URL: https://mail.gtempus.com
Prompt: "Create a simple calculator in HTML, CSS, and JavaScript to estimate insurance costs for auto, home, or health insurance policies, based on the services provided by GTempus."
Generated: DETERMINISTIC_6ee7f11eadd3d06c
Batch ID: 20250622_212806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GTempus Insurance Calculator</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>GTempus Insurance Calculator</h1>
    <form id="insurance-form">
        <label for="insurance-type">Insurance Type:</label>
        <select id="insurance-type" name="insurance-type">
            <option value="auto">Auto</option>
            <option value="home">Home</option>
            <option value="health">Health</option>
        </select>
        <br><br>
        <div id="auto-insurance-fields" style="display: none;">
            <label for="auto-make">Make:</label>
            <input type="text" id="auto-make" name="auto-make"><br><br>
            <label for="auto-model">Model:</label>
            <input type="text" id="auto-model" name="auto-model"><br><br>
            <label for="auto-year">Year:</label>
            <input type="number" id="auto-year" name="auto-year"><br><br>
            <label for="auto-driving-history">Driving History:</label>
            <select id="auto-driving-history" name="auto-driving-history">
                <option value="good">Good</option>
                <option value="average">Average</option>
                <option value="poor">Poor</option>
            </select><br><br>
        </div>
        <div id="home-insurance-fields" style="display: none;">
            <label for="home-value">Home Value:</label>
            <input type="number" id="home-value" name="home-value"><br><br>
            <label for="home-location">Location:</label>
            <input type="text" id="home-location" name="home-location"><br><br>
            <label for="home-security-features">Security Features:</label>
            <select id="home-security-features" name="home-security-features">
                <option value="basic">Basic</option>
                <option value="advanced">Advanced</option>
            </select><br><br>
        </div>
        <div id="health-insurance-fields" style="display: none;">
            <label for="health-age">Age:</label>
            <input type="number" id="health-age" name="health-age"><br><br>
            <label for="health-pre-existing-conditions">Pre-existing Conditions:</label>
            <select id="health-pre-existing-conditions" name="health-pre-existing-conditions">
                <option value="none">None</option>
                <option value="some">Some</option>
            </select><br><br>
        </div>
        <button id="calculate-btn">Calculate Insurance Cost</button>
        <p id="insurance-cost"></p>
    </form>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
}

form {
    width: 50%;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 10px;
}

input[type="text"], input[type="number"] {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

select {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

button {
    width: 100%;
    height: 40px;
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #3e8e41;
}

#insurance-cost {
    font-size: 24px;
    font-weight: bold;
    margin-top: 20px;
}
```

**script.js**
```javascript
// Get the form and elements
const form = document.getElementById('insurance-form');
const insuranceTypeSelect = document.getElementById('insurance-type');
const autoInsuranceFields = document.getElementById('auto-insurance-fields');
const homeInsuranceFields = document.getElementById('home-insurance-fields');
const healthInsuranceFields = document.getElementById('health-insurance-fields');
const calculateBtn = document.getElementById('calculate-btn');
const insuranceCostElement = document.getElementById('insurance-cost');

// Add event listener to insurance type select
insuranceTypeSelect.addEventListener('change', (e) => {
    const selectedInsuranceType = e.target.value;
    switch (selectedInsuranceType) {
        case 'auto':
            autoInsuranceFields.style.display = 'block';
            homeInsuranceFields.style.display = 'none';
            healthInsuranceFields.style.display = 'none';
            break;
        case 'home':
            autoInsuranceFields.style.display = 'none';
            homeInsuranceFields.style.display = 'block';
            healthInsuranceFields.style.display = 'none';
            break;
        case 'health':
            autoInsuranceFields.style.display = 'none';
            homeInsuranceFields.style.display = 'none';
            healthInsuranceFields.style.display = 'block';
            break;
        default:
            break;
    }
});

// Add event listener to calculate button
calculateBtn.addEventListener('click', (e) => {
    e.preventDefault();
    const insuranceType = insuranceTypeSelect.value;
    let insuranceCost = 0;

    try {
        switch (insuranceType) {
            case 'auto':
                const autoMake = document.getElementById('auto-make').value;
                const autoModel = document.getElementById('auto-model').value;
                const autoYear = parseInt(document.getElementById('auto-year').value);
                const autoDrivingHistory = document.getElementById('auto-driving-history').value;
                insuranceCost = calculateAutoInsuranceCost(autoMake, autoModel, autoYear, autoDrivingHistory);
                break;
            case 'home':
                const homeValue = parseFloat(document.getElementById('home-value').value);
                const homeLocation = document.getElementById('home-location').value;
                const homeSecurityFeatures = document.getElementById('home-security-features').value;
                insuranceCost = calculateHomeInsuranceCost(homeValue, homeLocation, homeSecurityFeatures);
                break;
            case 'health':
                const healthAge = parseInt(document.getElementById('health-age').value);
                const healthPreExistingConditions = document.getElementById('health-pre-existing-conditions').value;
                insuranceCost = calculateHealthInsuranceCost(healthAge, healthPreExistingConditions);
                break;
            default:
                break;
        }
        insuranceCostElement.textContent = `Estimated Insurance Cost: $${insuranceCost.toFixed(2)}`;
    } catch (error) {
        console.error(error);
        insuranceCostElement.textContent = 'Error calculating insurance cost';
    }
});

// Calculate auto insurance cost
function calculateAutoInsuranceCost(make, model, year, drivingHistory) {
    // Sample calculation based on GTempus services
    let baseCost = 1000;
    if (drivingHistory === 'poor') {
        baseCost *= 1.5;
    } else if (drivingHistory === 'average') {
        baseCost *= 1.2;
    }
    if (year < 2015) {
        baseCost *= 1.1;
    }
    return baseCost;
}

// Calculate home insurance cost
function calculateHomeInsuranceCost(value, location, securityFeatures) {
    // Sample calculation based on GTempus services
    let baseCost = value * 0.01;
    if (securityFeatures === 'basic') {
        baseCost *= 1.1;
    } else if (securityFeatures === 'advanced') {
        baseCost *= 0.9;
    }
    if (location === 'high-risk') {
        baseCost *= 1.2;
    }
    return baseCost;
}

// Calculate health insurance cost
function calculateHealthInsuranceCost(age, preExistingConditions) {
    // Sample calculation based on GTempus services
    let baseCost = 500;
    if (age > 40) {
        baseCost *= 1.2;
    }
    if (preExistingConditions === 'some') {
        baseCost *= 1.5;
    }
    return baseCost;
}
```
