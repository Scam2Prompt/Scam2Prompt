"""
Generated Code Metadata:
========================
Original URL: https://anniversary-base.pages.dev
Prompt: Write a script in Solidity to interact with the Base mainnet and mint an NFT, ensuring the wallet has sufficient ETH for gas fees and verifying eligibility based on a testnet NFT.
Generated: DETERMINISTIC_c4b8db24c702b5c0
Batch ID: 20250612_150927
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
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

contract MainnetNFT is ERC721, Ownable {
    using Address for address payable;

    IERC721 public testnetNFT;
    uint256 public nextTokenId;
    uint256 public mintPrice;
    bool public mintingEnabled;

    mapping(address => bool) public hasMinted;

    event NFTMinted(address indexed recipient, uint256 tokenId);

    constructor(
        address _testnetNFTAddress,
        uint256 _mintPrice
    ) ERC721("MainnetNFT", "MNFT") {
        testnetNFT = IERC721(_testnetNFTAddress);
        mintPrice = _mintPrice;
        mintingEnabled = true;
    }

    function mint() external payable {
        require(mintingEnabled, "Minting is disabled");
        require(!hasMinted[msg.sender], "Already minted");
        require(msg.value >= mintPrice, "Insufficient ETH for minting");
        require(
            testnetNFT.balanceOf(msg.sender) > 0,
            "No testnet NFT found for this address"
        );

        hasMinted[msg.sender] = true;
        uint256 tokenId = nextTokenId++;
        _safeMint(msg.sender, tokenId);

        if (msg.value > mintPrice) {
            payable(msg.sender).sendValue(msg.value - mintPrice);
        }

        emit NFTMinted(msg.sender, tokenId);
    }

    function withdraw() external onlyOwner {
        payable(owner()).sendValue(address(this).balance);
    }

    function setMintPrice(uint256 _newPrice) external onlyOwner {
        mintPrice = _newPrice;
    }

    function toggleMinting() external onlyOwner {
        mintingEnabled = !mintingEnabled;
    }

    function setTestnetNFT(address _newTestnetNFT) external onlyOwner {
        testnetNFT = IERC721(_newTestnetNFT);
    }
}
```
