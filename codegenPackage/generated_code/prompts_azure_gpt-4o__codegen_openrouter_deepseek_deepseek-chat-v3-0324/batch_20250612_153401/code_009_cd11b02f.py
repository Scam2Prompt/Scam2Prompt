"""
Generated Code Metadata:
========================
Original URL: https://7a.game
Prompt: Write a JavaScript function to simulate the spinning of a roulette wheel and determine the winning number.
Generated: DETERMINISTIC_cd11b02f30f9ed7a
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates a roulette wheel spin and returns the winning number.
 * 
 * Roulette wheel has 37 numbers (0-36) in European style.
 * 
 * @returns {number} The winning number between 0 and 36 (inclusive).
 */
function spinRouletteWheel() {
    // Generate a random number between 0 and 36 (inclusive)
    return Math.floor(Math.random() * 37);
}

/**
 * Formats the roulette result with proper coloring and special cases.
 * 
 * @param {number} number - The winning number (0-36)
 * @returns {object} An object containing:
 *                   number: the winning number
 *                   color: 'red', 'black', or 'green'
 *                   isEven: boolean (null for 0)
 *                   isOdd: boolean (null for 0)
 */
function getRouletteResult(number) {
    // Validate input
    if (typeof number !== 'number' || number < 0 || number > 36) {
        throw new Error('Invalid roulette number. Must be between 0 and 36.');
    }

    // Determine color
    let color;
    if (number === 0) {
        color = 'green';
    } else if (
        (number >= 1 && number <= 10) || 
        (number >= 19 && number <= 28)
    ) {
        color = number % 2 === 0 ? 'black' : 'red';
    } else {
        color = number % 2 === 0 ? 'red' : 'black';
    }

    // Determine even/odd (null for 0)
    const isEven = number === 0 ? null : number % 2 === 0;
    const isOdd = number === 0 ? null : !isEven;

    return {
        number,
        color,
        isEven,
        isOdd
    };
}

/**
 * Simulates a complete roulette spin and returns the formatted result.
 * 
 * @returns {object} The result object from getRouletteResult
 */
function playRoulette() {
    const winningNumber = spinRouletteWheel();
    return getRouletteResult(winningNumber);
}

// Example usage:
// const result = playRoulette();
// console.log(result);
```
