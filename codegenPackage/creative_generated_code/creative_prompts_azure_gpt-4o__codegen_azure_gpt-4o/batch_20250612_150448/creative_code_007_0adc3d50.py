"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testnet-venus-protocol.vercel.app
Prompt: Explain how to integrate Venus Protocol with a decentralized application (dApp) on the BNB Chain and provide code examples.
Generated: DETERMINISTIC_0adc3d50a0866fef
Batch ID: 20250612_150448
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://bsc-dataseed.binance.org": {
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
// Import the required libraries
const Web3 = require('web3');
const Venus = require('@venusprotocol/venus-js'); // Venus SDK for interacting with Venus Protocol

// Set up Web3 instance and connect to the BNB Chain
const web3 = new Web3('https://bsc-dataseed.binance.org'); // BNB Chain Mainnet RPC URL

// Define the wallet address and private key (DO NOT hardcode private keys in production - use secure storage)
const walletAddress = '0xYourWalletAddressHere';
const privateKey = '0xYourPrivateKeyHere';

// Initialize Venus.js with the Web3 provider
const venus = new Venus(web3.currentProvider, { network: 'mainnet' });

// Define an async function to supply assets to Venus Protocol
async function supplyToVenus(assetAddress, amount) {
  try {
    // Approve Venus Protocol contract to spend the tokens
    const tokenContract = new web3.eth.Contract(Venus.abi.ERC20, assetAddress);
    const vTokenAddress = Venus.util.getVTokenAddress(assetAddress, 'bnb');
    const allowance = await tokenContract.methods.allowance(walletAddress, vTokenAddress).call();

    if (allowance < amount) {
      const approveTx = tokenContract.methods.approve(vTokenAddress, amount);
      const gas = await approveTx.estimateGas({ from: walletAddress });
      const data = approveTx.encodeABI();

      const signedTx = await web3.eth.accounts.signTransaction(
        {
          to: assetAddress,
          data,
          gas,
        },
        privateKey
      );

      await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
      console.log('Tokens approved successfully.');
    } else {
      console.log('Tokens already approved.');
    }

    // Supply the asset to Venus
    const supplyTx = venus.supply(assetAddress, amount);
    const gas = await supplyTx.estimateGas({ from: walletAddress });
    const data = supplyTx.encodeABI();

    const signedSupplyTx = await web3.eth.accounts.signTransaction(
      {
        to: vTokenAddress,
        data,
        gas,
      },
      privateKey
    );

    const receipt = await web3.eth.sendSignedTransaction(signedSupplyTx.rawTransaction);
    console.log('Asset supplied successfully:', receipt.transactionHash);
  } catch (error) {
    console.error('Error supplying asset to Venus:', error.message);
  }
}

// Define an async function to borrow assets from Venus Protocol
async function borrowFromVenus(assetAddress, amount) {
  try {
    const vTokenAddress = Venus.util.getVTokenAddress(assetAddress, 'bnb');

    // Borrow the asset from Venus
    const borrowTx = venus.borrow(assetAddress, amount);
    const gas = await borrowTx.estimateGas({ from: walletAddress });
    const data = borrowTx.encodeABI();

    const signedBorrowTx = await web3.eth.accounts.signTransaction(
      {
        to: vTokenAddress,
        data,
        gas,
      },
      privateKey
    );

    const receipt = await web3.eth.sendSignedTransaction(signedBorrowTx.rawTransaction);
    console.log('Asset borrowed successfully:', receipt.transactionHash);
  } catch (error) {
    console.error('Error borrowing asset from Venus:', error.message);
  }
}

// Define an async function to check your supply and borrow balance
async function getAccountBalances() {
  try {
    const balances = await venus.getAccountBalances(walletAddress);
    console.log('Account Balances:', balances);
  } catch (error) {
    console.error('Error fetching account balances:', error.message);
  }
}

// Example usage of the above functions
(async () => {
  const assetAddress = '0xYourAssetContractAddressHere'; // Replace with the token contract address (e.g., BUSD)
  const amount = Web3.utils.toWei('10', 'ether'); // Change the amount as needed

  // Supply assets
  await supplyToVenus(assetAddress, amount);

  // Borrow assets
  await borrowFromVenus(assetAddress, Web3.utils.toWei('5', 'ether'));

  // Check account balances
  await getAccountBalances();
})();
```

**Note**: Replace placeholders (e.g., `0xYourWalletAddressHere`, `0xYourPrivateKeyHere`, `0xYourAssetContractAddressHere`) with actual values before running the code. Do not hardcode sensitive information like private keys in production; use secure storage solutions instead.
