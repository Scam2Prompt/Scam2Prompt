"""
Generated Code Metadata:
========================
Original URL: https://mbdfinancialsmig.pages.dev
Prompt: "Create a token utility model for a decentralized entertainment district in the metaverse, incorporating tokenization and NFTs for creators and fans, as envisioned in MBD Entertainment District."
Generated: DETERMINISTIC_40c83e4841b846ea
Batch ID: 20250622_204752
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract MBDToken is ERC20, ERC20Burnable, ERC20Snapshot, AccessControl {
    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    bytes32 public constant SNAPSHOT_ROLE = keccak256("SNAPSHOT_ROLE");

    constructor() ERC20("MBD Entertainment Token", "MBD") {
        _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _setupRole(MINTER_ROLE, msg.sender);
        _setupRole(SNAPSHOT_ROLE, msg.sender);
    }

    function mint(address to, uint256 amount) public onlyRole(MINTER_ROLE) {
        _mint(to, amount);
    }

    function snapshot() public onlyRole(SNAPSHOT_ROLE) returns (uint256) {
        return _snapshot();
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20, ERC20Snapshot) {
        super._beforeTokenTransfer(from, to, amount);
    }
}

contract MBDNFT is ERC721, ERC721Enumerable, ERC721URIStorage, AccessControl {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");

    constructor() ERC721("MBD Entertainment NFT", "MBDNFT") {
        _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _setupRole(MINTER_ROLE, msg.sender);
        _setupRole(ADMIN_ROLE, msg.sender);
    }

    function safeMint(address to, string memory uri) public onlyRole(MINTER_ROLE) {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, uri);
    }

    function updateTokenURI(uint256 tokenId, string memory newURI) public onlyRole(ADMIN_ROLE) {
        require(_exists(tokenId), "Token does not exist");
        _setTokenURI(tokenId, newURI);
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override(ERC721, ERC721Enumerable) {
        super._beforeTokenTransfer(from, to, tokenId);
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

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable, AccessControl)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}

contract MBDEntertainmentDistrict {
    MBDToken public token;
    MBDNFT public nft;

    struct Creator {
        address wallet;
        string name;
        bool isVerified;
    }

    struct Fan {
        address wallet;
        uint256 loyaltyPoints;
    }

    mapping(address => Creator) public creators;
    mapping(address => Fan) public fans;
    mapping(uint256 => address) public nftOwners;

    event CreatorRegistered(address indexed creator, string name);
    event CreatorVerified(address indexed creator);
    event FanRegistered(address indexed fan);
    event NFTPurchased(address indexed buyer, uint256 tokenId);
    event TokenRewarded(address indexed receiver, uint256 amount);

    constructor(address _tokenAddress, address _nftAddress) {
        token = MBDToken(_tokenAddress);
        nft = MBDNFT(_nftAddress);
    }

    function registerCreator(string memory name) external {
        require(creators[msg.sender].wallet == address(0), "Creator already registered");
        creators[msg.sender] = Creator(msg.sender, name, false);
        emit CreatorRegistered(msg.sender, name);
    }

    function verifyCreator(address creator) external {
        require(hasRole(DEFAULT_ADMIN_ROLE, msg.sender), "Only admin can verify");
        creators[creator].isVerified = true;
        emit CreatorVerified(creator);
    }

    function registerFan() external {
        require(fans[msg.sender].wallet == address(0), "Fan already registered");
        fans[msg.sender] = Fan(msg.sender, 0);
        emit FanRegistered(msg.sender);
    }

    function purchaseNFT(string memory uri) external payable {
        require(fans[msg.sender].wallet != address(0), "Fan not registered");
        nft.safeMint(msg.sender, uri);
        uint256 tokenId = nft.totalSupply() - 1;
        nftOwners[tokenId] = msg.sender;
        emit NFTPurchased(msg.sender, tokenId);
    }

    function rewardTokens(address receiver, uint256 amount) external {
        require(hasRole(DEFAULT_ADMIN_ROLE, msg.sender), "Only admin can reward");
        token.mint(receiver, amount);
        emit TokenRewarded(receiver, amount);
    }

    function updateNFTOwner(uint256 tokenId, address newOwner) external {
        require(nft.ownerOf(tokenId) == msg.sender, "Not the owner");
        nftOwners[tokenId] = newOwner;
    }

    function getCreator(address creatorAddress) external view returns (Creator memory) {
        return creators[creatorAddress];
    }

    function getFan(address fanAddress) external view returns (Fan memory) {
        return fans[fanAddress];
    }
}
```
