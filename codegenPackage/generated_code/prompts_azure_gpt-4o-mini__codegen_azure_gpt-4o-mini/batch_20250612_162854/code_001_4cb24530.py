"""
Generated Code Metadata:
========================
Original URL: https://moxie.community
Prompt: Write a smart contract that integrates with the Moxie Protocol to automate shared payouts for rewards earned on Farcaster.
Generated: DETERMINISTIC_4cb24530a6957c39
Batch ID: 20250612_162854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Smart contract for automating shared payouts using Moxie Protocol
contract SharedPayouts is Ownable {
    // Event to log payouts
    event Payout(address indexed recipient, uint256 amount);

    // Mapping to track rewards for each user
    mapping(address => uint256) public rewards;

    // Address of the Moxie Protocol token
    IERC20 public moxieToken;

    // Constructor to initialize the contract with the Moxie token address
    constructor(address _moxieToken) {
        require(_moxieToken != address(0), "Invalid token address");
        moxieToken = IERC20(_moxieToken);
    }

    // Function to add rewards for a user
    function addReward(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than zero");

        rewards[user] += amount;
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 amount = rewards[msg.sender];
        require(amount > 0, "No rewards to claim");

        // Reset the user's reward balance before transferring tokens to prevent re-entrancy
        rewards[msg.sender] = 0;

        // Transfer the rewards to the user
        bool success = moxieToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit Payout(msg.sender, amount);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(moxieToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        bool success = moxieToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }

    // Function to check the contract's balance of Moxie tokens
    function getContractBalance() external view returns (uint256) {
        return moxieToken.balanceOf(address(this));
    }
}
```
