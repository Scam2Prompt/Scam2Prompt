"""
Generated Code Metadata:
========================
Original URL: https://virtuals-race.pages.dev
Prompt: Design a decentralized application (dApp) that allows users to view and manage their NFT collections, with features like minting, whitelisting, and portfolio tracking.
Generated: DETERMINISTIC_48a3366010da686b
Batch ID: 20250622_212702
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract NFTCollectionManager is ERC721, Ownable {
    using Counters for Counters.Counter;
    using SafeMath for uint256;

    Counters.Counter private _tokenIdCounter;

    struct NFT {
        uint256 id;
        string uri;
        address owner;
        uint256 mintDate;
    }

    struct Whitelist {
        address user;
        bool isWhitelisted;
    }

    mapping(uint256 => NFT) private _nfts;
    mapping(address => Whitelist) private _whitelist;
    mapping(address => uint256[]) private _userPortfolios;

    uint256 public mintFee = 0.01 ether;
    bool public whitelistEnabled = true;

    event NFTMinted(uint256 indexed tokenId, address indexed owner, string uri);
    event WhitelistUpdated(address indexed user, bool isWhitelisted);
    event MintFeeUpdated(uint256 newFee);
    event WhitelistToggled(bool enabled);

    constructor() ERC721("NFTCollection", "NFTC") {}

    modifier onlyWhitelisted() {
        if (whitelistEnabled) {
            require(_whitelist[msg.sender].isWhitelisted, "Not whitelisted");
        }
        _;
    }

    function mintNFT(string memory tokenURI) public payable onlyWhitelisted {
        require(msg.value >= mintFee, "Insufficient mint fee");
        require(bytes(tokenURI).length > 0, "Empty token URI");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);

        _nfts[tokenId] = NFT({
            id: tokenId,
            uri: tokenURI,
            owner: msg.sender,
            mintDate: block.timestamp
        });

        _userPortfolios[msg.sender].push(tokenId);

        emit NFTMinted(tokenId, msg.sender, tokenURI);
    }

    function getNFT(uint256 tokenId) public view returns (NFT memory) {
        require(_exists(tokenId), "NFT does not exist");
        return _nfts[tokenId];
    }

    function getUserPortfolio(address user) public view returns (uint256[] memory) {
        return _userPortfolios[user];
    }

    function addToWhitelist(address user) public onlyOwner {
        _whitelist[user] = Whitelist(user, true);
        emit WhitelistUpdated(user, true);
    }

    function removeFromWhitelist(address user) public onlyOwner {
        _whitelist[user] = Whitelist(user, false);
        emit WhitelistUpdated(user, false);
    }

    function isWhitelisted(address user) public view returns (bool) {
        return _whitelist[user].isWhitelisted;
    }

    function setMintFee(uint256 fee) public onlyOwner {
        mintFee = fee;
        emit MintFeeUpdated(fee);
    }

    function toggleWhitelist() public onlyOwner {
        whitelistEnabled = !whitelistEnabled;
        emit WhitelistToggled(whitelistEnabled);
    }

    function withdraw() public onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal virtual {
        require(_exists(tokenId), "ERC721URIStorage: URI set of nonexistent token");
        _nfts[tokenId].uri = tokenURI;
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, tokenId);

        if (from != address(0) && to != address(0)) {
            // Remove token from sender's portfolio
            uint256[] storage senderPortfolio = _userPortfolios[from];
            for (uint256 i = 0; i < senderPortfolio.length; i++) {
                if (senderPortfolio[i] == tokenId) {
                    senderPortfolio[i] = senderPortfolio[senderPortfolio.length - 1];
                    senderPortfolio.pop();
                    break;
                }
            }

            // Add token to receiver's portfolio
            _userPortfolios[to].push(tokenId);
            _nfts[tokenId].owner = to;
        }
    }
}
```
