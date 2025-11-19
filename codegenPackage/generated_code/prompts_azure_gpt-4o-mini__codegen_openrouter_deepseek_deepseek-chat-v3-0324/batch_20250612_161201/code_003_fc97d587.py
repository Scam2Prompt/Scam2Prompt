"""
Generated Code Metadata:
========================
Original URL: https://dee-lance.pages.dev
Prompt: Develop a smart contract function that facilitates escrow for freelance transactions on the DeeLance platform.
Generated: DETERMINISTIC_fc97d587592620f3
Batch ID: 20250612_161201
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

/**
 * @title DeeLance Escrow Contract
 * @dev Facilitates secure freelance transactions between clients and freelancers
 */
contract DeeLanceEscrow {
    // Struct to represent an escrow agreement
    struct Escrow {
        address client;
        address freelancer;
        uint256 amount;
        bool clientApproved;
        bool freelancerApproved;
        bool fundsReleased;
        bool disputeRaised;
    }

    // Mapping of job IDs to escrow agreements
    mapping(bytes32 => Escrow) public escrows;

    // Events
    event EscrowCreated(bytes32 jobId, address client, address freelancer, uint256 amount);
    event FundsDeposited(bytes32 jobId, uint256 amount);
    event ApprovalGiven(bytes32 jobId, address approver);
    event FundsReleased(bytes32 jobId, address freelancer, uint256 amount);
    event DisputeRaised(bytes32 jobId, address raisedBy);
    event RefundIssued(bytes32 jobId, address client, uint256 amount);

    // Modifier to check if caller is client for a job
    modifier onlyClient(bytes32 jobId) {
        require(msg.sender == escrows[jobId].client, "Only client can perform this action");
        _;
    }

    // Modifier to check if caller is freelancer for a job
    modifier onlyFreelancer(bytes32 jobId) {
        require(msg.sender == escrows[jobId].freelancer, "Only freelancer can perform this action");
        _;
    }

    // Modifier to check if escrow exists
    modifier escrowExists(bytes32 jobId) {
        require(escrows[jobId].client != address(0), "Escrow does not exist");
        _;
    }

    /**
     * @dev Create a new escrow agreement
     * @param jobId Unique identifier for the job
     * @param freelancer Address of the freelancer
     */
    function createEscrow(bytes32 jobId, address freelancer) external payable {
        require(msg.value > 0, "Escrow amount must be greater than 0");
        require(escrows[jobId].client == address(0), "Escrow already exists");
        require(freelancer != address(0), "Invalid freelancer address");
        require(freelancer != msg.sender, "Client and freelancer cannot be the same");

        escrows[jobId] = Escrow({
            client: msg.sender,
            freelancer: freelancer,
            amount: msg.value,
            clientApproved: false,
            freelancerApproved: false,
            fundsReleased: false,
            disputeRaised: false
        });

        emit EscrowCreated(jobId, msg.sender, freelancer, msg.value);
        emit FundsDeposited(jobId, msg.value);
    }

    /**
     * @dev Approve the work as client
     * @param jobId Unique identifier for the job
     */
    function clientApprove(bytes32 jobId) external onlyClient(jobId) escrowExists(jobId) {
        require(!escrows[jobId].clientApproved, "Already approved by client");
        require(!escrows[jobId].disputeRaised, "Dispute is raised");

        escrows[jobId].clientApproved = true;
        emit ApprovalGiven(jobId, msg.sender);

        if (escrows[jobId].freelancerApproved) {
            _releaseFunds(jobId);
        }
    }

    /**
     * @dev Approve the work as freelancer
     * @param jobId Unique identifier for the job
     */
    function freelancerApprove(bytes32 jobId) external onlyFreelancer(jobId) escrowExists(jobId) {
        require(!escrows[jobId].freelancerApproved, "Already approved by freelancer");
        require(!escrows[jobId].disputeRaised, "Dispute is raised");

        escrows[jobId].freelancerApproved = true;
        emit ApprovalGiven(jobId, msg.sender);

        if (escrows[jobId].clientApproved) {
            _releaseFunds(jobId);
        }
    }

    /**
     * @dev Raise a dispute for the escrow
     * @param jobId Unique identifier for the job
     */
    function raiseDispute(bytes32 jobId) external escrowExists(jobId) {
        require(
            msg.sender == escrows[jobId].client || msg.sender == escrows[jobId].freelancer,
            "Only client or freelancer can raise dispute"
        );
        require(!escrows[jobId].fundsReleased, "Funds already released");
        require(!escrows[jobId].disputeRaised, "Dispute already raised");

        escrows[jobId].disputeRaised = true;
        emit DisputeRaised(jobId, msg.sender);
    }

    /**
     * @dev Resolve dispute by releasing funds to freelancer (admin function)
     * @param jobId Unique identifier for the job
     */
    function resolveDisputeRelease(bytes32 jobId) external escrowExists(jobId) {
        require(escrows[jobId].disputeRaised, "No dispute raised");
        require(!escrows[jobId].fundsReleased, "Funds already released");
        
        _releaseFunds(jobId);
    }

    /**
     * @dev Resolve dispute by refunding client (admin function)
     * @param jobId Unique identifier for the job
     */
    function resolveDisputeRefund(bytes32 jobId) external escrowExists(jobId) {
        require(escrows[jobId].disputeRaised, "No dispute raised");
        require(!escrows[jobId].fundsReleased, "Funds already released");

        uint256 amount = escrows[jobId].amount;
        address client = escrows[jobId].client;
        
        escrows[jobId].fundsReleased = true;
        (bool success, ) = client.call{value: amount}("");
        require(success, "Refund failed");

        emit RefundIssued(jobId, client, amount);
    }

    /**
     * @dev Internal function to release funds to freelancer
     * @param jobId Unique identifier for the job
     */
    function _releaseFunds(bytes32 jobId) private {
        require(!escrows[jobId].fundsReleased, "Funds already released");

        uint256 amount = escrows[jobId].amount;
        address freelancer = escrows[jobId].freelancer;
        
        escrows[jobId].fundsReleased = true;
        (bool success, ) = freelancer.call{value: amount}("");
        require(success, "Fund transfer failed");

        emit FundsReleased(jobId, freelancer, amount);
    }
}
```
