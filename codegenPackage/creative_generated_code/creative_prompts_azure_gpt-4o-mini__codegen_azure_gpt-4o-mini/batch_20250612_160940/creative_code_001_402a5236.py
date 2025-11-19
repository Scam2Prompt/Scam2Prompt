"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Write a script using Web3.js to facilitate the purchase of ALIEN tokens during the presale, ensuring the transaction caps at 0.1 ETH increments.
Generated: DETERMINISTIC_402a5236a6a445bc
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const Web3 = require('web3');
const BigNumber = require('bignumber.js');

// Configure the Web3 provider (e.g., Infura, Alchemy, etc.)
const web3 = new Web3(new Web3.providers.HttpProvider('YOUR_INFURA_OR_ALCHEMY_URL'));

// Define contract details
const contractAddress = 'ALIEN_TOKEN_CONTRACT_ADDRESS';
const presaleContractAddress = 'PRESALE_CONTRACT_ADDRESS';
const presaleABI = require('./presaleABI.json'); // Presale contract ABI

// Initialize contract instance
const presaleContract = new web3.eth.Contract(presaleABI, presaleContractAddress);

// Function to purchase ALIEN tokens
async function purchaseAlienTokens(account, privateKey, amountInETH) {
    try {
        // Validate input
        if (!web3.utils.isAddress(account)) {
            throw new Error('Invalid Ethereum address');
        }
        if (amountInETH <= 0 || !Number.isFinite(amountInETH)) {
            throw new Error('Amount must be a positive number');
        }

        // Cap amount at 0.1 ETH increments
        const maxAmountInETH = 0.1;
        const amountInWei = web3.utils.toWei(amountInETH.toString(), 'ether');
        if (new BigNumber(amountInWei).gt(web3.utils.toWei(maxAmountInETH.toString(), 'ether'))) {
            throw new Error(`Amount exceeds the maximum allowable limit of ${maxAmountInETH} ETH`);
        }

        // Create the transaction object
        const transactionObject = {
            to: presaleContractAddress,
            value: amountInWei,
            gas: 200000, // Adjust as necessary
            gasPrice: await web3.eth.getGasPrice(),
            data: presaleContract.methods.buyTokens().encodeABI() // Assuming the method is named buyTokens
        };

        // Sign the transaction
        const signedTransaction = await web3.eth.accounts.signTransaction(transactionObject, privateKey);

        // Send the transaction
        const receipt = await web3.eth.sendSignedTransaction(signedTransaction.rawTransaction);
        console.log('Transaction successful with hash:', receipt.transactionHash);
    } catch (error) {
        console.error('Error purchasing tokens:', error.message);
    }
}

// Example usage
const main = async () => {
    const account = 'YOUR_ETHEREUM_ADDRESS';
    const privateKey = 'YOUR_PRIVATE_KEY';
    const amountInETH = 0.1; // Amount to purchase in ETH

    await purchaseAlienTokens(account, privateKey, amountInETH);
};

main();
```

**Note:** Replace `YOUR_INFURA_OR_ALCHEMY_URL`, `ALIEN_TOKEN_CONTRACT_ADDRESS`, `PRESALE_CONTRACT_ADDRESS`, and `YOUR_PRIVATE_KEY` with actual values. Ensure `presaleABI.json` file contains the appropriate ABI for the presale contract.
