"""
Generated Code Metadata:
========================
Original URL: https://paraswap-3y3.pages.dev
Prompt: Generate a smart contract code that implements ParaSwap's staking mechanism for PSP/ETH, allowing users to stake and earn rewards in the form of gas refunds.
Generated: DETERMINISTIC_9c9cd43610d88b13
Batch ID: 20250622_204955
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the ParaSwap token (PSP)
interface IParaSwap is IERC20 {
    function mint(address to, uint256 amount) external;
}

// Staking contract for PSP/ETH
contract ParaSwapStaking is Ownable {
    // State variables
    IParaSwap public pspToken; // PSP token contract
    uint256 public totalStaked; // Total amount of PSP staked
    uint256 public rewardRate; // Reward rate for gas refunds
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public rewards; // Rewards for each user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the PSP token address and reward rate
    constructor(IParaSwap _pspToken, uint256 _rewardRate) {
        pspToken = _pspToken;
        rewardRate = _rewardRate;
    }

    // Function to stake PSP tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(pspToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staked amount and total staked
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake PSP tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update staked amount and total staked
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(pspToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate and claim rewards
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available");

        // Update rewards and mint new tokens
        rewards[msg.sender] = 0;
        pspToken.mint(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards for a user
    function calculateRewards(address user) internal view returns (uint256) {
        return (stakedAmount[user] * rewardRate) / 1e18; // Assuming rewardRate is in wei
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw any ERC20 tokens sent to the contract by mistake (only owner)
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
