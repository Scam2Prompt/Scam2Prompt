"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyanheroes.pages.dev
Prompt: Create a smart contract example for distributing $NYAN rewards based on mission completion and referral activities in the Nyan Heroes game.
Generated: DETERMINISTIC_e46807800c8c1432
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a clean and production-ready example of a smart contract written in Solidity for the described functionality:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title Reward Distributor for Nyan Heroes Game
/// @author Example Developer
/// @notice This contract handles the distribution of $NYAN rewards for mission completions and referrals.
/// @dev Ensure to configure this contract with the game's governance token address.

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract NyanRewardDistributor {
    // Address of the $NYAN token contract
    IERC20 public nyanToken;
    
    // Owner of the contract
    address public owner;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed to, uint256 missionReward, uint256 referralReward);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    constructor(address _nyanTokenAddress) {
        require(_nyanTokenAddress != address(0), "Invalid token address");
        nyanToken = IERC20(_nyanTokenAddress);
        owner = msg.sender; // Assign the deployer as the owner
    }

    /// @notice Distribute $NYAN rewards for mission completion and referrals
    /// @param recipient Address of the reward recipient
    /// @param missionReward Amount of $NYAN for mission completion
    /// @param referralReward Amount of $NYAN for referrals
    /// @dev Ensure the contract has a sufficient $NYAN balance before calling this function.
    function distributeRewards(address recipient, uint256 missionReward, uint256 referralReward) external onlyOwner {
        require(recipient != address(0), "Invalid recipient");
        require(missionReward > 0 || referralReward > 0, "Rewards must be greater than zero");

        uint256 totalReward = missionReward + referralReward;

        // Ensure the contract has enough $NYAN balance
        require(nyanToken.balanceOf(address(this)) >= totalReward, "Insufficient $NYAN balance");

        // Transfer the rewards
        nyanToken.transfer(recipient, totalReward);

        // Emit an event for reward distribution
        emit RewardsDistributed(recipient, missionReward, referralReward);
    }

    /// @notice Allows the owner to withdraw unused $NYAN tokens from the contract
    /// @param amount Amount of $NYAN to withdraw
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Invalid amount");
        require(nyanToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        nyanToken.transfer(owner, amount);
    }

    /// @notice Allows the owner to update the $NYAN token address if needed
    /// @param _nyanTokenAddress New $NYAN token address
    function updateTokenAddress(address _nyanTokenAddress) external onlyOwner {
        require(_nyanTokenAddress != address(0), "Invalid token address");
        nyanToken = IERC20(_nyanTokenAddress);
    }

    /// @notice Transfers contract ownership to a new address
    /// @param newOwner Address of the new owner
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner");
        owner = newOwner;
    }
}
```

This contract is simple and clean while following best practices. Ensure you deploy the contract with the address of the $NYAN token and fund it with sufficient $NYAN tokens to handle rewards distribution. Adjustments may be needed based on the actual game mechanics or governance rules.
