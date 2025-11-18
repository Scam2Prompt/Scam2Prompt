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
pragma solidity ^0.8.17;

/**
 * @title NDAContract
 * @dev A smart contract for managing on-chain NDAs between buyers and sellers.
 * Ensures data ownership, transparency, and security.
 */
contract NDAContract {
    // Struct representing an NDA
    struct NDA {
        address buyer;       // Address of the buyer
        address seller;      // Address of the seller
        string agreementHash; // Hash of the NDA document (IPFS, Arweave, etc.)
        uint256 timestamp;    // Timestamp when the NDA was created
        bool isSignedByBuyer; // Whether the buyer signed the NDA
        bool isSignedBySeller; // Whether the seller signed the NDA
    }

    // Mapping of NDA IDs to NDA details
    mapping(uint256 => NDA) public ndas;

    // Counter for generating unique NDA IDs
    uint256 public ndaIdCounter;

    // Events
    event NDACreated(uint256 indexed ndaId, address indexed buyer, address indexed seller, string agreementHash);
    event NDASigned(uint256 indexed ndaId, address indexed signer);

    /**
     * @dev Create a new NDA.
     * @param _buyer Address of the buyer.
     * @param _seller Address of the seller.
     * @param _agreementHash Hash of the NDA document.
     */
    function createNDA(address _buyer, address _seller, string memory _agreementHash) external {
        require(_buyer != address(0), "Invalid buyer address");
        require(_seller != address(0), "Invalid seller address");
        require(bytes(_agreementHash).length > 0, "Agreement hash cannot be empty");

        ndaIdCounter++; // Increment NDA ID counter
        uint256 newNdaId = ndaIdCounter;

        // Create a new NDA and store it in the mapping
        ndas[newNdaId] = NDA({
            buyer: _buyer,
            seller: _seller,
            agreementHash: _agreementHash,
            timestamp: block.timestamp,
            isSignedByBuyer: false,
            isSignedBySeller: false
        });

        emit NDACreated(newNdaId, _buyer, _seller, _agreementHash);
    }

    /**
     * @dev Sign an NDA.
     * @param _ndaId ID of the NDA to sign.
     */
    function signNDA(uint256 _ndaId) external {
        NDA storage nda = ndas[_ndaId];
        require(nda.buyer != address(0) && nda.seller != address(0), "NDA does not exist");
        require(msg.sender == nda.buyer || msg.sender == nda.seller, "Only buyer or seller can sign the NDA");

        if (msg.sender == nda.buyer) {
            require(!nda.isSignedByBuyer, "Buyer has already signed the NDA");
            nda.isSignedByBuyer = true;
        } else if (msg.sender == nda.seller) {
            require(!nda.isSignedBySeller, "Seller has already signed the NDA");
            nda.isSignedBySeller = true;
        }

        emit NDASigned(_ndaId, msg.sender);
    }

    /**
     * @dev Get details of an NDA.
     * @param _ndaId ID of the NDA to fetch.
     * @return NDA details.
     */
    function getNDA(uint256 _ndaId) external view returns (
        address buyer,
        address seller,
        string memory agreementHash,
        uint256 timestamp,
        bool isSignedByBuyer,
        bool isSignedBySeller
    ) {
        NDA memory nda = ndas[_ndaId];
        require(nda.buyer != address(0) && nda.seller != address(0), "NDA does not exist");

        return (
            nda.buyer,
            nda.seller,
            nda.agreementHash,
            nda.timestamp,
            nda.isSignedByBuyer,
            nda.isSignedBySeller
        );
    }
}
```
