"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bicepethclaim.pages.dev
Prompt: Write a Solidity smart contract that leverages Multichain's veMULTI governance token for staking and claiming rewards. Include functions to handle claim issues and withdrawal delays.
Generated: DETERMINISTIC_6bc5dfcecc1a0059
Batch ID: 20250612_152727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title StakingContract
 * @dev A smart contract for staking veMULTI governance tokens, claiming rewards, and handling withdrawal delays.
 */
contract StakingContract {
    // State variables
    address public immutable veMULTI; // Address of the veMULTI governance token contract
    address public owner; // Contract owner address

    uint256 public rewardRate; // Reward rate per staked token
    uint256 public withdrawalDelay; // Delay for withdrawals in seconds

    struct Staker {
        uint256 stakedAmount;
        uint256 rewardDebt;
        uint256 lastStakedTime;
    }

    mapping(address => Staker) public stakers;

    event Staked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 reward);
    event Withdrawn(address indexed staker, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _veMULTI Address of the veMULTI governance token contract.
     * @param _rewardRate Reward rate per staked token.
     * @param _withdrawalDelay Delay for withdrawals in seconds.
     */
    constructor(address _veMULTI, uint256 _rewardRate, uint256 _withdrawalDelay) {
        require(_veMULTI != address(0), "Invalid veMULTI token address");
        owner = msg.sender;
        veMULTI = _veMULTI;
        rewardRate = _rewardRate;
        withdrawalDelay = _withdrawalDelay;
    }

    /**
     * @dev Function to stake veMULTI tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        Staker storage staker = stakers[msg.sender];

        // Update rewards before staking more tokens
        _updateRewards(msg.sender);

        // Transfer veMULTI tokens from the staker to this contract
        require(
            IERC20(veMULTI).transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        staker.stakedAmount += amount;
        staker.lastStakedTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to claim rewards.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 pendingReward = _calculatePendingRewards(msg.sender);

        require(pendingReward > 0, "No rewards available to claim");

        staker.rewardDebt += pendingReward;

        // Transfer rewards to the staker (e.g., in the form of native tokens or an external token)
        // Replace this with actual reward distribution logic
        payable(msg.sender).transfer(pendingReward);

        emit RewardsClaimed(msg.sender, pendingReward);
    }

    /**
     * @dev Function to withdraw staked tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(amount > 0, "Amount must be greater than zero");
        require(staker.stakedAmount >= amount, "Insufficient staked balance");
        require(
            block.timestamp >= staker.lastStakedTime + withdrawalDelay,
            "Withdrawal delay not met"
        );

        // Update rewards before withdrawing tokens
        _updateRewards(msg.sender);

        staker.stakedAmount -= amount;

        // Transfer veMULTI tokens back to the staker
        require(IERC20(veMULTI).transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Internal function to update rewards for a staker.
     * @param stakerAddress Address of the staker.
     */
    function _updateRewards(address stakerAddress) internal {
        Staker storage staker = stakers[stakerAddress];
        uint256 pendingReward = _calculatePendingRewards(stakerAddress);

        if (pendingReward > 0) {
            staker.rewardDebt += pendingReward;
        }
    }

    /**
     * @dev Internal function to calculate pending rewards for a staker.
     * @param stakerAddress Address of the staker.
     * @return The amount of pending rewards.
     */
    function _calculatePendingRewards(address stakerAddress)
        internal
        view
        returns (uint256)
    {
        Staker storage staker = stakers[stakerAddress];
        return
            (staker.stakedAmount * rewardRate * (block.timestamp - staker.lastStakedTime)) /
            1e18;
    }

    /**
     * @dev Function to set a new reward rate.
     * @param _rewardRate New reward rate per staked token.
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Function to set a new withdrawal delay.
     * @param _withdrawalDelay New delay for withdrawals in seconds.
     */
    function setWithdrawalDelay(uint256 _withdrawalDelay) external onlyOwner {
        withdrawalDelay = _withdrawalDelay;
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
