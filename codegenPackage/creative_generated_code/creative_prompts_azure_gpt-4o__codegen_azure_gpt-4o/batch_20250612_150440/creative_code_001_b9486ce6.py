"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-snap-polkadot.pages.dev
Prompt: How can I enable JavaScript to interact with the Polkadot Wallet Snap in a dApp as described on the Metamask Snap Polkadot page?
Generated: DETERMINISTIC_b9486ce6e3a2f8f1
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript code to interact with the Polkadot Wallet Snap in a dApp.
// This assumes that MetaMask is installed and the Polkadot Snap is already set up.
// Ensure that the dApp is running in a secure context (HTTPS) for MetaMask Snap compatibility.

/**
 * Initialize the Polkadot Snap in MetaMask.
 * Prompts the user to install the Polkadot Snap if not already installed.
 */
async function enablePolkadotSnap() {
  try {
    // Request the installation and enablement of the Polkadot Snap
    const response = await window.ethereum.request({
      method: 'wallet_enable',
      params: [
        {
          wallet_snap: {
            'npm:@chainsafe/metamask-polkadot-snap': {}, // Polkadot Snap identifier
          },
        },
      ],
    });

    console.log('Polkadot Snap enabled:', response);
    return response;
  } catch (error) {
    console.error('Error enabling Polkadot Snap:', error);
    throw new Error('Failed to enable the Polkadot Snap. Ensure MetaMask and the Snap are installed.');
  }
}

/**
 * Get the current Polkadot Snap configuration.
 */
async function getPolkadotSnapConfig() {
  try {
    const config = await window.ethereum.request({
      method: 'wallet_invokeSnap',
      params: [
        'npm:@chainsafe/metamask-polkadot-snap', // Polkadot Snap identifier
        { method: 'getConfiguration' },
      ],
    });

    console.log('Polkadot Snap configuration:', config);
    return config;
  } catch (error) {
    console.error('Error retrieving Polkadot Snap configuration:', error);
    throw new Error('Failed to retrieve Polkadot Snap configuration.');
  }
}

/**
 * Get the current Polkadot account from the Snap.
 */
async function getPolkadotAccount() {
  try {
    const account = await window.ethereum.request({
      method: 'wallet_invokeSnap',
      params: [
        'npm:@chainsafe/metamask-polkadot-snap', // Polkadot Snap identifier
        { method: 'getAccount' },
      ],
    });

    console.log('Polkadot account:', account);
    return account;
  } catch (error) {
    console.error('Error retrieving Polkadot account:', error);
    throw new Error('Failed to retrieve Polkadot account.');
  }
}

/**
 * Example usage of the above functions.
 * This can be triggered on a button click or some other user interaction.
 */
async function initializePolkadotWallet() {
  try {
    console.log('Initializing Polkadot Snap...');
    await enablePolkadotSnap();

    console.log('Fetching Polkadot Snap configuration...');
    const config = await getPolkadotSnapConfig();
    console.log('Snap Config:', config);

    console.log('Fetching Polkadot account...');
    const account = await getPolkadotAccount();
    console.log('Polkadot Account:', account);
  } catch (error) {
    console.error('Error initializing Polkadot wallet:', error);
  }
}

// Example: Call the initialization function upon page load or button click
// initializePolkadotWallet();
```

This code adheres to the best practices for interacting with MetaMask Snaps and includes proper error handling. Ensure that you integrate this with a proper UI in your dApp for a seamless user experience.
