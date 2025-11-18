"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-claimportal.pages.dev
Prompt: Write a smart contract in Solidity for staking DOGE20 tokens on the Ethereum blockchain, ensuring rewards are distributed proportionally over a two-year period as described in the DOGE20 roadmap.
Generated: DETERMINISTIC_e4042728432d185c
Batch ID: 20250612_152235
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

// Import interfaces for ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the DOGE20 token
interface IDOGE20 is IERC20 {
    function mint(address to, uint256 amount) external;
}

// Staking contract for DOGE20 token
contract StakingDoge20 {
    using SafeMath for uint256;

    // Token to be staked
    IDOGE20 public doge20Token;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount;
        uint256 timestamp;
        uint256 rewards;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total rewards to be distributed over 2 years
    uint256 public totalRewards;
    uint256 public rewardDistributionStart;
    uint256 public rewardDuration = 365 days * 2; // 2 years in seconds

    // Events for staking and reward distribution
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the DOGE20 token address and total rewards
    constructor(address _doge20Token, uint256 _totalRewards) {
        doge20Token = IDOGE20(_doge20Token);
        totalRewards = _totalRewards;
        rewardDistributionStart = block.timestamp;
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(doge20Token.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        Stake storage userStake = stakes[msg.sender];
        userStake.amount = userStake.amount.add(_amount);
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount == 0) return 0;

        uint256 elapsed = block.timestamp.sub(userStake.timestamp);
        uint256 totalElapsedRevenue = (elapsed > rewardDuration) ? rewardDuration : elapsed;

        return userStake.amount.mul(totalRewards).div(totalRewardSupply()).mul(totalElapsedRevenue).div(rewardDuration);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        stakes[msg.sender].rewards = stakes[msg.sender].rewards.add(reward);
        doge20Token.mint(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to unstake DOGE20 tokens
    function unstake(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        userStake.amount = userStake.amount.sub(_amount);
        userStake.rewards = calculateRewards(msg.sender);
        userStake.timestamp = block.timestamp;

        require(doge20Token.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Function to get total supply of rewards based on total rewards schedule
    function totalRewardSupply() public view returns (uint256) {
        return totalRewards;
    }
}
```
