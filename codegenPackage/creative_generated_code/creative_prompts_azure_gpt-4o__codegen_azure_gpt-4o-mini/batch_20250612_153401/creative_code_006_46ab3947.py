"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plenaclaim.vercel.app
Prompt: Write a smart contract to allocate 2% of the total $PLENA token supply to eligible participants of the airdrop campaign, ensuring fairness and transparency.
Generated: DETERMINISTIC_46ab3947f465338d
Batch ID: 20250612_153401
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

// Importing the OpenZeppelin ERC20 token implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Airdrop contract for $PLENA token
contract PLENAirdrop is Ownable {
    // The ERC20 token contract
    ERC20 public plenToken;

    // Total supply of $PLENA tokens
    uint256 public totalSupply;

    // Total airdrop allocation (2% of total supply)
    uint256 public airdropAmount;

    // Mapping to track whether an address has claimed their airdrop
    mapping(address => bool) public hasClaimed;

    // Event emitted when an airdrop is claimed
    event AirdropClaimed(address indexed participant, uint256 amount);

    // Constructor to initialize the contract
    constructor(address _tokenAddress) {
        plenToken = ERC20(_tokenAddress);
        totalSupply = plenToken.totalSupply();
        airdropAmount = (totalSupply * 2) / 100; // Calculate 2% of total supply
    }

    // Function to airdrop tokens to eligible participants
    function claimAirdrop() external {
        require(!hasClaimed[msg.sender], "Airdrop already claimed");
        require(airdropAmount > 0, "No airdrop tokens left");

        // Mark the participant as having claimed the airdrop
        hasClaimed[msg.sender] = true;

        // Transfer airdrop tokens to the participant
        uint256 amountToTransfer = airdropAmount / (address(this).balance > 0 ? address(this).balance : 1);
        plenToken.transfer(msg.sender, amountToTransfer);
        
        // Emit the event for tracking
        emit AirdropClaimed(msg.sender, amountToTransfer);
    }

    // Function to withdraw any tokens remaining in the contract
    function withdrawTokens() external onlyOwner {
        uint256 balance = plenToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        plenToken.transfer(owner(), balance);
    }

    // Fallback function to accept ETH (if needed)
    receive() external payable {}
}
```
