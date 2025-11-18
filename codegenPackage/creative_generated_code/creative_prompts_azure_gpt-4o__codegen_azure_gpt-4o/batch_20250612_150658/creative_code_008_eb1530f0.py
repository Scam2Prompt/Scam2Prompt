"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-cellframe.com
Prompt: Provide a code example for building a dapp that allows users to buy, sell, and swap cryptocurrencies via MetaMask.
Generated: DETERMINISTIC_eb1530f02b059099
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is an example of a simple decentralized application (DApp) written in JavaScript and Solidity using MetaMask, Web3.js, and the Ethereum blockchain.

Make sure to install the necessary dependencies (`web3` and `dotenv`) and deploy the Solidity smart contract code on an Ethereum-compatible test network before hooking it to the frontend.

---

### Solidity Smart Contract

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title CryptoSwap
 * @dev A simple smart contract for buying, selling, and swapping cryptocurrencies.
 */
contract CryptoSwap {
    address public owner;

    event Buy(address indexed buyer, uint256 amount);
    event Sell(address indexed seller, uint256 amount);
    event Swap(address indexed user, uint256 amountSent, uint256 amountReceived);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to buy tokens by sending ETH.
     */
    function buy() public payable {
        require(msg.value > 0, "Must send ETH to buy tokens");
        emit Buy(msg.sender, msg.value);
    }

    /**
     * @dev Allows users to sell tokens and receive ETH.
     * @param amount Amount of tokens to sell (for demonstration purposes, no real tokens used)
     */
    function sell(uint256 amount) public {
        require(amount > 0, "Amount must be greater than zero");
        // Transfer ETH equivalent back to the user
        payable(msg.sender).transfer(amount);
        emit Sell(msg.sender, amount);
    }

    /**
     * @dev Allows users to swap between two tokens (for simplicity, no real tokens involved).
     * @param amountSent Amount of source token sent.
     * @param amountReceived Amount of destination token received (mock calculation).
     */
    function swap(uint256 amountSent, uint256 amountReceived) public {
        require(amountSent > 0 && amountReceived > 0, "Invalid swap amounts");
        emit Swap(msg.sender, amountSent, amountReceived);
    }

    /**
     * @dev Fallback function to accept ETH.
     */
    receive() external payable {}

    /**
     * @dev Allows the owner to withdraw contract's ETH balance.
     */
    function withdraw() public onlyOwner {
        payable(owner).transfer(address(this).balance);
    }
}
```

---

### Frontend Code (JavaScript)

```javascript
// Import dependencies and initialize web3
const Web3 = require("web3");
require("dotenv").config();

const CONTRACT_ADDRESS = "YOUR_DEPLOYED_CONTRACT_ADDRESS"; // Replace with your contract address
const CONTRACT_ABI = [ /* ABI from the compiled contract */ ]; // Replace with your contract ABI

// Initialize Web3 instance and connect to MetaMask
const web3 = new Web3(window.ethereum);

// Connect to the deployed smart contract
const contract = new web3.eth.Contract(CONTRACT_ABI, CONTRACT_ADDRESS);

/**
 * Prompts the user to connect their MetaMask wallet.
 */
async function connectWallet() {
  try {
    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
    console.log("Connected account:", accounts[0]);
    return accounts[0];
  } catch (error) {
    console.error("Error connecting wallet:", error);
  }
}

/**
 * Allows users to buy tokens by sending ETH.
 * @param {string} account - The user's MetaMask account.
 * @param {number} amount - Amount of ETH to send (in Wei).
 */
async function buyTokens(account, amount) {
  try {
    await contract.methods.buy().send({
      from: account,
      value: web3.utils.toWei(amount.toString(), "ether"),
    });
    console.log("Tokens purchased successfully!");
  } catch (error) {
    console.error("Error buying tokens:", error);
  }
}

/**
 * Allows users to sell tokens and receive ETH.
 * @param {string} account - The user's MetaMask account.
 * @param {number} tokenAmount - Amount of tokens to sell (mock value).
 */
async function sellTokens(account, tokenAmount) {
  try {
    await contract.methods.sell(web3.utils.toWei(tokenAmount.toString(), "ether")).send({
      from: account,
    });
    console.log("Tokens sold successfully!");
  } catch (error) {
    console.error("Error selling tokens:", error);
  }
}

/**
 * Allows users to swap between two tokens.
 * @param {string} account - The user's MetaMask account.
 * @param {number} amountSent - Amount of source token sent (mock value).
 * @param {number} amountReceived - Amount of destination token received (mock value).
 */
async function swapTokens(account, amountSent, amountReceived) {
  try {
    await contract.methods.swap(
      web3.utils.toWei(amountSent.toString(), "ether"),
      web3.utils.toWei(amountReceived.toString(), "ether")
    ).send({
      from: account,
    });
    console.log("Tokens swapped successfully!");
  } catch (error) {
    console.error("Error swapping tokens:", error);
  }
}

// Event listeners for MetaMask account changes
window.ethereum.on("accountsChanged", (accounts) => {
  console.log("Accounts changed:", accounts);
});

// Example usage (ensure wallet is connected first)
(async () => {
  const account = await connectWallet();
  await buyTokens(account, 0.01); // Buy tokens with 0.01 ETH
  await sellTokens(account, 0.005); // Sell tokens equivalent to 0.005 ETH
  await swapTokens(account, 0.002, 0.001); // Swap tokens
})();
```

---

This code is ready for use, provided you deploy the smart contract and replace placeholders like `CONTRACT_ADDRESS` and `CONTRACT_ABI` in the frontend code. Ensure your MetaMask setup is ready, and test thoroughly in a development environment before deploying to production.
