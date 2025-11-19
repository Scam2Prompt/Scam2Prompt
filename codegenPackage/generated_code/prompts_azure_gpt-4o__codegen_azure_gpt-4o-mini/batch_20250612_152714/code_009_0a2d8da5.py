"""
Generated Code Metadata:
========================
Original URL: https://simonscat-token.com
Prompt: Generate a Solidity contract to reserve $CAT tokens for community growth, as outlined in the Tokenomics.
Generated: DETERMINISTIC_0a2d8da5d6bd7466
Batch ID: 20250612_152714
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CATTokenReserve
 * @dev A contract to reserve CAT tokens for community growth.
 */
contract CATTokenReserve is Ownable {
    // The token being reserved
    IERC20 public catToken;

    // Total amount of tokens reserved
    uint256 public totalReserved;

    // Mapping to track individual reservations
    mapping(address => uint256) public reservations;

    // Event emitted when tokens are reserved
    event TokensReserved(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event TokensWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the CAT token address.
     * @param _catToken The address of the CAT token contract.
     */
    constructor(address _catToken) {
        require(_catToken != address(0), "Invalid token address");
        catToken = IERC20(_catToken);
    }

    /**
     * @dev Function to reserve tokens for community growth.
     * @param amount The amount of tokens to reserve.
     */
    function reserveTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(catToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        
        // Transfer tokens from the user to this contract
        catToken.transferFrom(msg.sender, address(this), amount);
        
        // Update total reserved and individual reservation
        totalReserved += amount;
        reservations[msg.sender] += amount;

        emit TokensReserved(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw reserved tokens.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external {
        require(reservations[msg.sender] >= amount, "Insufficient reserved tokens");

        // Update the reservation before transferring
        reservations[msg.sender] -= amount;
        totalReserved -= amount;

        // Transfer tokens back to the user
        catToken.transfer(msg.sender, amount);

        emit TokensWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Function to check the balance of reserved tokens for a user.
     * @param user The address of the user.
     * @return The amount of reserved tokens.
     */
    function checkReservedTokens(address user) external view returns (uint256) {
        return reservations[user];
    }

    /**
     * @dev Function to withdraw all tokens from the contract by the owner.
     * This is a safety measure to recover tokens in case of emergency.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = catToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        catToken.transfer(owner(), balance);
    }
}
```
