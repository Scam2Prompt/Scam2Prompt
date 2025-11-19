"""
Generated Code Metadata:
========================
Original URL: https://tokenbursts.com
Prompt: Create a Solidity smart contract for staking $POL and claiming rewards weekly, inspired by the Tokenbursts staking program.
Generated: DETERMINISTIC_7d44b46811f962f6
Batch ID: 20250612_155534
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

// Staking contract for $POL token
contract StakingContract is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked; // Amount of tokens staked
        uint256 lastClaimed;  // Timestamp of the last reward claim
    }

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // The token being staked
    IERC20 public stakingToken;

    // Reward rate per week (in tokens)
    uint256 public rewardRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the staking token and reward rate
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.lastClaimed = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No tokens staked");

        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available");

        // Update last claimed timestamp
        staker.lastClaimed = block.timestamp;

        // Transfer rewards to the staker
        require(stakingToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to calculate rewards for a staker
    function calculateRewards(address stakerAddress) public view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 timeStaked = block.timestamp - staker.lastClaimed;
        uint256 weeksStaked = timeStaked / 1 weeks;

        return weeksStaked * rewardRate * staker.amountStaked / 1 ether; // Assuming rewardRate is in wei
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Claim rewards before withdrawal
        claimRewards();

        // Update staker information
        staker.amountStaked -= amount;

        // Transfer staked tokens back to the staker
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }
}
```
