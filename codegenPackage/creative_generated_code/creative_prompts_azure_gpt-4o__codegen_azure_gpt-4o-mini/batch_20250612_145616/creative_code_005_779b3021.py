"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://verse-support.pages.dev
Prompt: Develop a smart contract that incorporates Bitcoin.com's Verse rewards and utility token, referencing the use cases specified in the "Verse" section of the webpage.
Generated: DETERMINISTIC_779b3021232670c3
Batch ID: 20250612_145616
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

/// @title VerseRewardsAndUtilityToken
/// @author Your Name
/// @notice This contract manages Verse rewards and utility token system.
/// @dev This contract allows users to earn Verse tokens and utilize them for various features.

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract VerseToken is ERC20, Ownable {
    // Mapping to keep track of user rewards
    mapping(address => uint256) private rewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("VerseToken", "VERSE") {
        // Mint an initial supply of tokens to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1,000,000 VERSE tokens
    }

    /// @notice Allows the owner to distribute rewards to users
    /// @param user The address of the user receiving rewards
    /// @param amount The amount of rewards to distribute
    function distributeRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");

        rewards[user] += amount;
        emit RewardsDistributed(user, amount);
    }

    /// @notice Allows users to claim their accumulated rewards
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the user's rewards to zero before transferring
        rewards[msg.sender] = 0;

        // Mint new tokens to the user based on their rewards
        _mint(msg.sender, rewardAmount);
    }

    /// @notice Check the rewards balance of a user
    /// @param user The address of the user
    /// @return The amount of rewards the user has
    function checkRewards(address user) external view returns (uint256) {
        return rewards[user];
    }

    /// @notice Allows users to utilize their Verse tokens for specific use cases
    /// @dev This function can be expanded to include various utility functionalities
    /// @param amount The amount of tokens to spend
    function useTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Burn the tokens spent by the user
        _burn(msg.sender, amount);

        // Additional logic for the specific use case can be implemented here
        // Example: grant access to premium features, etc.
    }
}
```

**Note:** Ensure you install the OpenZeppelin Contracts library in your project to use the ERC20 and Ownable contracts:
```bash
npm install @openzeppelin/contracts
```
