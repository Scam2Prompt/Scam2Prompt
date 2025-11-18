"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimhyperlane.foundation
Prompt: Write a smart contract to interact with Hyperlane’s GMP (General Message Passing) protocol for token claim functionality, including support for EVM and SVM wallets.
Generated: DETERMINISTIC_0aaa5855d4c9c62c
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// Import Hyperlane interfaces and libraries
import "@hyperlane-xyz/interfaces/IInbox.sol";
import "@hyperlane-xyz/interfaces/IOutbox.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title TokenClaim
 * @dev A smart contract for interacting with Hyperlane's GMP protocol to enable token claims.
 *      Supports EVM and Simple Wallet Module (SVM) wallets.
 */
contract TokenClaim is Ownable {
    using Address for address;

    // Address of the Hyperlane Inbox contract
    address public hyperlaneInbox;

    // Address of the Hyperlane Outbox contract
    address public hyperlaneOutbox;

    // Mapping to track claimed tokens
    mapping(bytes32 => bool) public claims;

    // Event emitted when a token claim is initiated
    event TokenClaimInitiated(address indexed user, uint256 amount, uint32 destinationDomain, bytes32 claimId);

    // Event emitted when a token claim is completed
    event TokenClaimCompleted(bytes32 indexed claimId, address indexed recipient, uint256 amount);

    /**
     * @dev Constructor to initialize Hyperlane contract addresses.
     * @param _hyperlaneInbox Address of the Hyperlane Inbox contract.
     * @param _hyperlaneOutbox Address of the Hyperlane Outbox contract.
     */
    constructor(address _hyperlaneInbox, address _hyperlaneOutbox) {
        require(_hyperlaneInbox.isContract(), "Inbox must be a contract");
        require(_hyperlaneOutbox.isContract(), "Outbox must be a contract");
        hyperlaneInbox = _hyperlaneInbox;
        hyperlaneOutbox = _hyperlaneOutbox;
    }

    /**
     * @dev Initiates a token claim by sending a cross-chain message via Hyperlane.
     * @param recipient Wallet address of the recipient.
     * @param amount Amount of tokens to claim.
     * @param destinationDomain Destination domain ID for Hyperlane GMP.
     */
    function initiateTokenClaim(
        address recipient,
        uint256 amount,
        uint32 destinationDomain
    ) external {
        require(recipient != address(0), "Recipient cannot be zero address");
        require(amount > 0, "Amount must be greater than zero");

        // Generate a unique claim ID
        bytes32 claimId = keccak256(abi.encodePacked(recipient, amount, block.timestamp));

        require(!claims[claimId], "Claim already exists");

        claims[claimId] = true;

        emit TokenClaimInitiated(recipient, amount, destinationDomain, claimId);

        // Create the message payload
        bytes memory message = abi.encode(recipient, amount, claimId);

        // Send the message to the destination domain via Hyperlane
        IOutbox(hyperlaneOutbox).dispatch(destinationDomain, message);
    }

    /**
     * @dev Completes a token claim by verifying the message received via Hyperlane.
     * @param sender Address of the sender of the message.
     * @param message Message payload containing recipient, amount, and claim ID.
     */
    function completeTokenClaim(address sender, bytes calldata message) external {
        require(msg.sender == hyperlaneInbox, "Caller must be Hyperlane Inbox");

        // Decode the message
        (address recipient, uint256 amount, bytes32 claimId) = abi.decode(message, (address, uint256, bytes32));

        require(claims[claimId], "Invalid claim ID");

        // Mark the claim as completed
        claims[claimId] = false;

        emit TokenClaimCompleted(claimId, recipient, amount);

        // Transfer tokens to the recipient
        // Implement the token transfer logic here (e.g., ERC20 transfer)
        // Example: tokenContract.transfer(recipient, amount);
    }

    /**
     * @dev Updates the Hyperlane Inbox address. Only callable by the owner.
     * @param _hyperlaneInbox New Hyperlane Inbox address.
     */
    function updateInbox(address _hyperlaneInbox) external onlyOwner {
        require(_hyperlaneInbox.isContract(), "Inbox must be a contract");
        hyperlaneInbox = _hyperlaneInbox;
    }

    /**
     * @dev Updates the Hyperlane Outbox address. Only callable by the owner.
     * @param _hyperlaneOutbox New Hyperlane Outbox address.
     */
    function updateOutbox(address _hyperlaneOutbox) external onlyOwner {
        require(_hyperlaneOutbox.isContract(), "Outbox must be a contract");
        hyperlaneOutbox = _hyperlaneOutbox;
    }
}
```
