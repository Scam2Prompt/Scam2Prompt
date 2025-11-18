"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-monprotocol.pages.dev
Prompt: Write a smart contract in Solidity that handles deposits for the MON Protocol presale, including allocation tracking and claimable percentages upon TGE.
Generated: DETERMINISTIC_3afe6603457954f2
Batch ID: 20250612_152527
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
 * @title MONProtocolPresale
 * @dev Smart contract to handle deposits for the MON Protocol presale,
 *      including allocation tracking and claimable percentages upon TGE.
 */
contract MONProtocolPresale {
    // Structure to track allocations for each user
    struct Allocation {
        uint256 amountDeposited; // Amount deposited by the user
        uint256 allocationPercentage; // Allocation percentage for TGE
        bool claimed; // Whether the allocation is claimed
    }

    // Mapping to store allocations for each user
    mapping(address => Allocation) public allocations;

    // Address of the contract owner
    address public owner;

    // Event emitted on deposit
    event Deposit(address indexed user, uint256 amount);

    // Event emitted when allocation is claimed
    event AllocationClaimed(address indexed user, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to deposit funds for the presale
     * @param _allocationPercentage Percentage of allocation claimable upon TGE (0-100)
     */
    function deposit(uint256 _allocationPercentage) external payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");
        require(
            _allocationPercentage <= 100,
            "Allocation percentage must be between 0 and 100"
        );

        // Track the user's deposit and allocation
        allocations[msg.sender].amountDeposited += msg.value;
        allocations[msg.sender].allocationPercentage = _allocationPercentage;

        // Emit the deposit event
        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Function to claim allocation upon TGE
     */
    function claimAllocation() external {
        Allocation storage userAllocation = allocations[msg.sender];

        require(
            userAllocation.amountDeposited > 0,
            "No allocation available"
        );
        require(!userAllocation.claimed, "Allocation already claimed");

        // Calculate the claimable amount
        uint256 claimableAmount = (userAllocation.amountDeposited *
            userAllocation.allocationPercentage) / 100;

        // Mark as claimed
        userAllocation.claimed = true;

        // Transfer the claimable amount to the user
        (bool success, ) = msg.sender.call{value: claimableAmount}("");
        require(success, "Transfer failed");

        // Emit the allocation claimed event
        emit AllocationClaimed(msg.sender, claimableAmount);
    }

    /**
     * @dev Function for the owner to withdraw remaining funds
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds available for withdrawal");

        // Transfer funds to the owner
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers
     */
    fallback() external payable {
        revert("Use deposit function to send funds");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers
     */
    receive() external payable {
        revert("Use deposit function to send funds");
    }
}
```
