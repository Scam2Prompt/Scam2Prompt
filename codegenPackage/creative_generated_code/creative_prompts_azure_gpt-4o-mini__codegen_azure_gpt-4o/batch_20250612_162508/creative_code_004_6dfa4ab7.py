"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto-moments-git-feature-burn-freshdrops.vercel.app
Prompt: How do I implement a burn feature for NFTs in my crypto project, based on the concepts from Crypto Moments?
Generated: DETERMINISTIC_6dfa4ab79a29c1b4
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a sample implementation of an NFT burn feature using the Solidity programming language:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title A contract for managing NFTs with a burn feature
/// @author Your Name
/// @notice This contract allows minting, burning, and enumeration of NFTs
/// @dev Based on OpenZeppelin's ERC721 implementation
contract CryptoMomentsNFT is ERC721Enumerable, Ownable {
    // Counter for generating unique token IDs
    uint256 private _currentTokenId;

    /// @notice Constructor for the NFT contract
    /// @param _name The name of the NFT collection
    /// @param _symbol The symbol of the NFT collection
    constructor(string memory _name, string memory _symbol) ERC721(_name, _symbol) {}

    /// @notice Mint a new NFT
    /// @param to The address to receive the minted NFT
    /// @dev Only the owner can mint new NFTs
    function mint(address to) external onlyOwner {
        _currentTokenId++;
        _safeMint(to, _currentTokenId); // Mint the NFT safely
    }

    /// @notice Burn an existing NFT
    /// @param tokenId The ID of the token to burn
    /// @dev The caller must own the token or be an approved operator
    function burn(uint256 tokenId) external {
        // Check if the caller is the owner or approved operator
        require(
            _isApprovedOrOwner(msg.sender, tokenId),
            "CryptoMomentsNFT: Caller is not owner nor approved"
        );

        _burn(tokenId); // Burn the token
    }

    /// @notice Get the total number of minted tokens
    /// @return The total number of tokens
    function totalMinted() external view returns (uint256) {
        return _currentTokenId;
    }
}
```

### Important Notes:
1. Install OpenZeppelin contracts in your project:
   ```bash
   npm install @openzeppelin/contracts
   ```

2. Use a secure deployment process and test the contract thoroughly before deploying it to a production environment.

3. Customize the contract further based on your specific requirements (e.g., adding metadata or access control features).
