"""
Generated Code Metadata:
========================
Original URL: https://burnfi.pages.dev
Prompt: Generate a smart contract code snippet in Solidity that handles the burning mechanism and reward distribution for $burn and $build tokens.
Generated: DETERMINISTIC_0a68f52a429baf79
Batch ID: 20250622_205955
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

/**
 * @title BurnAndBuildToken
 * @dev Smart contract to handle burning mechanism and reward distribution for $burn and $build tokens.
 */
contract BurnAndBuildToken {
    // State variables
    address public owner;
    uint256 public burnRate; // Percentage of tokens to burn (e.g., 5 for 5%)
    uint256 public rewardRate; // Percentage of tokens to distribute as rewards (e.g., 10 for 10%)

    mapping(address => uint256) public balances;
    mapping(address => uint256) public rewards;

    event TokensBurned(address indexed from, uint256 amount);
    event RewardsDistributed(address indexed to, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(uint256 _burnRate, uint256 _rewardRate) {
        require(_burnRate + _rewardRate <= 100, "Invalid rates: Total must not exceed 100%");
        owner = msg.sender;
        burnRate = _burnRate;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Function to transfer tokens with burn and reward mechanism.
     * @param to Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     */
    function transfer(address to, uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");

        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 rewardAmount = (amount * rewardRate) / 100;
        uint256 transferAmount = amount - burnAmount - rewardAmount;

        // Burn tokens
        balances[msg.sender] -= amount;
        emit TokensBurned(msg.sender, burnAmount);

        // Distribute rewards
        rewards[to] += rewardAmount;
        emit RewardsDistributed(to, rewardAmount);

        // Transfer remaining tokens
        balances[to] += transferAmount;
    }

    /**
     * @dev Function to mint new tokens (only owner can call this).
     * @param to Address to mint tokens to.
     * @param amount Amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        balances[to] += amount;
    }

    /**
     * @dev Function to update burn and reward rates (only owner can call this).
     * @param _burnRate New burn rate.
     * @param _rewardRate New reward rate.
     */
    function updateRates(uint256 _burnRate, uint256 _rewardRate) external onlyOwner {
        require(_burnRate + _rewardRate <= 100, "Invalid rates: Total must not exceed 100%");
        burnRate = _burnRate;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Function to check balance of an address.
     * @param account Address to check balance for.
     * @return Balance of the given address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Function to check rewards of an address.
     * @param account Address to check rewards for.
     * @return Rewards of the given address.
     */
    function rewardsOf(address account) external view returns (uint256) {
        return rewards[account];
    }
}
```
