"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abc-abracadabra.web.app
Prompt: How can I implement a whitelist feature for NFT minting in a Solidity smart contract, inspired by the ABC - Abracadabra project?
Generated: DETERMINISTIC_84016e7ebf3ee492
Batch ID: 20250612_163945
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
 * @title WhitelistedNFTMinting
 * @dev Implements a whitelist feature for NFT minting. Inspired by the ABC - Abracadabra project.
 */
contract WhitelistedNFTMinting {
    // Owner address
    address public owner;

    // Mapping to store whitelisted addresses
    mapping(address => bool) public whitelistedAddresses;

    // Event emitted when an address is successfully added to the whitelist
    event AddressWhitelisted(address indexed user);

    // Event emitted when an address is removed from the whitelist
    event AddressRemovedFromWhitelist(address indexed user);

    // Event emitted when an NFT is minted
    event NFTMinted(address indexed user, uint256 tokenId);

    // Token counter for minting unique NFT IDs
    uint256 public tokenCounter;

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Modifier to check if an address is whitelisted
    modifier onlyWhitelisted() {
        require(whitelistedAddresses[msg.sender], "Not whitelisted");
        _;
    }

    /**
     * @dev Constructor to set the initial owner and initialize the token counter.
     */
    constructor() {
        owner = msg.sender;
        tokenCounter = 0;
    }

    /**
     * @dev Adds an address to the whitelist.
     * @param _address Address to be added to the whitelist.
     */
    function addToWhitelist(address _address) external onlyOwner {
        require(_address != address(0), "Invalid address");
        require(!whitelistedAddresses[_address], "Already whitelisted");

        whitelistedAddresses[_address] = true;
        emit AddressWhitelisted(_address);
    }

    /**
     * @dev Removes an address from the whitelist.
     * @param _address Address to be removed from the whitelist.
     */
    function removeFromWhitelist(address _address) external onlyOwner {
        require(whitelistedAddresses[_address], "Address not whitelisted");

        whitelistedAddresses[_address] = false;
        emit AddressRemovedFromWhitelist(_address);
    }

    /**
     * @dev Mints an NFT to the sender if they are whitelisted.
     */
    function mintNFT() external onlyWhitelisted {
        tokenCounter += 1;
        emit NFTMinted(msg.sender, tokenCounter);

        // Logic for actual NFT minting can be added here. For now, we just emit an event.
    }

    /**
     * @dev Transfers ownership of the contract to a new owner.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        owner = _newOwner;
    }
}
```
