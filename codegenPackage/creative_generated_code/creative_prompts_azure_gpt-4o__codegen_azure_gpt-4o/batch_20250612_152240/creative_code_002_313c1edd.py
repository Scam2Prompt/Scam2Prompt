"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supertrumpcoin-io.pages.dev
Prompt: Generate code to implement a staking mechanism for a cryptocurrency token with tokenomics similar to Super Trump Coin, ensuring 4% of the supply is reserved for staking rewards.
Generated: DETERMINISTIC_313c1edd9b744682
Batch ID: 20250612_152240
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
 * @title StakingToken
 * @dev A staking mechanism for a cryptocurrency token with 4% supply reserved for staking rewards
 */
contract StakingToken {
    // Token metadata
    string public constant name = "Super Trump Coin";
    string public constant symbol = "STC";
    uint8 public constant decimals = 18;

    // Total supply of the token
    uint256 public totalSupply;

    // 4% of the total supply reserved for staking rewards
    uint256 public constant STAKING_REWARD_PERCENTAGE = 4;

    // Mapping to track balances and stakes
    mapping(address => uint256) public balances;
    mapping(address => uint256) public stakes;
    mapping(address => uint256) public stakingStartTime;

    // Total staked tokens
    uint256 public totalStaked;

    // Staking reward pool
    uint256 public stakingRewardPool;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount, uint256 reward);

    /**
     * @dev Constructor initializes the token supply and staking reward pool
     * @param initialSupply The initial total supply of the token
     */
    constructor(uint256 initialSupply) {
        totalSupply = initialSupply * (10**decimals);
        stakingRewardPool = (totalSupply * STAKING_REWARD_PERCENTAGE) / 100;

        // Assign the entire supply to the contract deployer
        balances[msg.sender] = totalSupply - stakingRewardPool;

        emit Transfer(address(0), msg.sender, balances[msg.sender]);
    }

    /**
     * @dev Modifier to check if the caller has enough balance
     * @param _amount The amount to check
     */
    modifier hasEnoughBalance(uint256 _amount) {
        require(balances[msg.sender] >= _amount, "Insufficient balance.");
        _;
    }

    /**
     * @dev Modifier to ensure staking amount is greater than zero
     * @param _amount The amount to check
     */
    modifier validStakeAmount(uint256 _amount) {
        require(_amount > 0, "Stake amount must be greater than 0.");
        _;
    }

    /**
     * @dev Transfer function to send tokens to another address
     * @param _to The recipient address
     * @param _amount The amount to send
     */
    function transfer(address _to, uint256 _amount) public hasEnoughBalance(_amount) returns (bool) {
        require(_to != address(0), "Cannot transfer to the zero address.");

        balances[msg.sender] -= _amount;
        balances[_to] += _amount;

        emit Transfer(msg.sender, _to, _amount);
        return true;
    }

    /**
     * @dev Stake tokens to participate in staking
     * @param _amount The amount to stake
     */
    function stake(uint256 _amount) public hasEnoughBalance(_amount) validStakeAmount(_amount) {
        balances[msg.sender] -= _amount;
        stakes[msg.sender] += _amount;
        stakingStartTime[msg.sender] = block.timestamp;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and claim rewards
     */
    function unstake() public {
        uint256 stakedAmount = stakes[msg.sender];
        require(stakedAmount > 0, "No staked tokens to unstake.");

        uint256 stakingDuration = block.timestamp - stakingStartTime[msg.sender];
        uint256 reward = calculateReward(msg.sender, stakingDuration);

        stakes[msg.sender] = 0;
        stakingStartTime[msg.sender] = 0;
        totalStaked -= stakedAmount;

        // Transfer staked tokens and rewards back to the user
        balances[msg.sender] += stakedAmount + reward;
        stakingRewardPool -= reward;

        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev Calculate staking reward for a user
     * @param _staker The staker's address
     * @param _duration The staking duration in seconds
     * @return The reward amount
     */
    function calculateReward(address _staker, uint256 _duration) public view returns (uint256) {
        uint256 stakedAmount = stakes[_staker];
        uint256 annualRewardRate = stakingRewardPool / totalSupply; // Simplified reward rate
        return (stakedAmount * annualRewardRate * _duration) / (365 days);
    }
}
```
