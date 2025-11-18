"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mindofpepetoken.network
Prompt: Create a smart contract in Solidity for staking $MIND tokens with dynamic APY rewards, ensuring compatibility with Ethereum-based wallets.
Generated: DETERMINISTIC_0e0905590dc23301
Batch ID: 20250612_153954
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
 * @title MIND Token Staking Contract
 * @dev This contract enables staking of $MIND tokens with dynamic APY rewards.
 */
contract MindTokenStaking {
    // ERC20 interface for the $MIND token
    IERC20 public immutable mindToken;

    // Struct to store staker information
    struct Staker {
        uint256 amountStaked;    // Amount of tokens staked
        uint256 rewardDebt;      // Rewards already claimed
        uint256 stakingTimestamp;// Timestamp of when staking started
    }

    // Mapping to store staking details for each user
    mapping(address => Staker) private stakers;

    // Current APY in basis points (e.g., 500 = 5%)
    uint256 public currentAPY;

    // Address of the contract owner
    address public owner;

    // Minimum staking duration in seconds
    uint256 public constant MIN_STAKING_DURATION = 7 days;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event APYUpdated(uint256 oldAPY, uint256 newAPY);

    // Modifier to restrict access to owner functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _mindToken Address of the $MIND token contract.
     * @param _initialAPY Initial APY in basis points (100 basis points = 1%).
     */
    constructor(IERC20 _mindToken, uint256 _initialAPY) {
        mindToken = _mindToken;
        currentAPY = _initialAPY;
        owner = msg.sender;
    }

    /**
     * @dev Stake $MIND tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Transfer $MIND tokens from the sender to the contract
        require(
            mindToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        Staker storage staker = stakers[msg.sender];

        // Calculate pending rewards before updating stake amount
        uint256 pendingReward = calculateReward(msg.sender);
        staker.rewardDebt += pendingReward;

        // Update staker details
        staker.amountStaked += _amount;
        staker.stakingTimestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake $MIND tokens and claim rewards.
     */
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No tokens staked");
        require(
            block.timestamp >= staker.stakingTimestamp + MIN_STAKING_DURATION,
            "Cannot unstake before minimum duration"
        );

        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);
        uint256 totalReward = reward + staker.rewardDebt;

        // Reset staker details
        uint256 amountToUnstake = staker.amountStaked;
        staker.amountStaked = 0;
        staker.rewardDebt = 0;
        staker.stakingTimestamp = 0;

        // Transfer staked tokens and rewards to the user
        require(
            mindToken.transfer(msg.sender, amountToUnstake),
            "Failed to transfer staked tokens"
        );
        if (totalReward > 0) {
            require(
                mindToken.transfer(msg.sender, totalReward),
                "Failed to transfer rewards"
            );
        }

        emit Unstaked(msg.sender, amountToUnstake, totalReward);
    }

    /**
     * @dev Update the APY percentage.
     * @param _newAPY New APY in basis points (100 basis points = 1%).
     */
    function updateAPY(uint256 _newAPY) external onlyOwner {
        require(_newAPY >= 100 && _newAPY <= 1000, "APY should be between 1% and 10%");
        uint256 oldAPY = currentAPY;
        currentAPY = _newAPY;
        emit APYUpdated(oldAPY, currentAPY);
    }

    /**
     * @dev Calculate staking rewards for a user.
     * @param _user Address of the user.
     * @return reward Calculated reward amount.
     */
    function calculateReward(address _user) public view returns (uint256 reward) {
        Staker memory staker = stakers[_user];
        if (staker.amountStaked == 0) {
            return 0;
        }
        uint256 stakingDuration = block.timestamp - staker.stakingTimestamp;
        uint256 yearlyReward = (staker.amountStaked * currentAPY) / 10000;
        reward = (yearlyReward * stakingDuration) / 365 days; // Pro-rate rewards based on staking duration
    }

    /**
     * @dev Emergency withdrawal in case of issues with the contract.
     *      Only callable by the owner.
     * @param _token Address of the token to withdraw.
     * @param _amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(
            IERC20(_token).transfer(owner, _amount),
            "Emergency withdrawal failed"
        );
    }
}

// Minimal IERC20 interface
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount)
        external
        returns (bool);
}
```
