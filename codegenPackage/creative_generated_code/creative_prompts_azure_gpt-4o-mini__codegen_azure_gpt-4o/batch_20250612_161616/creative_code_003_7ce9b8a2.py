"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20claim.pages.dev
Prompt: What are the steps to integrate a dynamic rewards calculation for DOGE20 staking in a smart contract?
Generated: DETERMINISTIC_7ce9b8a24f41e9a1
Batch ID: 20250612_161616
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
 * @title Doge20StakingRewards
 * @dev A smart contract for staking DOGE20 tokens and dynamically calculating rewards.
 */
contract Doge20StakingRewards {
    // State variables
    address public owner;
    IERC20 public doge20Token; // DOGE20 token interface
    uint256 public rewardRate; // Reward rate in percentage (e.g., 5% = 500)
    uint256 public constant REWARD_PRECISION = 10000; // Precision for reward calculations
    uint256 public totalStaked; // Total tokens staked in the contract
    mapping(address => uint256) public stakedBalances; // Staked balances per user
    mapping(address => uint256) public rewardBalances; // Rewards earned per user
    mapping(address => uint256) public lastUpdated; // Last time rewards were calculated per user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier updateRewards(address _user) {
        if (_user != address(0)) {
            rewardBalances[_user] += _earnedRewards(_user);
            lastUpdated[_user] = block.timestamp;
        }
        _;
    }

    constructor(address _doge20Token, uint256 _initialRewardRate) {
        require(_doge20Token != address(0), "Invalid token address");
        require(_initialRewardRate > 0, "Reward rate must be positive");
        owner = msg.sender;
        doge20Token = IERC20(_doge20Token);
        rewardRate = _initialRewardRate;
    }

    /**
     * @dev Stake DOGE20 tokens in the contract.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Cannot stake 0 tokens");
        require(doge20Token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");
        stakedBalances[msg.sender] += _amount;
        totalStaked += _amount;
        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked DOGE20 tokens.
     * @param _amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Cannot withdraw 0 tokens");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");
        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;
        require(doge20Token.transfer(msg.sender, _amount), "Token transfer failed");
        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim accumulated rewards for the sender.
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 rewards = rewardBalances[msg.sender];
        require(rewards > 0, "No rewards available");
        rewardBalances[msg.sender] = 0;
        require(doge20Token.transfer(msg.sender, rewards), "Token transfer failed");
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Update the reward rate.
     * @param _newRate The new reward rate in percentage (e.g., 5% = 500).
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Reward rate must be positive");
        rewardRate = _newRate;
        emit RewardRateUpdated(_newRate);
    }

    /**
     * @dev Calculate rewards for a user since the last update.
     * @param _user The address of the user.
     * @return The earned rewards.
     */
    function _earnedRewards(address _user) internal view returns (uint256) {
        uint256 staked = stakedBalances[_user];
        if (staked == 0) {
            return 0;
        }
        uint256 timeElapsed = block.timestamp - lastUpdated[_user];
        return (staked * rewardRate * timeElapsed) / (REWARD_PRECISION * 365 days);
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
