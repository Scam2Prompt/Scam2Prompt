"""
Generated Code Metadata:
========================
Original URL: https://telos-4ji.pages.dev
Prompt: Develop a smart contract on Telos EVM for a simple NFT marketplace, utilizing LayerZero for omnichain interoperability.
Generated: DETERMINISTIC_8f319f86a4cc824a
Batch ID: 20250622_205627
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@layerzerolabs/solidity-examples/contracts/token/onft/ONFT721.sol";

contract NFTMarketplace is ONFT721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    struct Listing {
        uint256 price;
        address seller;
        bool isListed;
    }

    mapping(uint256 => Listing) public listings;
    uint256 public listingFee = 0.01 ether;

    event NFTListed(uint256 tokenId, uint256 price, address seller);
    event NFTSold(uint256 tokenId, uint256 price, address seller, address buyer);
    event NFTUnlisted(uint256 tokenId, address owner);

    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _minGasToTransfer,
        address _lzEndpoint
    ) ONFT721(_name, _symbol, _minGasToTransfer, _lzEndpoint) {}

    function mint(string memory tokenURI) public payable returns (uint256) {
        require(msg.value >= listingFee, "Insufficient listing fee");
        
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();
        _mint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        return newTokenId;
    }

    function listNFT(uint256 tokenId, uint256 price) public {
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        require(price > 0, "Price must be greater than 0");

        listings[tokenId] = Listing({
            price: price,
            seller: msg.sender,
            isListed: true
        });

        emit NFTListed(tokenId, price, msg.sender);
    }

    function buyNFT(uint256 tokenId) public payable {
        Listing memory listing = listings[tokenId];
        require(listing.isListed, "NFT not listed for sale");
        require(msg.value >= listing.price, "Insufficient funds");

        address seller = listing.seller;
        _transfer(seller, msg.sender, tokenId);

        (bool success, ) = seller.call{value: msg.value}("");
        require(success, "Transfer failed");

        delete listings[tokenId];
        emit NFTSold(tokenId, listing.price, seller, msg.sender);
    }

    function unlistNFT(uint256 tokenId) public {
        require(listings[tokenId].seller == msg.sender, "Not the seller");
        require(listings[tokenId].isListed, "NFT not listed");

        delete listings[tokenId];
        emit NFTUnlisted(tokenId, msg.sender);
    }

    function setListingFee(uint256 _fee) public onlyOwner {
        listingFee = _fee;
    }

    function withdrawFees() public onlyOwner {
        (bool success, ) = owner().call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }

    function _setTokenURI(uint256 tokenId, string memory _tokenURI) internal virtual {
        require(_exists(tokenId), "ERC721URIStorage: URI set of nonexistent token");
        _tokenURIs[tokenId] = _tokenURI;
    }

    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "ERC721URIStorage: URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }

    // LayerZero functions
    function estimateSendFee(
        uint16 _dstChainId,
        bytes memory _toAddress,
        uint256 _tokenId,
        bool _useZro,
        bytes memory _adapterParams
    ) public view returns (uint256 nativeFee, uint256 zroFee) {
        return lzEndpoint.estimateSendFee(_dstChainId, _toAddress, _tokenId, _useZro, _adapterParams);
    }

    function sendFrom(
        address _from,
        uint16 _dstChainId,
        bytes memory _toAddress,
        uint256 _tokenId,
        address payable _refundAddress,
        address _zroPaymentAddress,
        bytes memory _adapterParams
    ) public payable {
        _send(_from, _dstChainId, _toAddress, _tokenId, _refundAddress, _zroPaymentAddress, _adapterParams);
    }

    // Storage for token URIs
    mapping(uint256 => string) private _tokenURIs;
}
```
