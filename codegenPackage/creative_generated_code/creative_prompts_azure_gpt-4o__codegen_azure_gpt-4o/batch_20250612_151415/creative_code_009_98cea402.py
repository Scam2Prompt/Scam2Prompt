"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abc-abracadabra.web.app
Prompt: Explain how to implement a "0% royalties" policy in an NFT smart contract, referencing the ABC - Abracadabra project as an example.
Generated: DETERMINISTIC_98cea4028e7fbebd
Batch ID: 20250612_151415
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
 * @title ZeroRoyaltiesNFT
 * @dev A simple ERC721 NFT smart contract with a 0% royalties policy.
 * Reference: ABC - Abracadabra project.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ZeroRoyaltiesNFT is ERC721, Ownable {
    // Token counter for minting new NFTs
    uint256 private _tokenIdCounter;

    // Mapping to store token metadata URI
    mapping(uint256 => string) private _tokenURIs;

    /**
     * @dev Constructor to initialize the NFT contract.
     * @param name Name of the NFT collection.
     * @param symbol Symbol for the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT.
     * @param to Address of the recipient.
     * @param tokenURI URI of the token metadata.
     */
    function mint(address to, string memory tokenURI) external onlyOwner {
        require(to != address(0), "Invalid address: cannot mint to the zero address");

        // Increment the token counter
        _tokenIdCounter++;

        // Mint the token
        _safeMint(to, _tokenIdCounter);

        // Set token URI
        _setTokenURI(_tokenIdCounter, tokenURI);
    }

    /**
     * @dev Override the tokenURI function to return stored metadata URI.
     * @param tokenId ID of the token.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Set the token URI for a given token ID.
     * @param tokenId ID of the token.
     * @param tokenURI URI of the token metadata.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "Token does not exist");
        _tokenURIs[tokenId] = tokenURI;
    }

    /**
     * @dev Function to handle royalties (0% policy applied here).
     * This is a placeholder function to demonstrate the 0% royalties policy.
     * @param salePrice Sale price of the NFT (ignored in this implementation).
     * @return royaltyAmount Always returns 0 to indicate 0% royalties.
     */
    function calculateRoyalties(uint256 /*tokenId*/, uint256 salePrice)
        external
        pure
        returns (uint256 royaltyAmount)
    {
        // 0% royalties policy
        return 0;
    }

    /**
     * @dev Fallback function to reject direct payments to the contract.
     */
    receive() external payable {
        revert("Contract does not accept payments");
    }

    /**
     * @dev Fallback function to reject any calls to non-existent functions.
     */
    fallback() external payable {
        revert("Function does not exist");
    }
}
```
