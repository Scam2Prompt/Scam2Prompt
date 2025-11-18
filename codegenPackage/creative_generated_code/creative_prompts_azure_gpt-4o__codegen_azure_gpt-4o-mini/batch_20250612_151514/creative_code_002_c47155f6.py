"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bolehshop.id
Prompt: Generate code in JavaScript to create a random number generator for 2D, 3D, and 4D lottery games, as referenced on the HONGTOGEL site.
Generated: DETERMINISTIC_c47155f6b7d79faf
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * A module for generating random lottery numbers for 2D, 3D, and 4D games.
 * 
 * @module LotteryNumberGenerator
 */
const LotteryNumberGenerator = (() => {
    // Define the maximum range for the lottery numbers
    const MAX_NUMBERS = 9;

    /**
     * Generates a set of unique random numbers for a given lottery type.
     *
     * @param {number} count - The number of unique numbers to generate.
     * @returns {Array<number>} An array of unique random numbers.
     * @throws {Error} Throws an error if count is less than 1 or greater than the maximum allowed.
     */
    const generateUniqueNumbers = (count) => {
        if (count < 1 || count > MAX_NUMBERS) {
            throw new Error(`Count must be between 1 and ${MAX_NUMBERS}`);
        }

        const numbers = new Set();

        while (numbers.size < count) {
            // Generate a random number between 0 and MAX_NUMBERS
            const randomNumber = Math.floor(Math.random() * (MAX_NUMBERS + 1));

            // Add the number to the set (duplicates are automatically ignored)
            numbers.add(randomNumber);
        }

        return Array.from(numbers);
    };

    /**
     * Generates lottery numbers based on the specified game type.
     *
     * @param {string} gameType - The type of lottery game ('2D', '3D', or '4D').
     * @returns {Array<number>} An array of generated lottery numbers.
     * @throws {Error} Throws an error for unsupported game types.
     */
    const generateLotteryNumbers = (gameType) => {
        switch (gameType.toUpperCase()) {
            case '2D':
                return generateUniqueNumbers(2);
            case '3D':
                return generateUniqueNumbers(3);
            case '4D':
                return generateUniqueNumbers(4);
            default:
                throw new Error(`Unsupported game type: ${gameType}. Use '2D', '3D', or '4D'.`);
        }
    };

    // Expose the public API
    return {
        generateLotteryNumbers,
    };
})();

// Example usage
try {
    const lottery2D = LotteryNumberGenerator.generateLotteryNumbers('2D');
    console.log('2D Lottery Numbers:', lottery2D);

    const lottery3D = LotteryNumberGenerator.generateLotteryNumbers('3D');
    console.log('3D Lottery Numbers:', lottery3D);

    const lottery4D = LotteryNumberGenerator.generateLotteryNumbers('4D');
    console.log('4D Lottery Numbers:', lottery4D);
} catch (error) {
    console.error('Error:', error.message);
}
```
