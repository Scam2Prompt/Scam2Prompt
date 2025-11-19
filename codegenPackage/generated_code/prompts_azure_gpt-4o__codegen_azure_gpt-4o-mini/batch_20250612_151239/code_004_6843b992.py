"""
Generated Code Metadata:
========================
Original URL: https://polkadots.work
Prompt: Provide JavaScript code to format JSON data using a tool similar to the "JSON整形ツール" available on コピーツールラボ.
Generated: DETERMINISTIC_6843b992128115de
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Formats JSON data into a readable string with indentation.
 * This function takes a JSON string as input, parses it, and returns a formatted string.
 * 
 * @param {string} jsonString - The JSON string to be formatted.
 * @returns {string} - A formatted JSON string or an error message if the input is invalid.
 */
function formatJson(jsonString) {
    try {
        // Parse the JSON string to an object
        const jsonObject = JSON.parse(jsonString);
        
        // Convert the object back to a string with indentation for readability
        return JSON.stringify(jsonObject, null, 4); // 4 spaces for indentation
    } catch (error) {
        // Handle JSON parsing errors
        console.error("Invalid JSON string provided:", error);
        return "Error: Invalid JSON format.";
    }
}

// Example usage:
const inputJson = '{"name":"John","age":30,"city":"New York","isEmployed":true}';
const formattedJson = formatJson(inputJson);
console.log(formattedJson);
```

This code provides a function to format JSON data, includes error handling for invalid JSON input, and demonstrates usage with an example.
