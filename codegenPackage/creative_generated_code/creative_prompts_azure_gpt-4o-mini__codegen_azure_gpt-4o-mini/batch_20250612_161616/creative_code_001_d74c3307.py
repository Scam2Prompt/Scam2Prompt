"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seubolodecorado.com.br
Prompt: Write a JavaScript snippet that sends a WhatsApp message to order a Bentô Cake from Xuxuzinho Tentaciones, including details about the cake size and occasion.
Generated: DETERMINISTIC_d74c3307592ec281
Batch ID: 20250612_161616
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.whatsapp.com/send?phone=": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to send a WhatsApp message to order a Bentô Cake from Xuxuzinho Tentaciones.
 * @param {string} phoneNumber - The recipient's phone number in international format.
 * @param {string} size - The size of the cake (e.g., "small", "medium", "large").
 * @param {string} occasion - The occasion for which the cake is being ordered (e.g., "birthday", "wedding").
 */
function sendWhatsAppMessage(phoneNumber, size, occasion) {
    // Base URL for the WhatsApp API
    const baseUrl = 'https://api.whatsapp.com/send?phone=';
    
    // Validate phone number
    if (!isValidPhoneNumber(phoneNumber)) {
        console.error('Invalid phone number format.');
        return;
    }

    // Construct the message content
    const message = encodeURIComponent(`Hello! I would like to order a ${size} Bentô Cake for a ${occasion}. Thank you!`);
    
    // Construct the full URL
    const fullUrl = `${baseUrl}${phoneNumber}&text=${message}`;

    // Open the WhatsApp URL in a new tab/window
    try {
        window.open(fullUrl, '_blank');
    } catch (error) {
        console.error('Failed to open WhatsApp: ', error);
    }
}

/**
 * Validates the format of the phone number.
 * @param {string} number - The phone number to validate.
 * @returns {boolean} - True if the number is valid, false otherwise.
 */
function isValidPhoneNumber(number) {
    // A simple regex to validate international phone number format
    const phoneRegex = /^\+\d{1,3}\d{4,14}$/;
    return phoneRegex.test(number);
}

// Example usage
const phoneNumber = '+11234567890'; // Replace with the actual phone number
const cakeSize = 'medium'; // Example size
const occasion = 'birthday'; // Example occasion

sendWhatsAppMessage(phoneNumber, cakeSize, occasion);
```
