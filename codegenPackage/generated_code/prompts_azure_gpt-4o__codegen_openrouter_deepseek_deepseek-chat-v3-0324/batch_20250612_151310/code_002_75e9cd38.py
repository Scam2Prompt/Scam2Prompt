"""
Generated Code Metadata:
========================
Original URL: https://presale-blockbets-casino.pages.dev
Prompt: Provide code for minting NFTs and distributing tokens using the COIN NODE protocol. Ensure compatibility with multiple wallets.
Generated: DETERMINISTIC_75e9cd381ce83fbc
Batch ID: 20250612_151310
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract CoinNodeNFT is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    IERC20 public token;
    uint256 public mintPrice;
    string public baseURI;

    event NFTMinted(address indexed recipient, uint256 tokenId);
    event TokensDistributed(address indexed recipient, uint256 amount);

    constructor(
        string memory name,
        string memory symbol,
        address _tokenAddress,
        uint256 _mintPrice,
        string memory _baseURI
    ) ERC721(name, symbol) {
        token = IERC20(_tokenAddress);
        mintPrice = _mintPrice;
        baseURI = _baseURI;
    }

    function setMintPrice(uint256 _mintPrice) external onlyOwner {
        mintPrice = _mintPrice;
    }

    function setBaseURI(string memory _baseURI) external onlyOwner {
        baseURI = _baseURI;
    }

    function setTokenAddress(address _tokenAddress) external onlyOwner {
        token = IERC20(_tokenAddress);
    }

    function mintNFT() external nonReentrant {
        require(token.balanceOf(msg.sender) >= mintPrice, "Insufficient token balance");
        require(token.allowance(msg.sender, address(this)) >= mintPrice, "Token allowance not set");

        bool success = token.transferFrom(msg.sender, address(this), mintPrice);
        require(success, "Token transfer failed");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(msg.sender, tokenId);

        emit NFTMinted(msg.sender, tokenId);
    }

    function distributeTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Arrays length mismatch");

        uint256 totalAmount;
        for (uint256 i = 0; i < amounts.length; i++) {
            totalAmount += amounts[i];
        }

        require(token.balanceOf(address(this)) >= totalAmount, "Insufficient contract balance");

        for (uint256 i = 0; i < recipients.length; i++) {
            bool success = token.transfer(recipients[i], amounts[i]);
            require(success, "Token transfer failed");
            emit TokensDistributed(recipients[i], amounts[i]);
        }
    }

    function withdrawTokens() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        bool success = token.transfer(owner(), balance);
        require(success, "Token transfer failed");
    }

    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }

    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
