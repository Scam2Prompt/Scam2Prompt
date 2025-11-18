"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://embersft.costhentic.com
Prompt: Create a Solidity contract snippet that includes a whitelist (WL) mechanism for Ember NFT minting, ensuring only "Lit List" members can participate in the Fire Sale.
Generated: DETERMINISTIC_d5d0ffd66d5a5a00
Batch ID: 20250612_151659
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

/// @title Ember NFT Whitelist Minting Contract
/// @author [Your Name]
/// @notice This contract implements a whitelist mechanism for NFT minting.
/// @dev Only addresses added to the "Lit List" can participate in the Fire Sale.

contract EmberNFT {
    // State variables
    address public owner; // Owner of the contract
    uint256 public mintPrice; // Price for minting an NFT
    mapping(address => bool) public litList; // Mapping to track whitelist members
    uint256 public totalSupply; // Total number of minted NFTs
    uint256 public maxSupply; // Maximum number of NFTs allowed

    // Events
    event AddedToLitList(address indexed account);
    event RemovedFromLitList(address indexed account);
    event Mint(address indexed account, uint256 tokenId);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function.");
        _;
    }

    modifier onlyLitList() {
        require(litList[msg.sender], "You are not on the Lit List.");
        _;
    }

    /// @dev Constructor to initialize the contract.
    /// @param _mintPrice The price to mint an NFT.
    /// @param _maxSupply The maximum supply of NFTs.
    constructor(uint256 _mintPrice, uint256 _maxSupply) {
        owner = msg.sender; // Set the contract deployer as the owner.
        mintPrice = _mintPrice; // Set the mint price.
        maxSupply = _maxSupply; // Set the max supply.
    }

    /// @notice Add an address to the Lit List.
    /// @dev Only callable by the contract owner.
    /// @param _account The address to whitelist.
    function addToLitList(address _account) external onlyOwner {
        require(!litList[_account], "Address is already on the Lit List.");
        litList[_account] = true;
        emit AddedToLitList(_account);
    }

    /// @notice Remove an address from the Lit List.
    /// @dev Only callable by the contract owner.
    /// @param _account The address to remove from the whitelist.
    function removeFromLitList(address _account) external onlyOwner {
        require(litList[_account], "Address is not on the Lit List.");
        litList[_account] = false;
        emit RemovedFromLitList(_account);
    }

    /// @notice Mint an NFT during the Fire Sale.
    /// @dev Only callable by addresses on the Lit List.
    function mint() external payable onlyLitList {
        require(msg.value == mintPrice, "Incorrect ETH sent for minting.");
        require(totalSupply < maxSupply, "Max supply reached.");

        totalSupply++; // Increment the total supply.
        emit Mint(msg.sender, totalSupply); // Emit the mint event.
    }

    /// @notice Withdraw funds from the contract.
    /// @dev Only callable by the contract owner.
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw.");
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed.");
    }
}
```
