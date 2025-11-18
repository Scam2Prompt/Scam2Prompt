"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimdoge20live.pages.dev
Prompt: Develop a smart contract in Solidity that automates DOGE20 staking, calculates rewards dynamically based on the pool percentage, and allows users to claim rewards directly.
Generated: DETERMINISTIC_d046f860bb9f5c04
Batch ID: 20250612_153400
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
 * @title DOGE20 Staking Smart Contract
 * @dev Allows users to stake DOGE20 tokens, earn rewards proportional to their pool share, and claim rewards.
 * NOTE: This contract assumes DOGE20 follows the ERC20 standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract DOGE20Staking {
    IERC20 public immutable doge20Token; // The token being staked
    uint256 public totalStaked; // Total amount of DOGE20 tokens staked in the contract
    uint256 public rewardPool; // Total reward pool available for distribution

    struct Staker {
        uint256 amountStaked; // Amount of DOGE20 tokens staked by the user
        uint256 pendingRewards; // Rewards accumulated over time and yet to be claimed
        uint256 rewardPerTokenPaid; // Tracks rewards paid per token for each staker
    }

    mapping(address => Staker) public stakers; // Tracks staking information for each user
    uint256 public rewardPerToken; // Rewards distributed per token staked

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardPoolFunded(uint256 amount);

    constructor(address _doge20Token) {
        require(_doge20Token != address(0), "Token address cannot be zero");
        doge20Token = IERC20(_doge20Token);
    }

    /**
     * @dev Modifier to update rewards before any state-changing action.
     */
    modifier updateRewards(address _account) {
        rewardPerToken = calculateRewardPerToken();
        if (_account != address(0)) {
            Staker storage staker = stakers[_account];
            staker.pendingRewards = calculatePendingRewards(_account);
            staker.rewardPerTokenPaid = rewardPerToken;
        }
        _;
    }

    /**
     * @dev Stakes DOGE20 tokens into the contract.
     * @param _amount Amount of DOGE20 tokens to stake.
     */
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Cannot stake zero tokens");
        stakers[msg.sender].amountStaked += _amount;
        totalStaked += _amount;

        // Transfer tokens from the staker to the contract
        require(doge20Token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");
        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraws staked tokens from the contract.
     * @param _amount Amount of DOGE20 tokens to withdraw.
     */
    function withdraw(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(stakers[msg.sender].amountStaked >= _amount, "Insufficient staked balance");

        stakers[msg.sender].amountStaked -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the staker
        require(doge20Token.transfer(msg.sender, _amount), "Token transfer failed");
        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claims pending rewards for the caller.
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 rewards = stakers[msg.sender].pendingRewards;
        require(rewards > 0, "No rewards to claim");

        stakers[msg.sender].pendingRewards = 0;
        rewardPool -= rewards;

        // Transfer rewards to the caller
        require(doge20Token.transfer(msg.sender, rewards), "Reward transfer failed");
        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @dev Funds the reward pool with additional DOGE20 tokens.
     * @param _amount Amount of DOGE20 tokens to add to the reward pool.
     */
    function fundRewardPool(uint256 _amount) external {
        require(_amount > 0, "Cannot fund zero tokens");
        
        rewardPool += _amount;

        // Transfer tokens from the funder to the contract
        require(doge20Token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");
        emit RewardPoolFunded(_amount);
    }

    /**
     * @dev Calculates the reward per token based on the reward pool and total staked tokens.
     */
    function calculateRewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerToken;
        }
        return rewardPerToken + (rewardPool * 1e18 / totalStaked);
    }

    /**
     * @dev Calculates pending rewards for a specific staker.
     * @param _account Address of the staker to calculate rewards for.
     */
    function calculatePendingRewards(address _account) public view returns (uint256) {
        Staker storage staker = stakers[_account];
        uint256 rewardsDue = (staker.amountStaked * (calculateRewardPerToken() - staker.rewardPerTokenPaid)) / 1e18;
        return staker.pendingRewards + rewardsDue;
    }

    /**
     * @dev Returns the pending rewards for the caller.
     */
    function getPendingRewards(address _account) external view returns (uint256) {
        return calculatePendingRewards(_account);
    }
}
```
