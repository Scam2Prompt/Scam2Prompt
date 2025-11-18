"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kevinland.pages.dev
Prompt: Write a smart contract in Solidity that reserves intellectual property rights for the NFT project team, while granting specific rights to NFT owners, as described in KevinLand's terms.
Generated: DETERMINISTIC_420f31433f30405c
Batch ID: 20250612_152827
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
 * @title IntellectualPropertyRights
 * @dev A smart contract to manage intellectual property rights
 *      for an NFT project team and NFT owners based on KevinLand's terms.
 */
contract IntellectualPropertyRights {
    // Address of the NFT project team
    address public projectTeam;
    
    // Mapping to track NFT owners and their granted rights
    mapping(uint256 => address) public nftOwners;

    // Struct to define rights for NFT owners
    struct Rights {
        bool canDisplay;       // Right to publicly display the NFT art
        bool canCommercialize; // Right to use the NFT art commercially
    }

    // Mapping to store rights of NFT owners per NFT ID
    mapping(uint256 => Rights) public nftRights;

    // Event emitted when an NFT owner updates their rights
    event RightsUpdated(uint256 indexed nftId, address indexed owner, Rights rights);

    // Modifier to restrict access to the project team
    modifier onlyProjectTeam() {
        require(msg.sender == projectTeam, "Only the project team can perform this action");
        _;
    }

    // Modifier to restrict access to the NFT owner of a specific NFT ID
    modifier onlyNFTOwner(uint256 nftId) {
        require(nftOwners[nftId] == msg.sender, "Only the NFT owner can perform this action");
        _;
    }

    // Constructor to initialize the contract with the project team's address
    constructor() {
        projectTeam = msg.sender;
    }

    /**
     * @dev Sets the NFT owner and their default rights.
     * @param nftId The unique identifier for the NFT.
     * @param owner The address of the NFT owner.
     */
    function setNFTOwner(uint256 nftId, address owner) external onlyProjectTeam {
        nftOwners[nftId] = owner;

        // Default rights granted to the NFT owner
        nftRights[nftId] = Rights({
            canDisplay: true,
            canCommercialize: false // Default: Commercial use not allowed
        });
    }

    /**
     * @dev Updates the rights for a specific NFT owned by the caller.
     * @param nftId The unique identifier for the NFT.
     * @param canDisplay Whether the NFT owner can display the NFT art publicly.
     * @param canCommercialize Whether the NFT owner can use the NFT art commercially.
     */
    function updateRights(uint256 nftId, bool canDisplay, bool canCommercialize) external onlyNFTOwner(nftId) {
        nftRights[nftId] = Rights({
            canDisplay: canDisplay,
            canCommercialize: canCommercialize
        });

        emit RightsUpdated(nftId, msg.sender, nftRights[nftId]);
    }

    /**
     * @dev Gets the rights of a specific NFT owner.
     * @param nftId The unique identifier for the NFT.
     * @return Rights The rights associated with the NFT owner.
     */
    function getRights(uint256 nftId) external view returns (Rights memory) {
        return nftRights[nftId];
    }

    /**
     * @dev Transfers the ownership of an NFT to a new owner.
     * @param nftId The unique identifier for the NFT.
     * @param newOwner The address of the new owner.
     */
    function transferNFTOwnership(uint256 nftId, address newOwner) external onlyNFTOwner(nftId) {
        nftOwners[nftId] = newOwner;

        // Reset rights for the new owner
        nftRights[nftId] = Rights({
            canDisplay: true,
            canCommercialize: false // Default rights reset
        });
    }
}
```

This contract demonstrates a clean implementation of intellectual property rights management for NFT project teams and owners, following Solidity best practices, with detailed inline comments for documentation.
