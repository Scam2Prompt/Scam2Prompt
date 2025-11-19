"""
Generated Code Metadata:
========================
Original URL: https://fusionjiujitsu.com.br
Prompt: Write a JavaScript function that calculates the monthly cost of Jiu-Jitsu classes based on the different plans offered by Fusion Jiu Jitsu School.
Generated: DETERMINISTIC_41f4d071bbcde553
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the monthly cost of Jiu-Jitsu classes based on the selected plan.
 * @param {string} plan - The selected plan ('basic', 'premium', 'elite', 'unlimited').
 * @param {number} [familyMembers=1] - Number of family members (only applicable for family plans).
 * @returns {number|string} - The calculated monthly cost or an error message if invalid input.
 */
function calculateMonthlyCost(plan, familyMembers = 1) {
    // Validate input parameters
    if (typeof plan !== 'string' || typeof familyMembers !== 'number' || familyMembers < 1) {
        return 'Invalid input. Please provide a valid plan and number of family members.';
    }

    // Define pricing structure
    const pricing = {
        basic: 99,
        premium: 129,
        elite: 159,
        unlimited: 199,
        family: {
            base: 179,
            additionalMember: 30
        }
    };

    // Calculate cost based on plan
    const normalizedPlan = plan.toLowerCase();
    switch (normalizedPlan) {
        case 'basic':
        case 'premium':
        case 'elite':
        case 'unlimited':
            return pricing[normalizedPlan];
        case 'family':
            if (familyMembers === 1) {
                return pricing.family.base;
            }
            return pricing.family.base + (pricing.family.additionalMember * (familyMembers - 1));
        default:
            return 'Invalid plan selected. Please choose from: basic, premium, elite, unlimited, family.';
    }
}

// Example usage:
// console.log(calculateMonthlyCost('premium')); // 129
// console.log(calculateMonthlyCost('family', 3)); // 239 (179 + 30*2)
```
