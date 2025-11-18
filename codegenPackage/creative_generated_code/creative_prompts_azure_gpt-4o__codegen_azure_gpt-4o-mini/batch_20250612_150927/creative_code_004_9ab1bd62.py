"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allocate-mode.app
Prompt: Create a smart contract in Solidity that integrates with the Mode Network to facilitate automated token claims for $MODE season 2.
Generated: DETERMINISTIC_9ab1bd62e687592b
Batch ID: 20250612_150927
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

// Importing necessary OpenZeppelin contracts for ERC20 and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ModeNetworkTokenClaim
 * @dev This contract facilitates automated token claims for $MODE season 2
 */
contract ModeNetworkTokenClaim is Ownable {
    // Events to log token claims
    event TokensClaimed(address indexed claimant, uint256 amount);

    // The address of the $MODE token contract
    IERC20 public modeToken;

    // Mapping to track claimed tokens for each address
    mapping(address => bool) public hasClaimed;

    // The total amount of tokens available for claims
    uint256 public totalTokens;

    // Constructor to initialize the contract with the MODE token address and total tokens
    constructor(address _modeToken, uint256 _totalTokens) {
        require(_modeToken != address(0), "Invalid token address");
        require(_totalTokens > 0, "Total tokens must be greater than zero");

        modeToken = IERC20(_modeToken);
        totalTokens = _totalTokens;
    }

    /**
     * @dev Function to claim $MODE tokens
     * Can only be called once per address
     * @param amount The amount of tokens to claim
     */
    function claimTokens(uint256 amount) external {
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        require(amount > 0, "Claim amount must be greater than zero");
        require(amount <= totalTokens, "Claim amount exceeds available tokens");

        // Mark as claimed
        hasClaimed[msg.sender] = true;

        // Transfer tokens to the claimant
        bool success = modeToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Emit the TokensClaimed event
        emit TokensClaimed(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw leftover tokens by the owner
     * Can only be called by the owner of the contract
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(amount <= modeToken.balanceOf(address(this)), "Withdraw amount exceeds contract balance");

        // Transfer the specified amount of tokens to the owner
        bool success = modeToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Function to check the contract's balance of $MODE tokens
     * @return The balance of $MODE tokens held by the contract
     */
    function checkBalance() external view returns (uint256) {
        return modeToken.balanceOf(address(this));
    }
}
```
