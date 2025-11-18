"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-claim-akz.pages.dev
Prompt: Write a smart contract in Solidity for staking ERC-20 tokens like $DOGE20, where rewards are distributed proportionally to the staker's share in the pool over a two-year period.
Generated: DETERMINISTIC_388a375cef07fa0f
Batch ID: 20250612_153420
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
 * @notice A smart contract for staking ERC-20 tokens and earning proportional rewards over a two-year period.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is Ownable {
    // ERC-20 token to be staked
    IERC20 public stakingToken;

    // Reward token distributed to stakers
    IERC20 public rewardToken;

    // Duration of staking rewards (2 years)
    uint256 public constant REWARD_DURATION = 2 * 365 days;

    // Timestamp when rewards end
    uint256 public rewardEndTime;

    // Total tokens staked in the contract
    uint256 public totalStaked;

    // Mapping of staker addresses to their staking balances
    mapping(address => uint256) public stakedBalances;

    // Mapping to track staker rewards
    mapping(address => uint256) public rewardBalances;

    // Pool-wide reward rate
    uint256 public rewardRate;

    // Last updated timestamp for reward calculations
    uint256 public lastUpdateTime;

    // Accumulated rewards per token staked
    uint256 public rewardPerTokenStored;

    // User-specific reward per token paid
    mapping(address => uint256) public userRewardPerTokenPaid;

    /**
     * @dev Emitted when tokens are staked.
     */
    event Staked(address indexed user, uint256 amount);

    /**
     * @dev Emitted when tokens are withdrawn.
     */
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Emitted when rewards are claimed.
     */
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize staking and reward tokens.
     * @param _stakingToken Address of the ERC-20 staking token
     * @param _rewardToken Address of the ERC-20 reward token
     * @param _rewardRate Tokens distributed as rewards per second
     */
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
        rewardEndTime = block.timestamp + REWARD_DURATION;
    }

    /**
     * @notice Modifier to update rewards before performing certain actions.
     * @param account Address of the user to update rewards for
     */
    modifier updateReward(address account) {
        rewardPerTokenStored = currentRewardPerToken();
        lastUpdateTime = lastApplicableRewardTime();
        if (account != address(0)) {
            rewardBalances[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    /**
     * @notice Function to get the last applicable reward time.
     * @return Timestamp of the last applicable reward time
     */
    function lastApplicableRewardTime() public view returns (uint256) {
        return block.timestamp < rewardEndTime ? block.timestamp : rewardEndTime;
    }

    /**
     * @notice Function to calculate the current reward per token.
     * @return Calculated reward per token
     */
    function currentRewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            ((rewardRate * (lastApplicableRewardTime() - lastUpdateTime) * 1e18) / totalStaked);
    }

    /**
     * @notice Function to calculate the earned rewards for a user.
     * @param account Address of the user
     * @return Rewards earned by the user
     */
    function earned(address account) public view returns (uint256) {
        return
            ((stakedBalances[account] * (currentRewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) +
            rewardBalances[account];
    }

    /**
     * @notice Function to stake tokens.
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0 tokens");
        stakingToken.transferFrom(msg.sender, address(this), amount);
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Function to withdraw staked tokens.
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0 tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient balance to withdraw");
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;
        stakingToken.transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @notice Function to claim rewards.
     */
    function claimRewards() external updateReward(msg.sender) {
        uint256 reward = rewardBalances[msg.sender];
        require(reward > 0, "No rewards available to claim");
        rewardBalances[msg.sender] = 0;
        rewardToken.transfer(msg.sender, reward);
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Function to rescue tokens mistakenly sent to the contract.
     * @dev Only callable by the owner.
     * @param token Address of the token to rescue
     * @param amount Amount of tokens to rescue
     */
    function rescueTokens(IERC20 token, uint256 amount) external onlyOwner {
        token.transfer(owner(), amount);
    }
}
```
