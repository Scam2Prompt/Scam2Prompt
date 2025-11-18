"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kenduinu-io.pages.dev
Prompt: Create a function in Solidity to implement staking rewards for $KENDU holders, ensuring compatibility with the existing smart contract.
Generated: DETERMINISTIC_27109d3020f6277b
Batch ID: 20250612_151141
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
 * @dev A smart contract to manage staking rewards for $KENDU holders. 
 * Users can stake tokens, earn rewards, and withdraw their stake and rewards.
 */
contract StakingRewards {
    IERC20 public kenduToken; // $KENDU token contract
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public lastUpdateTime; // Last timestamp when rewards were calculated
    uint256 public rewardPerTokenStored; // Accumulated rewards per token staked

    mapping(address => uint256) public userStake; // Mapping of user addresses to their staked amount
    mapping(address => uint256) public userRewardPerTokenPaid; // Rewards already paid per token for each user
    mapping(address => uint256) public rewards; // Mapping of user addresses to their earned rewards

    // Modifier to ensure only positive staking amounts
    modifier nonZeroAmount(uint256 amount) {
        require(amount > 0, "Staking amount must be greater than zero");
        _;
    }

    // Modifier to update rewards before any state-changing operation
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _kenduToken The address of the $KENDU token contract.
     * @param _rewardRate The reward rate per second.
     */
    constructor(IERC20 _kenduToken, uint256 _rewardRate) {
        kenduToken = _kenduToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Calculates the reward per token staked.
     * @return The reward per token.
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + ((rewardRate * (block.timestamp - lastUpdateTime) * 1e18) / totalStaked);
    }

    /**
     * @dev Calculates the earned rewards for a user.
     * @param account The address of the user.
     * @return The earned rewards.
     */
    function earned(address account) public view returns (uint256) {
        return ((userStake[account] * (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) + rewards[account];
    }

    /**
     * @dev Allows a user to stake $KENDU tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external nonZeroAmount(amount) updateReward(msg.sender) {
        totalStaked += amount;
        userStake[msg.sender] += amount;
        kenduToken.transferFrom(msg.sender, address(this), amount); // Transfer tokens to the contract
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to withdraw their staked tokens along with earned rewards.
     */
    function withdraw() external updateReward(msg.sender) {
        uint256 stakedAmount = userStake[msg.sender];
        uint256 rewardAmount = rewards[msg.sender];
        require(stakedAmount > 0, "No tokens to withdraw");

        totalStaked -= stakedAmount;
        userStake[msg.sender] = 0;
        rewards[msg.sender] = 0;

        kenduToken.transfer(msg.sender, stakedAmount + rewardAmount); // Transfer staked tokens and rewards to the user
        emit Withdrawn(msg.sender, stakedAmount, rewardAmount);
    }

    /**
     * @dev Allows a user to claim their earned rewards without withdrawing their stake.
     */
    function claimRewards() external updateReward(msg.sender) {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        rewards[msg.sender] = 0;
        kenduToken.transfer(msg.sender, rewardAmount); // Transfer rewards to the user
        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Event emitted when a user stakes tokens.
     * @param user The address of the user.
     * @param amount The amount of tokens staked.
     */
    event Staked(address indexed user, uint256 amount);

    /**
     * @dev Event emitted when a user withdraws their stake and rewards.
     * @param user The address of the user.
     * @param stakedAmount The amount of tokens withdrawn.
     * @param rewardAmount The amount of rewards withdrawn.
     */
    event Withdrawn(address indexed user, uint256 stakedAmount, uint256 rewardAmount);

    /**
     * @dev Event emitted when a user claims their rewards.
     * @param user The address of the user.
     * @param rewardAmount The amount of rewards claimed.
     */
    event RewardsClaimed(address indexed user, uint256 rewardAmount);
}

/**
 * @dev Interface for ERC20 token.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
