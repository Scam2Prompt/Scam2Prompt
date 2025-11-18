"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zoracocollectbase0xdba43fe81b31ba402de5b9a2de6.pages.dev
Prompt: Provide Solidity code for a smart contract that mints "Kaira Mythos: Centaur" NFTs and links them to "$ENJOY" token balances.
Generated: DETERMINISTIC_2742b3169000b626
Batch ID: 20250612_151255
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title KairaMythosCentaurNFT
 * @dev A smart contract for minting "Kaira Mythos: Centaur" NFTs that are tied to $ENJOY token balances.
 */
contract KairaMythosCentaurNFT is ERC721URIStorage, Ownable {
    // Reference to the $ENJOY token contract
    IERC20 public enjoyToken;

    // Counter for NFT token IDs
    uint256 private _tokenCounter;

    // Minimum $ENJOY token balance required to mint an NFT
    uint256 public minimumEnjoyBalance;

    // Event emitted when an NFT is minted
    event NFTMinted(address indexed recipient, uint256 tokenId, string tokenURI);

    /**
     * @dev Initializes the contract with the $ENJOY token address and minimum balance requirement.
     * @param _enjoyToken Address of the $ENJOY token contract.
     * @param _minimumEnjoyBalance Minimum $ENJOY token balance required to mint an NFT.
     */
    constructor(address _enjoyToken, uint256 _minimumEnjoyBalance) ERC721("Kaira Mythos: Centaur", "MYTHOS") {
        require(_enjoyToken != address(0), "Invalid $ENJOY token address");
        enjoyToken = IERC20(_enjoyToken);
        minimumEnjoyBalance = _minimumEnjoyBalance;
    }

    /**
     * @dev Allows the owner to set a new minimum $ENJOY token balance requirement.
     * @param newMinimumBalance New minimum balance.
     */
    function setMinimumEnjoyBalance(uint256 newMinimumBalance) external onlyOwner {
        minimumEnjoyBalance = newMinimumBalance;
    }

    /**
     * @dev Mints a new "Kaira Mythos: Centaur" NFT if the sender meets the $ENJOY token balance requirement.
     * @param recipient Address to receive the minted NFT.
     * @param tokenURI URI pointing to the NFT metadata.
     */
    function mintNFT(address recipient, string memory tokenURI) external {
        require(recipient != address(0), "Invalid recipient address");
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        // Check the sender's $ENJOY token balance
        uint256 senderBalance = enjoyToken.balanceOf(msg.sender);
        require(senderBalance >= minimumEnjoyBalance, "Insufficient $ENJOY token balance");

        // Mint the NFT
        uint256 newTokenId = _tokenCounter;
        _mint(recipient, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        // Increment the token counter
        _tokenCounter++;

        // Emit the NFTMinted event
        emit NFTMinted(recipient, newTokenId, tokenURI);
    }

    /**
     * @dev Returns the total number of NFTs minted.
     * @return Total number of NFTs minted.
     */
    function totalMinted() external view returns (uint256) {
        return _tokenCounter;
    }
}
```
