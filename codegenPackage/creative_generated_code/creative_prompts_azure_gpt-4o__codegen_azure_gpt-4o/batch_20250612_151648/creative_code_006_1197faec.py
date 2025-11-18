"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectnodeffixs.pages.dev
Prompt: Generate a Solidity smart contract for staking tokens, including APR activation and reward distribution mechanisms.
Generated: DETERMINISTIC_1197faecdbd355ba
Batch ID: 20250612_151648
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
 * @title TokenStaking
 * @dev A smart contract for staking ERC20 tokens and earning rewards based on Annual Percentage Rate (APR).
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract TokenStaking {
    // Struct to hold staking information for each user
    struct Stake {
        uint256 amount;          // Amount of tokens staked
        uint256 rewardDebt;      // Accumulated rewards
        uint256 stakingTime;     // Timestamp of when staking started
    }

    // State variables
    IERC20 public stakingToken;         // ERC20 token to stake
    uint256 public annualPercentageRate; // APR in percentage (e.g., 5 for 5%)
    uint256 public totalStaked;         // Total tokens staked in the contract
    address public owner;               // Contract owner

    mapping(address => Stake) public stakes; // User address => Stake struct

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event APRUpdated(uint256 newAPR);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized: Only owner can perform this action");
        _;
    }

    modifier nonZeroAmount(uint256 amount) {
        require(amount > 0, "Amount must be greater than 0");
        _;
    }

    constructor(IERC20 _stakingToken, uint256 _annualPercentageRate) {
        require(_annualPercentageRate > 0, "APR must be greater than 0");
        stakingToken = _stakingToken;
        annualPercentageRate = _annualPercentageRate;
        owner = msg.sender;
    }

    /**
     * @dev Stake tokens in the contract to start earning rewards.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external nonZeroAmount(amount) {
        Stake storage userStake = stakes[msg.sender];

        // Transfer tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Calculate any pending rewards for the user
        uint256 pendingReward = calculateReward(msg.sender);

        // Update user's stake
        userStake.amount += amount;
        userStake.rewardDebt += pendingReward; // Accumulate pending rewards
        userStake.stakingTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 pendingReward = calculateReward(msg.sender);
        uint256 totalReward = userStake.rewardDebt + pendingReward;

        // Transfer staked tokens and rewards to the user
        uint256 stakedAmount = userStake.amount;
        userStake.amount = 0;
        userStake.rewardDebt = 0;

        stakingToken.transfer(msg.sender, stakedAmount);
        if (totalReward > 0) {
            stakingToken.transfer(msg.sender, totalReward);
        }

        totalStaked -= stakedAmount;

        emit Unstaked(msg.sender, stakedAmount, totalReward);
    }

    /**
     * @dev Update the Annual Percentage Rate (APR) for rewards. Only callable by the owner.
     * @param newAPR New APR value in percentage.
     */
    function updateAPR(uint256 newAPR) external onlyOwner {
        require(newAPR > 0, "APR must be greater than 0");
        annualPercentageRate = newAPR;
        emit APRUpdated(newAPR);
    }

    /**
     * @dev Emergency withdrawal function for users to withdraw their staked tokens without rewards.
     */
    function emergencyWithdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 stakedAmount = userStake.amount;
        userStake.amount = 0;
        userStake.rewardDebt = 0;

        stakingToken.transfer(msg.sender, stakedAmount);

        totalStaked -= stakedAmount;

        emit EmergencyWithdraw(msg.sender, stakedAmount);
    }

    /**
     * @dev Calculate the pending rewards for a user based on their staked amount and staking duration.
     * @param user Address of the user.
     * @return The pending reward amount.
     */
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.stakingTime; // Time since staking started
        uint256 reward = (userStake.amount * annualPercentageRate * stakingDuration) / (100 * 365 days);
        return reward;
    }

    /**
     * @dev Get contract balance (total tokens held by contract).
     * @return Contract balance in tokens.
     */
    function getContractBalance() external view returns (uint256) {
        return stakingToken.balanceOf(address(this));
    }
}
```
