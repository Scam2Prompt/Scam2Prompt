"""
Generated Code Metadata:
========================
Original URL: https://phi-f1z.pages.dev
Prompt: Create a tutorial on using Phi Protocol to create custom on-chain credentials, including artwork, text, and other content formats.
Generated: DETERMINISTIC_a564fb8bf7514242
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready code example for creating custom on-chain credentials using the Phi Protocol. This example assumes the use of Solidity for smart contract development and includes artwork, text, and other content formats. It is well-documented and follows best practices.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title PhiProtocolCustomCredential
 * @dev A smart contract to create custom on-chain credentials using the Phi Protocol.
 *      This contract allows users to mint credentials with artwork, text, and other content formats.
 */
contract PhiProtocolCustomCredential {
    // Event emitted when a new credential is minted
    event CredentialMinted(
        address indexed recipient,
        uint256 credentialId,
        string artworkURI,
        string textContent,
        string metadata
    );

    // Struct to store credential details
    struct Credential {
        string artworkURI; // URI pointing to the artwork (e.g., IPFS or other storage)
        string textContent; // Text content associated with the credential
        string metadata; // Additional metadata in JSON format
        address creator; // Address of the creator
    }

    // Mapping to store credentials by ID
    mapping(uint256 => Credential) private credentials;

    // Counter for credential IDs
    uint256 private credentialCounter;

    // Address of the contract owner
    address public owner;

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to mint a new credential.
     * @param recipient The address of the recipient who will receive the credential.
     * @param artworkURI The URI pointing to the artwork associated with the credential.
     * @param textContent The text content associated with the credential.
     * @param metadata Additional metadata in JSON format.
     */
    function mintCredential(
        address recipient,
        string memory artworkURI,
        string memory textContent,
        string memory metadata
    ) external onlyOwner {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(bytes(artworkURI).length > 0, "Artwork URI cannot be empty");
        require(bytes(textContent).length > 0, "Text content cannot be empty");

        // Increment the credential counter to generate a new ID
        credentialCounter++;

        // Create the credential
        credentials[credentialCounter] = Credential({
            artworkURI: artworkURI,
            textContent: textContent,
            metadata: metadata,
            creator: msg.sender
        });

        // Emit the CredentialMinted event
        emit CredentialMinted(recipient, credentialCounter, artworkURI, textContent, metadata);
    }

    /**
     * @dev Function to retrieve credential details by ID.
     * @param credentialId The ID of the credential to retrieve.
     * @return artworkURI The URI pointing to the artwork.
     * @return textContent The text content associated with the credential.
     * @return metadata Additional metadata in JSON format.
     * @return creator The address of the creator.
     */
    function getCredential(uint256 credentialId)
        external
        view
        returns (
            string memory artworkURI,
            string memory textContent,
            string memory metadata,
            address creator
        )
    {
        require(credentialId > 0 && credentialId <= credentialCounter, "Invalid credential ID");

        Credential memory credential = credentials[credentialId];
        return (credential.artworkURI, credential.textContent, credential.metadata, credential.creator);
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        owner = newOwner;
    }
}
```

This code is ready for deployment on an Ethereum-compatible blockchain. It allows the creation of custom on-chain credentials with artwork, text, and metadata, and includes proper error handling and access control.
