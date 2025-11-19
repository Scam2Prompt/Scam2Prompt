"""
Generated Code Metadata:
========================
Original URL: https://xpxpay.pages.dev
Prompt: How can I implement a staking protocol in a smart contract that rewards XPX token holders based on buy and sell tax contributions?
Generated: DETERMINISTIC_86581743e83e0ee7
Batch ID: 20250612_163751
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

// Staking contract for XPX token holders
contract StakingProtocol is Ownable {
    // Token to be staked
    IERC20 public xpxToken;

    // Struct to hold user staking information
    struct Staker {
        uint256 amountStaked;
        uint256 lastClaimed;
    }

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total amount of XPX tokens staked
    uint256 public totalStaked;

    // Tax contribution rate (in basis points, e.g., 500 = 5%)
    uint256 public taxRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the XPX token address and tax rate
    constructor(IERC20 _xpxToken, uint256 _taxRate) {
        xpxToken = _xpxToken;
        taxRate = _taxRate;
    }

    // Function to stake XPX tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(xpxToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staker information
        stakers[msg.sender].amountStaked += amount;
        stakers[msg.sender].lastClaimed = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake XPX tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakers[msg.sender].amountStaked >= amount, "Insufficient staked amount");

        // Update staker information
        stakers[msg.sender].amountStaked -= amount;
        totalStaked -= amount;

        require(xpxToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards based on tax contributions
    function calculateRewards(address stakerAddress) public view returns (uint256) {
        uint256 stakedAmount = stakers[stakerAddress].amountStaked;
        uint256 totalTaxContributions = totalStaked * taxRate / 10000; // Convert basis points to percentage

        if (totalTaxContributions == 0 || totalStaked == 0) {
            return 0;
        }

        return (stakedAmount * totalTaxContributions) / totalStaked;
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Update last claimed timestamp
        stakers[msg.sender].lastClaimed = block.timestamp;

        // Transfer rewards to the staker
        require(xpxToken.transfer(msg.sender, rewards), "Transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to update the tax rate (only owner can call)
    function updateTaxRate(uint256 newTaxRate) external onlyOwner {
        require(newTaxRate <= 10000, "Tax rate must be in basis points (max 10000)");
        taxRate = newTaxRate;
    }
}
```
