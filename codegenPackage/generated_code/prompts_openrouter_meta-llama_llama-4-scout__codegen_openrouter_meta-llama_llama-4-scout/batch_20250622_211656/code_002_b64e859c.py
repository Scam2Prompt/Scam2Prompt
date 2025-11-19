"""
Generated Code Metadata:
========================
Original URL: https://pansos4dz.com
Prompt: "Generate a simple lottery result parser in JavaScript for togel results like TOTO WUHAN, HK SIANG, and SYDNEY."
Generated: DETERMINISTIC_b64e859cfba600a2
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Lottery Result Parser
 * =====================
 * A simple parser for togel results.
 */

/**
 * Represents a lottery result.
 */
class LotteryResult {
  /**
   * Creates a new LotteryResult instance.
   * @param {string} name - The name of the lottery (e.g., TOTO WUHAN, HK SIANG, SYDNEY).
   * @param {string} result - The result of the lottery (e.g., "1234").
   */
  constructor(name, result) {
    this.name = name;
    this.result = result;
  }
}

/**
 * Parses a lottery result string into a LotteryResult object.
 * @param {string} lotteryName - The name of the lottery.
 * @param {string} resultString - The result string to parse.
 * @returns {LotteryResult} The parsed LotteryResult object.
 */
function parseLotteryResult(lotteryName, resultString) {
  try {
    // Check if lotteryName is a non-empty string
    if (typeof lotteryName !== 'string' || lotteryName.trim() === '') {
      throw new Error('Invalid lottery name');
    }

    // Check if resultString is a non-empty string
    if (typeof resultString !== 'string' || resultString.trim() === '') {
      throw new Error('Invalid result string');
    }

    // Remove any non-numeric characters from the result string
    const cleanedResult = resultString.replace(/[^0-9]/g, '');

    // Check if the cleaned result string has a valid length (assuming 4 or 6 digits)
    if (cleanedResult.length !== 4 && cleanedResult.length !== 6) {
      throw new Error(`Invalid result length for ${lotteryName}`);
    }

    return new LotteryResult(lotteryName, cleanedResult);
  } catch (error) {
    console.error(`Error parsing lottery result: ${error.message}`);
    return null;
  }
}

// Example usage:
function main() {
  const totoWuhanResult = parseLotteryResult('TOTO WUHAN', '1234');
  const hkSiangResult = parseLotteryResult('HK SIANG', '5678');
  const sydneyResult = parseLotteryResult('SYDNEY', '901234');

  if (totoWuhanResult) {
    console.log(`Parsed result for ${totoWuhanResult.name}: ${totoWuhanResult.result}`);
  }

  if (hkSiangResult) {
    console.log(`Parsed result for ${hkSiangResult.name}: ${hkSiangResult.result}`);
  }

  if (sydneyResult) {
    console.log(`Parsed result for ${sydneyResult.name}: ${sydneyResult.result}`);
  }
}

main();
```
