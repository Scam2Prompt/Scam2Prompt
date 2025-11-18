"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dre-8x7.pages.dev
Prompt: Generate code to implement a tiered presale system where contributors receive different amounts of DRE tokens based on their FTM contributions (e.g., 250, 500, 1000, 2000, 3000 FTM).
Generated: DETERMINISTIC_fe2d046aede10b7f
Batch ID: 20250612_152710
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol"; // Import the ERC20 interface
import "@openzeppelin/contracts/access/Ownable.sol"; // Import the Ownable contract for access control

contract TieredPresale is Ownable {
    IERC20 public dreToken; // DRE token contract
    uint256 public presaleEnd; // Timestamp for presale end
    bool public isPresaleActive; // Indicates if presale is active

    // Mapping to track contributions of each address
    mapping(address => uint256) public contributions;
    
    // Contribution tiers in FTM and corresponding DRE tokens awarded
    uint256[5] public tiers = [250 ether, 500 ether, 1000 ether, 2000 ether, 3000 ether];
    uint256[5] public rewards = [250 * 10**18, 600 * 10**18, 1500 * 10**18, 3200 * 10**18, 7000 * 10**18]; // DRE tokens to reward

    event ContributionReceived(address indexed contributor, uint256 amount);
    event TokensClaimed(address indexed contributor, uint256 amount);

    constructor(address _dreToken, uint256 _presaleDuration) {
        dreToken = IERC20(_dreToken);
        presaleEnd = block.timestamp + _presaleDuration;
        isPresaleActive = true;
    }

    // Function to contribute FTM to the presale
    function contribute() external payable {
        require(isPresaleActive, "Presale is not active");
        require(block.timestamp < presaleEnd, "Presale has ended");
        require(msg.value > 0, "Must send FTM to contribute");

        contributions[msg.sender] += msg.value;
        emit ContributionReceived(msg.sender, msg.value);
    }

    // Function for contributors to claim their DRE tokens based on FTM contributions
    function claimTokens() external {
        require(!isPresaleActive, "Presale is still active");
        require(contributions[msg.sender] > 0, "No contributions to claim tokens for");

        uint256 contribution = contributions[msg.sender];
        uint256 tokenAmount = 0;

        for (uint256 i = 0; i < tiers.length; i++) {
            if (contribution >= tiers[i]) {
                tokenAmount += rewards[i];
            }
        }

        require(tokenAmount > 0, "No tokens to claim");

        // Reset the user's contribution to prevent multiple claims
        contributions[msg.sender] = 0;

        // Transfer DRE tokens to the contributor
        require(dreToken.transfer(msg.sender, tokenAmount), "Token transfer failed");
        emit TokensClaimed(msg.sender, tokenAmount);
    }

    // Function to end the presale
    function endPresale() external onlyOwner {
        require(isPresaleActive, "Presale is not active");
        require(block.timestamp >= presaleEnd, "Presale duration has not yet expired");
        
        isPresaleActive = false;
    }

    // Fallback function to receive FTM contributions
    receive() external payable {
        contribute();
    }
}
```

This Solidity smart contract implements a tiered presale system for distributing DRE tokens based on FTM contributions. It includes access control, contribution tracking, and error handling to ensure safe operations during the presale.
