"""
Generated Code Metadata:
========================
Original URL: https://nft-shibonk-wl.web.app
Prompt: Create a basic smart contract in Solidity for managing NFT whitelist minting, including free minting for token holders with a limited supply.
Generated: DETERMINISTIC_d123145b8f6845f8
Batch ID: 20250622_210443
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
 * @title NFTWhitelistMint
 * @dev A smart contract for managing NFT whitelist minting with free minting for token holders and limited supply.
 */
contract NFTWhitelistMint {
    // State variables
    uint256 public constant MAX_SUPPLY = 1000; // Maximum number of NFTs that can be minted
    uint256 public totalMinted; // Tracks the total number of NFTs minted
    address public owner; // Contract owner
    mapping(address => bool) public whitelist; // Whitelisted addresses
    mapping(address => uint256) public freeMintAllowance; // Free mint allowance for token holders

    // Events
    event Mint(address indexed minter, uint256 quantity);
    event WhitelistUpdated(address indexed user, bool status);
    event FreeMintAllowanceUpdated(address indexed user, uint256 allowance);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier onlyWhitelisted() {
        require(whitelist[msg.sender], "Caller is not whitelisted");
        _;
    }

    modifier supplyAvailable(uint256 quantity) {
        require(totalMinted + quantity <= MAX_SUPPLY, "Exceeds maximum supply");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    /**
     * @dev Mint NFTs for whitelisted users.
     * @param quantity Number of NFTs to mint.
     */
    function mint(uint256 quantity) external onlyWhitelisted supplyAvailable(quantity) {
        require(quantity > 0, "Quantity must be greater than zero");
        totalMinted += quantity;
        emit Mint(msg.sender, quantity);
    }

    /**
     * @dev Free mint for token holders with allowance.
     * @param quantity Number of NFTs to mint.
     */
    function freeMint(uint256 quantity) external supplyAvailable(quantity) {
        require(quantity > 0, "Quantity must be greater than zero");
        require(freeMintAllowance[msg.sender] >= quantity, "Insufficient free mint allowance");

        freeMintAllowance[msg.sender] -= quantity;
        totalMinted += quantity;
        emit Mint(msg.sender, quantity);
    }

    /**
     * @dev Add or remove an address from the whitelist.
     * @param user Address to update.
     * @param status Whitelist status (true to add, false to remove).
     */
    function updateWhitelist(address user, bool status) external onlyOwner {
        whitelist[user] = status;
        emit WhitelistUpdated(user, status);
    }

    /**
     * @dev Set free mint allowance for a token holder.
     * @param user Address of the token holder.
     * @param allowance Number of NFTs allowed for free minting.
     */
    function setFreeMintAllowance(address user, uint256 allowance) external onlyOwner {
        freeMintAllowance[user] = allowance;
        emit FreeMintAllowanceUpdated(user, allowance);
    }

    /**
     * @dev Withdraw contract balance (if any) to the owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}
}
```
