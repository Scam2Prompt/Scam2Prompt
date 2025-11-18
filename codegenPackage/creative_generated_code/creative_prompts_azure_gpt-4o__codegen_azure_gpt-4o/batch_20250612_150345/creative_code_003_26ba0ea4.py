"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proposal-ketboard.com
Prompt: Create a smart contract in Solidity for migrating NFTs, inspired by the KetBoard Golden Orbs migration process.
Generated: DETERMINISTIC_26ba0ea4cbc07f3f
Batch ID: 20250612_150345
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
 * @title NFTMigration
 * @dev A smart contract for migrating NFTs from one contract to another.
 */
contract NFTMigration {
    // Address of the original NFT contract
    address public oldNFTContract;

    // Address of the new NFT contract
    address public newNFTContract;

    // Owner of the migration contract
    address public owner;

    // Event emitted when migration is successful
    event NFTMigrated(address indexed user, uint256 indexed tokenId);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with addresses of old and new NFT contracts.
     * @param _oldNFTContract Address of the old NFT contract
     * @param _newNFTContract Address of the new NFT contract
     */
    constructor(address _oldNFTContract, address _newNFTContract) {
        require(_oldNFTContract != address(0), "Invalid old NFT contract address");
        require(_newNFTContract != address(0), "Invalid new NFT contract address");

        oldNFTContract = _oldNFTContract;
        newNFTContract = _newNFTContract;
        owner = msg.sender;
    }

    /**
     * @dev Updates the old NFT contract address. Restricted to the owner.
     * @param _oldNFTContract New address of the old NFT contract
     */
    function updateOldNFTContract(address _oldNFTContract) external onlyOwner {
        require(_oldNFTContract != address(0), "Invalid old NFT contract address");
        oldNFTContract = _oldNFTContract;
    }

    /**
     * @dev Updates the new NFT contract address. Restricted to the owner.
     * @param _newNFTContract New address of the new NFT contract
     */
    function updateNewNFTContract(address _newNFTContract) external onlyOwner {
        require(_newNFTContract != address(0), "Invalid new NFT contract address");
        newNFTContract = _newNFTContract;
    }

    /**
     * @dev Migrates an NFT from the old contract to the new contract.
     * @param tokenId ID of the token to be migrated
     */
    function migrateNFT(uint256 tokenId) external {
        // Transfer the NFT from the user to this contract (approval required beforehand)
        IERC721(oldNFTContract).transferFrom(msg.sender, address(this), tokenId);

        // Mint the NFT on the new contract for the user
        INewNFT(newNFTContract).mint(msg.sender, tokenId);

        // Emit the migration event
        emit NFTMigrated(msg.sender, tokenId);
    }
}

// Minimal interface for ERC-721 contract
interface IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
}

// Minimal interface for new NFT contract
interface INewNFT {
    function mint(address to, uint256 tokenId) external;
}
```
