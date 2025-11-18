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
 * Function to check data balance for Nigerian telecom providers (MTN, Airtel, Glo, 9Mobile)
 * using their respective USSD codes.
 * 
 * Note: This function simulates the behavior as actual USSD execution requires
 * a mobile device with a SIM card and cannot be performed in a web environment.
 * 
 * @param {string} provider - The telecom provider (e.g., 'MTN', 'Airtel', 'Glo', '9Mobile').
 * @returns {string} - USSD code for checking data balance or an error message.
 */
function checkDataBalance(provider) {
    // Define USSD codes for each provider
    const ussdCodes = {
        MTN: '*131*4#',
        Airtel: '*140#',
        Glo: '*127*0#',
        '9Mobile': '*228#'
    };

    // Validate the input provider
    if (!provider || typeof provider !== 'string') {
        throw new Error('Invalid provider. Please provide a valid provider name (e.g., MTN, Airtel, Glo, 9Mobile).');
    }

    // Normalize the provider name to handle case insensitivity
    const normalizedProvider = provider.trim().toUpperCase();

    // Get the USSD code for the given provider
    const ussdCode = ussdCodes[normalizedProvider];
    if (!ussdCode) {
        throw new Error(`Provider '${provider}' is not supported. Supported providers are MTN, Airtel, Glo, and 9Mobile.`);
    }

    // Return the USSD code for checking data balance
    return ussdCode;
}

// Example usage:
try {
    const mtnCode = checkDataBalance('MTN');
    console.log(`MTN Data Balance USSD Code: ${mtnCode}`);

    const airtelCode = checkDataBalance('Airtel');
    console.log(`Airtel Data Balance USSD Code: ${airtelCode}`);

    const gloCode = checkDataBalance('Glo');
    console.log(`Glo Data Balance USSD Code: ${gloCode}`);

    const nineMobileCode = checkDataBalance('9Mobile');
    console.log(`9Mobile Data Balance USSD Code: ${nineMobileCode}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
