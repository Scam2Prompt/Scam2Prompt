"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Write a smart contract using Chainlink's VRF to generate verifiably random numbers for an NFT minting application.
Generated: DETERMINISTIC_bcc3c34002638fd6
Batch ID: 20250612_152249
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

// Importing necessary interfaces and libraries from OpenZeppelin and Chainlink
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";

// Smart contract for NFT minting with Chainlink VRF for randomness
contract RandomNFT is ERC721, VRFConsumerBase, Ownable {
    // Variables for minting and VRF
    uint256 public tokenCounter;
    bytes32 internal keyHash;
    uint256 internal fee;
    mapping(uint256 => uint256) public randomWords; // Mapping to store random words

    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 tokenId, uint256 randomNumber);

    // Constructor to initialize the ERC721 token and VRF
    constructor(address _vrfCoordinator, address _link, bytes32 _keyHash)
        VRFConsumerBase(_vrfCoordinator, _link)
        ERC721("RandomNFT", "RNFT")
    {
        tokenCounter = 0;
        keyHash = _keyHash;
        fee = 0.1 * 10**18; // Set the fee for requesting randomness (in LINK)
    }

    // Function to mint a new NFT and request a random number
    function mintNFT() public onlyOwner returns (uint256 requestId) {
        require(LINK.balanceOf(address(this)) >= fee, "Not enough LINK to pay fee");
        
        // Requesting a random number
        requestId = requestRandomness(keyHash, fee);
    }

    // Callback function for Chainlink VRF to receive the random number
    function fulfillRandomness(bytes32 requestId, uint256 randomness) internal override {
        uint256 tokenId = tokenCounter;
        randomWords[tokenId] = randomness; // Store the generated random number
        _safeMint(msg.sender, tokenId); // Mint the NFT
        emit NFTMinted(tokenId, randomness); // Emit event for minted NFT
        tokenCounter++; // Increment the token ID counter
    }

    // Function to withdraw LINK tokens from the contract
    function withdrawLINK() public onlyOwner {
        uint256 balance = LINK.balanceOf(address(this));
        require(balance > 0, "No LINK to withdraw");
        LINK.transfer(msg.sender, balance);
    }

    // Function to set the fee for randomness requests (onlyOwner)
    function setFee(uint256 _fee) public onlyOwner {
        fee = _fee;
    }

    // Function to update the keyHash (onlyOwner)
    function setKeyHash(bytes32 _keyHash) public onlyOwner {
        keyHash = _keyHash;
    }

    // Function to check contract's LINK balance
    function getLINKBalance() public view returns (uint256) {
        return LINK.balanceOf(address(this));
    }
}
```
