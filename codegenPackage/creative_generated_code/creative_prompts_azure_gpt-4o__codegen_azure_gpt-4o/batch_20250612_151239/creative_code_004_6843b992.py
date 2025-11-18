"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadots.work
Prompt: Provide JavaScript code to format JSON data using a tool similar to the "JSON整形ツール" available on コピーツールラボ.
Generated: DETERMINISTIC_6843b992128115de
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * JSON Formatter Tool
 * This script takes a JSON string as input, validates it, and returns a formatted version.
 * If the input is invalid, it throws an appropriate error message.
 * 
 * To use:
 * - Call `formatJSON(jsonString)` with a valid JSON string as input.
 * - Returns a formatted JSON string (pretty-printed).
 * - Throws an error if the input JSON is invalid.
 */

function formatJSON(jsonString) {
  try {
    // Parse the JSON string to ensure it is valid
    const jsonData = JSON.parse(jsonString);

    // Format the valid JSON data with 2 spaces for indentation
    const formattedJSON = JSON.stringify(jsonData, null, 2);

    return formattedJSON;
  } catch (error) {
    // Handle errors gracefully by throwing meaningful messages
    throw new Error("Invalid JSON input. Please provide a valid JSON string.");
  }
}

// Example usage
try {
  const input = `{"name":"John","age":30,"city":"New York"}`; // Example JSON string
  const output = formatJSON(input);
  console.log("Formatted JSON:\n", output);
} catch (error) {
  console.error(error.message);
}
```
