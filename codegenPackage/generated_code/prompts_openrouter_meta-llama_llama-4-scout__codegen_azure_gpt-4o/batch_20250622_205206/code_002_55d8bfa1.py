"""
Generated Code Metadata:
========================
Original URL: https://mint-safe-scrowl.pages.dev
Prompt: Generate a smart contract code for an NFT minting process with multiple stages, including whitelist, FCFS (first-come-first-served), and public sale phases, on the Ethereum network.
Generated: DETERMINISTIC_55d8bfa1f9ec6dd8
Batch ID: 20250622_205206
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
 * @title NFTMintingContract
 * @dev A smart contract for minting NFTs with multiple sale phases: Whitelist, FCFS, and Public Sale.
 */
contract NFTMintingContract {
    // State variables
    uint256 public constant MAX_SUPPLY = 10000; // Maximum number of NFTs
    uint256 public constant WHITELIST_PRICE = 0.05 ether; // Price for whitelist sale
    uint256 public constant FCFS_PRICE = 0.07 ether; // Price for FCFS sale
    uint256 public constant PUBLIC_PRICE = 0.1 ether; // Price for public sale
    uint256 public totalMinted; // Total number of NFTs minted

    enum SalePhase { Closed, Whitelist, FCFS, Public }
    SalePhase public currentPhase; // Current sale phase

    mapping(address => bool) public whitelist; // Whitelisted addresses
    mapping(address => uint256) public mintedPerAddress; // Track mints per address

    address public owner; // Contract owner

    // Events
    event Mint(address indexed minter, uint256 quantity);
    event PhaseChanged(SalePhase newPhase);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier isValidPhase(SalePhase phase) {
        require(currentPhase == phase, "Invalid phase for this operation");
        _;
    }

    modifier canMint(uint256 quantity) {
        require(totalMinted + quantity <= MAX_SUPPLY, "Exceeds maximum supply");
        _;
    }

    modifier hasPaid(uint256 price, uint256 quantity) {
        require(msg.value == price * quantity, "Incorrect payment amount");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender;
        currentPhase = SalePhase.Closed; // Start with the sale closed
    }

    // Owner functions
    function setPhase(SalePhase phase) external onlyOwner {
        currentPhase = phase;
        emit PhaseChanged(phase);
    }

    function addToWhitelist(address[] calldata addresses) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            whitelist[addresses[i]] = true;
        }
    }

    function removeFromWhitelist(address[] calldata addresses) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            whitelist[addresses[i]] = false;
        }
    }

    // Minting functions
    function mintWhitelist(uint256 quantity)
        external
        payable
        isValidPhase(SalePhase.Whitelist)
        canMint(quantity)
        hasPaid(WHITELIST_PRICE, quantity)
    {
        require(whitelist[msg.sender], "Not whitelisted");
        _mint(quantity);
    }

    function mintFCFS(uint256 quantity)
        external
        payable
        isValidPhase(SalePhase.FCFS)
        canMint(quantity)
        hasPaid(FCFS_PRICE, quantity)
    {
        _mint(quantity);
    }

    function mintPublic(uint256 quantity)
        external
        payable
        isValidPhase(SalePhase.Public)
        canMint(quantity)
        hasPaid(PUBLIC_PRICE, quantity)
    {
        _mint(quantity);
    }

    // Internal minting logic
    function _mint(uint256 quantity) internal {
        mintedPerAddress[msg.sender] += quantity;
        totalMinted += quantity;
        emit Mint(msg.sender, quantity);
    }

    // Withdraw funds
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdraw failed");
    }

    // Fallback function to prevent accidental ETH transfers
    fallback() external payable {
        revert("Direct ETH transfers not allowed");
    }

    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
