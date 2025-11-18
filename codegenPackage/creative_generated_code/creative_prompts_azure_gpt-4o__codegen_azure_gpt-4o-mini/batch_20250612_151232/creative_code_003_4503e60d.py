"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-en.pages.dev
Prompt: Create a Solidity function for staking Pushd tokens, allowing users to earn interest between 7% to 17% based on the number of tokens staked.
Generated: DETERMINISTIC_4503e60db576bc27
Batch ID: 20250612_151232
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

contract PushdStaking {
    // State variable to hold the Pushd token contract address
    IERC20 public pushdToken;
    
    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the staking
    }

    // Mapping from user addresses to their staking details
    mapping(address => Stake) public stakes;

    // Event to emit when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event to emit when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Interest rate for staking
    uint256 public constant MIN_RATE = 7; // Minimum interest rate
    uint256 public constant MAX_RATE = 17; // Maximum interest rate
    uint256 public constant RATE_INCREMENT = 1; // Increment for interest rate based on staking amount threshold

    // Constructor to set the Pushd token contract address
    constructor(address _pushdToken) {
        pushdToken = IERC20(_pushdToken);
    }

    // Function to stake Pushd tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(pushdToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate earned interest based on staked amount and time
    function calculateRewards(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 interestRate = getInterestRate(userStake.amount);
        uint256 rewards = (userStake.amount * interestRate * stakingDuration) / (100 * 365 days);

        return rewards;
    }

    // Function to get interest rate based on staked amount
    function getInterestRate(uint256 amount) internal pure returns (uint256) {
        if (amount < 1000 * 10 ** 18) {
            return MIN_RATE;
        } else if (amount < 5000 * 10 ** 18) {
            return MIN_RATE + RATE_INCREMENT;
        } else {
            return MAX_RATE;
        }
    }

    // Function for users to claim their rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        stakes[msg.sender].timestamp = block.timestamp; // Resetting timestamp after claiming
        require(pushdToken.transfer(msg.sender, rewards), "Rewards transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to allow users to withdraw their staked tokens (no rewards)
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens to withdraw");

        uint256 amountToWithdraw = userStake.amount;
        userStake.amount = 0; // Reset the user's stake

        require(pushdToken.transfer(msg.sender, amountToWithdraw), "Token transfer failed");
    }
}

// Interface for ERC20 token interaction
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
