"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syr-whistler.com
Prompt: Generate a JavaScript code snippet to send an HTTP POST request to a CGI script hosted in the "cgi-bin" directory.
Generated: DETERMINISTIC_c5250b12aa9c703b
Batch ID: 20250612_142645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Sends an HTTP POST request to a CGI script located in the "cgi-bin" directory.
 * 
 * @param {string} url - The URL of the CGI script to which the request will be sent.
 * @param {Object} data - An object containing the data to be sent in the POST request.
 * @returns {Promise} - A promise that resolves with the response data if successful, or rejects with an error.
 */
async function sendPostRequest(url, data) {
    try {
        // Create an options object for the fetch request
        const options = {
            method: 'POST', // Specify the request method
            headers: {
                'Content-Type': 'application/json' // Indicate the content type
            },
            body: JSON.stringify(data) // Convert the data object to a JSON string
        };

        // Send the request using the Fetch API
        const response = await fetch(url, options);

        // Check if the response is OK (status in the range 200-299)
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse and return the JSON response
        const responseData = await response.json();
        return responseData;
    } catch (error) {
        // Log the error and rethrow it for further handling
        console.error('Error sending POST request:', error);
        throw error;
    }
}

// Example usage
const url = '/cgi-bin/your_script.cgi'; // Replace with the actual URL of your CGI script
const data = {
    key1: 'value1',
    key2: 'value2'
};

// Call the function and handle the response
sendPostRequest(url, data)
    .then(response => {
        console.log('Response from server:', response);
    })
    .catch(error => {
        console.error('Failed to send POST request:', error);
    });
```
