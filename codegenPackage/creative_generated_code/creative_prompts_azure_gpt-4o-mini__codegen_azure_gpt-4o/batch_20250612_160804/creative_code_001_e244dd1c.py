"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ronin-cyberkongz.pages.dev
Prompt: Write a Solidity contract that utilizes the Guardian Contract for on-chain two-factor authentication for NFTs.
Generated: DETERMINISTIC_e244dd1c47d6ae35
Batch ID: 20250612_160804
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
 * @title TwoFactorNFT
 * @dev Implements on-chain two-factor authentication for NFTs using a Guardian Contract.
 */
contract TwoFactorNFT {
    // State variables
    address public owner; // Owner of the contract
    address public guardianContract; // Address of the Guardian Contract
    mapping(uint256 => address) public nftOwners; // Mapping of NFT IDs to their owners
    
    // Events
    event NFTMinted(uint256 indexed nftId, address indexed to);
    event NFTTransferred(uint256 indexed nftId, address indexed from, address indexed to);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier onlyGuardian() {
        require(msg.sender == guardianContract, "Caller is not the guardian");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the owner and guardian contract address.
     * @param _guardianContract Address of the Guardian Contract.
     */
    constructor(address _guardianContract) {
        require(_guardianContract != address(0), "Guardian contract address cannot be zero");
        owner = msg.sender;
        guardianContract = _guardianContract;
    }

    /**
     * @dev Updates the guardian contract address. Only callable by the owner.
     * @param _newGuardianContract Address of the new Guardian Contract.
     */
    function updateGuardianContract(address _newGuardianContract) external onlyOwner {
        require(_newGuardianContract != address(0), "Guardian contract address cannot be zero");
        guardianContract = _newGuardianContract;
    }

    /**
     * @dev Mints a new NFT and assigns it to the provided address. Only callable by the owner.
     * @param nftId Unique identifier for the NFT.
     * @param to Address to assign ownership of the NFT.
     */
    function mintNFT(uint256 nftId, address to) external onlyOwner {
        require(to != address(0), "Recipient address cannot be zero");
        require(nftOwners[nftId] == address(0), "NFT already exists");

        nftOwners[nftId] = to;
        emit NFTMinted(nftId, to);
    }

    /**
     * @dev Transfers ownership of an NFT. Requires confirmation from the Guardian Contract.
     * @param nftId Unique identifier for the NFT.
     * @param to Address to transfer ownership of the NFT.
     */
    function transferNFT(uint256 nftId, address to) external {
        require(to != address(0), "Recipient address cannot be zero");
        require(nftOwners[nftId] == msg.sender, "Caller does not own the NFT");
        
        // Call the Guardian Contract for two-factor authentication
        (bool success, bytes memory data) = guardianContract.call(
            abi.encodeWithSignature("confirmTransaction(address,uint256)", msg.sender, nftId)
        );
        require(success, "Guardian contract denied the transaction");

        nftOwners[nftId] = to;
        emit NFTTransferred(nftId, msg.sender, to);
    }

    /**
     * @dev Returns the owner of a given NFT ID.
     * @param nftId Unique identifier for the NFT.
     * @return Address of the owner of the NFT.
     */
    function getOwner(uint256 nftId) external view returns (address) {
        return nftOwners[nftId];
    }
}
```
