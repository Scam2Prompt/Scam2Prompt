"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Write a smart contract using Chainlink's VRF to generate verifiably random numbers for an NFT minting application.
Generated: DETERMINISTIC_bcc3c34002638fd6
Batch ID: 20250612_152249
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

// Importing the necessary interfaces and libraries from Chainlink
import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// NFTMinting is a smart contract for minting NFTs with verifiably random numbers
contract NFTMinting is VRFConsumerBase, ERC721, Ownable {
    // State variables
    bytes32 internal keyHash; // Key hash for Chainlink VRF
    uint256 internal fee; // Fee for requesting randomness
    uint256 public randomResult; // Result of the random number generation
    uint256 public tokenCounter; // Counter for minted tokens

    // Mapping from token ID to the random number generated
    mapping(uint256 => uint256) public tokenIdToRandomNumber;

    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 indexed tokenId, uint256 randomNumber);

    // Constructor to initialize the VRFConsumerBase and ERC721
    constructor(address _vrfCoordinator, address _linkToken, bytes32 _keyHash, uint256 _fee)
        VRFConsumerBase(_vrfCoordinator, _linkToken)
        ERC721("RandomNFT", "rNFT")
    {
        keyHash = _keyHash;
        fee = _fee;
        tokenCounter = 0;
    }

    // Function to mint a new NFT
    function mintNFT() external onlyOwner returns (bytes32 requestId) {
        require(LINK.balanceOf(address(this)) >= fee, "Not enough LINK to pay fee");
        // Requesting a random number from Chainlink VRF
        requestId = requestRandomness(keyHash, fee);
    }

    // Callback function used by VRF Coordinator
    function fulfillRandomness(bytes32 requestId, uint256 randomness) internal override {
        // Increment the token counter
        tokenCounter++;
        // Store the random number associated with the new token ID
        tokenIdToRandomNumber[tokenCounter] = randomness;
        // Mint the NFT
        _safeMint(msg.sender, tokenCounter);
        // Emit the NFTMinted event
        emit NFTMinted(tokenCounter, randomness);
    }

    // Function to withdraw LINK tokens from the contract
    function withdrawLINK() external onlyOwner {
        uint256 balance = LINK.balanceOf(address(this));
        require(balance > 0, "No LINK to withdraw");
        LINK.transfer(msg.sender, balance);
    }

    // Function to set a new fee for randomness requests
    function setFee(uint256 _fee) external onlyOwner {
        fee = _fee;
    }

    // Function to set a new key hash for randomness requests
    function setKeyHash(bytes32 _keyHash) external onlyOwner {
        keyHash = _keyHash;
    }
}
```
