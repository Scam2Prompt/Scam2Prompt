"""
Generated Code Metadata:
========================
Original URL: https://normilio.pages.dev
Prompt: Create a smart contract snippet for managing $NORMILIO token claims, emphasizing the "no funny business" principle.
Generated: DETERMINISTIC_f5f43c2e570e5a65
Batch ID: 20250612_150622
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title NormilioTokenClaims
 * @dev A smart contract for managing claims of the $NORMILIO token.
 * This contract ensures that only eligible users can claim tokens, adhering to the "no funny business" principle.
 */
contract NormilioTokenClaims is Ownable {
    // The ERC20 token contract for $NORMILIO
    IERC20 public normilioToken;

    // Mapping to track claimed status of addresses
    mapping(address => bool) public hasClaimed;

    // Event emitted when a claim is made
    event Claimed(address indexed claimant, uint256 amount);

    // Constructor to set the token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        normilioToken = IERC20(_tokenAddress);
    }

    /**
     * @dev Allows eligible users to claim their $NORMILIO tokens.
     * @param amount The amount of tokens to claim.
     */
    function claimTokens(uint256 amount) external {
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        require(amount > 0, "Claim amount must be greater than zero");
        require(normilioToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Mark the address as having claimed
        hasClaimed[msg.sender] = true;

        // Transfer the tokens to the claimant
        bool success = normilioToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit Claimed(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to withdraw any remaining tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(normilioToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer the tokens to the owner
        bool success = normilioToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Allows the owner to set a new token address if needed.
     * @param newTokenAddress The new token address.
     */
    function setTokenAddress(address newTokenAddress) external onlyOwner {
        require(newTokenAddress != address(0), "Invalid token address");
        normilioToken = IERC20(newTokenAddress);
    }
}
```
