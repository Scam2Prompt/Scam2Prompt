"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe20-vip.web.app
Prompt: Develop a function in Solidity to handle token purchases and integrate it with a frontend wallet connection system.
Generated: DETERMINISTIC_b82dcd7577fb54bc
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract TokenSale {
    // Address of the ERC20 token being sold
    address public tokenAddress;
    // Owner of the contract
    address public owner;
    // Price of one token in wei (1 token = X wei)
    uint256 public tokenPrice;
    // Event triggered on token purchase
    event TokenPurchase(address indexed buyer, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    constructor(address _tokenAddress, uint256 _tokenPrice) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenPrice > 0, "Token price must be greater than zero");

        tokenAddress = _tokenAddress;
        tokenPrice = _tokenPrice;
        owner = msg.sender;
    }

    // Function to buy tokens
    function buyTokens(uint256 tokenAmount) external payable {
        // Calculate total cost
        uint256 totalCost = tokenAmount * tokenPrice;

        // Ensure the user sent enough ETH
        require(msg.value >= totalCost, "Insufficient ETH sent");

        // Ensure the contract has enough tokens to sell
        uint256 contractBalance = IERC20(tokenAddress).balanceOf(address(this));
        require(contractBalance >= tokenAmount, "Not enough tokens available");

        // Transfer tokens to the buyer
        bool success = IERC20(tokenAddress).transfer(msg.sender, tokenAmount);
        require(success, "Token transfer failed");

        // Refund excess ETH if sent more than required
        uint256 excess = msg.value - totalCost;
        if (excess > 0) {
            (bool refundSuccess, ) = msg.sender.call{value: excess}("");
            require(refundSuccess, "Refund failed");
        }

        // Emit the purchase event
        emit TokenPurchase(msg.sender, tokenAmount);
    }

    // Owner can withdraw ETH accumulated in the contract
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    // Owner can set a new token price
    function setTokenPrice(uint256 _tokenPrice) external onlyOwner {
        require(_tokenPrice > 0, "Token price must be greater than zero");
        tokenPrice = _tokenPrice;
    }

    // Fallback function to prevent sending ETH directly to the contract
    fallback() external payable {
        revert("Direct ETH transfers not allowed");
    }

    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```

Frontend (JavaScript/React):

```javascript
import React, { useState } from 'react';
import Web3 from 'web3';

const TokenSale = ({ contractAddress, abi }) => {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState(null);
  const [tokenAmount, setTokenAmount] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  
  const connectWallet = async () => {
    try {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        const accounts = await web3Instance.eth.getAccounts();
        setWeb3(web3Instance);
        setAccount(accounts[0]);
      } else {
        setError("Metamask not detected");
      }
    } catch (err) {
      setError("Failed to connect wallet");
    }
  };

  const buyTokens = async () => {
    try {
      if (!web3 || !account) {
        setError("Connect your wallet first");
        return;
      }

      const contract = new web3.eth.Contract(abi, contractAddress);
      const tokenPrice = await contract.methods.tokenPrice().call();
      const totalCost = tokenAmount * tokenPrice;

      await contract.methods.buyTokens(tokenAmount).send({
        from: account,
        value: totalCost,
      });

      setSuccess(`Successfully purchased ${tokenAmount} tokens`);
    } catch (err) {
      setError("Failed to purchase tokens");
    }
  };

  return (
    <div>
      <button onClick={connectWallet}>Connect Wallet</button>
      <div>
        <input
          type="number"
          value={tokenAmount}
          onChange={(e) => setTokenAmount(e.target.value)}
          placeholder="Enter token amount"
        />
        <button onClick={buyTokens}>Buy Tokens</button>
      </div>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {success && <p style={{ color: 'green' }}>{success}</p>}
    </div>
  );
};

export default TokenSale;
```
