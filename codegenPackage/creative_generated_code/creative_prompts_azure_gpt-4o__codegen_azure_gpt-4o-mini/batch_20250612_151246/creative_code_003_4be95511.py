"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-app.pages.dev
Prompt: Develop a Solidity contract for a play-to-earn game that integrates $KANG token rewards based on Kangamoon's roadmap for in-game rewards structure.
Generated: DETERMINISTIC_4be9551157a6465d
Batch ID: 20250612_151246
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

// Importing the ERC20 interface to interact with the $KANG token contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// A simple PlayToEarn contract for earning $KANG tokens
contract PlayToEarn is Ownable {
    // State variables
    IERC20 public kangToken;  // The $KANG token contract
    mapping(address => uint256) public playerRewards;  // Mapping to track player rewards
    mapping(address => bool) public hasClaimed;  // Track whether the player has claimed their rewards

    // Event declaration for reward claims
    event RewardClaimed(address indexed player, uint256 amount);

    // Constructor to set the $KANG token address
    constructor(address _kangTokenAddress) {
        require(_kangTokenAddress != address(0), "Invalid token address");
        kangToken = IERC20(_kangTokenAddress);
    }

    // Function to reward players with $KANG tokens based on in-game activity
    function rewardPlayer(address player, uint256 amount) external onlyOwner {
        require(player != address(0), "Invalid player address");
        require(amount > 0, "Amount must be greater than zero");

        playerRewards[player] += amount;
    }

    // Function for players to claim their rewards
    function claimRewards() external {
        uint256 rewardAmount = playerRewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");
        require(!hasClaimed[msg.sender], "Rewards already claimed");

        // Resetting the player's rewards to prevent re-entrancy attacks
        playerRewards[msg.sender] = 0;
        hasClaimed[msg.sender] = true;

        // Transfer $KANG tokens to the player
        require(kangToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance");
        bool sent = kangToken.transfer(msg.sender, rewardAmount);
        require(sent, "Failed to transfer $KANG tokens");

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    // Function to withdraw tokens from the contract in case of emergencies
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20 token = IERC20(tokenAddress);
        uint256 contractBalance = token.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient contract balance");

        bool sent = token.transfer(msg.sender, amount);
        require(sent, "Failed to transfer tokens");
    }
}
```
