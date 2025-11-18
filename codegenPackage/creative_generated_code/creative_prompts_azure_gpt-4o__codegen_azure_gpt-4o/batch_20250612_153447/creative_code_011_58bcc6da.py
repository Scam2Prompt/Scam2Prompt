"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-site.pages.dev
Prompt: Provide a step-by-step guide to create a staking pool for $PEPU tokens on the Pepe Unchained Layer 2 blockchain, including reward distribution logic.
Generated: DETERMINISTIC_58bcc6da2af35adc
Batch ID: 20250612_153447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a step-by-step code implementation for creating a staking pool for `$PEPU` tokens on the Pepe Unchained Layer 2 blockchain. This implementation is written in Solidity, as it is the most commonly used language for smart contracts.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title PEPU Staking Pool
 * @dev A smart contract for creating a staking pool for $PEPU tokens,
 * allowing users to stake tokens and earn rewards.
 */
contract PEPUStakingPool {
    // ERC20 interface for the $PEPU token
    IERC20 public pepuToken;

    // Pool parameters
    uint256 public totalStaked;
    uint256 public rewardRate; // Rewards per token per second
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    // Mapping of user balances and reward data
    mapping(address => uint256) public userStaked;
    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    constructor(address _pepuTokenAddress, uint256 _rewardRate) {
        require(_pepuTokenAddress != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        pepuToken = IERC20(_pepuTokenAddress);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to update pool rewards before executing any function.
     */
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
     * @dev Calculates reward per token.
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }

        return
            rewardPerTokenStored +
            (rewardRate * (block.timestamp - lastUpdateTime) * 1e18) /
            totalStaked;
    }

    /**
     * @dev Calculates earned rewards for a specific account.
     */
    function earned(address account) public view returns (uint256) {
        return
            (userStaked[account] *
                (rewardPerToken() - userRewardPerTokenPaid[account])) /
            1e18 +
            rewards[account];
    }

    /**
     * @dev Stake $PEPU tokens into the pool.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0 tokens");

        // Transfer PEPU tokens to the staking pool
        pepuToken.transferFrom(msg.sender, address(this), amount);

        totalStaked += amount;
        userStaked[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked $PEPU tokens from the pool.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0 tokens");
        require(userStaked[msg.sender] >= amount, "Insufficient staked balance");

        totalStaked -= amount;
        userStaked[msg.sender] -= amount;

        // Transfer PEPU tokens back to the user
        pepuToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim earned rewards from the pool.
     */
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0;

        // Transfer reward tokens to the user
        pepuToken.transfer(msg.sender, reward);

        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Updates the reward rate. Only callable by the contract owner.
     * @param _rewardRate New reward rate.
     */
    function setRewardRate(uint256 _rewardRate) external {
        // Add access control (e.g., Ownable modifier) for production use
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        rewardRate = _rewardRate;
    }
}

/**
 * @dev Minimal IERC20 interface for interacting with PEPU tokens.
 */
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

### Notes:
- Ensure access control (`Ownable`) is implemented for sensitive functions like `setRewardRate`, `constructor`, and `reward distribution logic` in a production environment.
- Deploy this contract after thoroughly testing it in a development environment and using audits for security.
