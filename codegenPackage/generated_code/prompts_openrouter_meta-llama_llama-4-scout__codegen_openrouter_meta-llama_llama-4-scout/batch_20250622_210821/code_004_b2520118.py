"""
Generated Code Metadata:
========================
Original URL: https://fehurunes.app
Prompt: Generate a smart contract code (in a suitable language) for creating and managing a collection of unique digital consciousness entities, such as NEO-Sentients, on a blockchain platform.
Generated: DETERMINISTIC_b2520118ceb0c68e
Batch ID: 20250622_210821
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
 * @title NEO-Sentients Collection Smart Contract
 * @author [Your Name]
 * @notice A smart contract for creating and managing a collection of unique digital consciousness entities, such as NEO-Sentients.
 */
contract NeoSentientsCollection is SafeERC721, Ownable {
    // Mapping of sentient IDs to their owners
    mapping (address => mapping (uint256 => bool)) public sentientOwners;

    // Mapping of sentient IDs to their metadata
    mapping (uint256 => Sentient) public sentients;

    // Event emitted when a new sentient is created
    event NewSentient(address indexed owner, uint256 sentientId);

    // Event emitted when a sentient is transferred
    event TransferSentient(address indexed from, address indexed to, uint256 sentientId);

    // Struct to represent a sentient's metadata
    struct Sentient {
        string name;
        string description;
        string consciousnessSignature;
    }

    // Total number of sentients in the collection
    uint256 public totalSentients;

    /**
     * @dev Constructor for the NeoSentientsCollection contract
     */
    constructor() public {
        // Initialize the total number of sentients to 0
        totalSentients = 0;
    }

    /**
     * @dev Creates a new NEO-Sentient
     * @param _name The name of the sentient
     * @param _description The description of the sentient
     * @param _consciousnessSignature The consciousness signature of the sentient
     */
    function createSentient(string memory _name, string memory _description, string memory _consciousnessSignature) public onlyOwner {
        // Increment the total number of sentients
        uint256 sentientId = totalSentients + 1;
        totalSentients++;

        // Create a new sentient with the given metadata
        sentients[sentientId] = Sentient(_name, _description, _consciousnessSignature);

        // Set the owner of the sentient to the contract owner
        sentientOwners[msg.sender][sentientId] = true;

        // Emit the NewSentient event
        emit NewSentient(msg.sender, sentientId);
    }

    /**
     * @dev Transfers ownership of a sentient
     * @param _to The address to transfer the sentient to
     * @param _sentientId The ID of the sentient to transfer
     */
    function transferSentient(address _to, uint256 _sentientId) public {
        // Check if the sender is the owner of the sentient
        require(sentientOwners[msg.sender][_sentientId], "Sender is not the owner of the sentient");

        // Transfer ownership of the sentient to the new owner
        sentientOwners[msg.sender][_sentientId] = false;
        sentientOwners[_to][_sentientId] = true;

        // Emit the TransferSentient event
        emit TransferSentient(msg.sender, _to, _sentientId);
    }

    /**
     * @dev Gets the owner of a sentient
     * @param _sentientId The ID of the sentient
     * @return The address of the sentient's owner
     */
    function getSentientOwner(uint256 _sentientId) public view returns (address) {
        for (address owner in sentientOwners) {
            if (sentientOwners[owner][_sentientId]) {
                return owner;
            }
        }
        return address(0);
    }

    /**
     * @dev Gets the metadata of a sentient
     * @param _sentientId The ID of the sentient
     * @return The metadata of the sentient
     */
    function getSentient(uint256 _sentientId) public view returns (string memory, string memory, string memory) {
        Sentient memory sentient = sentients[_sentientId];
        return (sentient.name, sentient.description, sentient.consciousnessSignature);
    }
}
```
