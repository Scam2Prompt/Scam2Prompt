"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinivi.io
Prompt: Provide a code example for a decentralized application (dApp) that allows users to buy IVI Tokens with various cryptocurrencies.
Generated: DETERMINISTIC_4a1956575b4ee00b
Batch ID: 20250612_155349
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for a decentralized application (dApp) that facilitates the purchase of IVI tokens using various cryptocurrencies. The code is written in Solidity (for the smart contract) and JavaScript (for the frontend interaction).

---

### **Solidity Smart Contract (IVITokenSale.sol)**

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title IVITokenSale
 * @dev A contract that allows users to buy IVI Tokens using Ether or other ERC20 tokens.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract IVITokenSale is Ownable {
    IERC20 public IVIToken;
    address payable public wallet; // Address where funds are collected
    uint256 public rate; // Rate of IVI tokens per Ether or equivalent ERC20 token

    event TokensPurchased(address indexed purchaser, uint256 amount);

    /**
     * @dev Constructor initializes the contract with the IVI token address, wallet, and rate.
     * @param _IVIToken Address of the IVI token contract
     * @param _wallet Address where funds will be collected
     * @param _rate Exchange rate (number of IVI tokens per Ether or ERC20 token unit)
     */
    constructor(IERC20 _IVIToken, address payable _wallet, uint256 _rate) {
        require(address(_IVIToken) != address(0), "Invalid token address");
        require(_wallet != address(0), "Invalid wallet address");
        require(_rate > 0, "Rate should be greater than zero");

        IVIToken = _IVIToken;
        wallet = _wallet;
        rate = _rate;
    }

    /**
     * @dev Function to buy IVI tokens with Ether.
     */
    function buyTokensWithEther() external payable {
        require(msg.value > 0, "Ether value must be greater than zero");

        uint256 tokenAmount = msg.value * rate;

        require(IVIToken.balanceOf(address(this)) >= tokenAmount, "Insufficient tokens in contract");

        IVIToken.transfer(msg.sender, tokenAmount);
        wallet.transfer(msg.value);

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Function to buy IVI tokens using an ERC20 token.
     * @param _paymentToken Address of the ERC20 token used for payment
     * @param _paymentAmount Amount of the ERC20 token sent for payment
     */
    function buyTokensWithERC20(IERC20 _paymentToken, uint256 _paymentAmount) external {
        require(_paymentAmount > 0, "Payment amount must be greater than zero");

        uint256 tokenAmount = _paymentAmount * rate;

        require(IVIToken.balanceOf(address(this)) >= tokenAmount, "Insufficient tokens in contract");

        require(_paymentToken.transferFrom(msg.sender, wallet, _paymentAmount), "Transfer failed");

        IVIToken.transfer(msg.sender, tokenAmount);

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Allows the owner to withdraw unsold IVI tokens.
     * @param _amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(IVIToken.balanceOf(address(this)) >= _amount, "Insufficient tokens");

        IVIToken.transfer(owner(), _amount);
    }
}
```

---

### **Frontend Interaction (JavaScript)**

```javascript
// Import web3 or ethers.js for interaction with Ethereum blockchain
import Web3 from "web3";
import IVITokenSaleABI from "./IVITokenSale.json"; // ABI of the deployed IVITokenSale contract

// Set up web3 provider
const web3 = new Web3(window.ethereum);

// Contract details
const contractAddress = "<DEPLOYED_CONTRACT_ADDRESS>";
const walletAddress = "<WALLET_ADDRESS>";
const IVITokenSale = new web3.eth.Contract(IVITokenSaleABI, contractAddress);

/**
 * @dev Function to buy tokens with Ether.
 * @param etherAmount Amount of Ether to send to contract
 */
async function buyTokensWithEther(etherAmount) {
    try {
        const accounts = await web3.eth.requestAccounts();
        const userAccount = accounts[0];

        const transaction = await IVITokenSale.methods.buyTokensWithEther().send({
            from: userAccount,
            value: web3.utils.toWei(etherAmount, "ether")
        });

        console.log("Transaction successful:", transaction);
    } catch (error) {
        console.error("Error purchasing tokens:", error);
    }
}

/**
 * @dev Function to buy tokens using an ERC20 token.
 * @param tokenAddress Address of the ERC20 token contract
 * @param tokenAmount Amount of ERC20 tokens to send to contract
 */
async function buyTokensWithERC20(tokenAddress, tokenAmount) {
    try {
        const accounts = await web3.eth.requestAccounts();
        const userAccount = accounts[0];

        const ERC20Contract = new web3.eth.Contract(
            IVITokenSaleABI,
            tokenAddress
        );

        await ERC20Contract.methods.approve(contractAddress, tokenAmount).send({
            from: userAccount
        });

        const transaction = await IVITokenSale.methods
            .buyTokensWithERC20(tokenAddress, tokenAmount)
            .send({ from: userAccount });

        console.log("Transaction successful:", transaction);
    } catch (error) {
        console.error("Error purchasing tokens:", error);
    }
}

/**
 * @dev Example usage
 */
// Buy 0.1 Ether worth of IVI tokens
buyTokensWithEther("0.1");

// Buy IVI tokens using 100 units of a hypothetical ERC20 token
buyTokensWithERC20("<ERC20_TOKEN_ADDRESS>", "100");
```

---

Ensure the contract is deployed, and the ABI/contract addresses are configured properly in the frontend before deploying to production.
