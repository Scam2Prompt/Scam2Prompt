"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dontclickneirotest.pages.dev
Prompt: Develop a Solidity-based smart contract that allows users to claim $NEIRO tokens by verifying their referral links and wallet addresses.
Generated: DETERMINISTIC_669dfa3458f6dcfb
Batch ID: 20250612_151343
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
 * @title ReferralReward
 * @dev A smart contract that allows users to claim $NEIRO tokens by verifying their referral links and wallet addresses.
 */
contract ReferralReward is Ownable {
    IERC20 public neiroToken; // The NEIRO token contract
    mapping(address => bool) public hasClaimed; // Tracks if the user has already claimed
    mapping(address => address) public referrals; // Maps a user to their referrer
    uint256 public rewardAmount; // The amount of NEIRO tokens to be rewarded

    event Claimed(address indexed user, address indexed referrer);

    /**
     * @dev Constructor to set the NEIRO token and reward amount.
     * @param _neiroToken Address of the NEIRO token contract.
     * @param _rewardAmount Amount of tokens to be claimed per referral.
     */
    constructor(IERC20 _neiroToken, uint256 _rewardAmount) {
        neiroToken = _neiroToken;
        rewardAmount = _rewardAmount;
    }

    /**
     * @dev Allows users to claim tokens if they haven't claimed before and if the referrer is valid.
     * @param referrer The address of the user who referred them.
     */
    function claimTokens(address referrer) external {
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        require(referrer != msg.sender, "Referrer cannot be self");
        require(referrer != address(0), "Invalid referrer address");

        // Record the referral
        referrals[msg.sender] = referrer;
        hasClaimed[msg.sender] = true;

        // Transfer NEIRO tokens to the user
        bool success = neiroToken.transfer(msg.sender, rewardAmount);
        require(success, "Token transfer failed");

        emit Claimed(msg.sender, referrer);
    }

    /**
     * @dev Owner function to withdraw tokens from the contract.
     * @param amount Amount of NEIRO tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(neiroToken.balanceOf(address(this)) >= amount, "Insufficient balance in contract");
        bool success = neiroToken.transfer(owner(), amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Update the reward amount, callable only by the owner.
     * @param newRewardAmount New reward amount to be set.
     */
    function updateRewardAmount(uint256 newRewardAmount) external onlyOwner {
        rewardAmount = newRewardAmount;
    }

    /**
     * @dev Function to check if a user has already claimed their tokens.
     * @param user The address of the user to check.
     * @return bool indicating if the user has claimed.
     */
    function hasUserClaimed(address user) external view returns (bool) {
        return hasClaimed[user];
    }

    /**
     * @dev Function to get the referrer of a user.
     * @param user The address of the user to get the referrer for.
     * @return address of the referrer.
     */
    function getReferrer(address user) external view returns (address) {
        return referrals[user];
    }
}
```
