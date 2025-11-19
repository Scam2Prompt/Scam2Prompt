"""
Generated Code Metadata:
========================
Original URL: https://yifistake.finance
Prompt: Write a smart contract in Solidity to enable staking and farming of YI12 tokens, including functionality for claiming rewards and unfarming as described on the YI12 Stake Finance platform.
Generated: DETERMINISTIC_9045404a100d1b5d
Batch ID: 20250612_145125
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

// Interface for the YI12 token
interface IYI12Token is IERC20 {
    function mint(address to, uint256 amount) external;
}

// Staking and Farming contract for YI12 tokens
contract YI12StakeFarm is Ownable {
    // Struct to hold user staking information
    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
        uint256 lastStakedTime; // Last time the user staked
    }

    // Mapping of user addresses to their staking information
    mapping(address => StakeInfo) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate per second (in YI12 tokens)
    uint256 public rewardRate;

    // The YI12 token contract
    IYI12Token public yi12Token;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IYI12Token _yi12Token, uint256 _rewardRate) {
        yi12Token = _yi12Token;
        rewardRate = _rewardRate;
    }

    // Function to stake YI12 tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(yi12Token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's stake information
        StakeInfo storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.rewardDebt += calculatePendingRewards(msg.sender);
        userStake.lastStakedTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake YI12 tokens
    function unstake(uint256 amount) external {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Claim rewards before unstaking
        claimRewards();

        // Update user's stake information
        userStake.amount -= amount;
        totalStaked -= amount;

        require(yi12Token.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() public {
        StakeInfo storage userStake = stakes[msg.sender];
        uint256 pendingRewards = calculatePendingRewards(msg.sender);

        require(pendingRewards > 0, "No rewards to claim");

        // Update reward debt
        userStake.rewardDebt += pendingRewards;
        userStake.lastStakedTime = block.timestamp;

        // Mint and transfer rewards to the user
        yi12Token.mint(msg.sender, pendingRewards);

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    // Internal function to calculate pending rewards for a user
    function calculatePendingRewards(address user) internal view returns (uint256) {
        StakeInfo storage userStake = stakes[user];
        uint256 timeStaked = block.timestamp - userStake.lastStakedTime;
        return (userStake.amount * rewardRate * timeStaked) / 1e18; // Adjusting for precision
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(yi12Token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
