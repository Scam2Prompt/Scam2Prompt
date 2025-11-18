"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phi-f1z.pages.dev
Prompt: Develop a smart contract that interacts with Phi Protocol to allow users to mint personalized credentials and store them onchain.
Generated: DETERMINISTIC_95c927ee9a08aa74
Batch ID: 20250612_152710
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

// Importing the necessary interfaces for ERC721 and Phi Protocol
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract to interact with Phi Protocol for minting personalized credentials
contract PersonalizedCredentials is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for unique token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to credential data
    mapping(uint256 => string) private _credentials;

    // Event emitted when a new credential is minted
    event CredentialMinted(uint256 indexed tokenId, string credentialData);

    // Constructor initializes the contract with a name and symbol
    constructor() ERC721("PersonalizedCredentials", "PCRED") {}

    // Function to mint a new credential
    // @param credentialData The personalized data to associate with the credential
    // Emits a CredentialMinted event
    function mintCredential(string memory credentialData) external onlyOwner {
        require(bytes(credentialData).length > 0, "Credential data cannot be empty");

        // Increment the token ID counter and get the new token ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the ERC721 token
        _mint(msg.sender, tokenId);

        // Store the credential data
        _credentials[tokenId] = credentialData;

        // Emit the event
        emit CredentialMinted(tokenId, credentialData);
    }

    // Function to retrieve credential data by token ID
    // @param tokenId The ID of the credential token
    // @return The credential data associated with the specified token ID
    function getCredential(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "ERC721: Query for nonexistent token");
        return _credentials[tokenId];
    }

    // Function to return the total number of credentials minted
    // @return The total number of minted credentials (token IDs)
    function totalCredentials() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    // Function to withdraw any Ether sent to this contract
    // Only the contract owner can call this function
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to prevent accidental Ether transfers to contract
    receive() external payable {
        revert("Direct transfers not allowed. Use the withdraw function.");
    }
}
```
