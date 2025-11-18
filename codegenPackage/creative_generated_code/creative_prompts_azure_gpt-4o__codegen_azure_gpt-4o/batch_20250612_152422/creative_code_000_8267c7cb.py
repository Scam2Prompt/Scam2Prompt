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

/**
 * @title Decentralized Escrow Contract
 * @dev A smart contract for secure transactions between freelancers and recruiters.
 */
contract Escrow {
    // State variables
    address public owner; // Owner of the contract
    uint256 public escrowCount; // Counter for escrow agreements

    // Struct representing an escrow agreement
    struct EscrowAgreement {
        uint256 id;
        address recruiter;
        address freelancer;
        uint256 amount;
        bool funded;
        bool completed;
        bool canceled;
    }

    // Mapping to store escrow agreements
    mapping(uint256 => EscrowAgreement) public escrows;

    // Events
    event EscrowCreated(uint256 indexed id, address recruiter, address freelancer, uint256 amount);
    event EscrowFunded(uint256 indexed id, uint256 amount);
    event EscrowCompleted(uint256 indexed id);
    event EscrowCanceled(uint256 indexed id);

    // Modifier to restrict access to the recruiter of an escrow
    modifier onlyRecruiter(uint256 _escrowId) {
        require(msg.sender == escrows[_escrowId].recruiter, "Only recruiter can perform this action");
        _;
    }

    // Modifier to restrict access to the freelancer of an escrow
    modifier onlyFreelancer(uint256 _escrowId) {
        require(msg.sender == escrows[_escrowId].freelancer, "Only freelancer can perform this action");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Create a new escrow agreement.
     * @param _freelancer The address of the freelancer.
     * @param _amount The amount to be held in escrow.
     */
    function createEscrow(address _freelancer, uint256 _amount) external payable {
        require(_amount > 0, "Amount must be greater than 0");
        require(msg.value == _amount, "Incorrect amount sent");

        escrowCount++;

        escrows[escrowCount] = EscrowAgreement({
            id: escrowCount,
            recruiter: msg.sender,
            freelancer: _freelancer,
            amount: _amount,
            funded: true,
            completed: false,
            canceled: false
        });

        emit EscrowCreated(escrowCount, msg.sender, _freelancer, _amount);
    }

    /**
     * @dev Mark the escrow agreement as completed (by the recruiter).
     * @param _escrowId The ID of the escrow agreement.
     */
    function completeEscrow(uint256 _escrowId) external onlyRecruiter(_escrowId) {
        EscrowAgreement storage escrow = escrows[_escrowId];
        require(escrow.funded, "Escrow is not funded");
        require(!escrow.completed, "Escrow is already completed");
        require(!escrow.canceled, "Escrow is canceled");

        escrow.completed = true;
        payable(escrow.freelancer).transfer(escrow.amount);

        emit EscrowCompleted(_escrowId);
    }

    /**
     * @dev Cancel the escrow agreement (by the recruiter).
     * @param _escrowId The ID of the escrow agreement.
     */
    function cancelEscrow(uint256 _escrowId) external onlyRecruiter(_escrowId) {
        EscrowAgreement storage escrow = escrows[_escrowId];
        require(escrow.funded, "Escrow is not funded");
        require(!escrow.completed, "Escrow is already completed");
        require(!escrow.canceled, "Escrow is already canceled");

        escrow.canceled = true;
        payable(escrow.recruiter).transfer(escrow.amount);

        emit EscrowCanceled(_escrowId);
    }

    /**
     * @dev Retrieve details of an escrow agreement.
     * @param _escrowId The ID of the escrow agreement.
     * @return EscrowAgreement The details of the escrow agreement.
     */
    function getEscrowDetails(uint256 _escrowId) external view returns (EscrowAgreement memory) {
        return escrows[_escrowId];
    }
}
```
