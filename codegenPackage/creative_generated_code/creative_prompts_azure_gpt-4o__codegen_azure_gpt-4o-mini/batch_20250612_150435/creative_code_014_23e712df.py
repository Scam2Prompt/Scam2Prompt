"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudoprotocols.web.app
Prompt: Generate a smart contract in Solidity for distributing referral bonuses in USDT to users based on their leaderboard rankings.
Generated: DETERMINISTIC_23e712df512249fe
Batch ID: 20250612_150435
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

// Importing ERC20 interface to interact with USDT tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract ReferralBonus {
    // State variables
    IERC20 public usdtToken; // USDT token contract reference
    address public owner;     // Contract owner address
    uint256 public bonusAmount; // Amount of USDT to distribute per rank
    mapping(address => uint256) public leaderboard; // User leaderboard rankings
    mapping(address => bool) public hasClaimed; // Tracking which users have claimed bonuses

    // Events
    event BonusDistributed(address indexed user, uint256 amount);
    event LeaderboardUpdated(address indexed user, uint256 rank);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(address _usdtToken, uint256 _bonusAmount) {
        usdtToken = IERC20(_usdtToken);
        owner = msg.sender; // Set the contract deployer as the owner
        bonusAmount = _bonusAmount; // Set the referral bonus amount
    }

    // Function to update leaderboard rankings
    function updateLeaderboard(address user, uint256 rank) external onlyOwner {
        require(rank > 0, "Rank must be greater than zero");
        leaderboard[user] = rank; // Update the user's rank
        emit LeaderboardUpdated(user, rank); // Emit an event for leaderboard updates
    }

    // Function for users to claim their referral bonus based on their ranking
    function claimBonus() external {
        require(leaderboard[msg.sender] > 0, "You are not ranked on the leaderboard");
        require(!hasClaimed[msg.sender], "Bonus has already been claimed");

        // Transfer USDT tokens to the user
        uint256 amountToTransfer = bonusAmount;
        require(usdtToken.balanceOf(address(this)) >= amountToTransfer, "Insufficient contract balance");
        require(usdtToken.transfer(msg.sender, amountToTransfer), "Transfer failed");

        hasClaimed[msg.sender] = true; // Mark the bonus as claimed
        emit BonusDistributed(msg.sender, amountToTransfer); // Emit a bonus distribution event
    }

    // Function to withdraw tokens from the contract (for owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(usdtToken.balanceOf(address(this)) >= amount, "Insufficient balance in contract");

        // Transfer tokens to the owner
        require(usdtToken.transfer(owner, amount), "Transfer failed");
    }

    // Fallback function to prevent sending Ether to the contract
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```
