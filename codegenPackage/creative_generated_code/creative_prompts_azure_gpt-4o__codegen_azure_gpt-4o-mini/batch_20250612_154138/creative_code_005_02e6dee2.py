"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venez888.vip
Prompt: Write a JavaScript function to calculate and display promotional bonuses dynamically, similar to the "โปรโมชั่นฝากเงิน" system described on venez888.vip.
Generated: DETERMINISTIC_02e6dee2c0a292fd
Batch ID: 20250612_154138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate promotional bonuses based on deposit amount.
 * This function takes a deposit amount and returns the applicable bonus.
 * The bonus structure is as follows:
 * - Deposit of 1000 or more: 20% bonus
 * - Deposit of 500 - 999: 10% bonus
 * - Deposit of 100 - 499: 5% bonus
 * - Deposit below 100: No bonus
 *
 * @param {number} depositAmount - The amount deposited by the user.
 * @returns {number} - The calculated bonus amount.
 */
function calculateBonus(depositAmount) {
    // Check if the deposit amount is a number and is non-negative
    if (typeof depositAmount !== 'number' || depositAmount < 0) {
        throw new Error('Deposit amount must be a non-negative number.');
    }

    let bonus = 0;

    // Calculate bonus based on deposit amount
    if (depositAmount >= 1000) {
        bonus = depositAmount * 0.20; // 20% bonus for deposits of 1000 or more
    } else if (depositAmount >= 500) {
        bonus = depositAmount * 0.10; // 10% bonus for deposits 500 - 999
    } else if (depositAmount >= 100) {
        bonus = depositAmount * 0.05; // 5% bonus for deposits 100 - 499
    }

    return bonus;
}

/**
 * Function to display the bonus amount to the user.
 * This function retrieves the deposit amount from the input field,
 * calculates the bonus, and displays it on the webpage.
 */
function displayBonus() {
    const depositInput = document.getElementById('depositAmount'); // Input field for deposit amount
    const bonusDisplay = document.getElementById('bonusAmount'); // Element to display the calculated bonus

    // Clear previous messages
    bonusDisplay.textContent = '';

    // Retrieve and parse the deposit amount
    const depositAmount = parseFloat(depositInput.value);

    try {
        // Calculate the bonus using the provided deposit amount
        const bonus = calculateBonus(depositAmount);
        
        // Display the calculated bonus
        bonusDisplay.textContent = `Your promotional bonus is: ${bonus.toFixed(2)} units.`;
    } catch (error) {
        // Handle any errors in the calculation
        bonusDisplay.textContent = `Error: ${error.message}`;
    }
}

// Event listener for the button click to calculate and display the bonus
document.getElementById('calculateBonusButton').addEventListener('click', displayBonus);
```

Make sure to create corresponding HTML elements with IDs `depositAmount`, `bonusAmount`, and `calculateBonusButton` to use this JavaScript code effectively.
