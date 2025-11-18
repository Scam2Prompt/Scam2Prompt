"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-etftoken.web.app
Prompt: Create a JavaScript function to connect a crypto wallet and purchase BTCETF tokens during presale using ETH or BNB, as described on the Bitcoin ETF Token site.
Generated: DETERMINISTIC_388c08e61c612250
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Connects a crypto wallet and facilitates the purchase of BTCETF tokens during presale using ETH or BNB.
 * Assumes web3.js and a modern web browser are available.
 */

async function connectWalletAndPurchase(presaleContractAddress, amount, currency) {
    // Check if the user has a web3 provider (like MetaMask)
    if (typeof window.ethereum === 'undefined') {
        throw new Error('No web3 provider found. Please install MetaMask or another wallet provider.');
    }

    // Create a Web3 instance
    const web3 = new Web3(window.ethereum);

    try {
        // Request account access
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        const accounts = await web3.eth.getAccounts();
        
        // Set the user's account
        const userAccount = accounts[0];
        
        // Ensure currency is either ETH or BNB
        if (currency !== 'ETH' && currency !== 'BNB') {
            throw new Error('Invalid currency. Please use ETH or BNB to purchase BTCETF tokens.');
        }

        // Create the contract instance
        const contract = new web3.eth.Contract(presaleABI, presaleContractAddress);

        // Check the amount to be sent
        const value = web3.utils.toWei(amount.toString(), 'ether');

        // Send the transaction
        const transaction = await contract.methods.purchaseTokens().send({
            from: userAccount,
            value: currency === 'ETH' ? value : '0', // set value to zero if using BNB
            gas: 3000000 // set an appropriate gas limit
        });

        console.log('Transaction successful:', transaction);
    } catch (error) {
        // Handle any errors that occurred during the transaction
        console.error('Transaction failed:', error);
        throw new Error('Transaction failed. Check console for details.');
    }
}

// Example usage:
// connectWalletAndPurchase('0xYourPresaleContractAddress', 1, 'ETH');
```

> Note: Replace `presaleABI` with the actual ABI of the presale contract and ensure you handle the BNB purchase logic accordingly, as this example primarily focuses on ETH transactions. Adjust the contract method `purchaseTokens` to match the actual method name in your contract.
