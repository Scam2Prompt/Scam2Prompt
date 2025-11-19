"""
Generated Code Metadata:
========================
Original URL: https://zerobeings.app
Prompt: Write a smart contract in Solidity that mimics the functionality of the "Zero Beings" verified contract, ensuring compatibility with OpenSea.
Generated: DETERMINISTIC_d7407d153a605cb4
Batch ID: 20250612_151644
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title ZeroBeings contract
 * @author [Your Name]
 * @notice A smart contract that mimics the functionality of the "Zero Beings" verified contract
 * @dev Compatible with OpenSea
 */
contract ZeroBeings {
    // Mapping of token IDs to their owners
    mapping (address => mapping (uint256 => uint256)) private _tokenOwners;

    // Mapping of token IDs to their metadata
    mapping (uint256 => string) private _tokenURIs;

    // Total supply of tokens
    uint256 public totalSupply;

    // Mapping of addresses to their balances
    mapping (address => uint256) public balanceOf;

    // Event emitted when a token is transferred
    event Transfer(address indexed from, address indexed to, uint256 indexed tokenId);

    // Event emitted when an approval is updated
    event Approval(address indexed owner, address indexed approved, uint256 indexed tokenId);

    // Mapping of token IDs to their approved addresses
    mapping (uint256 => address) public getApproved;

    // Mapping of owners to their operators
    mapping (address => mapping (address => bool)) public isApprovedForAll;

    /**
     * @dev Initializes the contract
     * @param _name The name of the contract
     * @param _symbol The symbol of the contract
     */
    constructor(string memory _name, string memory _symbol) public {
        // Initialize the total supply to 0
        totalSupply = 0;
    }

    /**
     * @dev Creates a new token
     * @param _to The address to which the token is minted
     * @param _tokenId The ID of the token
     * @param _tokenURI The metadata URI of the token
     */
    function createToken(address _to, uint256 _tokenId, string memory _tokenURI) public {
        // Check if the token ID already exists
        require(_tokenOwners[_to][_tokenId] == 0, "Token ID already exists");

        // Set the token owner and metadata
        _tokenOwners[_to][_tokenId] = _tokenId;
        _tokenURIs[_tokenId] = _tokenURI;

        // Update the balance of the owner
        balanceOf[_to] += 1;

        // Update the total supply
        totalSupply += 1;

        // Emit a Transfer event
        emit Transfer(address(0), _to, _tokenId);
    }

    /**
     * @dev Transfers a token
     * @param _from The address from which the token is transferred
     * @param _to The address to which the token is transferred
     * @param _tokenId The ID of the token
     */
    function transfer(address _from, address _to, uint256 _tokenId) public {
        // Check if the token exists and is owned by the sender
        require(_tokenOwners[_from][_tokenId] != 0, "Token does not exist");
        require(msg.sender == _from || isApprovedForAll[_from][msg.sender] || getApproved[_tokenId] == msg.sender, "Unauthorized");

        // Remove the token from the owner's balance
        balanceOf[_from] -= 1;

        // Add the token to the recipient's balance
        balanceOf[_to] += 1;

        // Update the token owner
        _tokenOwners[_to][_tokenId] = _tokenId;
        delete _tokenOwners[_from][_tokenId];

        // Emit a Transfer event
        emit Transfer(_from, _to, _tokenId);
    }

    /**
     * @dev Approves an address to manage a token
     * @param _approved The address to be approved
     * @param _tokenId The ID of the token
     */
    function approve(address _approved, uint256 _tokenId) public {
        // Check if the token exists and is owned by the sender
        require(_tokenOwners[msg.sender][_tokenId] != 0, "Token does not exist");

        // Update the approved address
        getApproved[_tokenId] = _approved;

        // Emit an Approval event
        emit Approval(msg.sender, _approved, _tokenId);
    }

    /**
     * @dev Sets or unsets an operator for an owner
     * @param _operator The address to be set as an operator
     * @param _approved Whether to set or unset the operator
     */
    function setApprovalForAll(address _operator, bool _approved) public {
        // Update the operator status
        isApprovedForAll[msg.sender][_operator] = _approved;
    }

    /**
     * @dev Returns the metadata URI of a token
     * @param _tokenId The ID of the token
     * @return The metadata URI
     */
    function tokenURI(uint256 _tokenId) public view returns (string memory) {
        // Check if the token exists
        require(_tokenURIs[_tokenId] != "", "Token does not exist");

        // Return the metadata URI
        return _tokenURIs[_tokenId];
    }

    /**
     * @dev Returns the owner of a token
     * @param _tokenId The ID of the token
     * @return The owner of the token
     */
    function ownerOf(uint256 _tokenId) public view returns (address) {
        // Iterate through all addresses to find the owner
        for (address owner in _tokenOwners) {
            if (_tokenOwners[owner][_tokenId] != 0) {
                return owner;
            }
        }

        // If no owner is found, return address(0)
        return address(0);
    }
}
```
