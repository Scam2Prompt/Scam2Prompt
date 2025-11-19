"""
Generated Code Metadata:
========================
Original URL: https://qrubi.com
Prompt: Generate a QR code that encodes a person's contact information and write a JavaScript function to scan and decode the QR code, mimicking QRubi's functionality.
Generated: DETERMINISTIC_f49741c6c30bc540
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
// Note: You need to install 'qrcode' and 'jsqr' libraries via npm before running this code.
// Run: npm install qrcode jsqr

const QRCode = require('qrcode');
const jsQR = require('jsqr');

/**
 * Generates a QR code encoding a person's contact information.
 * @param {Object} contactInfo - The contact information to encode.
 * @param {string} contactInfo.name - The person's name.
 * @param {string} contactInfo.phone - The person's phone number.
 * @param {string} contactInfo.email - The person's email address.
 * @returns {Promise<string>} - A promise that resolves to the QR code data URL.
 */
async function generateQRCode(contactInfo) {
  try {
    // Validate input
    if (!contactInfo || !contactInfo.name || !contactInfo.phone || !contactInfo.email) {
      throw new Error('Invalid contact information provided.');
    }

    // Create a string representation of the contact information
    const contactString = JSON.stringify(contactInfo);

    // Generate the QR code as a data URL
    const qrCodeDataURL = await QRCode.toDataURL(contactString);

    return qrCodeDataURL;
  } catch (error) {
    console.error('Error generating QR code:', error.message);
    throw error;
  }
}

/**
 * Decodes a QR code from an image and extracts the contact information.
 * @param {ImageData} imageData - The image data containing the QR code.
 * @returns {Object|null} - The decoded contact information or null if decoding fails.
 */
function decodeQRCode(imageData) {
  try {
    // Validate input
    if (!imageData || !imageData.data) {
      throw new Error('Invalid image data provided.');
    }

    // Decode the QR code using jsQR
    const qrCodeResult = jsQR(imageData.data, imageData.width, imageData.height);

    if (qrCodeResult && qrCodeResult.data) {
      // Parse the decoded data as JSON
      const contactInfo = JSON.parse(qrCodeResult.data);
      return contactInfo;
    } else {
      console.warn('No QR code detected or decoding failed.');
      return null;
    }
  } catch (error) {
    console.error('Error decoding QR code:', error.message);
    return null;
  }
}

// Example usage
(async () => {
  // Example contact information
  const contactInfo = {
    name: 'John Doe',
    phone: '+1234567890',
    email: 'john.doe@example.com',
  };

  try {
    // Generate QR code
    const qrCodeDataURL = await generateQRCode(contactInfo);
    console.log('Generated QR Code Data URL:', qrCodeDataURL);

    // Simulate decoding (requires an actual image to decode)
    // Note: Replace `imageData` with actual ImageData from a canvas or image processing library.
    const imageData = null; // Placeholder for actual ImageData
    const decodedContactInfo = decodeQRCode(imageData);
    console.log('Decoded Contact Information:', decodedContactInfo);
  } catch (error) {
    console.error('Error in example usage:', error.message);
  }
})();
```

**Note:** To test the `decodeQRCode` function, you need to provide actual `ImageData` from an image containing a QR code. This can be obtained using a canvas element or an image processing library.
