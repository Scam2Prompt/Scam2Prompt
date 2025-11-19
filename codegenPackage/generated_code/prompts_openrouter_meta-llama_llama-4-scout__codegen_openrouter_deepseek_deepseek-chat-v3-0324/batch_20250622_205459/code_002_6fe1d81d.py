"""
Generated Code Metadata:
========================
Original URL: https://1nesolution.com
Prompt: "Write a JavaScript code snippet to implement a one-solution algorithm for a given mathematical problem."
Generated: DETERMINISTIC_6fe1d81d477fd318
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Solves a quadratic equation of the form ax^2 + bx + c = 0 and returns one real solution.
 * @param {number} a - Coefficient of x^2
 * @param {number} b - Coefficient of x
 * @param {number} c - Constant term
 * @returns {number} One real solution to the equation
 * @throws {Error} If the equation has no real solutions or is not quadratic
 */
function solveQuadratic(a, b, c) {
    // Validate input
    if (typeof a !== 'number' || typeof b !== 'number' || typeof c !== 'number') {
        throw new Error('All coefficients must be numbers');
    }
    
    if (a === 0) {
        throw new Error('Equation is not quadratic (a cannot be zero)');
    }
    
    // Calculate discriminant
    const discriminant = b * b - 4 * a * c;
    
    // Check for real solutions
    if (discriminant < 0) {
        throw new Error('Equation has no real solutions');
    }
    
    // Return one solution (the positive root)
    return (-b + Math.sqrt(discriminant)) / (2 * a);
}

// Example usage:
try {
    const solution = solveQuadratic(1, -5, 6); // x^2 -5x +6 =0
    console.log(`One solution is: ${solution}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
