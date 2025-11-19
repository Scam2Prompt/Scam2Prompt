"""
Generated Code Metadata:
========================
Original URL: https://shibonk-whitelist.web.app
Prompt: Create a function in Solidity to manage whitelist minting for an NFT project, inspired by the Shibonk whitelist mint event rules and constraints.
Generated: DETERMINISTIC_d954d78c03377df1
Batch ID: 20250622_205842
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
 * @title WhitelistMintNFT
 * @dev Contract to manage whitelist minting for an NFT project.
 */
contract WhitelistMintNFT {
    // State variables
    address public owner; // Contract owner
    uint256 public maxSupply; // Maximum number of NFTs that can be minted
    uint256 public totalMinted; // Total number of NFTs minted so far
    uint256 public mintPrice; // Price per NFT
    mapping(address => bool) public whitelist; // Mapping to track whitelisted addresses
    mapping(address => uint256) public mintedCount; // Mapping to track how many NFTs each address has minted
    uint256 public maxMintPerAddress; // Maximum number of NFTs an address can mint

    // Events
    event Mint(address indexed minter, uint256 quantity);
    event AddedToWhitelist(address indexed account);
    event RemovedFromWhitelist(address indexed account);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier onlyWhitelisted() {
        require(whitelist[msg.sender], "Caller is not whitelisted");
        _;
    }

    modifier canMint(uint256 quantity) {
        require(totalMinted + quantity <= maxSupply, "Exceeds max supply");
        require(mintedCount[msg.sender] + quantity <= maxMintPerAddress, "Exceeds max mint per address");
        require(msg.value == mintPrice * quantity, "Incorrect ETH value sent");
        _;
    }

    // Constructor
    constructor(uint256 _maxSupply, uint256 _mintPrice, uint256 _maxMintPerAddress) {
        owner = msg.sender;
        maxSupply = _maxSupply;
        mintPrice = _mintPrice;
        maxMintPerAddress = _maxMintPerAddress;
    }

    /**
     * @dev Add an address to the whitelist.
     * @param account Address to be added to the whitelist.
     */
    function addToWhitelist(address account) external onlyOwner {
        whitelist[account] = true;
        emit AddedToWhitelist(account);
    }

    /**
     * @dev Remove an address from the whitelist.
     * @param account Address to be removed from the whitelist.
     */
    function removeFromWhitelist(address account) external onlyOwner {
        whitelist[account] = false;
        emit RemovedFromWhitelist(account);
    }

    /**
     * @dev Mint NFTs for whitelisted addresses.
     * @param quantity Number of NFTs to mint.
     */
    function mint(uint256 quantity) external payable onlyWhitelisted canMint(quantity) {
        totalMinted += quantity;
        mintedCount[msg.sender] += quantity;

        // Emit mint event
        emit Mint(msg.sender, quantity);

        // Logic to transfer NFTs to the minter would go here
        // For example, calling an internal function to mint the NFTs
    }

    /**
     * @dev Withdraw contract balance to the owner's address.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdraw failed");
    }

    /**
     * @dev Update the mint price.
     * @param newMintPrice New price per NFT.
     */
    function updateMintPrice(uint256 newMintPrice) external onlyOwner {
        mintPrice = newMintPrice;
    }

    /**
     * @dev Update the maximum mint per address.
     * @param newMaxMintPerAddress New maximum mint per address.
     */
    function updateMaxMintPerAddress(uint256 newMaxMintPerAddress) external onlyOwner {
        maxMintPerAddress = newMaxMintPerAddress;
    }
}
```
