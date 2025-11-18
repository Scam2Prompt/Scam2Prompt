"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.social
Prompt: Write a smart contract using the Moxie Protocol to create a Fan Token for a Farcaster channel, including programmatic rewards for followers' actions.
Generated: DETERMINISTIC_15bf37b6c864aa17
Batch ID: 20250612_150715
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the Moxie Protocol
interface IMoxieProtocol {
    function rewardUser(address user, uint256 amount) external;
}

// FanToken contract for a Farcaster channel
contract FanToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Moxie Protocol address for rewards
    IMoxieProtocol public moxieProtocol;

    // Mapping to track user actions and their rewards
    mapping(address => uint256) public userActions;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the token and Moxie Protocol
    constructor(string memory name, string memory symbol, address _moxieProtocol)
        ERC20(name, symbol)
    {
        require(_moxieProtocol != address(0), "Moxie Protocol address cannot be zero");
        moxieProtocol = IMoxieProtocol(_moxieProtocol);
    }

    // Function to mint tokens to a user's account
    function mintTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to zero address");
        require(amount > 0, "Amount must be greater than zero");

        _mint(to, amount);
    }

    // Function to record user actions and reward them
    function recordUserAction(address user, uint256 actionValue) external onlyOwner {
        require(user != address(0), "Cannot record action for zero address");
        require(actionValue > 0, "Action value must be greater than zero");

        // Update user actions
        userActions[user] = userActions[user].add(actionValue);

        // Calculate and distribute rewards based on the action value
        uint256 rewardAmount = calculateReward(actionValue);
        moxieProtocol.rewardUser(user, rewardAmount);

        emit RewardsDistributed(user, rewardAmount);
    }

    // Internal function to calculate rewards based on action value
    function calculateReward(uint256 actionValue) internal pure returns (uint256) {
        // For simplicity, let's say the reward is 10% of the action value
        return actionValue.mul(10).div(100);
    }

    // Function to withdraw tokens sent to this contract by mistake
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Cannot withdraw from zero address");
        require(amount > 0, "Amount must be greater than zero");

        // transfer tokens to the owner
        ERC20(token).transfer(owner(), amount);
    }
}
```
