"""
Generated Code Metadata:
========================
Original URL: https://walletconnect.network
Prompt: Design a smart contract for staking and rewarding WCT tokens on the WalletConnect Network, considering scalability and decentralization.
Generated: DETERMINISTIC_a90c28741c0714d9
Batch ID: 20250622_205139
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

// Smart contract for staking and rewarding WCT tokens
contract WCTStaking is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked; // Amount of WCT tokens staked
        uint256 rewardDebt;    // Reward debt for the staker
        uint256 lastStakedTime; // Last time the staker staked tokens
    }

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total amount of WCT tokens staked in the contract
    uint256 public totalStaked;

    // Reward rate per second (in WCT tokens)
    uint256 public rewardRate;

    // The WCT token contract
    IERC20 public wctToken;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the WCT token address and reward rate
    constructor(IERC20 _wctToken, uint256 _rewardRate) {
        wctToken = _wctToken;
        rewardRate = _rewardRate;
    }

    // Function to stake WCT tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(wctToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.rewardDebt += calculateReward(msg.sender);
        staker.lastStakedTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake WCT tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update staker information
        staker.rewardDebt += calculateReward(msg.sender);
        staker.amountStaked -= amount;
        totalStaked -= amount;

        require(wctToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update reward debt
        staker.rewardDebt += reward;
        require(wctToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to calculate the reward for a staker
    function calculateReward(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 timeStaked = block.timestamp - staker.lastStakedTime;
        return (staker.amountStaked * rewardRate * timeStaked) / 1e18; // Adjusting for precision
    }

    // Function to set a new reward rate (only owner can call)
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    // Function to withdraw tokens in case of emergency (only owner can call)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(wctToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
