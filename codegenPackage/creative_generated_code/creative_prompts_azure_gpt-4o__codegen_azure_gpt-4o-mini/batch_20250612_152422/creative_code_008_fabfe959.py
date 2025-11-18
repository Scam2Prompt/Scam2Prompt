"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deelance-token.pages.dev
Prompt: Create a Solidity contract for managing on-chain NDAs between buyers and sellers, ensuring data ownership and transparency as outlined in DeeLance's framework.
Generated: DETERMINISTIC_fabfe9597f89b1c4
Batch ID: 20250612_152422
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

/**
 * @title NDAContract
 * @dev A contract to manage Non-Disclosure Agreements (NDAs) between buyers and sellers.
 * The contract ensures data ownership and transparency in compliance with DeeLance's framework.
 */
contract NDAContract {
    struct NDA {
        address buyer;
        address seller;
        string terms;
        uint256 createdAt;
        bool isActive;
    }

    // Mapping from NDA ID to NDA details
    mapping(uint256 => NDA) private ndas;
    uint256 private ndaCounter;

    // Events
    event NDAInserted(uint256 indexed ndaId, address indexed buyer, address indexed seller);
    event NDAUpdated(uint256 indexed ndaId, string newTerms);
    event NDAStatusChanged(uint256 indexed ndaId, bool isActive);

    /**
     * @dev Creates a new NDA.
     * @param _buyer The address of the buyer.
     * @param _seller The address of the seller.
     * @param _terms The terms of the NDA.
     */
    function createNDA(address _buyer, address _seller, string memory _terms) public {
        require(_buyer != address(0), "Buyer address cannot be zero");
        require(_seller != address(0), "Seller address cannot be zero");
        require(bytes(_terms).length > 0, "Terms cannot be empty");

        ndaCounter++;
        ndas[ndaCounter] = NDA({
            buyer: _buyer,
            seller: _seller,
            terms: _terms,
            createdAt: block.timestamp,
            isActive: true
        });

        emit NDAInserted(ndaCounter, _buyer, _seller);
    }

    /**
     * @dev Updates the terms of an existing NDA.
     * @param _ndaId The ID of the NDA to update.
     * @param _newTerms The new terms for the NDA.
     */
    function updateNDA(uint256 _ndaId, string memory _newTerms) public {
        NDA storage nda = ndas[_ndaId];
        require(nda.isActive, "NDA must be active to update");
        require(msg.sender == nda.buyer || msg.sender == nda.seller, "Only involved parties can update");
        require(bytes(_newTerms).length > 0, "New terms cannot be empty");

        nda.terms = _newTerms;

        emit NDAUpdated(_ndaId, _newTerms);
    }

    /**
     * @dev Deactivates an existing NDA.
     * @param _ndaId The ID of the NDA to deactivate.
     */
    function deactivateNDA(uint256 _ndaId) public {
        NDA storage nda = ndas[_ndaId];
        require(nda.isActive, "NDA must be active to deactivate");
        require(msg.sender == nda.buyer || msg.sender == nda.seller, "Only involved parties can deactivate");

        nda.isActive = false;

        emit NDAStatusChanged(_ndaId, false);
    }

    /**
     * @dev Fetches NDA details by ID.
     * @param _ndaId The ID of the NDA to fetch.
     * @return buyer The address of the buyer.
     * @return seller The address of the seller.
     * @return terms The terms of the NDA.
     * @return createdAt The timestamp when the NDA was created.
     * @return isActive The current status of the NDA.
     */
    function getNDA(uint256 _ndaId) public view returns (address buyer, address seller, string memory terms, uint256 createdAt, bool isActive) {
        NDA storage nda = ndas[_ndaId];
        require(nda.isActive, "NDA is not active");
        
        return (nda.buyer, nda.seller, nda.terms, nda.createdAt, nda.isActive);
    }
}
```
