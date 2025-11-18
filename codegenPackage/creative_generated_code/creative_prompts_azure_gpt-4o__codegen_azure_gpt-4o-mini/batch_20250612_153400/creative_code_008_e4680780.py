"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyanheroes.pages.dev
Prompt: Create a smart contract example for distributing $NYAN rewards based on mission completion and referral activities in the Nyan Heroes game.
Generated: DETERMINISTIC_e46807800c8c1432
Batch ID: 20250612_153400
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Contract to manage the distribution of $NYAN rewards
contract NyanRewards {
    // Token interface for $NYAN
    IERC20 public nyanToken;

    // Struct to hold player information
    struct Player {
        uint256 totalRewards;
        uint256 missionsCompleted;
        uint256 referrals;
    }

    // Mapping of player addresses to their respective info
    mapping(address => Player) public players;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed player, uint256 amount);

    // Constructor to initialize the contract with the NYAN token address
    constructor(IERC20 _nyanToken) {
        require(address(_nyanToken) != address(0), "Invalid token address");
        nyanToken = _nyanToken;
    }

    // Function to record mission completion
    function completeMission(address player) external {
        require(player != address(0), "Invalid player address");

        // Increment the number of missions completed for the player
        players[player].missionsCompleted += 1;

        // Distribute rewards based on mission completion
        uint256 reward = calculateMissionReward(players[player].missionsCompleted);
        players[player].totalRewards += reward;

        // Emit an event for rewards distribution
        emit RewardsDistributed(player, reward);
    }

    // Function to record referral activity
    function referPlayer(address referrer) external {
        require(referrer != address(0), "Invalid referrer address");
        require(referrer != msg.sender, "You cannot refer yourself");

        // Increment the number of referrals for the referrer
        players[referrer].referrals += 1;

        // Distribute rewards based on referrals
        uint256 reward = calculateReferralReward(players[referrer].referrals);
        players[referrer].totalRewards += reward;

        // Emit an event for rewards distribution
        emit RewardsDistributed(referrer, reward);
    }

    // Function to calculate mission reward (example logic)
    function calculateMissionReward(uint256 missionsCompleted) internal pure returns (uint256) {
        // Reward logic could be adjusted as per game design
        return missionsCompleted * 10 * 10**18; // Example: 10 NYAN per mission
    }

    // Function to calculate referral reward (example logic)
    function calculateReferralReward(uint256 referrals) internal pure returns (uint256) {
        // Reward logic could be adjusted as per game design
        return referrals * 5 * 10**18; // Example: 5 NYAN per referral
    }

    // Function to withdraw rewards for the player
    function withdrawRewards() external {
        Player storage player = players[msg.sender];
        uint256 amountToWithdraw = player.totalRewards;

        require(amountToWithdraw > 0, "No rewards to withdraw");

        // Reset the player's total rewards after withdrawal
        player.totalRewards = 0;

        // Transfer $NYAN tokens to the player
        require(nyanToken.transfer(msg.sender, amountToWithdraw), "Transfer failed");
    }

    // Function to check the balance of $NYAN tokens in the contract
    function checkContractBalance() external view returns (uint256) {
        return nyanToken.balanceOf(address(this));
    }

    // Function to withdraw tokens from the contract (only owner can call)
    function withdrawTokens(address to, uint256 amount) external {
        require(to != address(0), "Invalid address");
        require(nyanToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens from contract to the specified address
        require(nyanToken.transfer(to, amount), "Transfer failed");
    }
}
```
