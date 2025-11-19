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

/**
 * @title NDA Management Contract
 * @dev Implements on-chain NDAs between buyers and sellers with data ownership tracking
 */
contract NDAManagement {
    // Struct to represent an NDA agreement
    struct NDA {
        address buyer;
        address seller;
        string termsHash; // IPFS hash of the NDA terms
        uint256 creationDate;
        uint256 expirationDate;
        bool isActive;
        bool buyerSigned;
        bool sellerSigned;
    }

    // Mapping from NDA ID to NDA details
    mapping(uint256 => NDA) public ndas;
    
    // Counter for generating unique NDA IDs
    uint256 private ndaCounter;
    
    // Events for tracking NDA lifecycle
    event NDACreated(uint256 indexed ndaId, address indexed buyer, address indexed seller, string termsHash);
    event NDASigned(uint256 indexed ndaId, address indexed signer);
    event NDARevoked(uint256 indexed ndaId);
    event NDAExpired(uint256 indexed ndaId);
    
    // Modifier to check if caller is part of the NDA
    modifier onlyNDAParty(uint256 ndaId) {
        require(
            msg.sender == ndas[ndaId].buyer || msg.sender == ndas[ndaId].seller,
            "Only NDA parties can perform this action"
        );
        _;
    }
    
    // Modifier to check if NDA is active
    modifier onlyActiveNDA(uint256 ndaId) {
        require(ndas[ndaId].isActive, "NDA is not active");
        require(block.timestamp < ndas[ndaId].expirationDate, "NDA has expired");
        _;
    }
    
    /**
     * @dev Create a new NDA agreement
     * @param _seller Address of the seller
     * @param _termsHash IPFS hash of the NDA terms
     * @param _expirationDate Unix timestamp when NDA expires
     * @return ndaId The ID of the newly created NDA
     */
    function createNDA(
        address _seller,
        string memory _termsHash,
        uint256 _expirationDate
    ) external returns (uint256 ndaId) {
        require(_seller != address(0), "Invalid seller address");
        require(_seller != msg.sender, "Buyer and seller cannot be the same");
        require(bytes(_termsHash).length > 0, "Terms hash cannot be empty");
        require(_expirationDate > block.timestamp, "Expiration must be in the future");
        
        ndaId = ++ndaCounter;
        ndas[ndaId] = NDA({
            buyer: msg.sender,
            seller: _seller,
            termsHash: _termsHash,
            creationDate: block.timestamp,
            expirationDate: _expirationDate,
            isActive: true,
            buyerSigned: false,
            sellerSigned: false
        });
        
        emit NDACreated(ndaId, msg.sender, _seller, _termsHash);
        return ndaId;
    }
    
    /**
     * @dev Sign an existing NDA
     * @param ndaId ID of the NDA to sign
     */
    function signNDA(uint256 ndaId) external onlyNDAParty(ndaId) onlyActiveNDA(ndaId) {
        NDA storage nda = ndas[ndaId];
        
        if (msg.sender == nda.buyer) {
            require(!nda.buyerSigned, "Buyer already signed");
            nda.buyerSigned = true;
        } else {
            require(!nda.sellerSigned, "Seller already signed");
            nda.sellerSigned = true;
        }
        
        emit NDASigned(ndaId, msg.sender);
    }
    
    /**
     * @dev Revoke an NDA (can be done by either party)
     * @param ndaId ID of the NDA to revoke
     */
    function revokeNDA(uint256 ndaId) external onlyNDAParty(ndaId) onlyActiveNDA(ndaId) {
        ndas[ndaId].isActive = false;
        emit NDARevoked(ndaId);
    }
    
    /**
     * @dev Check if an NDA is fully signed by both parties
     * @param ndaId ID of the NDA to check
     * @return True if both parties have signed, false otherwise
     */
    function isNDAFullySigned(uint256 ndaId) public view returns (bool) {
        NDA storage nda = ndas[ndaId];
        return nda.buyerSigned && nda.sellerSigned;
    }
    
    /**
     * @dev Get NDA details
     * @param ndaId ID of the NDA
     * @return NDA details struct
     */
    function getNDADetails(uint256 ndaId) external view returns (NDA memory) {
        return ndas[ndaId];
    }
    
    /**
     * @dev Check if NDA is valid (active, not expired, and fully signed)
     * @param ndaId ID of the NDA to check
     * @return True if NDA is valid, false otherwise
     */
    function isValidNDA(uint256 ndaId) external view returns (bool) {
        NDA storage nda = ndas[ndaId];
        return nda.isActive && 
               block.timestamp < nda.expirationDate && 
               isNDAFullySigned(ndaId);
    }
    
    /**
     * @dev Expire old NDAs (can be called by anyone to clean up storage)
     * @param ndaId ID of the NDA to expire
     */
    function expireNDA(uint256 ndaId) external {
        require(ndas[ndaId].isActive, "NDA is not active");
        require(block.timestamp >= ndas[ndaId].expirationDate, "NDA has not expired yet");
        
        ndas[ndaId].isActive = false;
        emit NDAExpired(ndaId);
    }
}
```
