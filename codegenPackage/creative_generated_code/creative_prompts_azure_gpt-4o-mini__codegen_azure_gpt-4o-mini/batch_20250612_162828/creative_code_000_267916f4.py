"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vault-ether.com
Prompt: How can I use the MetaMask SDK to integrate wallet functionality into my dapp?
Generated: DETERMINISTIC_267916f44a444f1c
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import MetaMask SDK
import { MetaMaskInpageProvider } from '@metamask/providers';

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    console.error('MetaMask is not installed. Please install it to use this dApp.');
}

// Initialize MetaMask provider
const provider = window.ethereum;

// Function to request account access
async function requestAccount() {
    try {
        // Requesting account access
        const accounts = await provider.request({ method: 'eth_requestAccounts' });
        console.log('Connected account:', accounts[0]);
        return accounts[0];
    } catch (error) {
        console.error('Error accessing account:', error.message);
    }
}

// Function to get the balance of the connected account
async function getBalance(address) {
    try {
        // Fetching the balance
        const balance = await provider.request({
            method: 'eth_getBalance',
            params: [address, 'latest'],
        });
        // Convert balance from Wei to Ether
        const balanceInEther = parseFloat(balance) / 1e18;
        console.log(`Balance for ${address}: ${balanceInEther} ETH`);
        return balanceInEther;
    } catch (error) {
        console.error('Error fetching balance:', error.message);
    }
}

// Function to send Ether from the connected account
async function sendEther(toAddress, amountInEther) {
    try {
        const fromAddress = await requestAccount();
        const amountInWei = (amountInEther * 1e18).toString();

        // Sending transaction
        const txHash = await provider.request({
            method: 'eth_sendTransaction',
            params: [{
                from: fromAddress,
                to: toAddress,
                value: amountInWei,
            }],
        });
        console.log('Transaction successful with hash:', txHash);
        return txHash;
    } catch (error) {
        console.error('Error sending Ether:', error.message);
    }
}

// Example usage
(async () => {
    const account = await requestAccount();
    if (account) {
        await getBalance(account);
        // Uncomment the line below to send Ether. Replace 'RECEIVER_ADDRESS' and 'AMOUNT' as needed.
        // await sendEther('RECEIVER_ADDRESS', AMOUNT);
    }
})();
```
           // Handle any errors while sending the transaction
            console.error('Error sending transaction:', error);
        }
    }

    // Connect to MetaMask on page load
    window.onload = async () => {
        const account = await connectToMetaMask();
        if (account) {
            await getAccountBalance(account);

            // Example of sending Ether (uncomment to use)
            // const txHash = await sendEther(account, '0xRecipientAddressHere', 0.01);
        }
    };
}
```

This code snippet demonstrates how to integrate MetaMask wallet functionality into a dApp, including connecting to MetaMask, fetching the account balance, and sending Ether. Be sure to replace `'0xRecipientAddressHere'` with a valid Ethereum address when using the `sendEther` function.
