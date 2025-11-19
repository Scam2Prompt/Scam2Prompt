"""
Generated Code Metadata:
========================
Original URL: https://incubetaipo.pages.dev
Prompt: Design a smart contract for creating and managing equity-based NFTs on the InQubeta platform, ensuring compatibility with the Ethereum network and $QUBE token.
Generated: DETERMINISTIC_de0d20c4ba887fd7
Batch ID: 20250622_211011
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

/**
 * @title EquityNFT
 * @dev Smart contract for creating and managing equity-based NFTs on the InQubeta platform.
 *      Compatible with the Ethereum network and $QUBE token.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract EquityNFT is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIds;

    // Address of the $QUBE token contract
    IERC20 public qubeToken;

    // Mapping to store equity percentage for each NFT
    mapping(uint256 => uint256) public equityPercentage;

    // Event emitted when a new NFT is minted
    event NFTMinted(
        uint256 indexed tokenId,
        address indexed recipient,
        uint256 equityPercentage,
        string tokenURI
    );

    /**
     * @dev Constructor to initialize the contract.
     * @param _qubeToken Address of the $QUBE token contract.
     */
    constructor(address _qubeToken) ERC721("EquityNFT", "EQUITY") {
        require(_qubeToken != address(0), "Invalid $QUBE token address");
        qubeToken = IERC20(_qubeToken);
    }

    /**
     * @dev Mint a new equity-based NFT.
     * @param recipient Address of the NFT recipient.
     * @param equity Equity percentage associated with the NFT.
     * @param tokenURI URI pointing to the NFT metadata.
     */
    function mintNFT(
        address recipient,
        uint256 equity,
        string memory tokenURI
    ) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(equity > 0 && equity <= 100, "Equity must be between 1 and 100");

        // Increment the token ID counter
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();

        // Mint the NFT
        _mint(recipient, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        // Store the equity percentage
        equityPercentage[newTokenId] = equity;

        // Emit the NFTMinted event
        emit NFTMinted(newTokenId, recipient, equity, tokenURI);
    }

    /**
     * @dev Withdraw $QUBE tokens from the contract.
     * @param amount Amount of $QUBE tokens to withdraw.
     */
    function withdrawQubeTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(
            qubeToken.balanceOf(address(this)) >= amount,
            "Insufficient $QUBE token balance"
        );

        // Transfer $QUBE tokens to the owner
        qubeToken.transfer(owner(), amount);
    }

    /**
     * @dev Get the equity percentage of a specific NFT.
     * @param tokenId ID of the NFT.
     * @return Equity percentage associated with the NFT.
     */
    function getEquityPercentage(uint256 tokenId)
        external
        view
        returns (uint256)
    {
        require(_exists(tokenId), "NFT does not exist");
        return equityPercentage[tokenId];
    }
}
```
