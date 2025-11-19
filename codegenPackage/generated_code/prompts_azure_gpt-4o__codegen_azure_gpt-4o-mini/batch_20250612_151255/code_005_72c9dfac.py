"""
Generated Code Metadata:
========================
Original URL: https://pixelverse-dashboard.pages.dev
Prompt: Create a smart contract for staking PIXFI tokens, ensuring compatibility with wallet connections like TON Wallet.
Generated: DETERMINISTIC_72c9dfac968ba1c4
Batch ID: 20250612_151255
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

// Staking contract for PIXFI tokens
contract PIXFIStaking is Ownable {
    // Token to be staked
    IERC20 public pixfiToken;

    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the PIXFI token address
    constructor(address _pixfiToken) {
        require(_pixfiToken != address(0), "Invalid token address");
        pixfiToken = IERC20(_pixfiToken);
    }

    // Function to stake PIXFI tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(pixfiToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to the contract
        pixfiToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake PIXFI tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update the user's stake
        userStake.amount -= amount;

        // Transfer tokens back to the user
        pixfiToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to get the staking timestamp of a user
    function getStakeTimestamp(address user) external view returns (uint256) {
        return stakes[user].timestamp;
    }

    // Function to withdraw any ERC20 tokens sent to the contract by mistake
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(pixfiToken), "Cannot withdraw staked token");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
