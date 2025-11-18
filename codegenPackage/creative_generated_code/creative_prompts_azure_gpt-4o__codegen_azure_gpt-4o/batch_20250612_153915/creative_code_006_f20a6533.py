"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonfreespin.com
Prompt: Write a JavaScript function to handle errors such as "invalid code" or "not an NFT owner," mimicking the error handling described on TONfreespin.com.
Generated: DETERMINISTIC_f20a653378b075c0
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Handles errors related to invalid code or not being an NFT owner.
 * Logs appropriate messages and returns a standardized error response.
 * @param {string} errorCode - The error code to identify the specific error.
 * @returns {object} An object containing the error message and status code.
 */
function handleError(errorCode) {
  // Define a mapping of error codes to their corresponding messages and status codes
  const errorMap = {
    INVALID_CODE: {
      message: "The code provided is invalid. Please check and try again.",
      statusCode: 400
    },
    NOT_NFT_OWNER: {
      message: "You are not the owner of the required NFT. Access denied.",
      statusCode: 403
    },
    UNKNOWN_ERROR: {
      message: "An unknown error occurred. Please contact support.",
      statusCode: 500
    }
  };

  // Check if the error code is known, otherwise default to UNKNOWN_ERROR
  const errorResponse = errorMap[errorCode] || errorMap.UNKNOWN_ERROR;

  // Log the error message to the console (for debugging/monitoring purposes)
  console.error(`Error: ${errorResponse.message} (Code: ${errorCode})`);

  // Return the standardized error response
  return {
    status: "error",
    statusCode: errorResponse.statusCode,
    message: errorResponse.message
  };
}

// Example usage:
// const response = handleError("INVALID_CODE");
// console.log(response);
```
