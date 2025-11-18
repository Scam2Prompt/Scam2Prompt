"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smog-tokens-en.pages.dev
Prompt: Write a Solidity smart contract to manage the staking of $SMOG tokens on Ethereum, ensuring tokens are locked for 90 days and APY rewards are distributed.
Generated: DETERMINISTIC_b387767c8f20bcfe
Batch ID: 20250612_152656
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
 * @title SMOGTokenStaking
 * @dev A smart contract for staking $SMOG tokens, locking them for 90 days, and distributing APY rewards.
 */
contract SMOGTokenStaking {
    // ERC20 interface for interacting with $SMOG tokens
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
    }

    // State variables
    IERC20 public smogToken; // Reference to the $SMOG token contract
    uint256 public apy = 15; // APY in percentage (e.g., 15%)
    uint256 public lockDuration = 90 days; // Lock duration in seconds

    // Struct to store staking information
    struct Stake {
        uint256 amount;       // Amount of staked tokens
        uint256 startTime;    // Timestamp when tokens were staked
        bool claimed;         // Whether rewards have been claimed
    }

    // Mapping to track stakes per user
    mapping(address => Stake) public stakes;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract with the $SMOG token address.
     * @param _smogToken Address of the $SMOG token contract.
     */
    constructor(IERC20 _smogToken) {
        smogToken = _smogToken;
    }

    /**
     * @dev Function to stake tokens for 90 days.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender].amount == 0, "Already staking");

        // Transfer tokens from the user to the contract
        bool success = smogToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Record the stake
        stakes[msg.sender] = Stake({
            amount: _amount,
            startTime: block.timestamp,
            claimed: false
        });

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to claim staking rewards after the lock duration.
     */
    function claim() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake");
        require(!userStake.claimed, "Rewards already claimed");

        // Check if the lock duration has passed
        require(block.timestamp >= userStake.startTime + lockDuration, "Lock period not yet complete");

        // Calculate rewards based on APY formula
        uint256 reward = (userStake.amount * apy * lockDuration) / (365 days * 100);

        // Mark as claimed
        userStake.claimed = true;

        // Transfer staked amount and rewards back to the user
        bool principalSuccess = smogToken.transfer(msg.sender, userStake.amount);
        require(principalSuccess, "Token transfer failed");

        bool rewardSuccess = smogToken.transfer(msg.sender, reward);
        require(rewardSuccess, "Reward transfer failed");

        emit Claimed(msg.sender, reward);
    }

    /**
     * @dev Function to get details of the user's stake.
     * @param _user Address of the user.
     * @return amount Amount of staked tokens.
     * @return startTime Timestamp when staking started.
     * @return claimed Whether rewards have been claimed.
     */
    function getStake(address _user) external view returns (uint256 amount, uint256 startTime, bool claimed) {
        Stake memory userStake = stakes[_user];
        return (userStake.amount, userStake.startTime, userStake.claimed);
    }
}
```
