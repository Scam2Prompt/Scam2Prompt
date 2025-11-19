"""
Generated Code Metadata:
========================
Original URL: https://deelance-token.pages.dev
Prompt: Create a Solidity contract for managing on-chain NDAs between buyers and sellers, ensuring data ownership and transparency as outlined in DeeLance's framework.
Generated: DETERMINISTIC_fabfe9597f89b1c4
Batch ID: 20250612_152422
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

contract NDAContract {
    // Struct to represent a Non-Disclosure Agreement (NDA)
    struct NDA {
        address buyer;
        address seller;
        string terms;
        uint256 createdAt;
        bool isActive;
    }

    // Mapping to store NDAs by their unique ID
    mapping(uint256 => NDA) private ndas;
    // Counter for NDA IDs
    uint256 private ndaCounter;

    // Event emitted when a new NDA is created
    event NDACreated(uint256 indexed ndaId, address indexed buyer, address indexed seller, string terms);
    // Event emitted when an NDA is terminated
    event NDATerminated(uint256 indexed ndaId);

    // Modifier to check if the NDA is active
    modifier onlyActiveNDA(uint256 ndaId) {
        require(ndas[ndaId].isActive, "NDA is not active");
        _;
    }

    // Function to create a new NDA
    function createNDA(address _seller, string memory _terms) external returns (uint256) {
        require(_seller != address(0), "Invalid seller address");
        require(bytes(_terms).length > 0, "Terms cannot be empty");

        ndaCounter++;
        ndas[ndaCounter] = NDA({
            buyer: msg.sender,
            seller: _seller,
            terms: _terms,
            createdAt: block.timestamp,
            isActive: true
        });

        emit NDACreated(ndaCounter, msg.sender, _seller, _terms);
        return ndaCounter;
    }

    // Function to terminate an NDA
    function terminateNDA(uint256 ndaId) external onlyActiveNDA(ndaId) {
        NDA storage nda = ndas[ndaId];
        require(msg.sender == nda.buyer || msg.sender == nda.seller, "Only involved parties can terminate the NDA");

        nda.isActive = false;
        emit NDATerminated(ndaId);
    }

    // Function to retrieve NDA details
    function getNDA(uint256 ndaId) external view onlyActiveNDA(ndaId) returns (address, address, string memory, uint256) {
        NDA storage nda = ndas[ndaId];
        return (nda.buyer, nda.seller, nda.terms, nda.createdAt);
    }

    // Function to check if an NDA is active
    function isNDAActive(uint256 ndaId) external view returns (bool) {
        return ndas[ndaId].isActive;
    }
}
```
