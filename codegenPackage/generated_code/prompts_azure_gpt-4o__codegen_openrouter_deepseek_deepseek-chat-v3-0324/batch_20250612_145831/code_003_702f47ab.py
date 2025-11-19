"""
Generated Code Metadata:
========================
Original URL: https://spacem-world.vercel.app
Prompt: Provide an example of a smart contract that facilitates swapping and staking of SpaceM Tokens, incorporating features like instant transactions and security as highlighted on the SpaceM World webpage.
Generated: DETERMINISTIC_702f47ab0806b708
Batch ID: 20250612_145831
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SpaceMStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user staking details
    struct Staker {
        uint256 amount;         // Amount of tokens staked
        uint256 rewardDebt;     // Reward debt for calculating pending rewards
        uint256 lastStakeTime;  // Last stake time for cooldown checks
    }

    // Token contracts
    IERC20 public spacemToken;
    IERC20 public rewardToken;

    // Staking parameters
    uint256 public totalStaked;
    uint256 public rewardPerTokenStored;
    uint256 public lastUpdateTime;
    uint256 public rewardRate;
    uint256 public constant REWARD_DURATION = 7 days;
    uint256 public constant COOLDOWN_PERIOD = 1 days;

    // Mapping of stakers
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardAdded(uint256 reward);
    event TokensSwapped(address indexed user, uint256 amountIn, uint256 amountOut);

    constructor(address _spacemToken, address _rewardToken) {
        spacemToken = IERC20(_spacemToken);
        rewardToken = IERC20(_rewardToken);
    }

    // Modifier to update reward calculations
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            stakers[account].rewardDebt = earned(account);
        }
        _;
    }

    // Calculate rewards per token
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + (
            (block.timestamp - lastUpdateTime) * rewardRate * 1e18 / totalStaked
        );
    }

    // Calculate earned rewards for an account
    function earned(address account) public view returns (uint256) {
        return (stakers[account].amount * (rewardPerToken() - stakers[account].rewardDebt)) / 1e18;
    }

    // Stake tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        Staker storage staker = stakers[msg.sender];
        staker.amount += amount;
        staker.rewardDebt = (staker.amount * rewardPerTokenStored) / 1e18;
        staker.lastStakeTime = block.timestamp;
        
        totalStaked += amount;
        spacemToken.safeTransferFrom(msg.sender, address(this), amount);
        
        emit Staked(msg.sender, amount);
    }

    // Withdraw staked tokens
    function withdraw(uint256 amount) external nonReentrant updateReward(msg.sender) {
        Staker storage staker = stakers[msg.sender];
        require(amount > 0, "Cannot withdraw 0");
        require(staker.amount >= amount, "Insufficient balance");
        require(block.timestamp >= staker.lastStakeTime + COOLDOWN_PERIOD, "Cooldown period not passed");

        staker.amount -= amount;
        staker.rewardDebt = (staker.amount * rewardPerTokenStored) / 1e18;
        
        totalStaked -= amount;
        spacemToken.safeTransfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount);
    }

    // Claim rewards
    function claimReward() external nonReentrant updateReward(msg.sender) {
        uint256 reward = earned(msg.sender);
        if (reward > 0) {
            stakers[msg.sender].rewardDebt = (stakers[msg.sender].amount * rewardPerTokenStored) / 1e18;
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    // Add rewards to the pool
    function notifyRewardAmount(uint256 reward) external onlyOwner updateReward(address(0)) {
        require(reward > 0, "No reward");
        
        if (block.timestamp >= lastUpdateTime + REWARD_DURATION) {
            rewardRate = reward / REWARD_DURATION;
        } else {
            uint256 remaining = lastUpdateTime + REWARD_DURATION - block.timestamp;
            uint256 leftover = remaining * rewardRate;
            rewardRate = (reward + leftover) / REWARD_DURATION;
        }
        
        lastUpdateTime = block.timestamp;
        rewardToken.safeTransferFrom(msg.sender, address(this), reward);
        
        emit RewardAdded(reward);
    }

    // Emergency withdraw without rewards
    function emergencyWithdraw() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        uint256 amount = staker.amount;
        require(amount > 0, "Nothing to withdraw");
        
        staker.amount = 0;
        staker.rewardDebt = 0;
        totalStaked -= amount;
        
        spacemToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Swap tokens (simplified example)
    function swapTokens(uint256 amountIn, uint256 minAmountOut) external nonReentrant {
        require(amountIn > 0, "Amount must be > 0");
        
        // In a real implementation, this would interact with a DEX or use an oracle
        // For this example, we assume a 1:1 swap ratio
        uint256 amountOut = amountIn;
        require(amountOut >= minAmountOut, "Insufficient output amount");
        
        spacemToken.safeTransferFrom(msg.sender, address(this), amountIn);
        rewardToken.safeTransfer(msg.sender, amountOut);
        
        emit TokensSwapped(msg.sender, amountIn, amountOut);
    }

    // Recover ERC20 tokens sent by mistake
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(spacemToken) && tokenAddress != address(rewardToken), 
            "Cannot withdraw staking or reward tokens");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
