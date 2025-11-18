"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presalenest-goodeggtoken.web.app
Prompt: Create a Solidity function for staking $GEGG tokens, allowing users to earn rewards based on their stake duration, as mentioned in the roadmap.
Generated: DETERMINISTIC_2f50479ff2938075
Batch ID: 20250612_145521
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the GEGG token
interface IGEGG is IERC20 {
    function mint(address to, uint256 amount) external;
}

contract StakingContract is Ownable {
    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount staked
        uint256 startTime; // Timestamp when staking started
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) private stakes;

    // Total rewards accumulated
    uint256 public totalRewards;

    // The GEGG token contract
    IGEGG public geggToken;

    // Reward rate per second (in GEGG tokens)
    uint256 public rewardRate;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to initialize the token and reward rate
    constructor(IGEGG _geggToken, uint256 _rewardRate) {
        geggToken = _geggToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(geggToken.balanceOf(msg.sender) >= amount, "Insufficient GEGG balance");

        // Transfer GEGG tokens from user to contract
        geggToken.transferFrom(msg.sender, address(this), amount);

        // Create or update the stake for the user
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate and return the rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }
        uint256 duration = block.timestamp - userStake.startTime;
        return (userStake.amount * rewardRate * duration) / 1e18; // Adjust for reward precision
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 reward = calculateRewards(msg.sender);

        // Update total rewards
        totalRewards += reward;

        // Transfer staked tokens back to the user
        uint256 amountToReturn = userStake.amount;
        userStake.amount = 0; // Reset user's stake to 0

        // Transfer the GEGG tokens and rewards
        geggToken.transfer(msg.sender, amountToReturn);
        geggToken.mint(msg.sender, reward); // Mint rewards for the user

        emit Unstaked(msg.sender, amountToReturn, reward);
    }

    // Function to withdraw accidental ERC20 tokens sent to the contract
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != geggToken, "Cannot withdraw GEGG tokens");
        token.transfer(msg.sender, amount);
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    // Function to get the stake details of a user
    function getStakeDetails(address user) external view returns (uint256 amount, uint256 startTime) {
        Stake memory userStake = stakes[user];
        return (userStake.amount, userStake.startTime);
    }
}
```
