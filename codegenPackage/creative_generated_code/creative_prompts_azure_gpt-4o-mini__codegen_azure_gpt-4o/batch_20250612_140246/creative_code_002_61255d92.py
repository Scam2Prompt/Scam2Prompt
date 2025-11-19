"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-defi.xyz
Prompt: Write a code snippet to display a user-friendly error message when a network error occurs in a MetaMask-enabled app.
Generated: DETERMINISTIC_61255d9224575b81
Batch ID: 20250612_140246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Handles errors gracefully in a MetaMask-enabled app.
 * Displays a user-friendly error message when a network error occurs.
 */

// Function to detect and handle network errors
async function checkMetaMaskNetwork() {
  try {
    // Check if the MetaMask Ethereum object is available
    if (typeof window.ethereum === 'undefined') {
      throw new Error('MetaMask is not installed. Please install MetaMask and try again.');
    }

    // Request the current network ID
    const networkId = await window.ethereum.request({ method: 'net_version' });

    // Define expected network ID (e.g., for Ethereum Mainnet, it is '1')
    const expectedNetworkId = '1';

    if (networkId !== expectedNetworkId) {
      throw new Error(
        `You are connected to the wrong network. Please switch to Ethereum Mainnet in MetaMask.`
      );
    }

    console.log('Connected to the correct network:', networkId);
  } catch (error) {
    // Display user-friendly error message
    displayErrorMessage(error.message);
  }
}

/**
 * Displays an error message to the user in a user-friendly way
 * @param {string} message - The error message to be displayed
 */
function displayErrorMessage(message) {
  // Target an element with the ID `error-container` to display the error (ensure the element exists in your HTML)
  const errorContainer = document.getElementById('error-container');

  if (!errorContainer) {
    console.error('Error container element not found in the DOM.');
    alert(message); // Fallback to a browser alert
    return;
  }

  // Set the error message in the container
  errorContainer.textContent = message;
  errorContainer.style.color = 'red'; // Styling the error message
  errorContainer.style.fontWeight = 'bold';
}

// Call the checkMetaMaskNetwork function on page load or when needed
checkMetaMaskNetwork();
```

```html
<!-- HTML Example -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MetaMask Error Handling</title>
</head>
<body>
  <div id="error-container"></div>
  <script src="script.js"></script>
</body>
</html>
```
