"""
Generated Code Metadata:
========================
Original URL: https://hgtrgf45refre.pages.dev
Prompt: Design a cryptocurrency airdrop system, similar to the $LOYAL community airdrop, using a programming language like JavaScript and a blockchain platform like Ethereum.
Generated: DETERMINISTIC_118855a1c72f6d59
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract Airdrop is Ownable, ReentrancyGuard {
    IERC20 public token;
    uint256 public airdropAmount;
    uint256 public airdropEndTime;
    mapping(address => bool) public hasClaimed;

    event AirdropClaimed(address indexed recipient, uint256 amount);

    constructor(
        IERC20 _token,
        uint256 _airdropAmount,
        uint256 _airdropDurationDays
    ) {
        require(address(_token) != address(0), "Invalid token address");
        require(_airdropAmount > 0, "Airdrop amount must be positive");

        token = _token;
        airdropAmount = _airdropAmount;
        airdropEndTime = block.timestamp + (_airdropDurationDays * 1 days);
    }

    function claimAirdrop() external nonReentrant {
        require(block.timestamp <= airdropEndTime, "Airdrop has ended");
        require(!hasClaimed[msg.sender], "Already claimed");
        require(token.balanceOf(address(this)) >= airdropAmount, "Insufficient tokens");

        hasClaimed[msg.sender] = true;
        require(token.transfer(msg.sender, airdropAmount), "Transfer failed");

        emit AirdropClaimed(msg.sender, airdropAmount);
    }

    function extendAirdrop(uint256 additionalDays) external onlyOwner {
        require(additionalDays > 0, "Additional days must be positive");
        airdropEndTime += additionalDays * 1 days;
    }

    function withdrawRemainingTokens() external onlyOwner {
        require(block.timestamp > airdropEndTime, "Airdrop not ended yet");
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(token.transfer(owner(), balance), "Transfer failed");
    }

    function updateAirdropAmount(uint256 newAmount) external onlyOwner {
        require(newAmount > 0, "Amount must be positive");
        airdropAmount = newAmount;
    }
}
```

```javascript
// Frontend interaction code using ethers.js
const { ethers } = require("ethers");

class AirdropService {
  constructor(contractAddress, provider, signer) {
    this.contract = new ethers.Contract(
      contractAddress,
      [
        "function claimAirdrop() external",
        "function hasClaimed(address) external view returns(bool)",
        "function airdropEndTime() external view returns(uint256)",
        "function airdropAmount() external view returns(uint256)",
        "event AirdropClaimed(address indexed recipient, uint256 amount)",
      ],
      signer
    );
    this.provider = provider;
    this.signer = signer;
  }

  async checkEligibility(userAddress) {
    try {
      const hasClaimed = await this.contract.hasClaimed(userAddress);
      const endTime = await this.contract.airdropEndTime();
      const currentTime = Math.floor(Date.now() / 1000);
      return {
        eligible: !hasClaimed && currentTime <= endTime,
        hasClaimed,
        isActive: currentTime <= endTime,
      };
    } catch (error) {
      console.error("Error checking eligibility:", error);
      throw error;
    }
  }

  async claimAirdrop() {
    try {
      const tx = await this.contract.claimAirdrop();
      await tx.wait();
      return tx.hash;
    } catch (error) {
      console.error("Error claiming airdrop:", error);
      throw error;
    }
  }

  async getAirdropDetails() {
    try {
      const amount = await this.contract.airdropAmount();
      const endTime = await this.contract.airdropEndTime();
      return {
        amount: ethers.utils.formatUnits(amount, 18), // Assuming 18 decimals
        endTime: new Date(endTime * 1000).toLocaleString(),
      };
    } catch (error) {
      console.error("Error getting airdrop details:", error);
      throw error;
    }
  }
}

// Example usage:
// const provider = new ethers.providers.Web3Provider(window.ethereum);
// const signer = provider.getSigner();
// const airdropService = new AirdropService(contractAddress, provider, signer);
```
