"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-snap-polkadot.pages.dev
Prompt: Write code to integrate the Polkadot Wallet Snap into a dApp using the example provided on the Metamask Snap Polkadot webpage.
Generated: DETERMINISTIC_b8548f8df2d758e5
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
import detectEthereumProvider from '@metamask/detect-provider';

// Function to connect the Polkadot Snap to a dApp
async function connectPolkadotSnap() {
  try {
    // Detect the MetaMask Ethereum provider
    const provider = await detectEthereumProvider();

    // Ensure the provider exists and is MetaMask
    if (!provider || !provider.isMetaMask) {
      throw new Error('MetaMask is not installed. Please install MetaMask to proceed.');
    }

    // Request for the Polkadot Snap to be enabled using MetaMask's wallet API
    const result = await provider.request({
      method: 'wallet_enable',
      params: [
        {
          wallet_snap: {
            'npm:@chainsafe/metamask-snap-polkadot': {},
          },
        },
      ],
    });

    // Log success message and the result object for debugging purposes
    console.log('Polkadot Snap enabled successfully:', result);

    return result; // Return the result object
  } catch (error) {
    // Handle errors gracefully and log them
    console.error('Error enabling Polkadot Snap:', error.message);
    throw error;
  }
}

// Fetch Polkadot account information from the Snap
async function getPolkadotAccount() {
  try {
    // Detect MetaMask provider
    const provider = await detectEthereumProvider();

    // Ensure the provider exists and is MetaMask
    if (!provider || !provider.isMetaMask) {
      throw new Error('MetaMask is not installed. Please install MetaMask to proceed.');
    }

    // Request account information from the Polkadot Snap
    const response = await provider.request({
      method: 'wallet_invokeSnap',
      params: {
        snapId: 'npm:@chainsafe/metamask-snap-polkadot',
        request: {
          method: 'polkadot_getAccount',
        },
      },
    });

    // Log account information for debugging
    console.log('Polkadot account information:', response);

    return response; // Return the account information
  } catch (error) {
    // Handle errors gracefully and log them
    console.error('Error fetching Polkadot account information:', error.message);
    throw error;
  }
}

// Attach event listeners to buttons in your dApp (example usage)
document.getElementById('connectSnap').addEventListener('click', async () => {
  try {
    // Trigger the connectPolkadotSnap function
    await connectPolkadotSnap();
    alert('Polkadot Snap connected successfully!');
  } catch (error) {
    alert(`Failed to connect Polkadot Snap: ${error.message}`);
  }
});

document.getElementById('getAccount').addEventListener('click', async () => {
  try {
    // Trigger the getPolkadotAccount function
    const account = await getPolkadotAccount();
    alert(`Polkadot Account: ${JSON.stringify(account)}`);
  } catch (error) {
    alert(`Failed to fetch Polkadot account: ${error.message}`);
  }
});
```

Ensure you have the appropriate HTML elements with IDs `connectSnap` and `getAccount` in your dApp, and that the required dependencies (e.g., `@metamask/detect-provider`) are installed and properly configured.
