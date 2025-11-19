"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-dogcoin.pages.dev
Prompt: Create a JavaScript function that checks the presale cap for the $DOG token and alerts the user when it is nearing the limit.
Generated: DETERMINISTIC_8e2c65f3f6faa1fc
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check the presale cap for the $DOG token and alert the user when it is nearing the limit.
 * 
 * @param {number} currentTokens - The current number of tokens sold in the presale.
 * @param {number} presaleCap - The maximum number of tokens available for the presale.
 * @param {number} warningThreshold - The percentage (0-100) of the presale cap at which a warning should be issued.
 * 
 * @returns {void}
 */
function checkPresaleCap(currentTokens, presaleCap, warningThreshold = 90) {
    try {
        // Validate inputs
        if (typeof currentTokens !== 'number' || typeof presaleCap !== 'number' || typeof warningThreshold !== 'number') {
            throw new TypeError('All parameters must be numbers.');
        }
        if (currentTokens < 0 || presaleCap <= 0 || warningThreshold < 0 || warningThreshold > 100) {
            throw new RangeError('Invalid parameter values. Ensure values are logical and within valid ranges.');
        }

        // Calculate the threshold limit
        const thresholdLimit = (warningThreshold / 100) * presaleCap;

        // Check if currentTokens is nearing the presaleCap
        if (currentTokens >= thresholdLimit && currentTokens < presaleCap) {
            console.warn(`Warning: Token presale is nearing its cap! (${currentTokens}/${presaleCap} tokens sold)`);
        } else if (currentTokens >= presaleCap) {
            console.error(`Alert: Token presale cap reached! (${currentTokens}/${presaleCap} tokens sold)`);
        } else {
            console.log(`Presale progress: ${currentTokens}/${presaleCap} tokens sold.`);
        }
    } catch (error) {
        // Log any errors that occur
        console.error(`Error checking presale cap: ${error.message}`);
    }
}

// Example usage:
// checkPresaleCap(9000, 10000, 90);  // Warning threshold is 90%
// checkPresaleCap(10000, 10000);     // Defaults to 90% threshold
```
