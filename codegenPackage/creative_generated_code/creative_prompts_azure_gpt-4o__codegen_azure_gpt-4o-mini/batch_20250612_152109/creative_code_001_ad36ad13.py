"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoindogsclub-claim.pages.dev
Prompt: Generate code to automate the claiming process for $0DOG tokens after the presale ends, ensuring the wallet used during the purchase is connected and tokens are added to a BRC20 wallet.
Generated: DETERMINISTIC_ad36ad13be609ef6
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const Web3 = require('web3');
const { abi: tokenAbi } = require('./BRC20Token.json'); // BRC20 Token ABI
const { presaleContractAddress, tokenContractAddress, rpcUrl } = require('./config.json'); // Configuration file

// Initialize web3 with the provided RPC URL
const web3 = new Web3(new Web3.providers.HttpProvider(rpcUrl));

// Function to claim $0DOG tokens after the presale ends
async function claimTokens(walletAddress, privateKey) {
    try {
        // Create an account using the provided private key
        const account = web3.eth.accounts.privateKeyToAccount(privateKey);
        web3.eth.accounts.wallet.add(account);
        web3.eth.defaultAccount = account.address;

        // Check if the wallet is connected and has purchased during the presale
        const presaleContract = new web3.eth.Contract(tokenAbi, presaleContractAddress);
        const hasPurchased = await presaleContract.methods.hasPurchased(walletAddress).call();

        if (!hasPurchased) {
            console.error("This wallet has not participated in the presale.");
            return;
        }

        // Calculate the amount of $0DOG tokens to claim
        const amountToClaim = await presaleContract.methods.calculateClaimable(walletAddress).call();

        if (amountToClaim <= 0) {
            console.log("No tokens available to claim.");
            return;
        }

        // Create transaction to claim tokens
        const transaction = presaleContract.methods.claimTokens(walletAddress);
        const gasEstimate = await transaction.estimateGas({ from: walletAddress });

        const tx = {
            from: walletAddress,
            to: presaleContractAddress,
            gas: gasEstimate,
            data: transaction.encodeABI()
        };

        // Sign and send the transaction
        const receipt = await web3.eth.sendTransaction(tx);
        console.log(`Transaction successful with hash: ${receipt.transactionHash}`);
    } catch (error) {
        console.error("An error occurred during the claiming process:", error);
    }
}

// Example usage
const walletAddress = "0xYourWalletAddress"; // Replace with actual wallet address
const privateKey = "YourPrivateKey"; // Replace with your private key
claimTokens(walletAddress, privateKey);
```

### Notes:
- Ensure that the `BRC20Token.json` file contains the ABI of your token contract and that the `config.json` has the necessary configuration parameters (`presaleContractAddress`, `tokenContractAddress`, and `rpcUrl`).
- Replace `"0xYourWalletAddress"` and `"YourPrivateKey"` with actual wallet address and private key before running the code.
- Always handle private keys securely and avoid hardcoding sensitive information within your code.
