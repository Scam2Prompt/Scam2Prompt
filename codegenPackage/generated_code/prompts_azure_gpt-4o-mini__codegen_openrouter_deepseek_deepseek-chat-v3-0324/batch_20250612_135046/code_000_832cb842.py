"""
Generated Code Metadata:
========================
Original URL: https://cryptotitties.fun
Prompt: Generate a Solidity contract for an NFT charity project similar to CryptOtitties, including features for donation tracking and ERC721 compliance.
Generated: DETERMINISTIC_832cb84233d8e55b
Batch ID: 20250612_135046
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";

contract CharityNFT is ERC721, ERC721Enumerable, Ownable {
    using SafeMath for uint256;
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;

    // Charity information
    address public charityWallet;
    string public charityName;
    string public charityDescription;

    // NFT metadata
    string private _baseTokenURI;
    uint256 public mintPrice;
    uint256 public totalDonations;

    // Events
    event DonationMade(address indexed donor, uint256 amount, uint256 tokenId);
    event CharityWalletUpdated(address newWallet);
    event MintPriceUpdated(uint256 newPrice);

    constructor(
        string memory name,
        string memory symbol,
        string memory baseTokenURI,
        uint256 _mintPrice,
        address _charityWallet,
        string memory _charityName,
        string memory _charityDescription
    ) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
        mintPrice = _mintPrice;
        charityWallet = _charityWallet;
        charityName = _charityName;
        charityDescription = _charityDescription;
    }

    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    function setMintPrice(uint256 _price) external onlyOwner {
        require(_price > 0, "Price must be greater than 0");
        mintPrice = _price;
        emit MintPriceUpdated(_price);
    }

    function setCharityWallet(address _wallet) external onlyOwner {
        require(_wallet != address(0), "Invalid wallet address");
        charityWallet = _wallet;
        emit CharityWalletUpdated(_wallet);
    }

    function mintNFT(address recipient) external payable {
        require(msg.value >= mintPrice, "Insufficient payment");
        require(recipient != address(0), "Invalid recipient address");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(recipient, tokenId);

        uint256 donationAmount = msg.value;
        totalDonations = totalDonations.add(donationAmount);
        
        (bool success, ) = charityWallet.call{value: donationAmount}("");
        require(success, "Donation transfer failed");

        emit DonationMade(msg.sender, donationAmount, tokenId);
    }

    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    // Override required for ERC721Enumerable
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override(ERC721, ERC721Enumerable) {
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

    function getTotalDonations() external view returns (uint256) {
        return totalDonations;
    }

    function getTotalMinted() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
