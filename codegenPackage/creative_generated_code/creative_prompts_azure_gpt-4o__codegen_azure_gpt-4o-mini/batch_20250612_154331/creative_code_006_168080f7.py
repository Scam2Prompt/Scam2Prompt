"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-trump-memes-2025.pages.dev
Prompt: Develop a Solidity smart contract that tracks the allocation and unlocking schedule of tokens similar to "$TRUMP," with ownership split between multiple entities.
Generated: DETERMINISTIC_168080f7d1df7568
Batch ID: 20250612_154331
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// @title TokenAllocation
// @dev Smart contract for managing token allocation and unlocking schedules
contract TokenAllocation is Ownable {
    using SafeMath for uint256;

    struct Allocation {
        uint256 totalAmount;          // Total amount allocated
        uint256 releasedAmount;       // Amount already released
        uint256 unlockTime;           // Time when tokens can be unlocked
        bool isActive;                // Active status of allocation
    }

    // Mapping from beneficiary address to their allocation
    mapping(address => Allocation) public allocations;

    // Event emitted when tokens are released
    event TokensReleased(address indexed beneficiary, uint256 amount);

    // @dev Creates an allocation for a specified beneficiary
    // @param beneficiary The address receiving the allocation
    // @param amount The total amount allocated
    // @param unlockTime The time at which the tokens can be released
    function allocateTokens(address beneficiary, uint256 amount, uint256 unlockTime) external onlyOwner {
        require(beneficiary != address(0), "Invalid beneficiary address");
        require(amount > 0, "Amount must be greater than zero");
        require(allocations[beneficiary].totalAmount == 0, "Allocation already exists");
        require(unlockTime > block.timestamp, "Unlock time must be in the future");

        allocations[beneficiary] = Allocation({
            totalAmount: amount,
            releasedAmount: 0,
            unlockTime: unlockTime,
            isActive: true
        });
    }

    // @dev Releases tokens to the beneficiary based on the allocation schedule
    // @param beneficiary The address of the beneficiary
    function releaseTokens(address beneficiary) external {
        Allocation storage allocation = allocations[beneficiary];
        
        require(allocation.isActive, "Allocation not active");
        require(block.timestamp >= allocation.unlockTime, "Tokens are still locked");

        uint256 unreleasedAmount = allocation.totalAmount.sub(allocation.releasedAmount);
        require(unreleasedAmount > 0, "No tokens to release");

        allocation.releasedAmount = allocation.totalAmount; // All tokens are now released
        allocation.isActive = false; // Mark allocation as inactive

        // Transfer tokens to the beneficiary (assuming this contract holds tokens)
        // Replace 'token' with your ERC20 token contract instance
        // token.transfer(beneficiary, unreleasedAmount);
        emit TokensReleased(beneficiary, unreleasedAmount);
    }

    // @dev Allows the owner to revoke an allocation before it is unlocked
    // @param beneficiary The address of the beneficiary
    function revokeTokens(address beneficiary) external onlyOwner {
        Allocation storage allocation = allocations[beneficiary];
        
        require(allocation.isActive, "Allocation not active");

        allocation.isActive = false; // Mark allocation as inactive

        // Optionally, you can return any allocated tokens back to owner
        // This assumes you have a mechanism to track the underlying tokens
    }

    // @dev Getter for allocation details
    // @param beneficiary The address of the beneficiary
    // @return totalAmount, releasedAmount, unlockTime, isActive
    function getAllocationDetails(address beneficiary) external view returns (uint256, uint256, uint256, bool) {
        Allocation memory allocation = allocations[beneficiary];
        return (allocation.totalAmount, allocation.releasedAmount, allocation.unlockTime, allocation.isActive);
    }
}
```
