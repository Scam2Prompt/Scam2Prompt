"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jwzt-dashboards-inqubeta.pages.dev
Prompt: Develop a smart contract that replicates the staking reward rate functionality for $QUBE tokens as described in the dashboard.
Generated: DETERMINISTIC_e1c45ad4da2594b5
Batch ID: 20250612_152358
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
 * @dev A smart contract for staking $QUBE tokens and earning rewards based on a fixed reward rate.
 * Users can stake their tokens, claim rewards, and withdraw their staked tokens.
 */
contract StakingContract {
    // State variables
    address public owner; // Owner of the contract
    IERC20 public qubeToken; // QUBE token contract address
    uint256 public rewardRate; // Reward rate (tokens rewarded per second per staked token)
    uint256 public totalStaked; // Total amount of tokens staked in the contract

    struct Staker {
        uint256 stakedAmount; // Amount of tokens staked by the user
        uint256 rewardDebt; // Rewards already calculated and claimed
        uint256 lastUpdated; // Timestamp of the last staking/claiming activity
    }

    mapping(address => Staker) public stakers; // Mapping of user addresses to their staking details

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _qubeToken Address of the QUBE token contract.
     * @param _rewardRate Reward rate per second per token.
     */
    constructor(address _qubeToken, uint256 _rewardRate) {
        owner = msg.sender;
        qubeToken = IERC20(_qubeToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows a user to stake a specified amount of QUBE tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Calculate pending rewards for the user
        _updateRewards(msg.sender);

        // Transfer tokens to the contract
        require(qubeToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user's staking details
        stakers[msg.sender].stakedAmount += _amount;
        stakers[msg.sender].lastUpdated = block.timestamp;

        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to withdraw their staked tokens.
     */
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount > 0, "No tokens to unstake");

        // Calculate pending rewards before unstaking
        _updateRewards(msg.sender);

        uint256 amountToUnstake = staker.stakedAmount;

        // Update user's staking details
        staker.stakedAmount = 0;
        staker.lastUpdated = block.timestamp;

        // Update total staked amount
        totalStaked -= amountToUnstake;

        // Transfer tokens back to the user
        require(qubeToken.transfer(msg.sender, amountToUnstake), "Token transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Allows a user to claim their pending rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        Staker storage staker = stakers[msg.sender];
        uint256 rewardToClaim = staker.rewardDebt;

        require(rewardToClaim > 0, "No rewards to claim");

        // Reset reward debt
        staker.rewardDebt = 0;

        // Transfer rewards to the user
        require(qubeToken.transfer(msg.sender, rewardToClaim), "Reward transfer failed");

        emit RewardClaimed(msg.sender, rewardToClaim);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user to update rewards for.
     */
    function _updateRewards(address _user) internal {
        Staker storage staker = stakers[_user];
        if (staker.stakedAmount > 0) {
            uint256 pendingReward = (block.timestamp - staker.lastUpdated) * staker.stakedAmount * rewardRate;
            staker.rewardDebt += pendingReward;
        }
        staker.lastUpdated = block.timestamp;
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param _newRewardRate New reward rate per second per token.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }

    // Interface for ERC20 token functionality
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    }
}
```
