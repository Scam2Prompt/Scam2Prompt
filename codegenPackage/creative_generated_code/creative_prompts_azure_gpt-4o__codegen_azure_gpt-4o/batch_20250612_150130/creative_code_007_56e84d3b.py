"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnm-boxes.pages.dev
Prompt: Develop a staking mechanism in Solidity that rewards users with $EARNM tokens based on their participation in the ecosystem.
Generated: DETERMINISTIC_56e84d3b8f94d4a0
Batch ID: 20250612_150130
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
 * @dev A staking mechanism that rewards users with $EARNM tokens based on their participation.
 */
contract StakingContract {
    // ERC20 token interface
    IERC20 public earnmToken;

    // Struct to store stakes information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 lastUpdated; // Timestamp of the last reward calculation
    }

    // Mapping of user address to their staking details
    mapping(address => Stake) public stakes;

    // Reward rate in tokens per second
    uint256 public rewardRate;

    // Owner address
    address public owner;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(IERC20 _earnmToken, uint256 _rewardRate) {
        require(address(_earnmToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        earnmToken = _earnmToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(earnmToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Calculate and update rewards before staking
        _updateRewards(msg.sender);

        // Update stake details
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastUpdated = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked balance");

        // Calculate and update rewards before withdrawal
        _updateRewards(msg.sender);

        // Update stake details
        stakes[msg.sender].amount -= _amount;

        // Transfer tokens back to the user
        require(earnmToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim accrued rewards.
     */
    function claimRewards() external {
        // Calculate and update rewards
        uint256 rewards = _updateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Transfer rewards to the user
        require(earnmToken.transfer(msg.sender, rewards), "Token transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Update rewards for a user and return the accrued amount.
     * @param _user Address of the user.
     * @return rewards Accrued rewards amount.
     */
    function _updateRewards(address _user) internal returns (uint256 rewards) {
        Stake storage stakeData = stakes[_user];
        if (stakeData.amount > 0) {
            // Calculate rewards based on the staking duration and reward rate
            uint256 stakingDuration = block.timestamp - stakeData.lastUpdated;
            rewards = stakingDuration * stakeData.amount * rewardRate / 1e18;

            // Update lastUpdated timestamp
            stakeData.lastUpdated = block.timestamp;
        }
    }

    /**
     * @dev Update the reward rate. Restricted to the owner.
     * @param _newRewardRate New reward rate in tokens per second.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;
    }
}

// Minimal ERC20 interface
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
