"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-icu.pages.dev
Prompt: Write a function in Solidity to calculate and distribute staking rewards for DOGE20 token holders over a two-year period, based on the smart contract's staking pool logic.
Generated: DETERMINISTIC_482ce2b63ea90e71
Batch ID: 20250612_152710
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
 * @title StakingRewards
 * @dev A smart contract to calculate and distribute staking rewards for DOGE20 token holders.
 */
contract StakingRewards {
    // State variables
    address public owner;
    IERC20 public doge20Token;
    uint256 public totalStaked;
    uint256 public rewardPool;
    uint256 public stakingStartTime;
    uint256 public stakingEndTime;
    uint256 constant REWARD_DURATION = 2 * 365 days; // Two-year period

    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public rewards;

    // Events
    event Staked(address indexed user, uint256 amount);
    event RewardDistributed(address indexed user, uint256 reward);
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Modifier to restrict access to the owner of the contract.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Modifier to check if staking is active.
     */
    modifier onlyActiveStaking() {
        require(block.timestamp >= stakingStartTime, "Staking has not started yet");
        require(block.timestamp <= stakingEndTime, "Staking period has ended");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of the DOGE20 token contract.
     * @param _rewardPool Initial reward pool for staking rewards.
     */
    constructor(address _token, uint256 _rewardPool) {
        require(_token != address(0), "Invalid token address");
        require(_rewardPool > 0, "Reward pool must be greater than zero");

        owner = msg.sender;
        doge20Token = IERC20(_token);
        rewardPool = _rewardPool;
        stakingStartTime = block.timestamp;
        stakingEndTime = stakingStartTime + REWARD_DURATION;
    }

    /**
     * @dev Stake DOGE20 tokens to the staking pool.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external onlyActiveStaking {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(doge20Token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        stakedBalances[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Calculate and distribute staking rewards proportionally to each staker's balance.
     */
    function distributeRewards() external onlyOwner {
        require(block.timestamp > stakingEndTime, "Staking period has not ended yet");
        require(totalStaked > 0, "No tokens staked");

        for (uint256 i = 0; i < totalStakers(); i++) {
            address staker = getStakerByIndex(i);
            uint256 reward = (stakedBalances[staker] * rewardPool) / totalStaked;
            rewards[staker] += reward;
        }

        emit RewardDistributed(msg.sender,reward );
    }

    /**
     * @dev Withdraw DOGE20 tokens and rewards after staking period ends.
     */
    function withdraw() external {
        require(block.timestamp > stakingEndTime, "Staking period has not ended yet");

        uint256 stakedAmount = stakedBalances[msg.sender];
        uint256 rewardAmount = rewards[msg.sender];

        require(stakedAmount > 0 || rewardAmount > 0, "No balance to withdraw");

        stakedBalances[msg.sender] = 0;
        rewards[msg.sender] = 0;
        totalStaked -= stakedAmount;

        require(doge20Token.transfer(msg.sender, stakedAmount + rewardAmount), "Token transfer failed");

        emit Withdrawn(msg.sender, stakedAmount + rewardAmount);
    }

    /**
     * @dev Fallback function to reject ether transfers.
     */
    receive() external payable {
        revert("Cannot accept Ether");
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
