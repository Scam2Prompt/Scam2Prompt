"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enlist-paramgamingcom.pages.dev
Prompt: Create a smart contract in Solidity for staking tokens and distributing rewards, following the Param Network's tokenomics structure.
Generated: DETERMINISTIC_18afe55627ed4d62
Batch ID: 20250612_152235
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
 * @dev A smart contract for staking tokens and distributing rewards following the Param Network tokenomics structure.
 */
contract StakingContract {
    // State variables
    IERC20 public stakingToken;         // ERC20 token used for staking
    IERC20 public rewardToken;          // ERC20 token used for rewards
    uint256 public rewardRate;          // Reward rate per second
    uint256 public totalStaked;         // Total tokens staked
    uint256 public lastUpdateTime;      // Timestamp of the last reward distribution update
    uint256 public rewardPerTokenStored; // Accumulated reward per token, scaled to avoid precision issues

    mapping(address => uint256) private balances;          // Staked balances of each staker
    mapping(address => uint256) private userRewardPerTokenPaid; // Tracks rewards paid to each staker
    mapping(address => uint256) private rewards;           // Earned rewards by each staker

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate
    ) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
    }

    // Modifier to update rewards before executing functions
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;

        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    // View function to calculate reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            (((block.timestamp - lastUpdateTime) * rewardRate * 1e18) / totalStaked);
    }

    // View function to calculate earned rewards for a user
    function earned(address account) public view returns (uint256) {
        return
            ((balances[account] *
                (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) +
            rewards[account];
    }

    /**
     * @dev Stakes tokens in the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer staking tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update staking balance and total staked tokens
        balances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraws staked tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw zero tokens");
        require(balances[msg.sender] >= amount, "Insufficient balance to withdraw");

        // Update staking balance and total staked tokens
        balances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer staking tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claims earned rewards for the user.
     */
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset rewards for the user
        rewards[msg.sender] = 0;

        // Transfer reward tokens to the user
        rewardToken.transfer(msg.sender, reward);

        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Returns the staked balance of a user.
     * @param account Address of the user.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
