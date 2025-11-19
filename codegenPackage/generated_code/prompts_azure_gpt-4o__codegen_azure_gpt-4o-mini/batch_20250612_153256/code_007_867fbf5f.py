"""
Generated Code Metadata:
========================
Original URL: https://lookscoin.com
Prompt: Generate a Solidity contract that enables staking $LOOK tokens to form a branch and encode payment distribution for contributors.
Generated: DETERMINISTIC_867fbf5f9bf47fef
Batch ID: 20250612_153256
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

// Staking contract for $LOOK tokens
contract LookStaking is Ownable {
    // Token to be staked
    IERC20 public lookToken;

    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked;
        uint256 lastClaimed;
    }

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event Claimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the token address
    constructor(IERC20 _lookToken) {
        lookToken = _lookToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(lookToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.lastClaimed = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update staker information
        staker.amountStaked -= amount;
        require(lookToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards (dummy implementation)
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update last claimed time
        staker.lastClaimed = block.timestamp;

        // Transfer rewards (dummy implementation)
        require(lookToken.transfer(msg.sender, rewards), "Transfer failed");

        emit Claimed(msg.sender, rewards);
    }

    // Function to calculate rewards (dummy implementation)
    function calculateRewards(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        // Simple reward calculation based on staked amount and time
        return (staker.amountStaked * (block.timestamp - staker.lastClaimed)) / 1 days; // 1 day reward
    }

    // Function to get staker information
    function getStakerInfo(address stakerAddress) external view returns (uint256 amountStaked, uint256 lastClaimed) {
        Staker storage staker = stakers[stakerAddress];
        return (staker.amountStaked, staker.lastClaimed);
    }
}
```
