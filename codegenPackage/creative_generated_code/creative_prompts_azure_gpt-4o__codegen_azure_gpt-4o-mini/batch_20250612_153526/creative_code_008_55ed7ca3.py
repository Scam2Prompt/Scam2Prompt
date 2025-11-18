"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plenafinance.vercel.app
Prompt: Write a smart contract to manage the allocation of 2% of the $PLENA token supply for Quest participants, including whitelist spot tracking.
Generated: DETERMINISTIC_55ed7ca3e6db6f09
Batch ID: 20250612_153526
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

/**
 * @title QuestManager
 * @dev Smart contract to manage the allocation of 2% of the $PLENA token supply for Quest participants
 */
contract QuestManager is Ownable {
    IERC20 public plenaToken; // Reference to the $PLENA token contract

    uint256 public constant ALLOCATION_PERCENTAGE = 2; // Allocation percentage for quests
    uint256 public constant TOTAL_SUPPLY = 1000000 * 10**18; // Example total supply of $PLENA token
    uint256 public totalAllocated; // Total tokens allocated for quests
    uint256 public allocationLimit; // Limit for quest allocation
    mapping(address => bool) public whitelisted; // Tracking whitelist status of participants

    event Whitelisted(address indexed participant);
    event Unwhitelisted(address indexed participant);
    event TokensAllocated(address indexed participant, uint256 amount);
    
    /**
     * @dev Constructor to initialize the contract
     * @param _plenaToken Address of the $PLENA token contract
     */
    constructor(address _plenaToken) {
        require(_plenaToken != address(0), "Invalid token address");
        plenaToken = IERC20(_plenaToken);
        allocationLimit = (TOTAL_SUPPLY * ALLOCATION_PERCENTAGE) / 100; // Calculate allocation limit
    }

    /**
     * @dev Whitelist an address for participation in quests
     * @param participant Address to be whitelisted
     */
    function whitelistParticipant(address participant) external onlyOwner {
        require(participant != address(0), "Invalid address");
        require(!whitelisted[participant], "Already whitelisted");

        whitelisted[participant] = true;
        emit Whitelisted(participant);
    }

    /**
     * @dev Remove an address from the whitelist
     * @param participant Address to be removed from whitelist
     */
    function unwhitelistParticipant(address participant) external onlyOwner {
        require(whitelisted[participant], "Not whitelisted");

        whitelisted[participant] = false;
        emit Unwhitelisted(participant);
    }

    /**
     * @dev Allocate tokens to a whitelisted participant
     * @param participant Address of the participant
     * @param amount Amount of tokens to allocate
     */
    function allocateTokens(address participant, uint256 amount) external onlyOwner {
        require(whitelisted[participant], "Not whitelisted");
        require(amount > 0, "Amount must be greater than zero");
        require(totalAllocated + amount <= allocationLimit, "Allocation limit exceeded");

        totalAllocated += amount; // Update total allocated amount
        // Transfer tokens from the contract to the participant
        require(plenaToken.transfer(participant, amount), "Token transfer failed");

        emit TokensAllocated(participant, amount);
    }

    /**
     * @dev Function to check the allocation limit
     * @return Remaining allocation limit
     */
    function remainingAllocation() external view returns (uint256) {
        return allocationLimit - totalAllocated;
    }
}
```
