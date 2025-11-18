"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-scorpion-casino.pages.dev
Prompt: Write a Solidity smart contract for a token-based affiliate reward system, allowing users to earn rewards for referring others, as described in the $SCORP token use cases.
Generated: DETERMINISTIC_483aa2b40e13c9d9
Batch ID: 20250612_152109
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

/**
 * @title SCORP Affiliate Reward System
 * @dev This contract implements a token-based affiliate reward system for the $SCORP token.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

contract AffiliateRewardSystem {
    // The $SCORP token contract
    IERC20 public token;

    // Maximum referral reward percentage
    uint256 public constant MAX_REWARD_PERCENT = 10;

    // Referral rewards ledger
    mapping(address => uint256) public rewards;

    // Referrer mapping: keeps track of who referred whom
    mapping(address => address) public referrer;

    // Events
    event ReferralAdded(address indexed referrer, address indexed referee);
    event RewardClaimed(address indexed referrer, uint256 rewardAmount);

    /**
     * @dev Constructor to initialize the $SCORP token address.
     * @param tokenAddress Address of the $SCORP token contract.
     */
    constructor(address tokenAddress) {
        require(tokenAddress != address(0), "Invalid token address");
        token = IERC20(tokenAddress);
    }

    /**
     * @dev Allows a user to register a referrer. Referrer must be an existing user.
     * @param _referrer Address of the referrer.
     */
    function addReferrer(address _referrer) external {
        require(_referrer != address(0), "Referrer cannot be zero address");
        require(_referrer != msg.sender, "Cannot refer yourself");
        require(referrer[msg.sender] == address(0), "Referrer already set");

        referrer[msg.sender] = _referrer;
        emit ReferralAdded(_referrer, msg.sender);
    }

    /**
     * @dev Handles token transfers and allocates rewards to referrers.
     * @param sender Address of the token sender.
     * @param recipient Address of the token recipient.
     * @param amount Amount of tokens to transfer.
     */
    function processReferralReward(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool) {
        require(sender != address(0), "Sender cannot be zero address");
        require(recipient != address(0), "Recipient cannot be zero address");
        require(amount > 0, "Amount must be greater than zero");
        require(
            token.transferFrom(sender, recipient, amount),
            "Token transfer failed"
        );

        // Check if the recipient has a referrer
        address _referrer = referrer[recipient];
        if (_referrer != address(0)) {
            // Calculate reward
            uint256 reward = (amount * MAX_REWARD_PERCENT) / 100;

            // Allocate reward to referrer
            rewards[_referrer] += reward;
        }
        return true;
    }

    /**
     * @dev Allows referrers to claim their accumulated rewards.
     */
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards available");

        // Ensure reward can be transferred
        require(
            token.balanceOf(address(this)) >= rewardAmount,
            "Insufficient reward balance in contract"
        );

        rewards[msg.sender] = 0;

        require(token.transfer(msg.sender, rewardAmount), "Reward transfer failed");
        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Fallback function to receive native token (not used in this contract).
     */
    receive() external payable {
        revert("Contract does not accept native tokens");
    }
}
```
