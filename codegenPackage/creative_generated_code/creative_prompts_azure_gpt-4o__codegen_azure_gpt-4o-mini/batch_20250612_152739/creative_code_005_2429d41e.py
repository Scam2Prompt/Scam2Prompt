"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-de.web.app
Prompt: Develop a staking pool smart contract in Solidity that allows users to stake $MGLS tokens and earn rewards based on their share of the pool.
Generated: DETERMINISTIC_2429d41ecd2e9e55
Batch ID: 20250612_152739
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

// Import the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Staking Pool Contract
contract StakingPool {
    // Token used for staking
    IERC20 public immutable stakingToken;
    
    // Struct to hold user staking data
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Total amount staked in the pool
    uint256 public totalStaked;
    
    // Total rewards distributed
    uint256 public totalRewards;

    // Reward per token staked
    uint256 public rewardPerTokenStored;
    
    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);
    
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Modifier to update rewards before any action
    modifier updateReward(address account) {
        if (totalStaked > 0) {
            rewardPerTokenStored = rewardPerToken();
        }
        if (account != address(0)) {
            stakes[account].rewardDebt = earned(account);
        }
        _;
    }

    // Function to stake tokens
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");

        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        stakes[msg.sender].amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient balance");

        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;

        stakingToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = earned(msg.sender);
        require(reward > 0, "No rewards to claim");

        stakes[msg.sender].rewardDebt = 0; // Reset reward debt
        totalRewards += reward;

        // Transfer rewards (you need to implement this mechanism)
        // For example, transfer from a rewards pool or mint new tokens
        // rewardsToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Function to calculate reward per token staked
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + ((totalRewards * 1e18) / totalStaked);
    }

    // Function to calculate earned rewards for a user
    function earned(address account) public view returns (uint256) {
        return (stakes[account].amount * rewardPerToken()) / 1e18 - stakes[account].rewardDebt;
    }

    // Function to set total rewards (for demonstration purposes)
    function setRewards(uint256 rewards) external {
        totalRewards += rewards; // Only for testing; replace with an access control mechanism
    }
}
```
