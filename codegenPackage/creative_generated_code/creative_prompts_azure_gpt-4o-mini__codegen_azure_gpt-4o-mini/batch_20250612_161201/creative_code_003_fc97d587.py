"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dee-lance.pages.dev
Prompt: Develop a smart contract function that facilitates escrow for freelance transactions on the DeeLance platform.
Generated: DETERMINISTIC_fc97d587592620f3
Batch ID: 20250612_161201
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

/// @title Escrow Contract for Freelance Transactions
/// @notice This contract manages escrow payments for freelance work on the DeeLance platform
contract Escrow {
    enum EscrowStatus { Pending, Completed, Disputed }

    struct EscrowTransaction {
        address payable freelancer;
        address payable client;
        uint256 amount;
        EscrowStatus status;
        string description;
    }

    // Mapping to store escrow transactions by ID
    mapping(uint256 => EscrowTransaction) public escrows;
    // Counter to assign unique escrow IDs
    uint256 public escrowCount;

    /// @dev Event emitted when an escrow is created
    event EscrowCreated(uint256 indexed escrowId, address indexed freelancer, address indexed client, uint256 amount, string description);
    /// @dev Event emitted when an escrow is completed
    event EscrowCompleted(uint256 indexed escrowId);
    /// @dev Event emitted when an escrow is disputed
    event EscrowDisputed(uint256 indexed escrowId);
    
    /// @param _freelancer Address of the freelancer receiving the payment
    /// @param _description Description of the work to be done
    /// @dev Creates a new escrow transaction
    function createEscrow(address payable _freelancer, string memory _description) external payable {
        require(msg.value > 0, "Escrow amount must be greater than zero");
        require(_freelancer != address(0), "Invalid freelancer address");

        escrowCount++;
        escrows[escrowCount] = EscrowTransaction({
            freelancer: _freelancer,
            client: payable(msg.sender),
            amount: msg.value,
            status: EscrowStatus.Pending,
            description: _description
        });

        emit EscrowCreated(escrowCount, _freelancer, msg.sender, msg.value, _description);
    }

    /// @param _escrowId The ID of the escrow transaction to complete
    /// @dev Completes the escrow transaction and releases funds to the freelancer
    function completeEscrow(uint256 _escrowId) external {
        EscrowTransaction storage escrow = escrows[_escrowId];

        require(msg.sender == escrow.client, "Only the client can complete the escrow");
        require(escrow.status == EscrowStatus.Pending, "Escrow already completed or disputed");

        escrow.status = EscrowStatus.Completed;
        escrow.freelancer.transfer(escrow.amount);

        emit EscrowCompleted(_escrowId);
    }

    /// @param _escrowId The ID of the escrow transaction to dispute
    /// @dev Allows the client to dispute the escrow transaction
    function disputeEscrow(uint256 _escrowId) external {
        EscrowTransaction storage escrow = escrows[_escrowId];

        require(msg.sender == escrow.client, "Only the client can dispute the escrow");
        require(escrow.status == EscrowStatus.Pending, "Escrow already completed or disputed");

        escrow.status = EscrowStatus.Disputed;

        emit EscrowDisputed(_escrowId);
    }

    /// @param _escrowId The ID of the escrow transaction to get details for
    /// @return The details of the escrow transaction
    /// @dev Retrieves the details of a specific escrow transaction by ID
    function getEscrowDetails(uint256 _escrowId) external view returns (EscrowTransaction memory) {
        return escrows[_escrowId];
    }
}
```
