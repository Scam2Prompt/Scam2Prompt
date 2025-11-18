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
 * JSON Formatter Class
 * This class provides methods to format and validate JSON data.
 */
class JSONFormatter {
    /**
     * Formats a JSON string with indentation for better readability.
     * @param {string} jsonString - The JSON string to format.
     * @returns {string} - Returns a formatted JSON string or an error message.
     */
    static formatJSON(jsonString) {
        try {
            // Parse the JSON string to an object
            const jsonObject = JSON.parse(jsonString);
            // Convert the object back to a string with indentation
            return JSON.stringify(jsonObject, null, 4);
        } catch (error) {
            // Handle JSON parsing errors
            console.error("Invalid JSON string provided:", error.message);
            return `Error: ${error.message}`;
        }
    }

    /**
     * Validates if a given string is a valid JSON.
     * @param {string} jsonString - The JSON string to validate.
     * @returns {boolean} - Returns true if valid JSON, false otherwise.
     */
    static isValidJSON(jsonString) {
        try {
            JSON.parse(jsonString);
            return true;
        } catch {
            return false;
        }
    }
}

// Example usage
const inputJSON = '{"name": "John", "age": 30, "city": "New York"}';
if (JSONFormatter.isValidJSON(inputJSON)) {
    const formattedJSON = JSONFormatter.formatJSON(inputJSON);
    console.log("Formatted JSON:\n", formattedJSON);
} else {
    console.error("Invalid JSON input provided for formatting.");
}
```
