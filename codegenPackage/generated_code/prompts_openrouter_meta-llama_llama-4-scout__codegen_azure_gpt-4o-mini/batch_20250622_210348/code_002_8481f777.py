"""
Generated Code Metadata:
========================
Original URL: https://pushd-store-en.pages.dev
Prompt: "Generate a Solidity code for a staking protocol that rewards users with 7-17% interest based on the number of tokens held, as outlined in the Pushd tokenomics."
Generated: DETERMINISTIC_8481f777b2dc980a
Batch ID: 20250622_210348
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for a token with variable interest rates based on the amount staked
contract StakingProtocol is Ownable {
    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // The token being staked
    IERC20 public stakingToken;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate the reward based on the amount staked
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        // Determine interest rate based on the amount staked
        uint256 interestRate = getInterestRate(userStake.amount);
        uint256 stakingDuration = block.timestamp - userStake.timestamp;

        // Calculate reward: (amount * interestRate * duration) / (365 days)
        return (userStake.amount * interestRate * stakingDuration) / (365 days * 100);
    }

    // Function to get interest rate based on the amount staked
    function getInterestRate(uint256 amount) internal pure returns (uint256) {
        if (amount < 1000 * 10**18) {
            return 7; // 7% for less than 1000 tokens
        } else if (amount < 5000 * 10**18) {
            return 10; // 10% for 1000 to 4999 tokens
        } else if (amount < 10000 * 10**18) {
            return 13; // 13% for 5000 to 9999 tokens
        } else {
            return 17; // 17% for 10000 tokens and above
        }
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate the reward
        uint256 reward = calculateReward(msg.sender);

        // Reset user's stake information
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].timestamp = 0;

        // Transfer staked tokens and reward to the user
        stakingToken.transfer(msg.sender, userStake.amount);
        if (reward > 0) {
            stakingToken.transfer(msg.sender, reward); // Assuming rewards are also in the same token
        }

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    // Function to check the user's stake amount
    function getStakeAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
}
```
