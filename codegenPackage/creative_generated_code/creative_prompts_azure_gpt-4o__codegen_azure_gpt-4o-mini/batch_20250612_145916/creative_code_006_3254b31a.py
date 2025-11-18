"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-free-ether.pages.dev
Prompt: Develop a step-by-step JavaScript application that interacts with Ethereum wallets to create tokens and manage liquidity pools, replicating the functionality of the "Token-Free Ether" platform.
Generated: DETERMINISTIC_3254b31a6b19a8b0
Batch ID: 20250612_145916
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
// Importing required libraries
const Web3 = require('web3');
const { abi: tokenAbi } = require('./Token.json'); // Assuming the ABI of your token contract is stored in Token.json
const { abi: factoryAbi } = require('./Factory.json'); // Assuming the ABI of your factory contract is stored in Factory.json

// Constants
const INFURA_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID';
const web3 = new Web3(new Web3.providers.HttpProvider(INFURA_URL));

// Your Ethereum wallet address and private key
const walletAddress = 'YOUR_WALLET_ADDRESS';
const privateKey = 'YOUR_PRIVATE_KEY';

// Function to create a new token
async function createToken(name, symbol, totalSupply) {
    try {
        const tokenContract = new web3.eth.Contract(tokenAbi);

        // Creating transaction to deploy the token contract
        const txData = tokenContract.deploy({
            data: tokenContract.deploy().encodeABI(),
            arguments: [name, symbol, totalSupply]
        }).encodeABI();

        const tx = {
            from: walletAddress,
            data: txData,
            gas: 2000000,
            gasPrice: web3.utils.toWei('10', 'gwei'), // Set gas price
            nonce: await web3.eth.getTransactionCount(walletAddress)
        };

        // Sign the transaction
        const signedTx = await web3.eth.accounts.signTransaction(tx, privateKey);
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
        
        console.log('Token created! Transaction receipt:', receipt);
        return receipt.contractAddress; // Return the new token contract address
    } catch (error) {
        console.error('Error creating token:', error);
    }
}

// Function to create a liquidity pool
async function createLiquidityPool(tokenAddress, ethAmount, tokenAmount) {
    try {
        const factoryContract = new web3.eth.Contract(factoryAbi, 'YOUR_FACTORY_CONTRACT_ADDRESS');
        
        const txData = factoryContract.methods.createPool(tokenAddress, ethAmount, tokenAmount).encodeABI();

        const tx = {
            from: walletAddress,
            to: factoryContract.options.address,
            data: txData,
            gas: 2000000,
            gasPrice: web3.utils.toWei('10', 'gwei'),
            value: web3.utils.toWei(ethAmount.toString(), 'ether'), // Send ETH for liquidity
            nonce: await web3.eth.getTransactionCount(walletAddress)
        };

        const signedTx = await web3.eth.accounts.signTransaction(tx, privateKey);
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
        
        console.log('Liquidity pool created! Transaction receipt:', receipt);
    } catch (error) {
        console.error('Error creating liquidity pool:', error);
    }
}

// Example usage
(async () => {
    const tokenAddress = await createToken('MyToken', 'MTK', 1000000);
    if (tokenAddress) {
        await createLiquidityPool(tokenAddress, 1, 1000); // Creating liquidity pool with 1 ETH and 1000 tokens
    }
})();
``` 

### Note:
- Make sure to replace `YOUR_INFURA_PROJECT_ID`, `YOUR_WALLET_ADDRESS`, `YOUR_PRIVATE_KEY`, and `YOUR_FACTORY_CONTRACT_ADDRESS` with actual values.
- The ABI files (Token.json and Factory.json) should contain the compiled contract ABIs for the token and factory contracts, respectively. 
- Ensure that you have the required libraries (`web3`) installed via npm:
    ```bash
    npm install web3
    ```
