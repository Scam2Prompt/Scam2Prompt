"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-live.pages.dev
Prompt: How can I implement a staking mechanism for DOGE20 that distributes rewards every block based on user participation in the staking pool?
Generated: DETERMINISTIC_cb08e4302e083b68
Batch ID: 20250612_162207
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
 * @title DOGE20 Staking Contract
 * @dev This contract implements a staking mechanism for DOGE20 tokens.
 *      Rewards are distributed every block based on user participation in the staking pool.
 */
contract DOGE20Staking {
    // Address of the DOGE20 token contract
    IERC20 public immutable doge20Token;

    // Total amount of DOGE20 tokens staked in the pool
    uint256 public totalStaked;

    // Reward rate per block (to be set by the contract owner)
    uint256 public rewardPerBlock;

    // Mapping from user address to their staking balance
    mapping(address => uint256) public stakingBalance;

    // Mapping from user address to their pending rewards
    mapping(address => uint256) public pendingRewards;

    // Mapping from user address to their last reward block
    mapping(address => uint256) public lastRewardBlock;

    // Contract owner address
    address public owner;

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRewardRate);

    /**
     * @dev Constructor to initialize the contract.
     * @param _doge20Token Address of the DOGE20 token contract.
     * @param _rewardPerBlock Initial reward rate per block.
     */
    constructor(IERC20 _doge20Token, uint256 _rewardPerBlock) {
        require(address(_doge20Token) != address(0), "Invalid token address");
        require(_rewardPerBlock > 0, "Reward per block must be greater than zero");
        doge20Token = _doge20Token;
        rewardPerBlock = _rewardPerBlock;
        owner = msg.sender;
    }

    /**
     * @dev Function to stake DOGE20 tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        updateRewards(msg.sender);

        // Transfer tokens from user to contract
        require(doge20Token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking balance and total staked
        stakingBalance[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to unstake DOGE20 tokens.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakingBalance[msg.sender] >= _amount, "Insufficient staking balance");
        updateRewards(msg.sender);

        // Update staking balance and total staked
        stakingBalance[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer tokens from contract to user
        require(doge20Token.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Function to claim pending rewards.
     */
    function claimRewards() external {
        updateRewards(msg.sender);

        uint256 rewards = pendingRewards[msg.sender];
        require(rewards > 0, "No rewards to claim");

        pendingRewards[msg.sender] = 0;

        // Transfer rewards to user
        require(doge20Token.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @dev Function to update staking rewards for a user.
     * @param _user Address of the user.
     */
    function updateRewards(address _user) internal {
        uint256 userStaked = stakingBalance[_user];
        if (userStaked > 0) {
            uint256 rewards = (block.number - lastRewardBlock[_user]) * rewardPerBlock * userStaked / totalStaked;
            pendingRewards[_user] += rewards;
        }
        lastRewardBlock[_user] = block.number;
    }

    /**
     * @dev Function to update the reward rate per block (only callable by the owner).
     * @param _newRewardRate New reward rate per block.
     */
    function updateRewardPerBlock(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward per block must be greater than zero");
        rewardPerBlock = _newRewardRate;

        emit RewardRateUpdated(_newRewardRate);
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
