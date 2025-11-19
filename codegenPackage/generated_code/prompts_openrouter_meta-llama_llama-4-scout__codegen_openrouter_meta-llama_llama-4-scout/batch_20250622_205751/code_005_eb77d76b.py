"""
Generated Code Metadata:
========================
Original URL: https://bafkreicoon64gkkbjxpmodgbslmgl7ogwalyvfj6heqdicaqv3pqkepbvm.ipfs.dweb.link
Prompt: What are the conditions for forfeiting rewards on the $BANANA token platform, and how can I implement these rules in a smart contract?
Generated: DETERMINISTIC_eb77d76b5363e27f
Batch ID: 20250622_205751
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title BananaToken
 * @author [Your Name]
 * @notice This contract manages the $BANANA token and its reward forfeiture conditions.
 */
contract BananaToken is ERC20, ReentrancyGuard {
    // Mapping of user accounts to their reward balances
    mapping(address => uint256) public rewardBalances;

    // Mapping of user accounts to their forfeiture status
    mapping(address => bool) public isForfeited;

    // Conditions for forfeiting rewards
    enum ForfeitureCondition {
        NONE,
        TRANSFER_TO_NON_WHITELISTED_ADDRESS,
        SUSPICIOUS_ACTIVITY_DETECTED
    }

    // Event emitted when rewards are forfeited
    event RewardsForfeited(address indexed user, ForfeitureCondition condition);

    // Whitelisted addresses
    mapping(address => bool) public whitelistedAddresses;

    /**
     * @dev Initializes the $BANANA token contract.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @dev Adds a user to the whitelist.
     * @param user The address to whitelist.
     */
    function addWhitelistedAddress(address user) public onlyOwner {
        whitelistedAddresses[user] = true;
    }

    /**
     * @dev Removes a user from the whitelist.
     * @param user The address to remove from the whitelist.
     */
    function removeWhitelistedAddress(address user) public onlyOwner {
        whitelistedAddresses[user] = false;
    }

    /**
     * @dev Mints rewards to a user's account.
     * @param user The address to mint rewards to.
     * @param amount The amount of rewards to mint.
     */
    function mintRewards(address user, uint256 amount) public onlyOwner {
        rewardBalances[user] += amount;
    }

    /**
     * @dev Transfers $BANANA tokens from one user to another.
     * @param from The address to transfer from.
     * @param to The address to transfer to.
     * @param amount The amount to transfer.
     */
    function transfer(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        // Check if the recipient is whitelisted
        if (!whitelistedAddresses[to]) {
            // Forfeit rewards if recipient is not whitelisted
            forfeitRewards(from, ForfeitureCondition.TRANSFER_TO_NON_WHITELISTED_ADDRESS);
        }

        // Perform token transfer
        return super.transfer(to, amount);
    }

    /**
     * @dev Forfeits a user's rewards based on a condition.
     * @param user The address to forfeit rewards for.
     * @param condition The condition for forfeiting rewards.
     */
    function forfeitRewards(address user, ForfeitureCondition condition) internal {
        // Check if rewards have already been forfeited
        if (isForfeited[user]) {
            return;
        }

        // Forfeit rewards
        rewardBalances[user] = 0;
        isForfeited[user] = true;

        // Emit event
        emit RewardsForfeited(user, condition);
    }

    /**
     * @dev Detects suspicious activity and forfeits rewards if necessary.
     * @param user The address to check for suspicious activity.
     */
    function detectSuspiciousActivity(address user) public {
        // Implement suspicious activity detection logic here
        // For demonstration purposes, assume suspicious activity is detected
        bool suspiciousActivityDetected = true;

        if (suspiciousActivityDetected) {
            forfeitRewards(user, ForfeitureCondition.SUSPICIOUS_ACTIVITY_DETECTED);
        }
    }

    /**
     * @dev Gets the reward balance of a user.
     * @param user The address to get the reward balance for.
     * @return The reward balance of the user.
     */
    function getRewardBalance(address user) public view returns (uint256) {
        return rewardBalances[user];
    }

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner {
        require(msg.sender == owner(), "Only the contract owner can perform this action");
        _;
    }
}
```
