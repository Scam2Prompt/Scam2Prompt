"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nfarcade.vercel.app
Prompt: Write a code snippet for a smart contract that manages the minting of Arcade Passes for a gaming platform.
Generated: DETERMINISTIC_f59af16c89604893
Batch ID: 20250612_135804
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
 * @title ArcadePass
 * @dev A smart contract to manage minting of Arcade Passes for a gaming platform.
 */
contract ArcadePass {
    // Event emitted when a new Arcade Pass is minted
    event ArcadePassMinted(address indexed to, uint256 indexed tokenId);

    // Owner of the contract
    address public owner;

    // Total number of Arcade Passes minted
    uint256 public totalMinted;

    // Mapping to store which address owns which token
    mapping(uint256 => address) public tokenOwners;

    // Mapping to store user balances
    mapping(address => uint256) public balances;

    // Maximum supply of Arcade Passes
    uint256 public constant MAX_SUPPLY = 10000;

    // Token price (in wei)
    uint256 public constant PASS_PRICE = 0.05 ether;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to mint a new Arcade Pass.
     * @param to Address to receive the Arcade Pass.
     */
    function mintArcadePass(address to) external payable {
        // Check if the maximum supply has been reached
        require(totalMinted < MAX_SUPPLY, "Max supply reached");

        // Check if the correct amount of ether was sent
        require(msg.value == PASS_PRICE, "Incorrect payment amount");

        // Increment the total minted count
        totalMinted++;

        // Assign the new token ID to the recipient
        tokenOwners[totalMinted] = to;

        // Update the balance of the recipient
        balances[to]++;

        // Emit the minting event
        emit ArcadePassMinted(to, totalMinted);
    }

    /**
     * @dev Function to withdraw ether from the contract.
     * Can only be called by the owner.
     */
    function withdraw() external onlyOwner {
        // Check if there are funds to withdraw
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the balance to the owner
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Function to get the owner of a specific token ID.
     * @param tokenId Token ID to query.
     * @return The address of the token owner.
     */
    function getTokenOwner(uint256 tokenId) external view returns (address) {
        return tokenOwners[tokenId];
    }

    /**
     * @dev Fallback function to prevent accidental ether transfers.
     */
    fallback() external payable {
        revert("Direct payments are not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ether transfers.
     */
    receive() external payable {
        revert("Direct payments are not allowed");
    }
}
```
