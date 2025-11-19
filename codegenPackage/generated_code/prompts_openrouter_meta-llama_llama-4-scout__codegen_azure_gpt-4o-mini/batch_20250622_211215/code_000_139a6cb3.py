"""
Generated Code Metadata:
========================
Original URL: https://moxie.community
Prompt: Write a smart contract for a Fan Token on the Moxie Protocol that enables programmatic rewards for Farcaster members and channels.
Generated: DETERMINISTIC_139a6cb3f58f2d14
Batch ID: 20250622_211215
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

// Importing OpenZeppelin's ERC20 implementation for token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for a Fan Token on the Moxie Protocol
contract FanToken is ERC20, Ownable {
    // Mapping to track rewards for each Farcaster member
    mapping(address => uint256) private _rewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed member, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("FanToken", "FAN") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to distribute rewards to a Farcaster member
    function distributeRewards(address member, uint256 amount) external onlyOwner {
        require(member != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");

        // Update the rewards mapping
        _rewards[member] += amount;

        // Emit an event for the reward distribution
        emit RewardsDistributed(member, amount);
    }

    // Function to claim rewards by a Farcaster member
    function claimRewards() external {
        uint256 rewardAmount = _rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the rewards for the member
        _rewards[msg.sender] = 0;

        // Transfer the reward amount to the member
        _transfer(owner(), msg.sender, rewardAmount);
    }

    // Function to check the rewards of a Farcaster member
    function checkRewards(address member) external view returns (uint256) {
        return _rewards[member];
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens from the contract to the owner
        _transfer(address(this), msg.sender, amount);
    }
}
```
