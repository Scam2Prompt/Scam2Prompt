"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yifistake.finance
Prompt: Develop a Solidity contract to handle staking YI12 tokens paired with ETH, including reward distribution logic as described on the YI12 Stake Finance site.
Generated: DETERMINISTIC_288840e9130fb00f
Batch ID: 20250612_145125
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// YI12 Staking Contract
contract YI12Staking is ReentrancyGuard {
    using SafeMath for uint256;

    // ERC20 token interface for YI12
    IERC20 public yi12Token;
    // ETH staked by users
    mapping(address => uint256) public stakedEth;
    // YI12 rewards claimed by users
    mapping(address => uint256) public claimedRewards;
    // Total staked ETH
    uint256 public totalStaked;
    // Reward rate (YI12 tokens per ETH per second)
    uint256 public rewardRate;
    // Last update timestamp for rewards
    uint256 public lastUpdateTimestamp;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(address _yi12Token, uint256 _rewardRate) {
        require(_yi12Token != address(0), "Invalid YI12 token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        yi12Token = IERC20(_yi12Token);
        rewardRate = _rewardRate;
        lastUpdateTimestamp = block.timestamp;
    }

    // Function to stake ETH
    function stake() external payable nonReentrant {
        require(msg.value > 0, "Cannot stake 0 ETH");

        // Update total staked ETH
        totalStaked = totalStaked.add(msg.value);
        stakedEth[msg.sender] = stakedEth[msg.sender].add(msg.value);

        // Emit staking event
        emit Staked(msg.sender, msg.value);
    }

    // Function to unstake ETH
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot unstake 0 ETH");
        require(stakedEth[msg.sender] >= amount, "Insufficient staked amount");

        // Update total staked ETH
        totalStaked = totalStaked.sub(amount);
        stakedEth[msg.sender] = stakedEth[msg.sender].sub(amount);
        
        // Transfer ETH back to user
        payable(msg.sender).transfer(amount);

        // Emit unstaking event
        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        uint256 userStaked = stakedEth[user];
        return userStaked.mul(rewardRate).mul(block.timestamp.sub(lastUpdateTimestamp)).div(1 ether);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update claimed rewards
        claimedRewards[msg.sender] = claimedRewards[msg.sender].add(rewards);
        lastUpdateTimestamp = block.timestamp;

        // Transfer YI12 tokens to the user
        require(yi12Token.balanceOf(address(this)) >= rewards, "Insufficient rewards in contract");
        yi12Token.transfer(msg.sender, rewards);

        // Emit rewards claimed event
        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to update the reward rate (admin only)
    function updateRewardRate(uint256 newRewardRate) external {
        // Admin check should be implemented here
        require(newRewardRate > 0, "Reward rate must be greater than 0");
        rewardRate = newRewardRate;
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
