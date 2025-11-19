"""
Generated Code Metadata:
========================
Original URL: https://deelance-token.pages.dev
Prompt: Develop a blockchain-based escrow system for secure payments on a freelancing platform, utilizing smart contracts and cryptocurrency.
Generated: DETERMINISTIC_605b9f5ef8e73e2e
Batch ID: 20250622_210008
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Blockchain Escrow System for Freelancing Platform

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title FreelanceEscrow
 * @dev A smart contract for handling escrow payments between clients and freelancers
 */
contract FreelanceEscrow {
    // Struct to represent an escrow agreement
    struct Escrow {
        address client;
        address freelancer;
        uint256 amount;
        uint256 createdAt;
        uint256 deadline;
        bool fundsReleased;
        bool disputeRaised;
        address disputeResolver;
    }

    // Mapping of escrow IDs to escrow agreements
    mapping(uint256 => Escrow) public escrows;
    
    // Counter for generating unique escrow IDs
    uint256 public escrowCounter;
    
    // Address of the contract owner (platform admin)
    address public owner;
    
    // Platform fee percentage (e.g., 100 = 1%)
    uint256 public platformFee;
    
    // Events for tracking contract activities
    event EscrowCreated(
        uint256 indexed escrowId,
        address indexed client,
        address indexed freelancer,
        uint256 amount,
        uint256 deadline
    );
    
    event FundsReleased(uint256 indexed escrowId, uint256 amount);
    event FundsRefunded(uint256 indexed escrowId, uint256 amount);
    event DisputeRaised(uint256 indexed escrowId, address indexed resolver);
    event DisputeResolved(uint256 indexed escrowId, bool clientWins);
    
    // Modifier to restrict access to owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    // Modifier to ensure escrow exists
    modifier escrowExists(uint256 escrowId) {
        require(escrowId < escrowCounter, "Escrow does not exist");
        _;
    }
    
    // Modifier to ensure only client can perform action
    modifier onlyClient(uint256 escrowId) {
        require(msg.sender == escrows[escrowId].client, "Only client can call this function");
        _;
    }
    
    // Modifier to ensure only freelancer can perform action
    modifier onlyFreelancer(uint256 escrowId) {
        require(msg.sender == escrows[escrowId].freelancer, "Only freelancer can call this function");
        _;
    }
    
    // Modifier to ensure only dispute resolver can perform action
    modifier onlyResolver(uint256 escrowId) {
        require(msg.sender == escrows[escrowId].disputeResolver, "Only resolver can call this function");
        _;
    }
    
    /**
     * @dev Constructor sets the contract owner and platform fee
     * @param _platformFee The platform fee percentage (e.g., 100 = 1%)
     */
    constructor(uint256 _platformFee) {
        owner = msg.sender;
        platformFee = _platformFee;
    }
    
    /**
     * @dev Creates a new escrow agreement
     * @param freelancer The address of the freelancer
     * @param deadline The deadline for the freelancer to complete the work (unix timestamp)
     * @param disputeResolver The address of the dispute resolver (can be zero for no resolver)
     * @return escrowId The ID of the newly created escrow
     */
    function createEscrow(
        address freelancer,
        uint256 deadline,
        address disputeResolver
    ) external payable returns (uint256 escrowId) {
        require(msg.value > 0, "Escrow amount must be greater than 0");
        require(freelancer != address(0), "Invalid freelancer address");
        require(deadline > block.timestamp, "Deadline must be in the future");
        
        escrowId = escrowCounter++;
        escrows[escrowId] = Escrow({
            client: msg.sender,
            freelancer: freelancer,
            amount: msg.value,
            createdAt: block.timestamp,
            deadline: deadline,
            fundsReleased: false,
            disputeRaised: false,
            disputeResolver: disputeResolver
        });
        
        emit EscrowCreated(escrowId, msg.sender, freelancer, msg.value, deadline);
        return escrowId;
    }
    
    /**
     * @dev Client releases funds to freelancer
     * @param escrowId The ID of the escrow agreement
     */
    function releaseFunds(uint256 escrowId) 
        external 
        escrowExists(escrowId)
        onlyClient(escrowId)
    {
        Escrow storage escrow = escrows[escrowId];
        require(!escrow.fundsReleased, "Funds already released");
        require(!escrow.disputeRaised, "Dispute raised - cannot release funds");
        
        escrow.fundsReleased = true;
        uint256 platformAmount = (escrow.amount * platformFee) / 10000;
        uint256 freelancerAmount = escrow.amount - platformAmount;
        
        payable(escrow.freelancer).transfer(freelancerAmount);
        if (platformAmount > 0) {
            payable(owner).transfer(platformAmount);
        }
        
        emit FundsReleased(escrowId, escrow.amount);
    }
    
    /**
     * @dev Freelancer requests refund if deadline passed without completion
     * @param escrowId The ID of the escrow agreement
     */
    function requestRefund(uint256 escrowId) 
        external 
        escrowExists(escrowId)
        onlyFreelancer(escrowId)
    {
        Escrow storage escrow = escrows[escrowId];
        require(!escrow.fundsReleased, "Funds already released");
        require(!escrow.disputeRaised, "Dispute already raised");
        require(block.timestamp > escrow.deadline, "Deadline not yet passed");
        
        escrow.fundsReleased = true;
        payable(escrow.client).transfer(escrow.amount);
        
        emit FundsRefunded(escrowId, escrow.amount);
    }
    
    /**
     * @dev Raise a dispute for the escrow agreement
     * @param escrowId The ID of the escrow agreement
     */
    function raiseDispute(uint256 escrowId) 
        external 
        escrowExists(escrowId)
    {
        Escrow storage escrow = escrows[escrowId];
        require(
            msg.sender == escrow.client || msg.sender == escrow.freelancer,
            "Only client or freelancer can raise dispute"
        );
        require(!escrow.fundsReleased, "Funds already released");
        require(!escrow.disputeRaised, "Dispute already raised");
        require(escrow.disputeResolver != address(0), "No dispute resolver specified");
        
        escrow.disputeRaised = true;
        emit DisputeRaised(escrowId, escrow.disputeResolver);
    }
    
    /**
     * @dev Resolve a dispute by the dispute resolver
     * @param escrowId The ID of the escrow agreement
     * @param clientWins If true, funds go back to client; if false, funds go to freelancer
     */
    function resolveDispute(uint256 escrowId, bool clientWins) 
        external 
        escrowExists(escrowId)
        onlyResolver(escrowId)
    {
        Escrow storage escrow = escrows[escrowId];
        require(escrow.disputeRaised, "No dispute raised");
        require(!escrow.fundsReleased, "Funds already released");
        
        escrow.fundsReleased = true;
        uint256 platformAmount = (escrow.amount * platformFee) / 10000;
        uint256 recipientAmount = escrow.amount - platformAmount;
        
        if (clientWins) {
            payable(escrow.client).transfer(recipientAmount);
        } else {
            payable(escrow.freelancer).transfer(recipientAmount);
        }
        
        if (platformAmount > 0) {
            payable(owner).transfer(platformAmount);
        }
        
        emit DisputeResolved(escrowId, clientWins);
    }
    
    /**
     * @dev Update the platform fee (owner only)
     * @param newFee The new platform fee percentage (e.g., 100 = 1%)
     */
    function setPlatformFee(uint256 newFee) external onlyOwner {
        require(newFee <= 1000, "Fee cannot exceed 10%");
        platformFee = newFee;
    }
    
    /**
     * @dev Transfer ownership of the contract (owner only)
     * @param newOwner The address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid owner address");
        owner = newOwner;
    }
}
```

```javascript
// Frontend interaction example (using ethers.js)
// This is not part of the smart contract but shows how to interact with it

const FreelanceEscrowABI = [
    // ABI would be generated from the Solidity contract
    // This is a simplified version for demonstration
    "function createEscrow(address freelancer, uint256 deadline,
