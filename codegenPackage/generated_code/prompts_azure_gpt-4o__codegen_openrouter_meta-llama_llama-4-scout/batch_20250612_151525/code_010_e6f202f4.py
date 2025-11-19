"""
Generated Code Metadata:
========================
Original URL: https://gmnt.org
Prompt: Create a Solidity smart contract for a GMNTCoin-based NFT marketplace that supports transactions on the Binance Smart Chain with reduced fees compared to Ethereum.
Generated: DETERMINISTIC_e6f202f43aee2b08
Batch ID: 20250612_151525
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title GMNTCoin-based NFT Marketplace
 * @author [Your Name]
 * @notice A decentralized marketplace for buying, selling, and trading NFTs on the Binance Smart Chain.
 */
contract GMNTMarketplace is SafeERC721, Ownable {
    // Mapping of NFT owners to their respective balances
    mapping (address => uint256) public balances;

    // Mapping of NFT owners to their respective NFTs
    mapping (address => mapping (uint256 => uint256)) public nftOwners;

    // Mapping of NFT IDs to their respective metadata
    mapping (uint256 => string) public nftMetadata;

    // Event emitted when an NFT is created
    event NewNFT(address indexed owner, uint256 nftId, string metadata);

    // Event emitted when an NFT is transferred
    event TransferNFT(address indexed from, address indexed to, uint256 nftId);

    // Event emitted when an NFT is sold
    event SaleNFT(address indexed seller, address indexed buyer, uint256 nftId, uint256 price);

    // GMNTCoin address
    address public gmntCoinAddress;

    // Fee for transactions (in GMNTCoin)
    uint256 public transactionFee;

    /**
     * @dev Constructor
     * @param _gmntCoinAddress Address of the GMNTCoin contract
     * @param _transactionFee Transaction fee (in GMNTCoin)
     */
    constructor(address _gmntCoinAddress, uint256 _transactionFee) public {
        gmntCoinAddress = _gmntCoinAddress;
        transactionFee = _transactionFee;
    }

    /**
     * @dev Creates a new NFT
     * @param _metadata Metadata for the NFT
     * @return The ID of the newly created NFT
     */
    function createNFT(string memory _metadata) public returns (uint256) {
        // Generate a unique NFT ID
        uint256 nftId = uint256(keccak256(abi.encodePacked(msg.sender, block.timestamp)));

        // Set the NFT owner to the creator
        nftOwners[msg.sender][nftId] = nftId;

        // Set the NFT metadata
        nftMetadata[nftId] = _metadata;

        // Emit the NewNFT event
        emit NewNFT(msg.sender, nftId, _metadata);

        return nftId;
    }

    /**
     * @dev Transfers an NFT
     * @param _to Address of the recipient
     * @param _nftId ID of the NFT to transfer
     */
    function transferNFT(address _to, uint256 _nftId) public {
        // Check if the sender is the owner of the NFT
        require(nftOwners[msg.sender][_nftId] == _nftId, "Only the owner can transfer the NFT");

        // Transfer the NFT
        nftOwners[_to][_nftId] = _nftId;
        delete nftOwners[msg.sender][_nftId];

        // Emit the TransferNFT event
        emit TransferNFT(msg.sender, _to, _nftId);
    }

    /**
     * @dev Sells an NFT
     * @param _buyer Address of the buyer
     * @param _nftId ID of the NFT to sell
     * @param _price Price of the NFT (in GMNTCoin)
     */
    function sellNFT(address _buyer, uint256 _nftId, uint256 _price) public {
        // Check if the sender is the owner of the NFT
        require(nftOwners[msg.sender][_nftId] == _nftId, "Only the owner can sell the NFT");

        // Check if the buyer has sufficient GMNTCoin balance
        require(IERC20(gmntCoinAddress).balanceOf(_buyer) >= _price, "Buyer has insufficient GMNTCoin balance");

        // Transfer the NFT
        nftOwners[_buyer][_nftId] = _nftId;
        delete nftOwners[msg.sender][_nftId];

        // Transfer the GMNTCoin
        IERC20(gmntCoinAddress).transferFrom(_buyer, msg.sender, _price);

        // Pay the transaction fee
        IERC20(gmntCoinAddress).transferFrom(_buyer, address(this), transactionFee);

        // Emit the SaleNFT event
        emit SaleNFT(msg.sender, _buyer, _nftId, _price);
    }

    /**
     * @dev Withdraws the transaction fees
     */
    function withdrawFees() public onlyOwner {
        IERC20(gmntCoinAddress).transfer(msg.sender, IERC20(gmntCoinAddress).balanceOf(address(this)));
    }
}

interface IERC20 {
    function balanceOf(address owner) external view returns (uint256);
    function transfer(address to, uint256 value) external returns (bool);
    function transferFrom(address from, address to, uint256 value) external returns (bool);
}
```
