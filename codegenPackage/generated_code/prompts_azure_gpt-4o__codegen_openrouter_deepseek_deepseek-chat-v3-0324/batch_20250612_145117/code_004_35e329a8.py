"""
Generated Code Metadata:
========================
Original URL: https://gotchipus.top
Prompt: Write a smart contract for minting unique digital assets, inspired by the functionality described on Gotchipus Mint.
Generated: DETERMINISTIC_35e329a81404f4b3
Batch ID: 20250612_145117
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
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract GotchipusMint is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;

    // Contract configuration
    uint256 public constant MAX_SUPPLY = 10000;
    uint256 public constant MINT_PRICE = 0.08 ether;
    uint256 public constant MAX_PER_WALLET = 5;
    bool public isPublicMintEnabled;
    string public baseTokenURI;

    // Track mints per wallet
    mapping(address => uint256) public walletMints;

    // Events
    event Minted(address indexed minter, uint256 tokenId);
    event BaseURIUpdated(string newBaseURI);
    event MintStateChanged(bool isEnabled);

    constructor(string memory _baseTokenURI) ERC721("GotchipusMint", "GOTCHI") {
        baseTokenURI = _baseTokenURI;
    }

    // Modifiers
    modifier onlyPublicMint() {
        require(isPublicMintEnabled, "Public mint is not enabled");
        _;
    }

    modifier withinMaxSupply(uint256 _quantity) {
        require(
            _tokenIdCounter.current() + _quantity <= MAX_SUPPLY,
            "Exceeds max supply"
        );
        _;
    }

    modifier validateMint(uint256 _quantity) {
        require(_quantity > 0, "Quantity must be positive");
        require(
            walletMints[msg.sender] + _quantity <= MAX_PER_WALLET,
            "Exceeds max per wallet"
        );
        require(msg.value >= MINT_PRICE * _quantity, "Insufficient ETH");
        _;
    }

    // Minting functions
    function publicMint(uint256 _quantity)
        external
        payable
        onlyPublicMint
        withinMaxSupply(_quantity)
        validateMint(_quantity)
        nonReentrant
    {
        _mintTokens(_quantity, msg.sender);
    }

    function ownerMint(uint256 _quantity, address _recipient)
        external
        onlyOwner
        withinMaxSupply(_quantity)
    {
        _mintTokens(_quantity, _recipient);
    }

    function _mintTokens(uint256 _quantity, address _recipient) private {
        for (uint256 i = 0; i < _quantity; i++) {
            _tokenIdCounter.increment();
            uint256 newTokenId = _tokenIdCounter.current();
            _safeMint(_recipient, newTokenId);
            walletMints[_recipient]++;
            emit Minted(_recipient, newTokenId);
        }
    }

    // Token URI
    function tokenURI(uint256 tokenId)
        public
        view
        override
        returns (string memory)
    {
        require(_exists(tokenId), "Token does not exist");
        return
            bytes(baseTokenURI).length > 0
                ? string(
                    abi.encodePacked(baseTokenURI, tokenId.toString(), ".json")
                )
                : "";
    }

    // Admin functions
    function setBaseURI(string memory _newBaseURI) external onlyOwner {
        baseTokenURI = _newBaseURI;
        emit BaseURIUpdated(_newBaseURI);
    }

    function togglePublicMint() external onlyOwner {
        isPublicMintEnabled = !isPublicMintEnabled;
        emit MintStateChanged(isPublicMintEnabled);
    }

    // Withdraw funds
    function withdraw() external onlyOwner nonReentrant {
        (bool success, ) = owner().call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }

    // View functions
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    function getMintsByAddress(address _address) external view returns (uint256) {
        return walletMints[_address];
    }
}
```
