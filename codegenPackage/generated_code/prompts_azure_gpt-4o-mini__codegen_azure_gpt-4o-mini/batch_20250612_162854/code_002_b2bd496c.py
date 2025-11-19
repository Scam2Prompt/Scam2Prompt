"""
Generated Code Metadata:
========================
Original URL: https://galaxyfoxs.live
Prompt: Create a Solidity smart contract that implements the staking mechanism for $GFOX tokens, including the 2% transaction reward feature.
Generated: DETERMINISTIC_b2bd496c7153f8ec
Batch ID: 20250612_162854
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

// Staking contract for $GFOX tokens
contract GFOXStaking is Ownable {
    // Token interface
    IERC20 public gfoxToken;

    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are distributed
    event RewardDistributed(address indexed user, uint256 reward);

    // Constructor to set the GFOX token address
    constructor(address _gfoxToken) {
        require(_gfoxToken != address(0), "Invalid token address");
        gfoxToken = IERC20(_gfoxToken);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(gfoxToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the user to the contract
        gfoxToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards (2% of the staked amount)
        uint256 reward = (userStake.amount * 2) / 100;

        // Update the user's stake before transferring tokens
        uint256 totalAmount = userStake.amount + reward;
        userStake.amount = 0; // Reset the stake amount

        // Transfer the staked tokens and rewards back to the user
        gfoxToken.transfer(msg.sender, totalAmount);

        emit Unstaked(msg.sender, totalAmount);
        emit RewardDistributed(msg.sender, reward);
    }

    // Function to check the user's stake
    function getStake(address user) external view returns (uint256 amount, uint256 timestamp) {
        Stake storage userStake = stakes[user];
        return (userStake.amount, userStake.timestamp);
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(gfoxToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        gfoxToken.transfer(msg.sender, amount);
    }
}
```
