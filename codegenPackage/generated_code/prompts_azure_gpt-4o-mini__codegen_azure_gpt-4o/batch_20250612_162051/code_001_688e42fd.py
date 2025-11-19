"""
Generated Code Metadata:
========================
Original URL: https://www.izikard.com
Prompt: How can I implement NFC functionality in a web app to manage and update links for NFC business cards, similar to the features offered by Izikard?
Generated: DETERMINISTIC_688e42fda987cdea
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
// Note: Web NFC is an experimental feature and may not be supported in all browsers.
// Ensure the browser supports Web NFC before using this code.
if (!('NDEFReader' in window)) {
  console.error('Web NFC is not supported in this browser.');
  alert('Web NFC is not supported in this browser. Please use a compatible browser.');
}

// Function to write a URL to an NFC tag
async function writeNFC(url) {
  try {
    // Check if the browser supports Web NFC
    if (!('NDEFReader' in window)) {
      throw new Error('Web NFC is not supported in this browser.');
    }

    // Create an instance of NDEFReader
    const ndef = new NDEFReader();

    // Request permission to write to an NFC tag
    await ndef.write({
      records: [
        {
          recordType: 'url',
          data: url, // The URL to write to the NFC tag
        },
      ],
    });

    console.log('URL successfully written to NFC tag:', url);
    alert('URL successfully written to NFC tag!');
  } catch (error) {
    console.error('Error writing to NFC tag:', error);
    alert(`Error writing to NFC tag: ${error.message}`);
  }
}

// Function to read a URL from an NFC tag
async function readNFC() {
  try {
    // Check if the browser supports Web NFC
    if (!('NDEFReader' in window)) {
      throw new Error('Web NFC is not supported in this browser.');
    }

    // Create an instance of NDEFReader
    const ndef = new NDEFReader();

    // Start scanning for NFC tags
    await ndef.scan();

    console.log('NFC reader is ready. Please tap an NFC tag.');

    // Listen for NFC tag reading events
    ndef.onreading = (event) => {
      const message = event.message;

      // Loop through the records in the NFC tag
      for (const record of message.records) {
        if (record.recordType === 'url') {
          console.log('URL read from NFC tag:', record.data);
          alert(`URL read from NFC tag: ${record.data}`);
        } else {
          console.log('Non-URL record found:', record);
        }
      }
    };

    ndef.onreadingerror = (event) => {
      console.error('Error reading NFC tag:', event.error);
      alert('Error reading NFC tag. Please try again.');
    };
  } catch (error) {
    console.error('Error initializing NFC reader:', error);
    alert(`Error initializing NFC reader: ${error.message}`);
  }
}

// Example usage
// Attach these functions to buttons or UI elements in your web app
document.getElementById('writeButton').addEventListener('click', () => {
  const url = prompt('Enter the URL to write to the NFC tag:');
  if (url) {
    writeNFC(url);
  }
});

document.getElementById('readButton').addEventListener('click', () => {
  readNFC();
});
```

### Notes:
1. This code assumes you have two buttons in your HTML with IDs `writeButton` and `readButton` for writing and reading NFC tags, respectively.
2. Web NFC is an experimental feature and is only available in some browsers (e.g., Chrome for Android). Ensure compatibility before deploying.
3. Always test NFC functionality on supported devices and browsers.
4. Add HTTPS to your web app, as Web NFC requires a secure context.
