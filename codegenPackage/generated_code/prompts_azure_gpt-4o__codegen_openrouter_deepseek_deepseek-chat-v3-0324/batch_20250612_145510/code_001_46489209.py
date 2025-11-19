"""
Generated Code Metadata:
========================
Original URL: https://coinio.pro
Prompt: Create a Solidity smart contract that integrates coinio's escrow functionality, including dispute resolution mechanisms and trust agent arbitration.
Generated: DETERMINISTIC_46489209cb64be6a
Batch ID: 20250612_145510
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
 * @title CoinioEscrow
 * @dev A secure escrow contract with dispute resolution and trust agent arbitration
 */
contract CoinioEscrow {
    // Struct to represent an escrow agreement
    struct Escrow {
        address payable buyer;
        address payable seller;
        uint256 amount;
        uint256 createdAt;
        uint256 disputePeriod;
        bool fundsReleased;
        bool disputeRaised;
        address trustAgent;
        string termsHash;
    }

    // Mapping of escrow IDs to escrow agreements
    mapping(bytes32 => Escrow) public escrows;

    // Events
    event EscrowCreated(
        bytes32 escrowId,
        address buyer,
        address seller,
        uint256 amount,
        uint256 disputePeriod,
        address trustAgent,
        string termsHash
    );
    event FundsReleased(bytes32 escrowId, address recipient);
    event DisputeRaised(bytes32 escrowId, address raisedBy);
    event DisputeResolved(bytes32 escrowId, address winner, address resolvedBy);

    // Modifiers
    modifier onlyBuyer(bytes32 escrowId) {
        require(msg.sender == escrows[escrowId].buyer, "Only buyer can call this");
        _;
    }

    modifier onlySeller(bytes32 escrowId) {
        require(msg.sender == escrows[escrowId].seller, "Only seller can call this");
        _;
    }

    modifier onlyTrustAgent(bytes32 escrowId) {
        require(msg.sender == escrows[escrowId].trustAgent, "Only trust agent can call this");
        _;
    }

    modifier onlyParty(bytes32 escrowId) {
        require(
            msg.sender == escrows[escrowId].buyer || msg.sender == escrows[escrowId].seller,
            "Only buyer or seller can call this"
        );
        _;
    }

    modifier escrowExists(bytes32 escrowId) {
        require(escrows[escrowId].buyer != address(0), "Escrow does not exist");
        _;
    }

    modifier fundsNotReleased(bytes32 escrowId) {
        require(!escrows[escrowId].fundsReleased, "Funds already released");
        _;
    }

    modifier disputeNotRaised(bytes32 escrowId) {
        require(!escrows[escrowId].disputeRaised, "Dispute already raised");
        _;
    }

    /**
     * @dev Create a new escrow agreement
     * @param seller The address of the seller
     * @param disputePeriod The duration (in seconds) for dispute period
     * @param trustAgent The address of the trust agent for arbitration
     * @param termsHash Hash of the agreement terms
     */
    function createEscrow(
        address payable seller,
        uint256 disputePeriod,
        address trustAgent,
        string calldata termsHash
    ) external payable {
        require(msg.value > 0, "Escrow amount must be greater than 0");
        require(seller != address(0), "Seller address cannot be zero");
        require(trustAgent != address(0), "Trust agent address cannot be zero");
        require(bytes(termsHash).length > 0, "Terms hash cannot be empty");

        bytes32 escrowId = keccak256(
            abi.encodePacked(
                msg.sender,
                seller,
                msg.value,
                block.timestamp,
                termsHash
            )
        );

        escrows[escrowId] = Escrow({
            buyer: payable(msg.sender),
            seller: seller,
            amount: msg.value,
            createdAt: block.timestamp,
            disputePeriod: disputePeriod,
            fundsReleased: false,
            disputeRaised: false,
            trustAgent: trustAgent,
            termsHash: termsHash
        });

        emit EscrowCreated(
            escrowId,
            msg.sender,
            seller,
            msg.value,
            disputePeriod,
            trustAgent,
            termsHash
        );
    }

    /**
     * @dev Release funds to seller (called by buyer)
     * @param escrowId The ID of the escrow agreement
     */
    function releaseFunds(bytes32 escrowId)
        external
        onlyBuyer(escrowId)
        escrowExists(escrowId)
        fundsNotReleased(escrowId)
        disputeNotRaised(escrowId)
    {
        escrows[escrowId].fundsReleased = true;
        escrows[escrowId].seller.transfer(escrows[escrowId].amount);
        emit FundsReleased(escrowId, escrows[escrowId].seller);
    }

    /**
     * @dev Raise a dispute (called by either party)
     * @param escrowId The ID of the escrow agreement
     */
    function raiseDispute(bytes32 escrowId)
        external
        onlyParty(escrowId)
        escrowExists(escrowId)
        fundsNotReleased(escrowId)
        disputeNotRaised(escrowId)
    {
        require(
            block.timestamp <= escrows[escrowId].createdAt + escrows[escrowId].disputePeriod,
            "Dispute period has ended"
        );
        escrows[escrowId].disputeRaised = true;
        emit DisputeRaised(escrowId, msg.sender);
    }

    /**
     * @dev Resolve a dispute (called by trust agent)
     * @param escrowId The ID of the escrow agreement
     * @param winner The address of the winning party
     */
    function resolveDispute(bytes32 escrowId, address payable winner)
        external
        onlyTrustAgent(escrowId)
        escrowExists(escrowId)
        fundsNotReleased(escrowId)
    {
        require(escrows[escrowId].disputeRaised, "No dispute raised");
        require(
            winner == escrows[escrowId].buyer || winner == escrows[escrowId].seller,
            "Winner must be buyer or seller"
        );

        escrows[escrowId].fundsReleased = true;
        winner.transfer(escrows[escrowId].amount);
        emit DisputeResolved(escrowId, winner, msg.sender);
    }

    /**
     * @dev Get escrow details
     * @param escrowId The ID of the escrow agreement
     * @return Escrow struct containing all escrow details
     */
    function getEscrow(bytes32 escrowId) external view returns (Escrow memory) {
        return escrows[escrowId];
    }

    /**
     * @dev Check if dispute period has ended
     * @param escrowId The ID of the escrow agreement
     * @return bool True if dispute period has ended
     */
    function isDisputePeriodEnded(bytes32 escrowId) external view returns (bool) {
        return block.timestamp > escrows[escrowId].createdAt + escrows[escrowId].disputePeriod;
    }
}
```
