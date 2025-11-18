"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan-eth.github.io
Prompt: Create a Solidity example of a smart contract that includes metadata for NFTs and demonstrate how to verify and track the contract on Etherscan.
Generated: DETERMINISTIC_260b6bec6e5b40dc
Batch ID: 20250612_153424
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

// Importing OpenZeppelin's ERC721 and Ownable contracts
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MyNFT
 * @dev This contract implements a simple NFT minting system with metadata.
 */
contract MyNFT is ERC721, Ownable {
    // Mapping from token ID to token metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Counter for the next token ID
    uint256 private _nextTokenId;

    // Event emitted when a new NFT is minted
    event Minted(uint256 indexed tokenId, string tokenURI);

    /**
     * @dev Constructor that sets the name and symbol for the NFT collection.
     */
    constructor() ERC721("MyNFT", "MNFT") {
        _nextTokenId = 1; // Start token IDs from 1
    }

    /**
     * @dev Function to mint a new NFT.
     * @param to The address that will receive the minted NFT.
     * @param tokenURI The metadata URI for the minted NFT.
     */
    function mint(address to, string memory tokenURI) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        uint256 tokenId = _nextTokenId; // Get the current token ID
        _nextTokenId++; // Increment for the next minting

        _mint(to, tokenId); // Mint the NFT
        _setTokenURI(tokenId, tokenURI); // Set the metadata URI

        emit Minted(tokenId, tokenURI); // Emit the Minted event
    }

    /**
     * @dev Internal function to set the token URI.
     * @param tokenId The ID of the token to set the URI for.
     * @param tokenURI The URI to be set for the token.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        _tokenURIs[tokenId] = tokenURI; // Store the token URI
    }

    /**
     * @dev Function to retrieve the token URI associated with a token ID.
     * @param tokenId The ID of the token.
     * @return The token URI.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist"); // Check if token exists
        return _tokenURIs[tokenId]; // Return the stored token URI
    }
}
```

### Deployment and Verification on Etherscan

To deploy and verify this contract on Etherscan, follow these steps:

1. **Compile the Contract**: Use a Solidity compiler (like Remix IDE or Truffle) to compile the contract.

2. **Deploy the Contract**: Deploy the contract to the Ethereum network using a wallet or deployment script.

3. **Get Deployment Transaction Hash**: After deployment, get the transaction hash from your wallet.

4. **Verify on Etherscan**:
   - Go to Etherscan and navigate to the "Contract" tab.
   - Click "Verify Contract".
   - Enter the contract address and the compiler version used.
   - Paste the Solidity code into the verification form.
   - Provide constructor parameters if required (none in this case).
   - Submit the verification request.

5. **Track the Contract**: Once verified, you can track NFT minting, ownership, and metadata directly on Etherscan.
