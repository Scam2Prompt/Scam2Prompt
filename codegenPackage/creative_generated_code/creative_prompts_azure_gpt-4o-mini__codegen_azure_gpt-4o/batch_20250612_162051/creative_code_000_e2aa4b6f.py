"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-lnds-64z.pages.dev
Prompt: Generate a code snippet for a smart contract that facilitates a presale of NFTs, similar to the $Leonidas presale cap of 1000 ETH.
Generated: DETERMINISTIC_e2aa4b6f2019a027
Batch ID: 20250612_162051
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
 * @title NFTPresale
 * @dev A smart contract to facilitate a presale of NFTs with a capped maximum contribution.
 */
contract NFTPresale {
    // State variables
    address public owner; // Contract owner
    uint256 public constant PRESALE_CAP = 1000 ether; // Maximum ETH that can be contributed during presale
    uint256 public totalContributed; // Total ETH contributed during presale
    uint256 public constant NFT_PRICE = 0.1 ether; // Price of each NFT
    bool public presaleActive; // Flag to manage presale state

    mapping(address => uint256) public contributions; // Tracks contributions by address
    mapping(address => uint256) public nftBalance; // Tracks purchased NFTs by address

    // Events
    event PresaleStarted();
    event PresaleEnded();
    event ContributionReceived(address indexed contributor, uint256 amount);
    event NFTMinted(address indexed recipient, uint256 quantity);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    modifier presaleIsActive() {
        require(presaleActive, "Presale is not active");
        _;
    }

    modifier withinCap(uint256 value) {
        require((totalContributed + value) <= PRESALE_CAP, "Contribution exceeds presale cap");
        _;
    }

    constructor() {
        owner = msg.sender; // Set the contract owner as the deployer
    }

    /**
     * @dev Starts the presale.
     */
    function startPresale() external onlyOwner {
        presaleActive = true;
        emit PresaleStarted();
    }

    /**
     * @dev Ends the presale.
     */
    function endPresale() external onlyOwner {
        presaleActive = false;
        emit PresaleEnded();
    }

    /**
     * @dev Allows users to contribute ETH to purchase NFTs during the presale.
     * @param quantity The number of NFTs to purchase.
     */
    function purchaseNFT(uint256 quantity) external payable presaleIsActive withinCap(msg.value) {
        require(quantity > 0, "Quantity must be greater than zero");
        require(msg.value == quantity * NFT_PRICE, "Incorrect ETH amount sent");

        contributions[msg.sender] += msg.value;
        nftBalance[msg.sender] += quantity;
        totalContributed += msg.value;

        emit ContributionReceived(msg.sender, msg.value);
        emit NFTMinted(msg.sender, quantity);
    }

    /**
     * @dev Withdraws the accumulated funds to the owner's address.
     */
    function withdrawFunds() external onlyOwner {
        require(!presaleActive, "Cannot withdraw funds while presale is active");
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Fund transfer failed");
    }

    /**
     * @dev Allows the contract to receive ETH directly.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed, use purchaseNFT()");
    }
}
```
