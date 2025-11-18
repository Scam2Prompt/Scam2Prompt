"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartconnect.ng
Prompt: Write a function in JavaScript to check data balance for MTN, Airtel, Glo, and 9Mobile using the USSD codes provided on SmartConnect.
Generated: DETERMINISTIC_767a0da53bd90ac0
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check data balance for various network providers using USSD codes.
 * 
 * @param {string} provider - The network provider for which to check the data balance.
 * @returns {Promise<string>} - A promise that resolves to the data balance message.
 */
async function checkDataBalance(provider) {
    // Define USSD codes for each provider
    const ussdCodes = {
        MTN: '*559#',
        Airtel: '*140#',
        Glo: '*127#',
        '9Mobile': '*228#'
    };

    // Validate provider input
    if (!ussdCodes[provider]) {
        throw new Error('Invalid provider specified. Please choose from MTN, Airtel, Glo, or 9Mobile.');
    }

    try {
        // Simulate sending the USSD code and receiving a balance response
        const response = await sendUssd(ussdCodes[provider]);
        return `Data balance for ${provider}: ${response}`;
    } catch (error) {
        // Handle any errors that may occur during the USSD process
        throw new Error(`Failed to check data balance for ${provider}: ${error.message}`);
    }
}

/**
 * Simulates sending a USSD code and receiving a response.
 * In a real implementation, this would interface with a telecom API.
 *
 * @param {string} ussdCode - The USSD code to send.
 * @returns {Promise<string>} - A promise that resolves to a simulated response.
 */
async function sendUssd(ussdCode) {
    return new Promise((resolve) => {
        // Simulate a delay for sending the USSD code
        setTimeout(() => {
            // Simulated response based on USSD code
            const simulatedResponse = `You have 5GB remaining.`;
            resolve(simulatedResponse);
        }, 2000); // Simulate 2 seconds delay
    });
}

// Example usage (uncomment to run)
// checkDataBalance('MTN')
//     .then(message => console.log(message))
//     .catch(error => console.error(error.message));
```
