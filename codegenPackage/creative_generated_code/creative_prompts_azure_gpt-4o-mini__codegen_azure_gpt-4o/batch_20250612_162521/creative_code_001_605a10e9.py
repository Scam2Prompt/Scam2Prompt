"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappass.neocities.org
Prompt: How can I implement a fair distribution mechanism for a limited NFT supply like the Dapp Pass?
Generated: DETERMINISTIC_605a10e985d69ca4
Batch ID: 20250612_162521
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
 * @title NFTFairDistribution
 * @dev This contract handles fair distribution of a limited NFT supply.
 * Users can participate in a randomized minting process to ensure fairness.
 */
contract NFTFairDistribution {
    // State variables
    uint256 public constant MAX_SUPPLY = 1000; // Total NFT supply
    uint256 public totalMinted;               // Counter for minted NFTs
    uint256 public mintPrice = 0.05 ether;    // Price per NFT
    address public owner;                     // Contract owner

    mapping(uint256 => bool) public mintedTokens; // Tracks minted token IDs

    // Events
    event Mint(address indexed recipient, uint256 tokenId);
    event Withdraw(address indexed owner, uint256 amount);

    // Constructor to set owner
    constructor() {
        owner = msg.sender;
    }

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner.");
        _;
    }

    // Function to mint an NFT
    function mint() external payable {
        require(totalMinted < MAX_SUPPLY, "All NFTs have been minted.");
        require(msg.value == mintPrice, "Incorrect payment amount.");

        // Generate a random token ID
        uint256 tokenId = _generateRandomTokenId();
        require(!mintedTokens[tokenId], "Token already minted."); // Ensure token ID is unique

        // Mark token ID as minted
        mintedTokens[tokenId] = true;
        totalMinted++;

        emit Mint(msg.sender, tokenId);
    }

    // Owner can withdraw funds from the contract
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw.");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed.");

        emit Withdraw(owner, balance);
    }

    // Function to generate a random token ID
    function _generateRandomTokenId() private view returns (uint256) {
        // Generate pseudo-random number based on block properties
        uint256 random = uint256(
            keccak256(
                abi.encodePacked(
                    block.timestamp,
                    block.difficulty,
                    msg.sender,
                    totalMinted
                )
            )
        );

        // Map random number to a valid token ID range
        uint256 tokenId = (random % MAX_SUPPLY) + 1;
        return tokenId;
    }

    // Fallback function to prevent accidental ETH transfers
    fallback() external payable {
        revert("ETH transfers not allowed.");
    }

    // Receive function to prevent accidental ETH transfers
    receive() external payable {
        revert("ETH transfers not allowed.");
    }
}
```
