"""
Generated Code Metadata:
========================
Original URL: https://hmhgbg.pages.dev
Prompt: Write a smart contract for minting Nakamigos-CLOAKS with worldwide gaming and commercial rights.
Generated: DETERMINISTIC_3a8ca0b5ee9ef899
Batch ID: 20250622_204816
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
 * @title NakamigosCloaks
 * @dev A smart contract for minting Nakamigos-CLOAKS NFTs with worldwide gaming and commercial rights.
 */
contract NakamigosCloaks {
    // State variables
    uint256 public totalSupply; // Total number of NFTs minted
    uint256 public maxSupply; // Maximum number of NFTs that can be minted
    uint256 public mintPrice; // Price per NFT in wei
    address public owner; // Contract owner

    mapping(uint256 => address) public tokenOwners; // Mapping from token ID to owner address
    mapping(address => uint256[]) public ownedTokens; // Mapping from owner address to list of owned token IDs

    // Events
    event Mint(address indexed minter, uint256 indexed tokenId);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier validMint(uint256 quantity) {
        require(quantity > 0, "Quantity must be greater than zero");
        require(totalSupply + quantity <= maxSupply, "Exceeds maximum supply");
        require(msg.value == mintPrice * quantity, "Incorrect payment amount");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _maxSupply Maximum number of NFTs that can be minted.
     * @param _mintPrice Price per NFT in wei.
     */
    constructor(uint256 _maxSupply, uint256 _mintPrice) {
        require(_maxSupply > 0, "Max supply must be greater than zero");
        require(_mintPrice > 0, "Mint price must be greater than zero");

        owner = msg.sender;
        maxSupply = _maxSupply;
        mintPrice = _mintPrice;
    }

    /**
     * @dev Mint new NFTs.
     * @param quantity Number of NFTs to mint.
     */
    function mint(uint256 quantity) external payable validMint(quantity) {
        for (uint256 i = 0; i < quantity; i++) {
            uint256 tokenId = totalSupply + 1; // Generate new token ID
            tokenOwners[tokenId] = msg.sender; // Assign ownership
            ownedTokens[msg.sender].push(tokenId); // Update owned tokens list
            totalSupply++; // Increment total supply

            emit Mint(msg.sender, tokenId); // Emit mint event
        }
    }

    /**
     * @dev Transfer ownership of the contract to a new owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Withdraw contract balance to the owner's address.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Get the list of token IDs owned by a specific address.
     * @param ownerAddress Address of the token owner.
     * @return List of token IDs owned by the address.
     */
    function getOwnedTokens(address ownerAddress) external view returns (uint256[] memory) {
        return ownedTokens[ownerAddress];
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct ETH transfers are not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }
}
```
