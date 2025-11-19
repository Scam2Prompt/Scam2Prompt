"""
Generated Code Metadata:
========================
Original URL: https://btcetftoken-63w.pages.dev
Prompt: Generate a Solidity contract for staking Bitcoin ETF Token (BTCETF) that rewards users based on the number of tokens staked.
Generated: DETERMINISTIC_ac6c523fcb89b150
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title BTCETF Staking Contract
 * @dev A contract for staking BTCETF tokens and rewarding users based on the number of tokens staked.
 */
contract BTCETFStaking {
    // ERC20 interface for interacting with the BTCETF token
    IERC20 public btcetfToken;

    // Struct to store staking information for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt to calculate pending rewards
        uint256 lastStakedTime; // Timestamp of the last staking action
    }

    // Mapping to store staking information for each user
    mapping(address => Stake) public stakes;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Reward rate per second (e.g., 1 token per second)
    uint256 public rewardRate;

    // Owner of the contract
    address public owner;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _btcetfToken Address of the BTCETF token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _btcetfToken, uint256 _rewardRate) {
        btcetfToken = _btcetfToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Stake BTCETF tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Update rewards for the user before modifying their stake
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        require(
            btcetfToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staking information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastStakedTime = block.timestamp;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake BTCETF tokens from the contract.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(
            stakes[msg.sender].amount >= _amount,
            "Insufficient staked amount"
        );

        // Update rewards for the user before modifying their stake
        _updateRewards(msg.sender);

        // Update staking information
        stakes[msg.sender].amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(
            btcetfToken.transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim staking rewards.
     */
    function claimRewards() external {
        // Update rewards for the user
        _updateRewards(msg.sender);

        // Calculate pending rewards
        uint256 reward = stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards available");

        // Reset reward debt
        stakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        require(
            btcetfToken.transfer(msg.sender, reward),
            "Reward transfer failed"
        );

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Update rewards for a user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        Stake storage stakeInfo = stakes[_user];
        if (stakeInfo.amount > 0) {
            uint256 pendingReward = ((block.timestamp -
                stakeInfo.lastStakedTime) * rewardRate * stakeInfo.amount) /
                totalStaked;
            stakeInfo.rewardDebt += pendingReward;
            stakeInfo.lastStakedTime = block.timestamp;
        }
    }

    /**
     * @dev Update the reward rate. Only callable by the owner.
     * @param _newRewardRate New reward rate per second.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }
}

// Minimal ERC20 interface
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```
