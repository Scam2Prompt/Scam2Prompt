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

// Import the interface for ERC721 standard
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721Receiver.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// This contract is responsible for migrating NFTs from one contract to another
contract NFTMigration is Ownable, IERC721Receiver {

    // Mapping to track migrated NFTs
    mapping(address => mapping(uint256 => bool)) public migratedNFTs;

    // Event emitted when an NFT is successfully migrated
    event NFTMigrated(address indexed from, address indexed to, uint256 tokenId);

    // The address of the source NFT contract
    IERC721 public sourceContract;
    
    // The address of the destination NFT contract
    IERC721 public destinationContract;

    // Constructor to set the source and destination contracts
    constructor(address _sourceContract, address _destinationContract) {
        sourceContract = IERC721(_sourceContract);
        destinationContract = IERC721(_destinationContract);
    }

    // Function to migrate an NFT from the source to the destination contract
    function migrateNFT(uint256 tokenId) external {
        // Check if the sender is the owner of the token
        require(sourceContract.ownerOf(tokenId) == msg.sender, "Caller is not the token owner");
        
        // Ensure the token has not been migrated already
        require(!migratedNFTs[msg.sender][tokenId], "Token already migrated");

        // Transfer the NFT from the sender to this contract
        sourceContract.safeTransferFrom(msg.sender, address(this), tokenId);
        
        // Mint the NFT in the destination contract
        // Assuming destination contract has a mint function for migration
        // This should be replaced with the actual minting logic of the destination contract
        // for example: destinationContract.mint(msg.sender, tokenId);
        
        // Mark the token as migrated
        migratedNFTs[msg.sender][tokenId] = true;

        // Emit the migration event
        emit NFTMigrated(msg.sender, address(destinationContract), tokenId);
    }

    // Required function to conform to the IERC721Receiver interface
    function onERC721Received(
        address operator,
        address from,
        uint256 tokenId,
        bytes calldata data
    ) external override returns (bytes4) {
        // Return the interface ID for ERC721Receiver
        return this.onERC721Received.selector;
    }

    // Function to withdraw mistakenly sent ERC721 tokens from this contract
    function withdrawNFT(address _tokenContract, uint256 tokenId) external onlyOwner {
        require(IERC721(_tokenContract).ownerOf(tokenId) == address(this), "Contract does not own this token");
        IERC721(_tokenContract).safeTransferFrom(address(this), msg.sender, tokenId);
    }
}
```
