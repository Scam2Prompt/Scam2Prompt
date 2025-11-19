"""
Generated Code Metadata:
========================
Original URL: https://presale-poodlinu.pages.dev
Prompt: Develop a smart contract for the Poodl Inu staking mechanism that locks tokens and calculates rewards based on the staking percentage (59%) and the annual return rate.
Generated: DETERMINISTIC_1123881d910c8626
Batch ID: 20250612_153400
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

// Staking contract for Poodl Inu
contract PoodlInuStaking is Ownable {
    // Token to be staked
    IERC20 public stakingToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Annual return rate (in basis points, e.g., 500 = 5%)
    uint256 public annualReturnRate = 500; // 5% annual return
    // Staking percentage (in basis points, e.g., 5900 = 59%)
    uint256 public stakingPercentage = 5900; // 59%

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    // Constructor to set the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate rewards based on the staked amount and time
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        // Calculate the time staked in years
        uint256 stakedDuration = block.timestamp - userStake.timestamp;
        uint256 yearsStaked = stakedDuration / 365 days;

        // Calculate reward based on the annual return rate and staking percentage
        uint256 reward = (userStake.amount * annualReturnRate * yearsStaked * stakingPercentage) / (10000 * 100);
        return reward;
    }

    // Function to withdraw staked tokens and rewards
    function withdraw() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);
        uint256 totalAmount = userStake.amount + reward;

        // Reset user's stake information
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].timestamp = 0;

        // Transfer staked tokens and rewards back to the user
        stakingToken.transfer(msg.sender, totalAmount);

        emit Withdrawn(msg.sender, userStake.amount, reward);
    }

    // Function to update the annual return rate (only owner can call)
    function updateAnnualReturnRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Rate must be greater than 0");
        annualReturnRate = newRate;
    }

    // Function to update the staking percentage (only owner can call)
    function updateStakingPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 10000, "Percentage must be 100% or less");
        stakingPercentage = newPercentage;
    }
}
```
