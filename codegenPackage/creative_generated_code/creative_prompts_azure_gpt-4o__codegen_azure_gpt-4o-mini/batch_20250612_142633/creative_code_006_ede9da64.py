"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-03.vip
Prompt: Create a smart contract example for a DeFi application on Ethereum that supports staking ETH.
Generated: DETERMINISTIC_ede9da6492549ff8
Batch ID: 20250612_142633
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for a simple ETH staking mechanism
contract EthStaking is Ownable {
    using SafeMath for uint256;

    struct Stake {
        uint256 amount;        // Amount of ETH staked
        uint256 timestamp;     // Time when ETH was staked
    }

    // Mapping to track user stakes
    mapping(address => Stake) private stakes;

    // Event emitted when a user stakes ETH
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    
    // Event emitted when a user unstakes ETH
    event Unstaked(address indexed user, uint256 amount, uint256 timestamp);

    // Modifier to ensure user has staked ETH
    modifier hasStaked() {
        require(stakes[msg.sender].amount > 0, "No stake found for user");
        _;
    }

    // Function to stake ETH
    function stake() external payable {
        require(msg.value > 0, "Cannot stake 0 ETH");
        
        // Update user's stake
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(msg.value);
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, msg.value, block.timestamp);
    }

    // Function to unstake ETH
    function unstake() external hasStaked {
        uint256 amount = stakes[msg.sender].amount;

        // Reset user's stake
        stakes[msg.sender].amount = 0;

        // Transfer staked ETH back to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit Unstaked(msg.sender, amount, block.timestamp);
    }

    // Function to check user's stake
    function getStake(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to withdraw contract balance by owner (for emergency)
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");
        
        // Transfer specified amount to owner
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
