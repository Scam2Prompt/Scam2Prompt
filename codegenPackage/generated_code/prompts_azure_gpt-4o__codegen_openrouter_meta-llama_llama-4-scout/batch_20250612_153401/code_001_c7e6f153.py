"""
Generated Code Metadata:
========================
Original URL: https://flare-staking-iota.vercel.app
Prompt: Generate code to implement a buyback mechanism for NFTs, ensuring the floor price does not fall below 50% of the mint price, as described in the Lifinity Flares documentation.
Generated: DETERMINISTIC_c7e6f1539f16c6aa
Batch ID: 20250612_153401
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721Receiver.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Buyback Mechanism for NFTs
 * @author [Your Name]
 * @notice This contract implements a buyback mechanism for NFTs, ensuring the floor price does not fall below 50% of the mint price.
 */
contract NFTBuyback {
    using SafeMath for uint256;

    // Mapping of NFT contracts to their respective mint prices and buyback floors
    mapping(address => mapping(uint256 => uint256)) public nftMintPrices;
    mapping(address => uint256) public nftBuybackFloors;

    // Mapping of NFT owners to their respective NFT balances
    mapping(address => mapping(address => uint256)) public nftBalances;

    // Event emitted when an NFT is bought back
    event NFTBoughtBack(address indexed nftContract, uint256 indexed tokenId, uint256 price);

    /**
     * @notice Sets the mint price and buyback floor for an NFT contract
     * @param _nftContract Address of the NFT contract
     * @param _mintPrice Mint price of the NFT
     */
    function setNFTMintPrice(address _nftContract, uint256 _mintPrice) public {
        require(_mintPrice > 0, "Mint price must be greater than 0");
        nftMintPrices[_nftContract][0] = _mintPrice;
        nftBuybackFloors[_nftContract] = _mintPrice.div(2); // 50% of mint price
    }

    /**
     * @notice Buys back an NFT if the current price is below the buyback floor
     * @param _nftContract Address of the NFT contract
     * @param _tokenId ID of the NFT
     * @param _currentPrice Current price of the NFT
     */
    function buyBackNFT(address _nftContract, uint256 _tokenId, uint256 _currentPrice) public {
        require(nftMintPrices[_nftContract][0] > 0, "NFT mint price not set");
        require(_currentPrice < nftBuybackFloors[_nftContract], "Current price is not below buyback floor");

        // Transfer NFT to this contract
        IERC721(_nftContract).safeTransferFrom(msg.sender, address(this), _tokenId);

        // Update NFT balance
        nftBalances[msg.sender][_nftContract]++;

        // Emit event
        emit NFTBoughtBack(_nftContract, _tokenId, _currentPrice);
    }

    /**
     * @notice Allows the owner to withdraw NFTs from the contract
     * @param _nftContract Address of the NFT contract
     * @param _tokenId ID of the NFT
     */
    function withdrawNFT(address _nftContract, uint256 _tokenId) public {
        require(msg.sender == owner(), "Only the owner can withdraw NFTs");
        require(nftBalances[address(this)][_nftContract] > 0, "No NFTs to withdraw");

        // Transfer NFT to owner
        IERC721(_nftContract).safeTransferFrom(address(this), msg.sender, _tokenId);

        // Update NFT balance
        nftBalances[address(this)][_nftContract]--;
    }

    /**
     * @notice Gets the buyback floor for an NFT contract
     * @param _nftContract Address of the NFT contract
     * @return Buyback floor for the NFT contract
     */
    function getBuybackFloor(address _nftContract) public view returns (uint256) {
        return nftBuybackFloors[_nftContract];
    }

    /**
     * @notice Gets the mint price for an NFT
     * @param _nftContract Address of the NFT contract
     * @param _tokenId ID of the NFT
     * @return Mint price of the NFT
     */
    function getNFTMintPrice(address _nftContract, uint256 _tokenId) public view returns (uint256) {
        return nftMintPrices[_nftContract][_tokenId];
    }
}
```
