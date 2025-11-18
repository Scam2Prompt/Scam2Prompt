"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify-fundnft-project.pages.dev
Prompt: Create a Solidity smart contract to facilitate token-based interactions between users and developers on the AGIX AI Marketplace, ensuring proportional rewards for contributors.
Generated: DETERMINISTIC_6cf4c5b680751eb4
Batch ID: 20250612_152954
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AGIX Marketplace Contract
 * @dev This contract facilitates token-based interactions between users and developers
 *      on the AGIX AI Marketplace, ensuring proportional rewards for contributors.
 */
contract AGIXMarketplace is Ownable {
    IERC20 public agixToken; // The AGIX token interface

    struct Contribution {
        address contributor;
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping to track contributions by users
    mapping(address => Contribution[]) public contributions;

    // Event to log contributions
    event ContributionReceived(address indexed contributor, uint256 amount, uint256 timestamp);
    event RewardDistributed(address indexed contributor, uint256 rewardAmount, uint256 timestamp);

    /**
     * @dev Constructor to initialize the AGIX token address
     * @param _agixToken Address of the AGIX token contract
     */
    constructor(address _agixToken) {
        require(_agixToken != address(0), "Invalid AGIX token address");
        agixToken = IERC20(_agixToken);
    }

    /**
     * @dev Allows users to contribute tokens to the marketplace
     * @param amount Amount of tokens to contribute
     */
    function contribute(uint256 amount) external {
        require(amount > 0, "Contribution amount must be greater than zero");
        
        // Transfer tokens from the contributor to the contract
        require(agixToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Record the contribution
        contributions[msg.sender].push(Contribution({
            contributor: msg.sender,
            amount: amount,
            timestamp: block.timestamp
        }));

        emit ContributionReceived(msg.sender, amount, block.timestamp);
    }

    /**
     * @dev Distributes rewards to contributors based on their contributions
     * @param contributor Address of the contributor to reward
     * @param rewardAmount Amount of tokens to reward
     */
    function distributeReward(address contributor, uint256 rewardAmount) external onlyOwner {
        require(contributions[contributor].length > 0, "No contributions found for this contributor");
        require(rewardAmount > 0, "Reward amount must be greater than zero");
        require(agixToken.balanceOf(address(this)) >= rewardAmount, "Insufficient balance in contract");

        // Transfer reward tokens to the contributor
        require(agixToken.transfer(contributor, rewardAmount), "Reward transfer failed");

        emit RewardDistributed(contributor, rewardAmount, block.timestamp);
    }

    /**
     * @dev Allows the owner to withdraw excess tokens from the contract
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(agixToken.balanceOf(address(this)) >= amount, "Insufficient balance in contract");

        // Transfer tokens to the owner
        require(agixToken.transfer(msg.sender, amount), "Token transfer failed");
    }

    /**
     * @dev Allows users to view their contributions
     * @param user Address of the user to check contributions for
     * @return array of Contribution structs
     */
    function viewContributions(address user) external view returns (Contribution[] memory) {
        return contributions[user];
    }
}
```
