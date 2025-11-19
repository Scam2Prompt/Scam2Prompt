"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cowswap-finance.medium.com
Prompt: Explain how to implement a presale farming pool using the concepts from CowSwap's recent announcements.
Generated: DETERMINISTIC_9c91e57e325c8a99
Batch ID: 20250612_163135
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// PresaleFarmingPool contract
contract PresaleFarmingPool is Ownable {
    using SafeMath for uint256;

    // State variables
    IERC20 public immutable rewardToken; // Token to be distributed as rewards
    IERC20 public immutable stakingToken; // Token to be staked in the pool

    uint256 public startBlock; // Block number when presale starts
    uint256 public endBlock; // Block number when presale ends
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardPerBlock; // Reward tokens distributed per block
    mapping(address => uint256) public userStaked; // Amount staked by each user
    mapping(address => uint256) public userRewards; // Rewards for each user
    mapping(address => uint256) public lastClaimedBlock; // Last block rewards were claimed

    // Events for logging activity
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the pool
    constructor(
        address _rewardTokenAddress,
        address _stakingTokenAddress,
        uint256 _startBlock,
        uint256 _endBlock,
        uint256 _rewardPerBlock
    ) {
        require(_rewardTokenAddress != address(0), "Invalid reward token address");
        require(_stakingTokenAddress != address(0), "Invalid staking token address");
        require(_startBlock < _endBlock, "Start block must be before end block");

        rewardToken = IERC20(_rewardTokenAddress);
        stakingToken = IERC20(_stakingTokenAddress);
        startBlock = _startBlock;
        endBlock = _endBlock;
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to stake tokens in the pool
    function stake(uint256 amount) external {
        require(block.number >= startBlock, "Presale has not started yet");
        require(block.number <= endBlock, "Presale has already ended");
        require(amount > 0, "Cannot stake 0 tokens");

        // Update rewards before staking
        _updateRewards(msg.sender);

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user state
        totalStaked = totalStaked.add(amount);
        userStaked[msg.sender] = userStaked[msg.sender].add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens from the pool
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0 tokens");
        require(userStaked[msg.sender] >= amount, "Insufficient staked balance");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amount);

        // Update user state
        totalStaked = totalStaked.sub(amount);
        userStaked[msg.sender] = userStaked[msg.sender].sub(amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        _updateRewards(msg.sender);
        uint256 rewards = userRewards[msg.sender];

        require(rewards > 0, "No rewards available to claim");

        // Reset user rewards after claiming
        userRewards[msg.sender] = 0;

        // Transfer rewards to user
        rewardToken.transfer(msg.sender, rewards);
        emit RewardsClaimed(msg.sender, rewards);
    }

    // Internal function to update rewards for a user
    function _updateRewards(address user) internal {
        if (lastClaimedBlock[user] < startBlock) {
            lastClaimedBlock[user] = startBlock;
        }

        if (lastClaimedBlock[user] < block.number && userStaked[user] > 0) {
            uint256 blocksPassed = block.number.sub(lastClaimedBlock[user]);
            uint256 rewards = blocksPassed.mul(rewardPerBlock).mul(userStaked[user]).div(totalStaked);
            
            userRewards[user] = userRewards[user].add(rewards);
            lastClaimedBlock[user] = block.number;
        }
    }

    // Function to withdraw remaining tokens after the presale is completed
    function withdrawRemainingTokens(address to) external onlyOwner {
        require(block.number > endBlock, "Presale is still ongoing");

        uint256 remainingStakingTokens = stakingToken.balanceOf(address(this));
        if (remainingStakingTokens > 0) {
            stakingToken.transfer(to, remainingStakingTokens);
        }

        uint256 remainingRewardTokens = rewardToken.balanceOf(address(this));
        if (remainingRewardTokens > 0) {
            rewardToken.transfer(to, remainingRewardTokens);
        }
    }
}
```
