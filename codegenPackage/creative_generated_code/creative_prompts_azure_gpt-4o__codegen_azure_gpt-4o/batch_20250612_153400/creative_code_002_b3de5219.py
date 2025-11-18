"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-3bb.pages.dev
Prompt: Create a function in Solidity to automate staking $POODL tokens, ensuring compatibility with Ethereum-based smart contracts as described in the Poodl Inu documentation.
Generated: DETERMINISTIC_b3de5219ba654aa7
Batch ID: 20250612_153400
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
 * @title POODL Staking Contract
 * @dev This contract allows users to stake POODL tokens and earn rewards over time.
 * Compatible with Ethereum-based smart contracts.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract PoodlStaking {
    // Address of the POODL token contract
    IERC20 public poodlToken;

    // Struct to track staker details
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping to track stakes by user address
    mapping(address => Stake) public stakes;

    // Reward rate (e.g., 5% annual reward rate, expressed in wei)
    uint256 public rewardRate;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens and claims rewards
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    /**
     * @dev Constructor to initialize the POODL token address and reward rate.
     * @param _poodlToken Address of the POODL token contract.
     * @param _rewardRate Annual reward rate (in wei).
     */
    constructor(IERC20 _poodlToken, uint256 _rewardRate) {
        poodlToken = _poodlToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake POODL tokens.
     * @param amount Amount of POODL tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(poodlToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // If the user has an existing stake, update the stake amount and reset timestamp
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Calculate reward for a staker based on the staking duration and reward rate.
     * @param staker Address of the staker.
     * @return Reward amount in POODL tokens.
     */
    function calculateReward(address staker) public view returns (uint256) {
        Stake storage userStake = stakes[staker];
        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        // Annual reward calculation: (amount * rewardRate * stakingDuration) / (365 days * 100)
        return (userStake.amount * rewardRate * stakingDuration) / (365 days * 100);
    }

    /**
     * @dev Unstake POODL tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 reward = calculateReward(msg.sender);
        uint256 totalAmount = userStake.amount + reward;

        // Reset the user's stake
        userStake.amount = 0;
        userStake.timestamp = 0;

        require(poodlToken.transfer(msg.sender, totalAmount), "Token transfer failed");

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Emergency function to withdraw staked tokens without rewards (admin only).
     * @param recipient Address to send the tokens to.
     */
    function emergencyWithdraw(address recipient) external {
        require(msg.sender == address(this), "Unauthorized"); // Replace with admin-role logic if needed.
        require(poodlToken.transfer(recipient, token.balanceof.requested qantity));
