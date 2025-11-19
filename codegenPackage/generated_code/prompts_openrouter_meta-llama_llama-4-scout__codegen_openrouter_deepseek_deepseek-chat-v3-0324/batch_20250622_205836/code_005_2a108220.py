"""
Generated Code Metadata:
========================
Original URL: https://kakaxa.pages.dev
Prompt: Develop a basic NFT sticker and emoji system for a GameFi project like $KAKAXA, using a suitable programming language and blockchain platform.
Generated: DETERMINISTIC_2a10822059d5e566
Batch ID: 20250622_205836
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract KakaxaStickers is ERC721, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    struct Sticker {
        uint256 id;
        string name;
        string symbol;
        string uri;
        uint256 price;
        bool isEmoji;
    }

    mapping(uint256 => Sticker) public stickers;
    mapping(address => mapping(uint256 => bool)) public ownedStickers;

    event StickerMinted(uint256 indexed tokenId, address indexed owner, string uri);
    event StickerPurchased(uint256 indexed tokenId, address indexed buyer);

    constructor() ERC721("KakaxaStickers", "KST") {}

    function mintSticker(
        string memory name,
        string memory symbol,
        string memory uri,
        uint256 price,
        bool isEmoji
    ) public onlyOwner {
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, uri);

        stickers[tokenId] = Sticker({
            id: tokenId,
            name: name,
            symbol: symbol,
            uri: uri,
            price: price,
            isEmoji: isEmoji
        });

        ownedStickers[msg.sender][tokenId] = true;
        emit StickerMinted(tokenId, msg.sender, uri);
    }

    function purchaseSticker(uint256 tokenId) public payable {
        require(_exists(tokenId), "Sticker does not exist");
        require(msg.value >= stickers[tokenId].price, "Insufficient funds");
        require(!ownedStickers[msg.sender][tokenId], "Already owns this sticker");

        address owner = ownerOf(tokenId);
        _transfer(owner, msg.sender, tokenId);
        ownedStickers[msg.sender][tokenId] = true;
        ownedStickers[owner][tokenId] = false;

        payable(owner).transfer(msg.value);
        emit StickerPurchased(tokenId, msg.sender);
    }

    function getStickerDetails(uint256 tokenId) public view returns (Sticker memory) {
        require(_exists(tokenId), "Sticker does not exist");
        return stickers[tokenId];
    }

    function getOwnedStickers(address owner) public view returns (Sticker[] memory) {
        uint256 totalStickers = _tokenIdCounter.current();
        uint256 ownedCount = 0;

        for (uint256 i = 1; i <= totalStickers; i++) {
            if (ownedStickers[owner][i]) {
                ownedCount++;
            }
        }

        Sticker[] memory result = new Sticker[](ownedCount);
        uint256 currentIndex = 0;

        for (uint256 i = 1; i <= totalStickers; i++) {
            if (ownedStickers[owner][i]) {
                result[currentIndex] = stickers[i];
                currentIndex++;
            }
        }

        return result;
    }

    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }
}
```
