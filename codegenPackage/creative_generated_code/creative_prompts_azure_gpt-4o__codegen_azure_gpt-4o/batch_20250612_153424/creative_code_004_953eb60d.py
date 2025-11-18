"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orbiterrfinance.github.io
Prompt: Create a step-by-step guide for integrating Orbiter Finance's borrowing and lending functionalities into a decentralized application using Web3.js.
Generated: DETERMINISTIC_953eb60d9a3570d3
Batch ID: 20250612_153424
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

// Step 1: Connect to Ethereum network
// Replace `YOUR_INFURA_URL` with your Infura or other Ethereum node provider URL
const web3 = new Web3('YOUR_INFURA_URL');

// Step 2: Set up wallet and contract details
// Replace with your wallet private key and Orbiter Finance contract address
const PRIVATE_KEY = 'YOUR_PRIVATE_KEY';
const WALLET_ADDRESS = 'YOUR_WALLET_ADDRESS';
const ORBITER_CONTRACT_ADDRESS = 'ORBITER_CONTRACT_ADDRESS';
const ORBITER_ABI = require('./orbiterFinanceABI.json'); // Ensure you have the ABI JSON file

// Step 3: Create contract instance
const orbiterContract = new web3.eth.Contract(ORBITER_ABI, ORBITER_CONTRACT_ADDRESS);

// Step 4: Borrow tokens
async function borrowTokens(amountToBorrow, tokenAddress) {
  try {
    // Convert amount to token's smallest unit (e.g., wei)
    const amountInWei = web3.utils.toWei(amountToBorrow.toString(), 'ether');

    // Prepare transaction data
    const data = orbiterContract.methods.borrow(tokenAddress, amountInWei).encodeABI();

    // Get gas estimate
    const gasEstimate = await web3.eth.estimateGas({
      from: WALLET_ADDRESS,
      to: ORBITER_CONTRACT_ADDRESS,
      data: data,
    });

    // Sign and send transaction
    const signedTx = await web3.eth.accounts.signTransaction(
      {
        to: ORBITER_CONTRACT_ADDRESS,
        data: data,
        gas: gasEstimate,
      },
      PRIVATE_KEY
    );

    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    console.log('Borrow transaction successful:', receipt);
  } catch (error) {
    console.error('Error borrowing tokens:', error);
  }
}

// Step 5: Lend tokens (deposit collateral)
async function lendTokens(amountToLend, tokenAddress) {
  try {
    // Convert amount to token's smallest unit (e.g., wei)
    const amountInWei = web3.utils.toWei(amountToLend.toString(), 'ether');

    // Approve Orbiter contract to spend your tokens
    const tokenContract = new web3.eth.Contract(ERC20_ABI, tokenAddress); // Replace with ERC20 ABI file path
    const approvalData = tokenContract.methods.approve(ORBITER_CONTRACT_ADDRESS, amountInWei).encodeABI();

    const approvalGas = await web3.eth.estimateGas({
      from: WALLET_ADDRESS,
      to: tokenAddress,
      data: approvalData,
    });

    const signedApprovalTx = await web3.eth.accounts.signTransaction(
      {
        to: tokenAddress,
        data: approvalData,
        gas: approvalGas,
      },
      PRIVATE_KEY
    );

    await web3.eth.sendSignedTransaction(signedApprovalTx.rawTransaction);
    console.log('Approval successful');

    // Deposit collateral
    const depositData = orbiterContract.methods.lend(tokenAddress, amountInWei).encodeABI();

    const depositGas = await web3.eth.estimateGas({
      from: WALLET_ADDRESS,
      to: ORBITER_CONTRACT_ADDRESS,
      data: depositData,
    });

    const signedDepositTx = await web3.eth.accounts.signTransaction(
      {
        to: ORBITER_CONTRACT_ADDRESS,
        data: depositData,
        gas: depositGas,
      },
      PRIVATE_KEY
    );

    const receipt = await web3.eth.sendSignedTransaction(signedDepositTx.rawTransaction);
    console.log('Lend transaction successful:', receipt);
  } catch (error) {
    console.error('Error lending tokens:', error);
  }
}

// Step 6: Usage example
(async () => {
  // Replace with actual token address and amounts
  const tokenAddress = 'TOKEN_CONTRACT_ADDRESS';
  const borrowAmount = 1; // Amount in Ether
  const lendAmount = 2; // Amount in Ether

  console.log('Borrowing tokens...');
  await borrowTokens(borrowAmount, tokenAddress);

  console.log('Lending tokens...');
  await lendTokens(lendAmount, tokenAddress);
})();
```

### Notes:
1. Replace placeholders (`YOUR_INFURA_URL`, `YOUR_PRIVATE_KEY`, etc.) with actual values.
2. Ensure the ABI files for Orbiter Finance (`orbiterFinanceABI.json`) and the ERC-20 tokens (`ERC20_ABI.json`) are available and correctly referenced.
3. Test the code in a development environment before deploying to production.
