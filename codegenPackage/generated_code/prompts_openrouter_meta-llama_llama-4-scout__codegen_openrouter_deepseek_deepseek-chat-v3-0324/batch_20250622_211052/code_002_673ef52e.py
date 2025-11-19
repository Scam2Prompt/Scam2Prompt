"""
Generated Code Metadata:
========================
Original URL: https://openswe.io
Prompt: Generate code for a simple NFT marketplace using blockchain technology, inspired by OpenSwe's features.
Generated: DETERMINISTIC_673ef52e3f89d859
Batch ID: 20250622_211052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Simple NFT Marketplace Smart Contract

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract NFTMarketplace is ReentrancyGuard, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _itemIds;
    Counters.Counter private _itemsSold;

    struct MarketItem {
        uint256 itemId;
        address nftContract;
        uint256 tokenId;
        address payable seller;
        address payable owner;
        uint256 price;
        bool sold;
    }

    mapping(uint256 => MarketItem) private idToMarketItem;

    event MarketItemCreated(
        uint256 indexed itemId,
        address indexed nftContract,
        uint256 indexed tokenId,
        address seller,
        address owner,
        uint256 price,
        bool sold
    );

    event MarketItemSold(
        uint256 indexed itemId,
        address indexed nftContract,
        uint256 indexed tokenId,
        address seller,
        address owner,
        uint256 price,
        bool sold
    );

    constructor() {}

    /**
     * @dev Creates a new market item listing
     */
    function createMarketItem(
        address nftContract,
        uint256 tokenId,
        uint256 price
    ) public nonReentrant {
        require(price > 0, "Price must be at least 1 wei");

        _itemIds.increment();
        uint256 itemId = _itemIds.current();

        idToMarketItem[itemId] = MarketItem(
            itemId,
            nftContract,
            tokenId,
            payable(msg.sender),
            payable(address(0)),
            price,
            false
        );

        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);

        emit MarketItemCreated(
            itemId,
            nftContract,
            tokenId,
            msg.sender,
            address(0),
            price,
            false
        );
    }

    /**
     * @dev Creates the sale of a marketplace item
     */
    function createMarketSale(address nftContract, uint256 itemId)
        public
        payable
        nonReentrant
    {
        MarketItem storage item = idToMarketItem[itemId];
        uint256 price = item.price;
        uint256 tokenId = item.tokenId;

        require(
            msg.value == price,
            "Please submit the asking price in order to complete the purchase"
        );
        require(!item.sold, "Item has already been sold");

        item.seller.transfer(msg.value);
        IERC721(nftContract).transferFrom(address(this), msg.sender, tokenId);
        item.owner = payable(msg.sender);
        item.sold = true;
        _itemsSold.increment();

        emit MarketItemSold(
            itemId,
            nftContract,
            tokenId,
            item.seller,
            msg.sender,
            price,
            true
        );
    }

    /**
     * @dev Returns all unsold market items
     */
    function fetchMarketItems() public view returns (MarketItem[] memory) {
        uint256 itemCount = _itemIds.current();
        uint256 unsoldItemCount = _itemIds.current() - _itemsSold.current();
        uint256 currentIndex = 0;

        MarketItem[] memory items = new MarketItem[](unsoldItemCount);
        for (uint256 i = 0; i < itemCount; i++) {
            if (idToMarketItem[i + 1].owner == address(0)) {
                MarketItem storage currentItem = idToMarketItem[i + 1];
                items[currentIndex] = currentItem;
                currentIndex += 1;
            }
        }
        return items;
    }

    /**
     * @dev Returns only items that a user has purchased
     */
    function fetchMyNFTs() public view returns (MarketItem[] memory) {
        uint256 totalItemCount = _itemIds.current();
        uint256 itemCount = 0;
        uint256 currentIndex = 0;

        for (uint256 i = 0; i < totalItemCount; i++) {
            if (idToMarketItem[i + 1].owner == msg.sender) {
                itemCount += 1;
            }
        }

        MarketItem[] memory items = new MarketItem[](itemCount);
        for (uint256 i = 0; i < totalItemCount; i++) {
            if (idToMarketItem[i + 1].owner == msg.sender) {
                MarketItem storage currentItem = idToMarketItem[i + 1];
                items[currentIndex] = currentItem;
                currentIndex += 1;
            }
        }
        return items;
    }

    /**
     * @dev Returns only items a user has listed
     */
    function fetchItemsListed() public view returns (MarketItem[] memory) {
        uint256 totalItemCount = _itemIds.current();
        uint256 itemCount = 0;
        uint256 currentIndex = 0;

        for (uint256 i = 0; i < totalItemCount; i++) {
            if (idToMarketItem[i + 1].seller == msg.sender) {
                itemCount += 1;
            }
        }

        MarketItem[] memory items = new MarketItem[](itemCount);
        for (uint256 i = 0; i < totalItemCount; i++) {
            if (idToMarketItem[i + 1].seller == msg.sender) {
                MarketItem storage currentItem = idToMarketItem[i + 1];
                items[currentIndex] = currentItem;
                currentIndex += 1;
            }
        }
        return items;
    }
}

contract NFT is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    constructor() ERC721("NFT Marketplace Token", "NFTM") {}

    /**
     * @dev Creates a new NFT token
     */
    function createToken(string memory tokenURI) public returns (uint256) {
        _tokenIds.increment();
        uint256 newItemId = _tokenIds.current();

        _mint(msg.sender, newItemId);
        _setTokenURI(newItemId, tokenURI);

        return newItemId;
    }
}
```

# Frontend React Component for NFT Marketplace

```javascript
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import NFTMarketplace from './contracts/NFTMarketplace.json';
import NFT from './contracts/NFT.json';

const Marketplace = () => {
  const [nfts, setNfts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [account, setAccount] = useState('');
  const [contract, setContract] = useState(null);
  const [nftContract, setNftContract] = useState(null);

  useEffect(() => {
    loadBlockchainData();
  }, []);

  async function loadBlockchainData() {
    if (window.ethereum) {
      try {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0]);

        const networkId = await window.ethereum.request({ method: 'net_version' });
        const marketplaceAddress = NFTMarketplace.networks[networkId].address;
        const marketplaceContract = new ethers.Contract(
          marketplaceAddress,
          NFTMarketplace.abi,
          signer
        );
        setContract(marketplaceContract);

        const nftAddress = NFT.networks[networkId].address;
        const nftContract = new ethers.Contract(nftAddress, NFT.abi, signer);
        setNftContract(nftContract);

        await loadMarketplaceItems(marketplaceContract);
      } catch (error) {
        console.error('Error loading blockchain data:', error);
      }
    } else {
      alert('Please install MetaMask to use this dApp!');
    }
  }

  async function loadMarketplaceItems(marketplaceContract) {
    const items = await marketplaceContract.fetchMarketItems();
    const formattedItems = await Promise.all(items.map(async (item) => {
      const tokenUri = await nftContract.tokenURI(item.tokenId);
      const price = ethers.utils.formatUnits(item.price.toString(), 'ether');
      return {
        itemId: item.itemId.toNumber(),
        tokenId: item.tokenId.toNumber(),
        seller: item.seller,
        owner: item.owner,
        price,
        tokenUri,
      };
    }));
    setNfts(formattedItems);
    setLoading(false);
  }

  async function buyNft(item) {
    try {
      setLoading(true);
      const price = ethers.utils.parseUnits(item.price, 'ether');
      const transaction = await contract.createMarket
