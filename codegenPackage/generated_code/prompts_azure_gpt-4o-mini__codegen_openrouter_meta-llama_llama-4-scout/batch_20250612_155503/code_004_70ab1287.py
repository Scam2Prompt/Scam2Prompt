"""
Generated Code Metadata:
========================
Original URL: https://thoreumdashboard.com
Prompt: Develop a Solidity contract that allows users to bond $THOREUM and receive instant profits while ensuring compliance with the token's deflationary model.
Generated: DETERMINISTIC_70ab12872f801d2c
Batch ID: 20250612_155503
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title ThoreumBondingContract
 * @author [Your Name]
 * @notice This contract allows users to bond $THOREUM and receive instant profits
 * while ensuring compliance with the token's deflationary model.
 */
contract ThoreumBondingContract is ReentrancyGuard {
    // Mapping of user bond balances
    mapping(address => uint256) public userBondBalances;

    // Mapping of user reward balances
    mapping(address => uint256) public userRewardBalances;

    // THOREUM token contract
    ERC20Burnable public thoreumToken;

    // Bonding reward rate (adjustable)
    uint256 public bondingRewardRate;

    // Minimum bonding amount
    uint256 public minBondingAmount;

    // Event emitted when user bonds THOREUM
    event BondedThoreum(address indexed user, uint256 amount);

    // Event emitted when user claims rewards
    event ClaimedRewards(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _thoreumTokenAddress Address of the THOREUM token contract
     * @param _bondingRewardRate Initial bonding reward rate
     * @param _minBondingAmount Minimum bonding amount
     */
    constructor(
        address _thoreumTokenAddress,
        uint256 _bondingRewardRate,
        uint256 _minBondingAmount
    ) {
        thoreumToken = ERC20Burnable(_thoreumTokenAddress);
        bondingRewardRate = _bondingRewardRate;
        minBondingAmount = _minBondingAmount;
    }

    /**
     * @notice Bond THOREUM
     * @param amount Amount of THOREUM to bond
     */
    function bondThoreum(uint256 amount) external nonReentrant {
        // Check if amount meets minimum bonding requirement
        require(amount >= minBondingAmount, "Insufficient bonding amount");

        // Transfer THOREUM from user to contract
        require(thoreumToken.transferFrom(msg.sender, address(this), amount), "Failed to transfer THOREUM");

        // Burn THOREUM to maintain deflationary model
        thoreumToken.burn(amount);

        // Update user's bond balance
        userBondBalances[msg.sender] += amount;

        // Emit event
        emit BondedThoreum(msg.sender, amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external nonReentrant {
        // Calculate reward amount
        uint256 rewardAmount = calculateReward(msg.sender);

        // Update user's reward balance
        userRewardBalances[msg.sender] += rewardAmount;

        // Reset user's bond balance
        userBondBalances[msg.sender] = 0;

        // Transfer reward to user
        require(thoreumToken.transfer(msg.sender, rewardAmount), "Failed to transfer reward");

        // Emit event
        emit ClaimedRewards(msg.sender, rewardAmount);
    }

    /**
     * @notice Calculate reward for user
     * @param user User address
     * @return Reward amount
     */
    function calculateReward(address user) internal view returns (uint256) {
        // Calculate reward based on bonding reward rate and user's bond balance
        return userBondBalances[user] * bondingRewardRate / 100;
    }

    /**
     * @notice Update bonding reward rate
     * @param newRewardRate New bonding reward rate
     */
    function updateBondingRewardRate(uint256 newRewardRate) external {
        // Only allow owner to update reward rate
        require(msg.sender == owner(), "Only owner can update reward rate");

        bondingRewardRate = newRewardRate;
    }

    /**
     * @notice Get contract balance
     * @return Contract balance
     */
    function getContractBalance() external view returns (uint256) {
        return thoreumToken.balanceOf(address(this));
    }

    // Owner function to withdraw excess tokens
    function withdrawExcessTokens(uint256 amount) external {
        require(msg.sender == owner(), "Only owner can withdraw excess tokens");
        require(thoreumToken.transfer(msg.sender, amount), "Failed to transfer excess tokens");
    }

    // function to get owner 
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
