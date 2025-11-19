"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustpad-app.pages.dev
Prompt: Generate a code snippet for a smart contract that could be used to manage allocations for IDOs on the TrustPad platform.
Generated: DETERMINISTIC_715a9f6388ed8581
Batch ID: 20250612_160656
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

/**
 * @title IDOAllocationManager
 * @dev Smart contract for managing allocations for IDOs on the TrustPad platform.
 */
contract IDOAllocationManager {
    // Struct to store allocation details for a participant
    struct Allocation {
        uint256 amount; // Amount allocated
        bool claimed;   // Whether the allocation has been claimed
    }

    // Mapping to store allocations for participants
    mapping(address => Allocation) public allocations;

    // Address of the owner (usually the IDO organizer)
    address public owner;

    // Event emitted when an allocation is set
    event AllocationSet(address indexed participant, uint256 amount);

    // Event emitted when an allocation is claimed
    event AllocationClaimed(address indexed participant, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "IDOAllocationManager: Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract with the owner address
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to set an allocation for a participant.
     * Can only be called by the owner.
     * @param participant The address of the participant.
     * @param amount The allocation amount.
     */
    function setAllocation(address participant, uint256 amount) external onlyOwner {
        require(participant != address(0), "IDOAllocationManager: Invalid participant address");
        require(amount > 0, "IDOAllocationManager: Allocation amount must be greater than zero");

        allocations[participant] = Allocation({amount: amount, claimed: false});

        emit AllocationSet(participant, amount);
    }

    /**
     * @dev Function for a participant to claim their allocation.
     */
    function claimAllocation() external {
        Allocation storage userAllocation = allocations[msg.sender];

        require(userAllocation.amount > 0, "IDOAllocationManager: No allocation available");
        require(!userAllocation.claimed, "IDOAllocationManager: Allocation already claimed");

        // Mark the allocation as claimed
        userAllocation.claimed = true;

        // Transfer the allocation amount (example logic, replace with actual transfer)
        // For production, ensure this handles the actual asset transfer (e.g., ERC20 tokens)
        payable(msg.sender).transfer(userAllocation.amount);

        emit AllocationClaimed(msg.sender, userAllocation.amount);
    }

    /**
     * @dev Function to withdraw leftover funds. Can only be called by the owner.
     * @param amount The amount to withdraw.
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "IDOAllocationManager: Insufficient contract balance");
        payable(owner).transfer(amount);
    }

    /**
     * @dev Fallback function to receive funds.
     */
    receive() external payable {}
}
```
