"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.pages.dev
Prompt: Provide a guide for setting up a staking rewards system on a multichain token, ensuring compatibility with wallets like TrustWallet and MetaMask, as described for $FROP.
Generated: DETERMINISTIC_119d0a1a5d27a0c7
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a concise and production-ready implementation of a staking rewards system for a multichain token. This code is implemented in Solidity for Ethereum-compatible blockchains.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title StakingRewards for Multichain Token
 * @dev Implements a staking rewards system compatible with wallets like TrustWallet and MetaMask.
 * This contract uses ERC20 tokens as staking and reward tokens.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract MultichainStakingRewards is Ownable, ReentrancyGuard {
    // Token used for staking
    IERC20 public stakingToken;

    // Token used for rewards
    IERC20 public rewardsToken;

    // Reward rate in tokens per second
    uint256 public rewardRate;

    // Last time rewards were updated
    uint256 public lastUpdateTime;

    // Reward per token stored
    uint256 public rewardPerTokenStored;

    // Mapping of user to rewards data
    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;

    // Total staking balance
    uint256 private _totalSupply;

    // User staking balances
    mapping(address => uint256) private _balances;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 oldRate, uint256 newRate);

    constructor(address _stakingToken, address _rewardsToken, uint256 _initialRewardRate) {
        stakingToken = IERC20(_stakingToken);
        rewardsToken = IERC20(_rewardsToken);
        rewardRate = _initialRewardRate;
        lastUpdateTime = block.timestamp;
    }

    /**
     * @dev Modifier to update reward for a user.
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
     * @notice Stake tokens to earn rewards.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake zero tokens");

        _totalSupply += amount;
        _balances[msg.sender] += amount;

        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Stake transfer failed");

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Withdraw staked tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw zero tokens");
        require(_balances[msg.sender] >= amount, "Insufficient staked balance");

        _totalSupply -= amount;
        _balances[msg.sender] -= amount;

        require(stakingToken.transfer(msg.sender, amount), "Withdraw transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @notice Claim earned rewards.
     */
    function getReward() external nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            require(rewardsToken.transfer(msg.sender, reward), "Reward transfer failed");

            emit RewardPaid(msg.sender, reward);
        }
    }

    /**
     * @notice Calculate the reward per token.
     * @return Reward per token.
     */
    function rewardPerToken() public view returns (uint256) {
        if (_totalSupply == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            ((block.timestamp - lastUpdateTime) * rewardRate * 1e18) / _totalSupply;
    }

    /**
     * @notice Calculate the earned rewards for a user.
     * @param account User address.
     * @return Earned rewards.
     */
    function earned(address account) public view returns (uint256) {
        return
            (_balances[account] * (rewardPerToken() - userRewardPerTokenPaid[account])) /
            1e18 +
            rewards[account];
    }

    /**
     * @notice Update the reward rate. Only owner can call this.
     * @param newRate New reward rate in tokens per second.
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        emit RewardRateUpdated(rewardRate, newRate);
        rewardRate = newRate;
    }

    /**
     * @notice Emergency withdrawal of staking tokens (Owner only).
     * @param token Address of the token to withdraw.
     * @param amount Amount to withdraw.
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner(), amount);
    }

    /**
     * @notice Get total staked tokens.
     * @return Total staked tokens.
     */
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Get balance of staked tokens for a user.
     * @param account User address.
     * @return Staked token balance for user.
     */
    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }
}
```

**Notes:**
1. This code uses OpenZeppelin's libraries for security and modularity.
2. Ensure that `stakingToken` and `rewardsToken` are initialized correctly (ERC-20 token addresses).
3. Deploy on a compatible EVM-based blockchain (e.g., Ethereum, Binance Smart Chain, Polygon).
4. The contract needs to be funded with sufficient `rewardToken` balance for rewards.
