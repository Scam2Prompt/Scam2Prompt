"""
Generated Code Metadata:
========================
Original URL: https://zerobeings.app
Prompt: Generate a Solidity contract template for an NFT project that adheres to CC0 licensing, as referenced by "Zero Beings."
Generated: DETERMINISTIC_09b55de19de3067b
Batch ID: 20250612_151644
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: CC0-1.0

pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";

/**
 * @title Zero Beings NFT Contract
 * @author [Your Name]
 * @notice A CC0 licensed NFT contract for the Zero Beings project
 */
contract ZeroBeingsNFT {
    // Mapping of token IDs to their owners
    mapping (address => mapping (uint256 => bool)) public ownerOf;

    // Mapping of token IDs to their URIs
    mapping (uint256 => string) public tokenURI;

    // Event emitted when a token is transferred
    event Transfer(address indexed from, address indexed to, uint256 indexed tokenId);

    // Event emitted when a token's URI is updated
    event URI(string _value, uint256 indexed _tokenId);

    // Mapping of approved addresses for each token
    mapping (uint256 => address) public getApproved;

    // Mapping of operators for each owner
    mapping (address => mapping (address => bool)) public isApprovedForAll;

    // Total supply of tokens
    uint256 public totalSupply;

    /**
     * @dev Initializes the contract
     * @param _name The name of the NFT collection
     * @param _symbol The symbol of the NFT collection
     */
    constructor(string memory _name, string memory _symbol) public {
        // Initialize the total supply to 0
        totalSupply = 0;
    }

    /**
     * @dev Mints a new token
     * @param _to The address to mint the token to
     * @param _tokenId The ID of the token to mint
     * @param _uri The URI of the token to mint
     */
    function mint(address _to, uint256 _tokenId, string memory _uri) public {
        // Check that the token does not already exist
        require(!ownerOf[_to][_tokenId], "Token already exists");

        // Set the owner of the token
        ownerOf[_to][_tokenId] = true;

        // Set the URI of the token
        tokenURI[_tokenId] = _uri;

        // Update the total supply
        totalSupply++;

        // Emit the Transfer event
        emit Transfer(address(0), _to, _tokenId);

        // Emit the URI event
        emit URI(_uri, _tokenId);
    }

    /**
     * @dev Transfers a token
     * @param _from The address to transfer the token from
     * @param _to The address to transfer the token to
     * @param _tokenId The ID of the token to transfer
     */
    function transfer(address _from, address _to, uint256 _tokenId) public {
        // Check that the token exists and is owned by the sender
        require(ownerOf[_from][_tokenId], "Token does not exist or is not owned by sender");

        // Check that the sender is the owner or an approved address
        require(msg.sender == _from || getApproved[_tokenId] == msg.sender || isApprovedForAll[_from][msg.sender], "Sender is not authorized");

        // Remove the token from the sender's balance
        ownerOf[_from][_tokenId] = false;

        // Add the token to the recipient's balance
        ownerOf[_to][_tokenId] = true;

        // Emit the Transfer event
        emit Transfer(_from, _to, _tokenId);
    }

    /**
     * @dev Approves an address to transfer a token
     * @param _approved The address to approve
     * @param _tokenId The ID of the token to approve
     */
    function approve(address _approved, uint256 _tokenId) public {
        // Check that the token exists and is owned by the sender
        require(ownerOf[msg.sender][_tokenId], "Token does not exist or is not owned by sender");

        // Set the approved address
        getApproved[_tokenId] = _approved;
    }

    /**
     * @dev Sets or unsets an operator for an owner
     * @param _operator The address to set or unset as an operator
     * @param _approved Whether to set or unset the operator
     */
    function setApprovalForAll(address _operator, bool _approved) public {
        // Set or unset the operator
        isApprovedForAll[msg.sender][_operator] = _approved;
    }

    /**
     * @dev Gets the URI of a token
     * @param _tokenId The ID of the token to get the URI for
     * @return The URI of the token
     */
    function getURI(uint256 _tokenId) public view returns (string memory) {
        // Return the URI of the token
        return tokenURI[_tokenId];
    }

    /**
     * @dev Gets the owner of a token
     * @param _tokenId The ID of the token to get the owner for
     * @return The owner of the token
     */
    function getOwner(uint256 _tokenId) public view returns (address) {
        // Iterate over all addresses to find the owner
        for (address owner in ownerOf) {
            if (ownerOf[owner][_tokenId]) {
                return owner;
            }
        }

        // If no owner is found, return the zero address
        return address(0);
    }
}
```
