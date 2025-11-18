"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xter-91z.pages.dev
Prompt: Create a smart contract in Solidity for Kokodi's NFT minting process, ensuring it handles whitelist eligibility and tracks the total minted NFTs.
Generated: DETERMINISTIC_a643c9449be29657
Batch ID: 20250612_151117
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
 * @title KokodiNFT
 * @dev A smart contract for minting NFTs with whitelist eligibility and tracking the total minted NFTs.
 */
contract KokodiNFT {
    // Events
    event NFTMinted(address indexed to, uint256 tokenId);

    // State variables
    uint256 public totalMinted; // Tracks the total number of minted NFTs
    uint256 public maxSupply; // Maximum number of NFTs allowed to mint
    address public owner; // Owner of the contract
    mapping(address => bool) public whitelist; // Whitelist mapping: true if eligible for minting
    mapping(uint256 => address) public tokenOwners; // Token ownership mapping

    // Token counter for generating token IDs
    uint256 private _currentTokenId;

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    /**
     * @dev Modifier to check whitelist eligibility.
     */
    modifier onlyWhitelisted() {
        require(whitelist[msg.sender], "You are not whitelisted to mint NFTs");
        _;
    }

    /**
     * @dev Modifier to ensure minting does not exceed max supply.
     */
    modifier canMint() {
        require(totalMinted < maxSupply, "Max supply reached, no more NFTs can be minted");
        _;
    }

    /**
     * @dev Contract constructor.
     * @param _maxSupply The maximum number of NFTs that can be minted.
     */
    constructor(uint256 _maxSupply) {
        owner = msg.sender;
        maxSupply = _maxSupply;
    }

    /**
     * @dev Adds an address to the whitelist.
     * @param _address The address to be whitelisted.
     */
    function addToWhitelist(address _address) external onlyOwner {
        whitelist[_address] = true;
    }

    /**
     * @dev Removes an address from the whitelist.
     * @param _address The address to be removed from the whitelist.
     */
    function removeFromWhitelist(address _address) external onlyOwner {
        whitelist[_address] = false;
    }

    /**
     * @dev Mints a new NFT to the caller's address if eligible and supply permits.
     */
    function mintNFT() external onlyWhitelisted canMint {
        _currentTokenId++;
        totalMinted++;
        tokenOwners[_currentTokenId] = msg.sender;

        emit NFTMinted(msg.sender, _currentTokenId); // Emit the minting event
    }

    /**
     * @dev Retrieves the owner of a specific token ID.
     * @param tokenId The ID of the token.
     * @return The address of the token owner.
     */
    function getTokenOwner(uint256 tokenId) external view returns (address) {
        return tokenOwners[tokenId];
    }

    /**
     * @dev Transfers ownership of the contract to a new address.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner must be a valid address");
        owner = newOwner;
    }
}
```
