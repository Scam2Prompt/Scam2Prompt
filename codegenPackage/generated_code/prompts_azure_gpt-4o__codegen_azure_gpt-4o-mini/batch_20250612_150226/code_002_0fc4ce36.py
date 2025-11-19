"""
Generated Code Metadata:
========================
Original URL: https://multichainclaimairdrop.pages.dev
Prompt: How can I use Chainlink's VRF to generate verifiably random numbers for an NFT minting process? Provide a code example.
Generated: DETERMINISTIC_0fc4ce366bba0c02
Batch ID: 20250612_150226
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

// Importing the Chainlink VRF consumer interface
import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";

// NFT contract that uses Chainlink VRF for random number generation
contract RandomNFT is VRFConsumerBase {
    // State variables
    bytes32 internal keyHash; // Key hash for the VRF
    uint256 internal fee; // Fee for requesting randomness
    uint256 public randomResult; // Result of the random number generation

    // Event to emit when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 tokenId);

    // Mapping to track minted NFTs
    mapping(uint256 => address) public nftOwners;

    // Constructor to set up the VRF consumer
    constructor(address _vrfCoordinator, address _linkToken, bytes32 _keyHash, uint256 _fee) 
        VRFConsumerBase(_vrfCoordinator, _linkToken) {
        keyHash = _keyHash;
        fee = _fee; // Set the fee for randomness
    }

    // Function to mint a new NFT
    function mintNFT() external returns (bytes32 requestId) {
        // Check if the contract has enough LINK to pay for the randomness
        require(LINK.balanceOf(address(this)) >= fee, "Not enough LINK to pay fee");

        // Request randomness from Chainlink VRF
        return requestRandomness(keyHash, fee);
    }

    // Callback function used by VRF Coordinator to return the random number
    function fulfillRandomness(bytes32 requestId, uint256 randomness) internal override {
        randomResult = randomness; // Store the random number

        // Generate a new token ID based on the random number
        uint256 tokenId = randomness % 10000; // Example: limit token IDs to 0-9999

        // Mint the NFT (this is a placeholder for actual minting logic)
        nftOwners[tokenId] = msg.sender; // Assign the NFT to the caller

        // Emit an event for the minted NFT
        emit NFTMinted(msg.sender, tokenId);
    }

    // Function to withdraw LINK tokens from the contract
    function withdrawLINK() external {
        uint256 balance = LINK.balanceOf(address(this));
        require(balance > 0, "No LINK to withdraw");
        LINK.transfer(msg.sender, balance); // Transfer LINK to the caller
    }
}
```
