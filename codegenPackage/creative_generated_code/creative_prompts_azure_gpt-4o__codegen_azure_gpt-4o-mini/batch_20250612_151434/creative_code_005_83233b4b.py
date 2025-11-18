"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uyhybuygu7ytgt7yug.pages.dev
Prompt: Write a Solidity smart contract to handle $PSYOP token claims and verify wallet connections.
Generated: DETERMINISTIC_83233b4b597d71e9
Batch ID: 20250612_151434
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title PSYOP Token Claim Contract
/// @notice This contract allows users to claim $PSYOP tokens and verifies wallet connections.
contract PsyopTokenClaim is Ownable {
    // Token interface for $PSYOP
    IERC20 public psyopToken;

    // Mapping to track whether an address has claimed tokens
    mapping(address => bool) public hasClaimed;

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed claimant, uint256 amount);

    // Constructor to set the token address
    constructor(IERC20 _psyopToken) {
        require(address(_psyopToken) != address(0), "Invalid token address");
        psyopToken = _psyopToken;
    }

    /// @notice Claim $PSYOP tokens
    /// @param amount The amount of tokens to claim
    function claimTokens(uint256 amount) external {
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        require(amount > 0, "Claim amount must be greater than zero");
        
        // Check if the contract has enough tokens to fulfill the claim
        require(psyopToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Mark the address as having claimed tokens
        hasClaimed[msg.sender] = true;

        // Transfer tokens to the claimer
        bool success = psyopToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Emit the event for successful claim
        emit TokensClaimed(msg.sender, amount);
    }

    /// @notice Withdraw tokens from the contract (only owner)
    /// @param amount The amount of tokens to withdraw
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        
        // Check if the contract has enough tokens
        require(psyopToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        bool success = psyopToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }

    /// @notice Check if an address has claimed tokens
    /// @param claimant The address to check
    /// @return True if the address has claimed, otherwise false
    function hasAddressClaimed(address claimant) external view returns (bool) {
        return hasClaimed[claimant];
    }
}
```
