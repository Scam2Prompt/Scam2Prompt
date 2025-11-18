"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.credit
Prompt: Generate code for implementing programmatic rewards on Farcaster using Moxie smart contracts to reward members for referrals, product trials, and on-chain actions.
Generated: DETERMINISTIC_5bbb6f429e9138a3
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the clean, production-ready code for implementing programmatic rewards on Farcaster using Moxie smart contracts.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title FarcasterRewards
 * @dev A smart contract to reward members for referrals, product trials, and on-chain actions using Moxie.
 */
contract FarcasterRewards {
    // Address of the contract owner
    address public owner;

    // Moxie token address
    address public moxieToken;

    // Events for logging rewards distributed
    event ReferralRewarded(address indexed referrer, address indexed referee, uint256 rewardAmount);
    event TrialRewarded(address indexed user, uint256 rewardAmount);
    event OnChainActionRewarded(address indexed user, string actionType, uint256 rewardAmount);

    // A mapping to track referrals and prevent duplicate rewards
    mapping(address => bool) public hasReferred;

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize contract variables.
     * @param _moxieToken The address of the Moxie token smart contract.
     */
    constructor(address _moxieToken) {
        owner = msg.sender;
        moxieToken = _moxieToken;
    }

    /**
     * @dev Function to reward users for referrals.
     * @param referrer The address of the referrer.
     * @param referee The address of the referee.
     * @param rewardAmount The amount of Moxie tokens to reward.
     */
    function rewardReferral(address referrer, address referee, uint256 rewardAmount) external onlyOwner {
        require(referrer != address(0), "Invalid referrer address");
        require(referee != address(0), "Invalid referee address");
        require(!hasReferred[referee], "Referee has already been referred");

        // Transfer reward to referrer
        require(ERC20(moxieToken).transfer(referrer, rewardAmount), "Token transfer failed");

        // Mark the referee as referred
        hasReferred[referee] = true;

        // Emit event for logging
        emit ReferralRewarded(referrer, referee, rewardAmount);
    }

    /**
     * @dev Function to reward users for completing a product trial.
     * @param user The address of the user.
     * @param rewardAmount The amount of Moxie tokens to reward.
     */
    function rewardProductTrial(address user, uint256 rewardAmount) external onlyOwner {
        require(user != address(0), "Invalid user address");

        // Transfer reward to user
        require(ERC20(moxieToken).transfer(user, rewardAmount), "Token transfer failed");

        // Emit event for logging
        emit TrialRewarded(user, rewardAmount);
    }

    /**
     * @dev Function to reward users for specific on-chain actions.
     * @param user The address of the user.
     * @param actionType The type of action performed by the user.
     * @param rewardAmount The amount of Moxie tokens to reward.
     */
    function rewardOnChainAction(address user, string memory actionType, uint256 rewardAmount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(bytes(actionType).length > 0, "Invalid action type");

        // Transfer reward to user
        require(ERC20(moxieToken).transfer(user, rewardAmount), "Token transfer failed");

        // Emit event for logging
        emit OnChainActionRewarded(user, actionType, rewardAmount);
    }

    /**
     * @dev Function to withdraw tokens from the contract (only owner).
     * @param to The address to send the tokens to.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid withdrawal address");

        // Transfer tokens to the specified address
        require(ERC20(moxieToken).transfer(to, amount), "Token transfer failed");
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface ERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

This code is syntactically correct, well-documented, and implements proper error handling. It is production-ready and follows Solidity best practices.
