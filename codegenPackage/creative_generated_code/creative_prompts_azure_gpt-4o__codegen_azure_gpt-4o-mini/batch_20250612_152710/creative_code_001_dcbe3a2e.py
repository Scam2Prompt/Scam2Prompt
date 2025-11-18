"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-d.pages.dev
Prompt: Generate code to integrate DOGE20 token staking functionality into a decentralized application (dApp) using the ERC-20 token standard and Ethereum smart contracts.
Generated: DETERMINISTIC_dcbe3a2e9f6081b6
Batch ID: 20250612_152710
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

// Import the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for DOGE20 staking
contract Doge20Staking is Ownable {
    // The ERC20 token being staked
    IERC20 public doge20Token;

    // Structure to hold user staking information
    struct Staker {
        uint256 amountStaked;
        uint256 lastClaimed;
    }

    // Mapping of user addresses to their staking information
    mapping(address => Staker) public stakers;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the token address
    constructor(address _doge20Token) {
        require(_doge20Token != address(0), "Invalid token address");
        doge20Token = IERC20(_doge20Token);
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from the user to the contract
        doge20Token.transferFrom(msg.sender, address(this), amount);

        // Update the staker's information
        stakers[msg.sender].amountStaked += amount;
        stakers[msg.sender].lastClaimed = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake DOGE20 tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Not enough staked tokens");

        // Update the staker's information
        staker.amountStaked -= amount;

        // Transfer tokens back to the user
        doge20Token.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards (dummy implementation)
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);
        
        // Update the last claimed time
        staker.lastClaimed = block.timestamp;

        // Transfer the rewards to the user (dummy implementation)
        doge20Token.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to calculate rewards based on staking duration
    function calculateRewards(address stakerAddress) internal view returns (uint256) {
        Staker memory staker = stakers[stakerAddress];
        uint256 stakingDuration = block.timestamp - staker.lastClaimed;

        // Example reward calculation (1 token per second staked)
        return (stakingDuration * staker.amountStaked) / 1e18; // Adjust according to your reward strategy
    }

    // Function to withdraw tokens from the contract (emergency only)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(doge20Token.balanceOf(address(this)) >= amount, "Insufficient balance");
        doge20Token.transfer(msg.sender, amount);
    }
}
```

Make sure to adjust the reward calculation logic and any other parameters as per your specific project requirements before deploying the contract.
