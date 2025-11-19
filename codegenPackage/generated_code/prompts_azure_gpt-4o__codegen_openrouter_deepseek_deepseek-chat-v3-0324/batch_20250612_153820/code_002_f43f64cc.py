"""
Generated Code Metadata:
========================
Original URL: https://good-games-guild.gitbook.io
Prompt: Generate code for a tier-based staking system for ArbiPad, incorporating the tier system details and user protection policy from the Good Games Guild documentation.
Generated: DETERMINISTIC_f43f64cc6a20018e
Batch ID: 20250612_153820
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract ArbiPadStaking is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    // Tier structure
    struct Tier {
        string name;
        uint256 minStake;
        uint256 allocationMultiplier; // Multiplier for IDO allocations
        uint256 lockPeriod; // In seconds
        uint256 rewardRate; // Reward tokens per second per staked token
    }

    // User staking details
    struct Stake {
        uint256 amount;
        uint256 tierIndex;
        uint256 stakedAt;
        uint256 lastRewardClaimedAt;
        uint256 unlockTime;
    }

    Tier[] public tiers;
    mapping(address => Stake) public stakes;
    mapping(address => bool) public isStaking;

    uint256 public totalStaked;
    uint256 public totalRewardsDistributed;

    event Staked(address indexed user, uint256 amount, uint256 tierIndex);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event TierAdded(uint256 index, string name, uint256 minStake, uint256 allocationMultiplier, uint256 lockPeriod, uint256 rewardRate);
    event TierUpdated(uint256 index, string name, uint256 minStake, uint256 allocationMultiplier, uint256 lockPeriod, uint256 rewardRate);

    constructor(address _stakingToken, address _rewardToken) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);

        // Initialize default tiers (example values)
        addTier("Bronze", 1000 ether, 1, 30 days, 1 ether / (30 days));
        addTier("Silver", 5000 ether, 2, 60 days, 2 ether / (30 days));
        addTier("Gold", 10000 ether, 3, 90 days, 3 ether / (30 days));
        addTier("Platinum", 25000 ether, 5, 120 days, 5 ether / (30 days));
    }

    // Add a new tier (only owner)
    function addTier(
        string memory _name,
        uint256 _minStake,
        uint256 _allocationMultiplier,
        uint256 _lockPeriod,
        uint256 _rewardRate
    ) public onlyOwner {
        tiers.push(
            Tier({
                name: _name,
                minStake: _minStake,
                allocationMultiplier: _allocationMultiplier,
                lockPeriod: _lockPeriod,
                rewardRate: _rewardRate
            })
        );
        emit TierAdded(tiers.length - 1, _name, _minStake, _allocationMultiplier, _lockPeriod, _rewardRate);
    }

    // Update an existing tier (only owner)
    function updateTier(
        uint256 _tierIndex,
        string memory _name,
        uint256 _minStake,
        uint256 _allocationMultiplier,
        uint256 _lockPeriod,
        uint256 _rewardRate
    ) public onlyOwner {
        require(_tierIndex < tiers.length, "Invalid tier index");
        
        tiers[_tierIndex] = Tier({
            name: _name,
            minStake: _minStake,
            allocationMultiplier: _allocationMultiplier,
            lockPeriod: _lockPeriod,
            rewardRate: _rewardRate
        });
        
        emit TierUpdated(_tierIndex, _name, _minStake, _allocationMultiplier, _lockPeriod, _rewardRate);
    }

    // Stake tokens into a specific tier
    function stake(uint256 _amount, uint256 _tierIndex) external nonReentrant {
        require(_tierIndex < tiers.length, "Invalid tier index");
        require(_amount >= tiers[_tierIndex].minStake, "Amount below tier minimum");
        require(!isStaking[msg.sender], "Already staking");

        // Transfer tokens from user to contract
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        Stake memory newStake = Stake({
            amount: _amount,
            tierIndex: _tierIndex,
            stakedAt: block.timestamp,
            lastRewardClaimedAt: block.timestamp,
            unlockTime: block.timestamp + tiers[_tierIndex].lockPeriod
        });

        stakes[msg.sender] = newStake;
        isStaking[msg.sender] = true;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount, _tierIndex);
    }

    // Unstake tokens (after lock period)
    function unstake() external nonReentrant {
        require(isStaking[msg.sender], "No active stake");
        Stake storage userStake = stakes[msg.sender];
        
        require(block.timestamp >= userStake.unlockTime, "Tokens still locked");

        // Claim any pending rewards first
        _claimRewards();

        uint256 amount = userStake.amount;
        totalStaked -= amount;

        // Clean up user stake
        delete stakes[msg.sender];
        isStaking[msg.sender] = false;

        // Return staked tokens
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Claim rewards without unstaking
    function claimRewards() external nonReentrant {
        require(isStaking[msg.sender], "No active stake");
        _claimRewards();
    }

    // Internal function to calculate and transfer rewards
    function _claimRewards() internal {
        Stake storage userStake = stakes[msg.sender];
        uint256 reward = calculateRewards(msg.sender);
        
        if (reward > 0) {
            userStake.lastRewardClaimedAt = block.timestamp;
            totalRewardsDistributed += reward;
            
            require(rewardToken.transfer(msg.sender, reward), "Reward transfer failed");
            emit RewardClaimed(msg.sender, reward);
        }
    }

    // Calculate pending rewards for a user
    function calculateRewards(address _user) public view returns (uint256) {
        if (!isStaking[_user]) return 0;
        
        Stake memory userStake = stakes[_user];
        Tier memory tier = tiers[userStake.tierIndex];
        
        uint256 timeElapsed = block.timestamp - userStake.lastRewardClaimedAt;
        return userStake.amount * tier.rewardRate * timeElapsed / 1 ether;
    }

    // Get user's current tier details
    function getUserTier(address _user) public view returns (Tier memory) {
        require(isStaking[_user], "User not staking");
        return tiers[stakes[_user].tierIndex];
    }

    // Get user's stake details
    function getUserStake(address _user) public view returns (Stake memory) {
        require(isStaking[_user], "User not staking");
        return stakes[_user];
    }

    // Emergency withdraw stuck tokens (only owner)
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(stakingToken), "Cannot withdraw staking token");
        IERC20(_token).transfer(owner(), _amount);
    }

    // Update reward token address (only owner)
    function setRewardToken(address _rewardToken) external onlyOwner {
        require(_rewardToken != address(0), "Invalid address");
        rewardToken = IERC20(_rewardToken);
    }

    // Update staking token address (only owner)
    function setStakingToken(address _stakingToken) external onlyOwner {
        require(_stakingToken != address(0), "Invalid address");
        stakingToken = IERC20(_stakingToken);
    }
}
```
