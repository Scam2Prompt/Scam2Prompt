"""
Generated Code Metadata:
========================
Original URL: https://tokencatgirl.pages.dev
Prompt: Develop a Solidity contract for a decentralized NFT marketplace similar to the one in the Catgirl ecosystem, including features for buying and selling CATGIRL¢-based NFTs.
Generated: DETERMINISTIC_2fe5474c3898dfe8
Batch ID: 20250612_153606
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract CatgirlNFT is ERC721, ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    constructor(string memory baseURI) ERC721("CatgirlNFT", "CATGIRL") {
        _baseTokenURI = baseURI;
    }

    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    function mint(address to) public onlyOwner {
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(to, tokenId);
    }

    // The following functions are overrides required by Solidity.
    function _beforeTokenTransfer(address from, address to, uint256 tokenId)
        internal
        override(ERC721, ERC721Enumerable)
    {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}

contract CatgirlMarketplace is Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _itemIds;

    IERC20 public catgirlToken;
    CatgirlNFT public catgirlNFT;

    struct MarketItem {
        uint256 itemId;
        uint256 tokenId;
        address payable seller;
        address payable owner;
        uint256 price;
        bool sold;
    }

    mapping(uint256 => MarketItem) private idToMarketItem;

    event MarketItemCreated(
        uint256 indexed itemId,
        uint256 indexed tokenId,
        address seller,
        address owner,
        uint256 price,
        bool sold
    );

    event MarketItemSold(
        uint256 indexed itemId,
        uint256 indexed tokenId,
        address seller,
        address buyer,
        uint256 price
    );

    constructor(address _catgirlTokenAddress, address _catgirlNFTAddress) {
        catgirlToken = IERC20(_catgirlTokenAddress);
        catgirlNFT = CatgirlNFT(_catgirlNFTAddress);
    }

    function createMarketItem(uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than 0");
        require(catgirlNFT.ownerOf(tokenId) == msg.sender, "You must own the NFT");

        _itemIds.increment();
        uint256 itemId = _itemIds.current();

        idToMarketItem[itemId] = MarketItem(
            itemId,
            tokenId,
            payable(msg.sender),
            payable(address(this)),
            price,
            false
        );

        catgirlNFT.transferFrom(msg.sender, address(this), tokenId);

        emit MarketItemCreated(
            itemId,
            tokenId,
            msg.sender,
            address(this),
            price,
            false
        );
    }

    function createMarketSale(uint256 itemId) external {
        MarketItem storage item = idToMarketItem[itemId];
        uint256 price = item.price;
        uint256 tokenId = item.tokenId;

        require(!item.sold, "Item already sold");
        require(catgirlToken.balanceOf(msg.sender) >= price, "Insufficient CATGIRL¢ balance");
        require(catgirlToken.allowance(msg.sender, address(this)) >= price, "Token allowance too low");

        item.seller.transfer(price);
        catgirlToken.transferFrom(msg.sender, item.seller, price);
        catgirlNFT.transferFrom(address(this), msg.sender, tokenId);

        item.owner = payable(msg.sender);
        item.sold = true;

        emit MarketItemSold(itemId, tokenId, item.seller, msg.sender, price);
    }

    function fetchMarketItems() public view returns (MarketItem[] memory) {
        uint256 itemCount = _itemIds.current();
        uint256 unsoldItemCount = _itemIds.current();
        uint256 currentIndex = 0;

        for (uint256 i = 1; i <= itemCount; i++) {
            if (!idToMarketItem[i].sold) {
                unsoldItemCount++;
            }
        }

        MarketItem[] memory items = new MarketItem[](unsoldItemCount);
        for (uint256 i = 1; i <= itemCount; i++) {
            if (!idToMarketItem[i].sold) {
                MarketItem storage currentItem = idToMarketItem[i];
                items[currentIndex] = currentItem;
                currentIndex++;
            }
        }
        return items;
    }

    function fetchMyNFTs() public view returns (MarketItem[] memory) {
        uint256 totalItemCount = _itemIds.current();
        uint256 itemCount = 0;
        uint256 currentIndex = 0;

        for (uint256 i = 1; i <= totalItemCount; i++) {
            if (idToMarketItem[i].owner == msg.sender) {
                itemCount++;
            }
        }

        MarketItem[] memory items = new MarketItem[](itemCount);
        for (uint256 i = 1; i <= totalItemCount; i++) {
            if (idToMarketItem[i].owner == msg.sender) {
                MarketItem storage currentItem = idToMarketItem[i];
                items[currentIndex] = currentItem;
                currentIndex++;
            }
        }
        return items;
    }

    function fetchItemsCreated() public view returns (MarketItem[] memory) {
        uint256 totalItemCount = _itemIds.current();
        uint256 itemCount = 0;
        uint256 currentIndex = 0;

        for (uint256 i = 1; i <= totalItemCount; i++) {
            if (idToMarketItem[i].seller == msg.sender) {
                itemCount++;
            }
        }

        MarketItem[] memory items = new MarketItem[](itemCount);
        for (uint256 i = 1; i <= totalItemCount; i++) {
            if (idToMarketItem[i].seller == msg.sender) {
                MarketItem storage currentItem = idToMarketItem[i];
                items[currentIndex] = currentItem;
                currentIndex++;
            }
        }
        return items;
    }
}
```
