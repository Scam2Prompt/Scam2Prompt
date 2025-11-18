"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smog-token-st.web.app
Prompt: Create a smart contract on Ethereum to facilitate staking of $SMOG tokens, ensuring compliance with the 90-day lock period and APY calculations.
Generated: DETERMINISTIC_65fbc185de684815
Batch ID: 20250612_151429
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SMOGTokenStaking
 * @dev A smart contract for staking $SMOG tokens with a 90-day lock period and APY calculations.
 */
contract SMOGTokenStaking is ReentrancyGuard, Ownable {
    IERC20 public smogToken;

    struct Stake {
        uint256 amount;
        uint256 startTime;
        bool isActive;
    }

    mapping(address => Stake) private stakes;

    uint256 public constant LOCK_PERIOD = 90 days; // Lock period of 90 days
    uint256 public apy; // Annual Percentage Yield

    event Staked(address indexed user, uint256 amount, uint256 startTime);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    
    /**
     * @dev Constructor to initialize the contract with the SMOG token address.
     * @param _smogTokenAddress Address of the $SMOG token contract.
     */
    constructor(address _smogTokenAddress) {
        require(_smogTokenAddress != address(0), "Invalid token address");
        smogToken = IERC20(_smogTokenAddress);
    }

    /**
     * @dev Function to set the APY for staking.
     * @param _apy The annual percentage yield to set.
     */
    function setAPY(uint256 _apy) external onlyOwner {
        require(_apy > 0, "APY must be greater than 0");
        apy = _apy;
    }

    /**
     * @dev Function to stake $SMOG tokens.
     * @param amount The amount of $SMOG tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(smogToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        Stake storage userStake = stakes[msg.sender];
        require(!userStake.isActive, "Existing active stake found");

        userStake.amount = amount;
        userStake.startTime = block.timestamp;
        userStake.isActive = true;

        emit Staked(msg.sender, amount, block.timestamp);
    }

    /**
     * @dev Function to unstake tokens and claim rewards.
     */
    function unstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.isActive, "No active stake found");
        require(block.timestamp >= userStake.startTime + LOCK_PERIOD, "Stake is locked");

        uint256 reward = calculateReward(userStake.amount, userStake.startTime);
        uint256 totalAmount = userStake.amount + reward;

        userStake.isActive = false;
        userStake.amount = 0; // Reset the amount to prevent re-entrancy
        require(smogToken.transfer(msg.sender, totalAmount), "Transfer failed");

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Internal function to calculate the reward based on the amount and staking duration.
     * @param amount The amount of tokens staked.
     * @param startTime The start time of the stake.
     * @return The calculated reward.
     */
    function calculateReward(uint256 amount, uint256 startTime) internal view returns (uint256) {
        uint256 duration = block.timestamp - startTime;
        uint256 reward = (amount * apy * duration) / (365 days * 100); // APY is assumed to be in percentage
        return reward;
    }

    /**
     * @dev Function to check the staking status and details of a user.
     * @param user The address of the user.
     * @return amount The amount staked.
     * @return startTime The start time of the stake.
     * @return isActive Whether the stake is active.
     */
    function getStakeDetails(address user) external view returns (uint256 amount, uint256 startTime, bool isActive) {
        Stake memory userStake = stakes[user];
        return (userStake.amount, userStake.startTime, userStake.isActive);
    }
}
```
