"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oooooo-money.pages.dev
Prompt: Provide an example of a smart contract that could be used for a treasure-hunting game involving wallet integration and reward distribution.
Generated: DETERMINISTIC_efd549f0d4f38bf8
Batch ID: 20250612_152527
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

// TreasureHunt is a smart contract for a treasure-hunting game
contract TreasureHunt is Ownable {
    // Mapping to track treasures and their status
    struct Treasure {
        string description;
        uint256 rewardAmount;
        address owner;
        bool claimed;
    }

    // Array to store all treasures
    Treasure[] public treasures;

    // Event emitted when a new treasure is created
    event TreasureCreated(uint256 indexed treasureId, string description, uint256 rewardAmount);

    // Event emitted when a treasure is claimed
    event TreasureClaimed(uint256 indexed treasureId, address indexed claimant, uint256 rewardAmount);

    // ERC20 token used for rewards
    IERC20 public rewardToken;

    // Constructor to set the reward token address
    constructor(address _rewardToken) {
        // Ensure the reward token address is valid
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }

    // Create a new treasure
    function createTreasure(string calldata _description, uint256 _rewardAmount) external onlyOwner {
        // Ensure the reward amount is greater than zero
        require(_rewardAmount > 0, "Reward amount must be greater than zero");

        // Create new treasure
        treasures.push(Treasure({
            description: _description,
            rewardAmount: _rewardAmount,
            owner: msg.sender,
            claimed: false
        }));

        emit TreasureCreated(treasures.length - 1, _description, _rewardAmount);
    }

    // Claim a treasure by providing the ID
    function claimTreasure(uint256 _treasureId) external {
        // Ensure the treasure ID is valid
        require(_treasureId < treasures.length, "Invalid treasure ID");

        Treasure storage treasure = treasures[_treasureId];

        // Ensure the treasure has not been claimed and caller is not the owner
        require(!treasure.claimed, "Treasure already claimed");
        require(msg.sender != treasure.owner, "Owner cannot claim their own treasure");

        // Mark treasure as claimed
        treasure.claimed = true;

        // Transfer the reward to the claimant
        require(rewardToken.transfer(msg.sender, treasure.rewardAmount), "Transfer failed");

        emit TreasureClaimed(_treasureId, msg.sender, treasure.rewardAmount);
    }

    // Withdraw remaining tokens from the contract (only owner)
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= _amount, "Insufficient balance");

        // Transfer the tokens to the owner
        require(rewardToken.transfer(msg.sender, _amount), "Transfer failed");
    }
}
```
