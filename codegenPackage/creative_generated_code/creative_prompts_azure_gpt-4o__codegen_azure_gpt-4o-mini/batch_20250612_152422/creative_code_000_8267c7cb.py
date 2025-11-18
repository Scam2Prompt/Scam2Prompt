"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deelance-token.pages.dev
Prompt: Write a smart contract in Solidity for a decentralized escrow system similar to the one described on the DeeLance platform, ensuring secure transactions between freelancers and recruiters.
Generated: DETERMINISTIC_8267c7cbb5104c28
Batch ID: 20250612_152422
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

/// @title Decentralized Escrow Contract
/// @notice This contract acts as an escrow service between freelancers and recruiters
contract Escrow {
    // State variables
    enum EscrowStatus {Pending, Completed, Canceled}
    
    struct EscrowDetails {
        uint256 amount;               // Amount held in escrow
        address payable freelancer;    // Address of the freelancer
        address payable recruiter;      // Address of the recruiter
        EscrowStatus status;          // Current status of the escrow
    }

    // Mapping of escrow agreements
    mapping(uint256 => EscrowDetails) public escrows;
    uint256 public escrowCount;      // Counter for escrow agreements

    // Events for logging
    event EscrowCreated(uint256 indexed escrowId, address indexed freelancer, address indexed recruiter, uint256 amount);
    event EscrowCompleted(uint256 indexed escrowId);
    event EscrowCanceled(uint256 indexed escrowId);

    // Modifier to check escrow status
    modifier onlyInStatus(uint256 _escrowId, EscrowStatus _status) {
        require(escrows[_escrowId].status == _status, "Invalid escrow status");
        _;
    }

    /// @notice Create a new escrow agreement
    /// @param _freelancer Address of the freelancer
    /// @param _recruiter Address of the recruiter
    /// @return escrowId The ID of the newly created escrow
    function createEscrow(address payable _freelancer, address payable _recruiter) external payable returns (uint256 escrowId) {
        require(msg.value > 0, "Escrow amount must be greater than 0");
        require(_freelancer != address(0) && _recruiter != address(0), "Invalid addresses");

        escrowId = escrowCount++;
        escrows[escrowId] = EscrowDetails({
            amount: msg.value,
            freelancer: _freelancer,
            recruiter: _recruiter,
            status: EscrowStatus.Pending
        });

        emit EscrowCreated(escrowId, _freelancer, _recruiter, msg.value);
    }

    /// @notice Complete the escrow agreement, releasing funds to the freelancer
    /// @param _escrowId ID of the escrow agreement
    function completeEscrow(uint256 _escrowId) external onlyInStatus(_escrowId, EscrowStatus.Pending) {
        EscrowDetails storage escrow = escrows[_escrowId];
        require(msg.sender == escrow.recruiter, "Only the recruiter can complete the escrow");

        escrow.status = EscrowStatus.Completed;
        escrow.freelancer.transfer(escrow.amount);

        emit EscrowCompleted(_escrowId);
    }

    /// @notice Cancel the escrow agreement and refund the recruiter
    /// @param _escrowId ID of the escrow agreement
    function cancelEscrow(uint256 _escrowId) external onlyInStatus(_escrowId, EscrowStatus.Pending) {
        EscrowDetails storage escrow = escrows[_escrowId];
        require(msg.sender == escrow.recruiter, "Only the recruiter can cancel the escrow");

        escrow.status = EscrowStatus.Canceled;
        escrow.recruiter.transfer(escrow.amount);

        emit EscrowCanceled(_escrowId);
    }

    /// @notice Get details of an escrow agreement
    /// @param _escrowId ID of the escrow agreement
    /// @return details Struct containing escrow details
    function getEscrowDetails(uint256 _escrowId) external view returns (EscrowDetails memory details) {
        return escrows[_escrowId];
    }
}
```
