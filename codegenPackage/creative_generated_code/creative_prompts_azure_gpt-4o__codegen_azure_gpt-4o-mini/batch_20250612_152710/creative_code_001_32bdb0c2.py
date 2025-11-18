"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mission-nyanheroe.pages.dev
Prompt: Generate a smart contract in Solidity for a mission-based reward system where users earn $NYAN tokens upon task completion.
Generated: DETERMINISTIC_32bdb0c204cd7b1a
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

// Importing OpenZeppelin's ERC20 contract for token creation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// This contract implements a mission-based reward system using the NYAN tokens
contract NyanToken is ERC20, Ownable {

    // Event emitted when a user completes a mission and earns tokens
    event MissionCompleted(address indexed user, uint256 rewardAmount);

    // Mapping to keep track of completed missions per user
    mapping(address => uint256) public missionsCompleted;

    // Constructor that initializes the token supply and assigns it to the owner
    constructor() ERC20("NyanToken", "NYAN") {
        // Mint initial supply of 1,000,000 NYAN tokens to the contract owner
        _mint(msg.sender, 1_000_000 * 10 ** decimals());
    }

    // Function to complete a mission and reward the user with tokens
    function completeMission(address user, uint256 rewardAmount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(rewardAmount > 0, "Reward amount must be greater than zero");

        // Increase the count of completed missions for the user
        missionsCompleted[user] += 1;

        // Mint new tokens as a reward for completing the mission
        _mint(user, rewardAmount);
        
        // Emit an event for the mission completion
        emit MissionCompleted(user, rewardAmount);
    }

    // Function to get the number of missions completed by a user
    function getMissionsCompleted(address user) external view returns (uint256) {
        return missionsCompleted[user];
    }

    // Function to withdraw tokens from the contract (onlyOwner)
    function withdrawTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid withdrawal address");
        require(balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer specified amount of tokens to the withdrawal address
        _transfer(address(this), to, amount);
    }
}
```
