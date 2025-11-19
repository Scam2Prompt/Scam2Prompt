"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decubate-platform.pages.dev
Prompt: Create a Solidity contract that allows users to stake DCB and earn rewards with compounding interest over 30 days.
Generated: DETERMINISTIC_b7957e173ff1cddb
Batch ID: 20250612_162325
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
 * @title StakingContract
 * @dev This contract allows users to stake DCB tokens and earn rewards with compounding interest.
 * Rewards are calculated and compounded over a 30-day period.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {
    IERC20 public dcbToken;
    address public owner;
    uint256 public constant INTEREST_RATE = 5; // Compounding interest rate (5% per 30 days)
    uint256 public constant COMPOUND_PERIOD = 30 days;

    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 pendingRewards;
    }

    mapping(address => Stake) public stakes;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);
    event RewardsClaimed(address indexed user, uint256 rewards);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can execute this");
        _;
    }

    /**
     * @dev Constructor function to initialize the staking contract.
     * @param _dcbToken Address of the DCB token contract.
     */
    constructor(IERC20 _dcbToken) {
        dcbToken = _dcbToken;
        owner = msg.sender;
    }

    /**
     * @dev Allows a user to stake DCB tokens into the contract.
     * @param _amount Amount of DCB tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(dcbToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        Stake storage userStake = stakes[msg.sender];

        // Compound existing rewards if the user has already staked
        if (userStake.amount > 0) {
            userStake.pendingRewards += calculateRewards(msg.sender);
        }

        userStake.amount += _amount;
        userStake.startTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to unstake their tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens to unstake");

        // Calculate final rewards
        uint256 rewards = calculateRewards(msg.sender) + userStake.pendingRewards;

        uint256 unstakeAmount = userStake.amount;
        userStake.amount = 0;
        userStake.pendingRewards = 0;

        require(dcbToken.transfer(msg.sender, unstakeAmount), "Token transfer failed");
        if (rewards > 0) {
            require(dcbToken.transfer(msg.sender, rewards), "Rewards transfer failed");
        }

        emit Unstaked(msg.sender, unstakeAmount, rewards);
    }

    /**
     * @dev Allows a user to claim their rewards without unstaking.
     */
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake");

        uint256 rewards = calculateRewards(msg.sender) + userStake.pendingRewards;
        require(rewards > 0, "No rewards available");

        userStake.pendingRewards = 0;
        userStake.startTime = block.timestamp;

        require(dcbToken.transfer(msg.sender, rewards), "Rewards transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculates the rewards for a given staker based on the compounding interest formula.
     * @param _staker Address of the staker.
     * @return rewards The calculated rewards.
     */
    function calculateRewards(address _staker) public view returns (uint256 rewards) {
        Stake storage userStake = stakes[_staker];
        if (userStake.amount == 0) return 0;

        uint256 elapsedTime = block.timestamp - userStake.startTime;
        uint256 periods = elapsedTime / COMPOUND_PERIOD;

        rewards = userStake.amount;
        for (uint256 i = 0; i < periods; i++) {
            rewards = rewards + (rewards * INTEREST_RATE) / 100;
        }

        return rewards - userStake.amount;
    }

    /**
     * @dev Emergency function to allow the owner to withdraw all tokens from the contract.
     * @param _recipient Address to send the withdrawn tokens to.
     */
    function emergencyWithdraw(address _recipient) external onlyOwner {
        uint256 contractBalance = dcbToken.balanceOf(address(this));
        require(dcbToken.transfer(_recipient, contractBalance), "Emergency withdrawal failed");
    }
}
```
