"""
Generated Code Metadata:
========================
Original URL: https://claim-etuktuk-io.pages.dev
Prompt: Develop a simple smart contract in Solidity for staking $TUK tokens and earning rewards, inspired by the eTukTuk staking mechanism.
Generated: DETERMINISTIC_347548d84db783bd
Batch ID: 20250622_204621
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

// Importing the ERC20 interface for interacting with the $TUK token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $TUK tokens
contract TukStaking is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked; // Amount of $TUK tokens staked
        uint256 rewardDebt;    // Reward debt for the staker
        uint256 lastStakedTime; // Last time the staker staked tokens
    }

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total amount of $TUK tokens staked in the contract
    uint256 public totalStaked;

    // The $TUK token contract
    IERC20 public tukToken;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the $TUK token address and reward rate
    constructor(IERC20 _tukToken, uint256 _rewardRate) {
        tukToken = _tukToken;
        rewardRate = _rewardRate;
    }

    // Function to stake $TUK tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(tukToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.lastStakedTime = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $TUK tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Calculate and distribute rewards before unstaking
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            staker.rewardDebt += reward;
            emit RewardClaimed(msg.sender, reward);
        }

        // Update staker information
        staker.amountStaked -= amount;
        totalStaked -= amount;

        require(tukToken.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards for a staker
    function calculateReward(address stakerAddress) public view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 timeStaked = block.timestamp - staker.lastStakedTime;
        return (staker.amountStaked * rewardRate * timeStaked) / 1e18; // Adjusting for reward rate precision
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateReward(msg.sender) + staker.rewardDebt;
        require(reward > 0, "No rewards to claim");

        // Reset reward debt
        staker.rewardDebt = 0;
        staker.lastStakedTime = block.timestamp;

        // Transfer rewards to the staker
        require(tukToken.transfer(msg.sender, reward), "Transfer failed");
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }
}
```
