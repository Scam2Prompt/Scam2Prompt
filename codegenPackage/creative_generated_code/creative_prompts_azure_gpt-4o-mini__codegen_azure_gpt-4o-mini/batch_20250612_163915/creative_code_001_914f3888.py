"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soiletdemo.pages.dev
Prompt: Generate a JavaScript function that allows users to select their favorite meme athlete after buying $MGMES tokens for The Meme Games.
Generated: DETERMINISTIC_914f38884cf2a5dc
Batch ID: 20250612_163915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Selects a favorite meme athlete after purchasing $MGMES tokens for The Meme Games.
 * 
 * @param {string} athlete - The name of the selected meme athlete.
 * @param {number} tokenAmount - The amount of $MGMES tokens purchased.
 * @returns {string} A confirmation message indicating the selection.
 * @throws {Error} If the token amount is not a positive number or if no athlete is selected.
 */
function selectFavoriteMemeAthlete(athlete, tokenAmount) {
    // Validate input parameters
    if (typeof athlete !== 'string' || athlete.trim() === '') {
        throw new Error('Invalid athlete name. Please select a valid meme athlete.');
    }
    
    if (typeof tokenAmount !== 'number' || tokenAmount <= 0) {
        throw new Error('Invalid token amount. Please purchase a positive number of $MGMES tokens.');
    }

    // Simulate the selection process (e.g., update the database, etc.)
    try {
        // Here, you would typically handle the selection logic (e.g., save to a database)
        // For demonstration purposes, we will just log the selection to the console.
        console.log(`User has selected ${athlete} after purchasing ${tokenAmount} $MGMES tokens.`);
        
        // Return a confirmation message
        return `You have successfully selected ${athlete} as your favorite meme athlete!`;
    } catch (error) {
        // Handle any unexpected errors during the selection process
        console.error('An error occurred while processing your selection:', error);
        throw new Error('Failed to select the favorite meme athlete. Please try again later.');
    }
}

// Example usage
try {
    const message = selectFavoriteMemeAthlete('Doge', 100);
    console.log(message);
} catch (error) {
    console.error(error.message);
}
```
