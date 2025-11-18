"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-earthmeta.pages.dev
Prompt: Write a smart contract in Solidity for staking $EMT tokens on the EarthMeta platform, ensuring compatibility with Ethereum and Polygon blockchains.
Generated: DETERMINISTIC_f9e39c999b399fed
Batch ID: 20250612_151219
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

// Importing required interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// EarthMeta Staking Contract
contract EarthMetaStaking is Ownable, ReentrancyGuard {
    // Define the EMT token interface
    IERC20 public emtToken;

    // Staking structure to store user information
    struct Stake {
        uint256 amount;     // Amount of tokens staked
        uint256 timestamp;  // Time when the tokens were staked
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the EMT token address
    constructor(address _emtToken) {
        require(_emtToken != address(0), "Invalid token address");
        emtToken = IERC20(_emtToken);
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(emtToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the user to the contract
        emtToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user's stake information
        userStake.amount -= amount;

        // Transfer tokens back to the user
        emtToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to view staking details
    function getStakeDetails(address user) external view returns (uint256 amount, uint256 timestamp) {
        Stake storage userStake = stakes[user];
        return (userStake.amount, userStake.timestamp);
    }

    // Function to withdraw ERC20 tokens accidentally sent to the contract
    function recoverTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(emtToken), "Cannot recover staking token");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
