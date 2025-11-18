"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bobothebear.pages.dev
Prompt: Create a function in Solidity to calculate and distribute $BOBO tokens based on the tokenomics model (e.g., 8% CEX listings, 92% community allocation) described on the Bobo the Bear website.
Generated: DETERMINISTIC_1fb52fa58bdef36f
Batch ID: 20250612_151158
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

/**
 * @title BoboToken
 * @dev This contract implements a token with specific tokenomics.
 * The total supply is distributed as per the specified model.
 */
contract BoboToken is ERC20, Ownable {
    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10**18; // 1 million tokens with 18 decimals
    
    // Allocation percentages
    uint256 public constant CEX_ALLOCATION_PERCENT = 8;
    uint256 public constant COMMUNITY_ALLOCATION_PERCENT = 92;

    // CEX and community allocation amounts
    uint256 public cexAllocation;
    uint256 public communityAllocation;

    // Events
    event TokensDistributed(address indexed beneficiary, uint256 amount);

    /**
     * @dev Constructor that initializes the token with total supply
     * and performs the allocation based on the specified percentages.
     */
    constructor() ERC20("BoboToken", "BOBO") {
        // Allocate tokens
        cexAllocation = (TOTAL_SUPPLY * CEX_ALLOCATION_PERCENT) / 100;
        communityAllocation = (TOTAL_SUPPLY * COMMUNITY_ALLOCATION_PERCENT) / 100;

        // Mint the allocated tokens to the contract owner (for CEX by default)
        _mint(msg.sender, cexAllocation);
        // Community allocation will be distributed later
    }

    /**
     * @dev Distribute community tokens to a specified address.
     * @param recipient The address to receive community tokens.
     * @param amount The amount of tokens to distribute.
     */
    function distributeCommunityTokens(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid address");
        require(amount <= communityAllocation, "Amount exceeds community allocation");

        // Adjust the community allocation
        communityAllocation -= amount;

        // Transfer tokens to the recipient
        _transfer(owner(), recipient, amount);
        emit TokensDistributed(recipient, amount);
    }

    /**
     * @dev Getter for the remaining community allocation.
     * @return The amount of community tokens left to distribute.
     */
    function getRemainingCommunityAllocation() external view returns (uint256) {
        return communityAllocation;
    }

    /**
     * @dev Prevent Ether from being sent to the contract.
     */
    receive() external payable {
        revert("Ether not accepted");
    }
}
```
