"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect-test-wallet.pages.dev
Prompt: Generate a JavaScript function to test WalletConnect session establishment using the WalletConnect Test Wallet.
Generated: DETERMINISTIC_6a43abbaa86fadf1
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Establishes a WalletConnect session using the WalletConnect Test Wallet.
 * 
 * @function testWalletConnectSession
 * @returns {Promise<void>} - A promise that resolves when the session is established or an error occurs.
 */
async function testWalletConnectSession() {
    // Check if WalletConnect is available in the window object
    if (typeof window.WalletConnectProvider === 'undefined') {
        console.error('WalletConnectProvider is not available. Please ensure you have included the WalletConnect library.');
        return;
    }
    
    // Create a new WalletConnect provider
    const provider = new window.WalletConnectProvider({
        infuraId: 'YOUR_INFURA_ID', // Replace with your Infura ID or a supported RPC URL
    });

    try {
        // Enable session (triggers QR Code modal)
        await provider.enable();
        console.log('WalletConnect session established successfully!');

        // Retrieve accounts and chain ID
        const accounts = await provider.request({ method: 'eth_accounts' });
        const chainId = await provider.request({ method: 'eth_chainId' });

        console.log(`Connected accounts: ${accounts}`);
        console.log(`Connected chain ID: ${chainId}`);

    } catch (error) {
        // Handle errors that may occur during the session establishment
        console.error('Failed to establish WalletConnect session:', error);
    } finally {
        // Close the provider session if applicable
        if (provider.connected) {
            await provider.disconnect();
            console.log('WalletConnect session disconnected.');
        }
    }
}

// Call the function to test the WalletConnect session
testWalletConnectSession();
```
