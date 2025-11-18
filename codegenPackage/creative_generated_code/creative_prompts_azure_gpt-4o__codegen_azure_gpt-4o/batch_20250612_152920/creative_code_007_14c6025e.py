"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenbursts.com
Prompt: Create a smart contract in Solidity that supports staking for $ETH, $BNB, and $POL, with functionality to calculate rewards based on Tokenbursts' APY values.
Generated: DETERMINISTIC_14c6025e4f0fd563
Batch ID: 20250612_152920
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
 * @title MultiTokenStakingContract
 * @dev A smart contract for staking ETH, BNB, and POL tokens and calculating rewards based on APY values.
 */
contract MultiTokenStakingContract {
    // Struct to store staking details
    struct StakeInfo {
        uint256 amount;       // Amount staked
        uint256 startTime;    // Timestamp when staking started
        bool exists;          // Flag indicating whether the stake exists
    }

    // Constants for APY values (as percentages, e.g., 5 for 5%)
    uint256 public constant APY_ETH = 5;  // APY for ETH
    uint256 public constant APY_BNB = 10; // APY for BNB
    uint256 public constant APY_POL = 15; // APY for POL

    // Mapping to store staking details for each token and user
    mapping(address => mapping(string => StakeInfo)) private stakes;

    // Supported tokens
    string constant TOKEN_ETH = "ETH";
    string constant TOKEN_BNB = "BNB";
    string constant TOKEN_POL = "POL";

    // Events
    event Staked(address indexed user, string token, uint256 amount, uint256 startTime);
    event Unstaked(address indexed user, string token, uint256 amount, uint256 reward);

    // Modifier to validate token type
    modifier validToken(string memory token) {
        require(
            keccak256(abi.encodePacked(token)) == keccak256(abi.encodePacked(TOKEN_ETH)) ||
            keccak256(abi.encodePacked(token)) == keccak256(abi.encodePacked(TOKEN_BNB)) ||
            keccak256(abi.encodePacked(token)) == keccak256(abi.encodePacked(TOKEN_POL)),
            "Unsupported token type"
        );
        _;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param token The token type ("ETH", "BNB", or "POL").
     */
    function stake(string memory token) external payable validToken(token) {
        require(msg.value > 0, "Stake amount must be greater than zero");

        StakeInfo storage stakeInfo = stakes[msg.sender][token];
        require(!stakeInfo.exists, "Already staking this token type");

        stakeInfo.amount = msg.value;
        stakeInfo.startTime = block.timestamp;
        stakeInfo.exists = true;

        emit Staked(msg.sender, token, msg.value, block.timestamp);
    }

    /**
     * @dev Unstake tokens and receive reward.
     * @param token The token type ("ETH", "BNB", or "POL").
     */
    function unstake(string memory token) external validToken(token) {
        StakeInfo storage stakeInfo = stakes[msg.sender][token];
        require(stakeInfo.exists, "No active stake for this token type");

        uint256 stakedAmount = stakeInfo.amount;
        uint256 stakingDuration = block.timestamp - stakeInfo.startTime;
        uint256 reward = calculateReward(token, stakedAmount, stakingDuration);

        // Reset stake info
        stakeInfo.amount = 0;
        stakeInfo.startTime = 0;
        stakeInfo.exists = false;

        uint256 totalAmount = stakedAmount + reward;

        // Send staked amount and reward to user
        (bool success, ) = msg.sender.call{value: totalAmount}("");
        require(success, "Transfer failed");

        emit Unstaked(msg.sender, token, stakedAmount, reward);
    }

    /**
     * @dev Calculate reward based on APY and staking duration.
     * @param token The token type ("ETH", "BNB", or "POL").
     * @param amount The staked amount.
     * @param duration The staking duration in seconds.
     * @return reward The calculated reward.
     */
    function calculateReward(
        string memory token,
        uint256 amount,
        uint256 duration
    ) private pure returns (uint256 reward) {
        uint256 apy;
        if (keccak256(abi.encodePacked(token)) == keccak256(abi.encodePacked(TOKEN_ETH))) {
            apy = APY_ETH;
        } else if (keccak256(abi.encodePacked(token)) == keccak256(abi.encodePacked(TOKEN_BNB))) {
            apy = APY_BNB;
        } else if (keccak256(abi.encodePacked(token)) == keccak256(abi.encodePacked(TOKEN_POL))) {
            apy = APY_POL;
        }

        // APY calculation: (amount * apy * duration) / (100 * seconds_in_a_year)
        uint256 secondsInYear = 365 * 24 * 60 * 60;
        reward = (amount * apy * duration) / (100 * secondsInYear);
    }

    /**
     * @dev Get staking details for a user and token type.
     * @param user The user's address.
     * @param token The token type ("ETH", "BNB", or "POL").
     * @return amount The staked amount.
     * @return startTime The staking start time.
     * @return exists Whether the stake exists.
     */
    function getStakeInfo(address user, string memory token)
        external
        view
        validToken(token)
        returns (uint256 amount, uint256 startTime, bool exists)
    {
        StakeInfo storage stakeInfo = stakes[user][token];
        return (stakeInfo.amount, stakeInfo.startTime, stakeInfo.exists);
    }
}
```
