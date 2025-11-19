"""
Generated Code Metadata:
========================
Original URL: https://iziswap.fi
Prompt: "Generate a smart contract code for a liquidity mining-based bond with no Impermanent Loss for LP Farming, similar to iZiSwap's Farm iUSD."
Generated: DETERMINISTIC_6d398ae5a5897f94
Batch ID: 20250622_210821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// LiquidityMiningBond contract for liquidity mining with no impermanent loss
contract LiquidityMiningBond is Ownable, ReentrancyGuard {
    // State variables
    IERC20 public immutable lpToken; // Liquidity Provider Token
    IERC20 public immutable rewardToken; // Reward Token
    uint256 public rewardRate; // Reward rate per block
    uint256 public totalStaked; // Total amount of LP tokens staked
    uint256 public lastUpdateBlock; // Last block when rewards were updated

    // Mapping of user balances and rewards
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public rewards;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(IERC20 _lpToken, IERC20 _rewardToken, uint256 _rewardRate) {
        lpToken = _lpToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
        lastUpdateBlock = block.number;
    }

    // Modifier to update rewards before any action
    modifier updateReward(address account) {
        rewards[account] += earned(account);
        lastUpdateBlock = block.number;
        _;
    }

    // Function to calculate earned rewards
    function earned(address account) public view returns (uint256) {
        return (stakedBalances[account] * rewardRate * (block.number - lastUpdateBlock)) / 1e18;
    }

    // Function to stake LP tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        lpToken.transferFrom(msg.sender, address(this), amount);
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    // Function to unstake LP tokens
    function unstake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot unstake 0");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;
        lpToken.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        rewards[msg.sender] = 0;
        rewardToken.transfer(msg.sender, reward);
        emit RewardPaid(msg.sender, reward);
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(IERC20 token, uint256 amount) external onlyOwner {
        token.transfer(msg.sender, amount);
    }
}
```
