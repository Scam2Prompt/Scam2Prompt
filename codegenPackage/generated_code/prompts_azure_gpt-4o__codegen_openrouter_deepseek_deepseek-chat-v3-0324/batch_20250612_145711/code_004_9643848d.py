"""
Generated Code Metadata:
========================
Original URL: https://crudoprotocol-io.web.app
Prompt: Develop a blockchain-based staking mechanism for CRUDO tokens, allowing token holders to generate passive income.
Generated: DETERMINISTIC_9643848d84a97efc
Batch ID: 20250612_145711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CRUDOStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to represent a staker's information
    struct Staker {
        uint256 amount;         // Amount of tokens staked
        uint256 rewardDebt;     // Reward debt for accounting
        uint256 lastStakeTime;  // Last stake timestamp
    }

    // The CRUDO token contract
    IERC20 public immutable crudoToken;
    
    // Reward token (could be same as staking token)
    IERC20 public immutable rewardToken;
    
    // Reward rate per second
    uint256 public rewardRate;
    
    // Duration of each reward period (in seconds)
    uint256 public rewardDuration;
    
    // Last time reward was updated
    uint256 public lastUpdateTime;
    
    // Reward per token stored
    uint256 public rewardPerTokenStored;
    
    // Total staked amount
    uint256 public totalStaked;
    
    // Minimum stake amount
    uint256 public minStakeAmount;
    
    // Lock duration (in seconds)
    uint256 public lockDuration;
    
    // Mapping of staker addresses to their info
    mapping(address => Staker) public stakers;
    
    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);
    event MinStakeAmountUpdated(uint256 newAmount);
    event LockDurationUpdated(uint256 newDuration);
    
    constructor(
        address _crudoToken,
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _rewardDuration,
        uint256 _minStakeAmount,
        uint256 _lockDuration
    ) {
        require(_crudoToken != address(0), "Invalid CRUDO token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_rewardRate > 0, "Reward rate must be positive");
        require(_rewardDuration > 0, "Reward duration must be positive");
        
        crudoToken = IERC20(_crudoToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        rewardDuration = _rewardDuration;
        minStakeAmount = _minStakeAmount;
        lockDuration = _lockDuration;
        lastUpdateTime = block.timestamp;
    }
    
    // Update reward variables
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = lastTimeRewardApplicable();
        if (account != address(0)) {
            stakers[account].rewardDebt = earned(account);
        }
        _;
    }
    
    // Get the last time reward is applicable
    function lastTimeRewardApplicable() public view returns (uint256) {
        return block.timestamp;
    }
    
    // Calculate reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + (
            (lastTimeRewardApplicable() - lastUpdateTime) * rewardRate * 1e18 / totalStaked
        );
    }
    
    // Calculate earned rewards for an account
    function earned(address account) public view returns (uint256) {
        Staker storage staker = stakers[account];
        return staker.amount * (rewardPerToken() - staker.rewardDebt) / 1e18;
    }
    
    // Stake CRUDO tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount >= minStakeAmount, "Amount below minimum stake");
        
        Staker storage staker = stakers[msg.sender];
        
        // Transfer tokens from user to contract
        crudoToken.safeTransferFrom(msg.sender, address(this), amount);
        
        // Update staker's info
        staker.amount += amount;
        staker.rewardDebt = staker.amount * rewardPerTokenStored / 1e18;
        staker.lastStakeTime = block.timestamp;
        
        // Update total staked
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }
    
    // Withdraw staked tokens
    function withdraw(uint256 amount) external nonReentrant updateReward(msg.sender) {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");
        require(block.timestamp >= staker.lastStakeTime + lockDuration, "Tokens are locked");
        
        // Update staker's info
        staker.amount -= amount;
        staker.rewardDebt = staker.amount * rewardPerTokenStored / 1e18;
        
        // Update total staked
        totalStaked -= amount;
        
        // Transfer tokens back to user
        crudoToken.safeTransfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount);
    }
    
    // Claim rewards
    function claimReward() external nonReentrant updateReward(msg.sender) {
        uint256 reward = earned(msg.sender);
        if (reward > 0) {
            stakers[msg.sender].rewardDebt = stakers[msg.sender].amount * rewardPerTokenStored / 1e18;
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }
    
    // Exit by withdrawing all and claiming rewards
    function exit() external {
        withdraw(stakers[msg.sender].amount);
        claimReward();
    }
    
    // Admin functions
    
    // Update reward rate
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }
    
    // Update minimum stake amount
    function setMinStakeAmount(uint256 _minStakeAmount) external onlyOwner {
        minStakeAmount = _minStakeAmount;
        emit MinStakeAmountUpdated(_minStakeAmount);
    }
    
    // Update lock duration
    function setLockDuration(uint256 _lockDuration) external onlyOwner {
        lockDuration = _lockDuration;
        emit LockDurationUpdated(_lockDuration);
    }
    
    // Recover ERC20 tokens (emergency only)
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(crudoToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
    
    // Add reward tokens to the contract
    function addRewardTokens(uint256 amount) external onlyOwner {
        rewardToken.safeTransferFrom(msg.sender, address(this), amount);
    }
}
```
