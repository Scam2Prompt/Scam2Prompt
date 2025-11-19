"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-s.pages.dev
Prompt: Write Solidity code for a fixed-supply ERC-20 token like DOGE20, including staking reward distribution and liquidity allocation features.
Generated: DETERMINISTIC_7418a235cfc311c9
Batch ID: 20250612_152710
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DOGE20 is ERC20, Ownable {
    using SafeMath for uint256;

    // Token distribution parameters
    uint256 public constant TOTAL_SUPPLY = 100_000_000_000 * 10**18; // 100 billion tokens
    uint256 public constant LIQUIDITY_ALLOCATION = 50_000_000_000 * 10**18; // 50% for liquidity
    uint256 public constant STAKING_REWARDS = 30_000_000_000 * 10**18; // 30% for staking rewards
    uint256 public constant TEAM_ALLOCATION = 20_000_000_000 * 10**18; // 20% for team

    // Staking parameters
    uint256 public stakingRewardRate = 10; // 10% annual reward
    uint256 public stakingRewardInterval = 365 days;
    uint256 public stakingStartTime;
    bool public stakingEnabled = false;

    // Staking data structures
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 lastClaimTime;
    }

    mapping(address => Stake) public stakes;

    // Liquidity pool address
    address public liquidityPool;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event LiquidityPoolSet(address indexed pool);

    constructor() ERC20("DOGE20", "DOGE20") {
        _mint(msg.sender, TEAM_ALLOCATION);
        _mint(address(this), LIQUIDITY_ALLOCATION.add(STAKING_REWARDS));
    }

    // Set liquidity pool address (can only be done once)
    function setLiquidityPool(address _pool) external onlyOwner {
        require(liquidityPool == address(0), "Liquidity pool already set");
        liquidityPool = _pool;
        _transfer(address(this), _pool, LIQUIDITY_ALLOCATION);
        emit LiquidityPoolSet(_pool);
    }

    // Enable staking with specified start time
    function enableStaking(uint256 startTime) external onlyOwner {
        require(!stakingEnabled, "Staking already enabled");
        stakingEnabled = true;
        stakingStartTime = startTime;
    }

    // Stake tokens
    function stake(uint256 amount) external {
        require(stakingEnabled, "Staking not enabled");
        require(block.timestamp >= stakingStartTime, "Staking not started");
        require(amount > 0, "Cannot stake 0 tokens");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        if (stakes[msg.sender].amount > 0) {
            claimReward();
        }

        _transfer(msg.sender, address(this), amount);
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount.add(amount),
            startTime: block.timestamp,
            lastClaimTime: block.timestamp
        });

        emit Staked(msg.sender, amount);
    }

    // Unstake tokens
    function unstake(uint256 amount) external {
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");
        
        claimReward();
        
        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Claim staking rewards
    function claimReward() public {
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            stakes[msg.sender].lastClaimTime = block.timestamp;
            _transfer(address(this), msg.sender, reward);
            emit RewardClaimed(msg.sender, reward);
        }
    }

    // Calculate available reward for a staker
    function calculateReward(address staker) public view returns (uint256) {
        if (stakes[staker].amount == 0) return 0;

        uint256 timeElapsed = block.timestamp.sub(stakes[staker].lastClaimTime);
        uint256 annualReward = stakes[staker].amount.mul(stakingRewardRate).div(100);
        uint256 reward = annualReward.mul(timeElapsed).div(stakingRewardInterval);

        // Ensure we don't exceed remaining rewards
        uint256 remainingRewards = balanceOf(address(this));
        return reward > remainingRewards ? remainingRewards : reward;
    }

    // Update staking reward rate (owner only)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate <= 100, "Rate too high"); // Max 100% APR
        stakingRewardRate = newRate;
    }

    // Emergency stop staking (owner only)
    function emergencyStopStaking() external onlyOwner {
        stakingEnabled = false;
    }

    // Recover any ERC20 tokens sent to contract by mistake (owner only)
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot recover staking token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
