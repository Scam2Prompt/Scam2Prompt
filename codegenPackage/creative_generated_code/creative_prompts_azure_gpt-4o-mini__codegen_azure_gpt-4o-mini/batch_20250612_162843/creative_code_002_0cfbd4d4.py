"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ru.ton-telegram.network
Prompt: Create an example of a smart contract for NFT minting on the TON blockchain, highlighting the unique features of TON's smart contract standard.
Generated: DETERMINISTIC_0cfbd4d4f6a78906
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma ton-solidity >=0.47.0;

// Import necessary libraries and interfaces
import "ton-solidity/contracts/utils/Address.sol";
import "ton-solidity/contracts/utils/Token.sol";

contract NFTMinting {
    using Address for address;

    // Event to notify NFT minted
    event NFTMinted(address indexed owner, uint256 tokenId, string uri);

    // Struct to represent an NFT
    struct NFT {
        uint256 id;
        address owner;
        string uri; // URI for metadata
    }

    // Mapping from token ID to NFT
    mapping(uint256 => NFT) public nfts;

    // Counter for the next token ID
    uint256 public nextTokenId;

    // Modifier to check if the caller is the owner of the NFT
    modifier onlyOwner(uint256 tokenId) {
        require(msg.sender == nfts[tokenId].owner, "You are not the owner of this NFT");
        _;
    }

    // Function to mint a new NFT
    function mint(string memory uri) public {
        // Increment the token ID counter
        uint256 tokenId = nextTokenId++;
        
        // Create the NFT
        nfts[tokenId] = NFT({
            id: tokenId,
            owner: msg.sender,
            uri: uri
        });
        
        // Emit the NFTMinted event
        emit NFTMinted(msg.sender, tokenId, uri);
    }

    // Function to transfer ownership of the NFT
    function transfer(uint256 tokenId, address newOwner) public onlyOwner(tokenId) {
        // Update the owner of the NFT
        nfts[tokenId].owner = newOwner;
    }

    // Function to get NFT details
    function getNFT(uint256 tokenId) public view returns (uint256, address, string memory) {
        // Ensure the NFT exists
        require(nfts[tokenId].owner != address(0), "NFT does not exist");
        
        // Return details of the NFT
        NFT memory nft = nfts[tokenId];
        return (nft.id, nft.owner, nft.uri);
    }
}
```
