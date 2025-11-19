"""
Generated Code Metadata:
========================
Original URL: https://skytradefinance.com
Prompt: Write a smart contract in Solidity for staking $SHE tokens on the Arbitrum blockchain, ensuring the ability to calculate APY and distribute rewards based on the SHE Protocol's yield farming mechanism.
Generated: DETERMINISTIC_ec20bfc9a7ae2e48
Batch ID: 20250612_152249
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

contract SHEStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to represent a staker's information
    struct Staker {
        uint256 amount;         // Amount of tokens staked
        uint256 rewardDebt;     // Reward debt for calculating pending rewards
        uint256 lastStakedTime; // Last time the user staked tokens
    }

    // The SHE token contract
    IERC20 public immutable sheToken;
    
    // Reward token (could be same as staking token)
    IERC20 public immutable rewardToken;
    
    // Reward rate per second
    uint256 public rewardRate;
    
    // Duration of reward distribution in seconds
    uint256 public rewardDuration;
    
    // Last time reward distribution was updated
    uint256 public lastUpdateTime;
    
    // Reward per token stored
    uint256 public rewardPerTokenStored;
    
    // Total amount staked
    uint256 public totalStaked;
    
    // Precision factor for reward calculation
    uint256 public constant PRECISION = 1e18;
    
    // Mapping of staker addresses to their info
    mapping(address => Staker) public stakers;
    
    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);
    event RewardDurationUpdated(uint256 newDuration);
    
    constructor(
        address _sheToken,
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _rewardDuration
    ) {
        require(_sheToken != address(0), "Invalid SHE token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        
        sheToken = IERC20(_sheToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        rewardDuration = _rewardDuration;
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
        return block.timestamp < (lastUpdateTime + rewardDuration) 
            ? block.timestamp 
            : (lastUpdateTime + rewardDuration);
    }
    
    // Calculate reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + (
            (lastTimeRewardApplicable() - lastUpdateTime) * rewardRate * PRECISION / totalStaked
        );
    }
    
    // Calculate earned rewards for an account
    function earned(address account) public view returns (uint256) {
        Staker storage staker = stakers[account];
        return staker.amount * (rewardPerToken() - staker.rewardDebt) / PRECISION;
    }
    
    // Calculate APY (Annual Percentage Yield)
    function calculateAPY() external view returns (uint256) {
        if (totalStaked == 0) return 0;
        return (rewardRate * 365 days * 100) / totalStaked;
    }
    
    // Stake SHE tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        Staker storage staker = stakers[msg.sender];
        totalStaked += amount;
        staker.amount += amount;
        staker.rewardDebt = staker.amount * rewardPerTokenStored / PRECISION;
        staker.lastStakedTime = block.timestamp;
        
        sheToken.safeTransferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }
    
    // Withdraw staked SHE tokens
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");
        
        totalStaked -= amount;
        staker.amount -= amount;
        staker.rewardDebt = staker.amount * rewardPerTokenStored / PRECISION;
        
        sheToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }
    
    // Claim rewards
    function claimReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = earned(msg.sender);
        if (reward > 0) {
            stakers[msg.sender].rewardDebt = stakers[msg.sender].amount * rewardPerTokenStored / PRECISION;
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }
    
    // Exit by withdrawing all staked tokens and claiming rewards
    function exit() external {
        withdraw(stakers[msg.sender].amount);
        claimReward();
    }
    
    // Admin functions
    
    // Update reward rate
    function setRewardRate(uint256 _rewardRate) external onlyOwner updateReward(address(0)) {
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }
    
    // Update reward duration
    function setRewardDuration(uint256 _rewardDuration) external onlyOwner {
        require(_rewardDuration > 0, "Duration must be positive");
        rewardDuration = _rewardDuration;
        emit RewardDurationUpdated(_rewardDuration);
    }
    
    // Recover ERC20 tokens (emergency only)
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(sheToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
    
    // Add reward tokens to the contract
    function addRewards(uint256 amount) external onlyOwner {
        rewardToken.safeTransferFrom(msg.sender, address(this), amount);
    }
}
```
