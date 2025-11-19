"""
Generated Code Metadata:
========================
Original URL: https://cryptotitties.fun
Prompt: Write a Solidity smart contract for an NFT charity project similar to CryptoTitties, ensuring it includes functionality for token minting, prize wallets, and donation tracking.
Generated: DETERMINISTIC_5808efd2742e66a2
Batch ID: 20250612_150323
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title NFT Charity Project Contract
 * @author [Your Name]
 * @notice This contract manages an NFT charity project similar to CryptoTitties.
 * It includes functionality for token minting, prize wallets, and donation tracking.
 */
contract NFTCharityProject {
    using SafeMath for uint256;
    using SafeERC721 for mapping(address => uint256);

    // Mapping of token ownership
    mapping (address => uint256) public tokenBalance;

    // Mapping of token metadata
    mapping (uint256 => TokenMetadata) public tokenMetadata;

    // Mapping of prize wallets
    mapping (address => bool) public prizeWallets;

    // Mapping of donation history
    mapping (address => Donation[]) public donationHistory;

    // Event emitted when a new token is minted
    event NewToken(address indexed owner, uint256 tokenId);

    // Event emitted when a donation is made
    event DonationMade(address indexed donor, uint256 amount);

    // Struct for token metadata
    struct TokenMetadata {
        string name;
        string description;
        string imageURI;
    }

    // Struct for donations
    struct Donation {
        address donor;
        uint256 amount;
    }

    // Address of the token contract
    address public tokenContract;

    // Address of the charity wallet
    address public charityWallet;

    // Total supply of tokens
    uint256 public totalSupply;

    // Token price
    uint256 public tokenPrice;

    /**
     * @dev Constructor function
     * @param _tokenContract Address of the token contract
     * @param _charityWallet Address of the charity wallet
     * @param _tokenPrice Price of each token
     */
    constructor(address _tokenContract, address _charityWallet, uint256 _tokenPrice) public {
        require(_tokenContract != address(0), "Token contract address cannot be zero");
        require(_charityWallet != address(0), "Charity wallet address cannot be zero");
        require(_tokenPrice > 0, "Token price must be greater than zero");

        tokenContract = _tokenContract;
        charityWallet = _charityWallet;
        tokenPrice = _tokenPrice;
    }

    /**
     * @dev Mint a new token
     * @param _owner Address of the token owner
     * @param _tokenId ID of the token to mint
     * @param _name Name of the token
     * @param _description Description of the token
     * @param _imageURI URI of the token image
     */
    function mintToken(address _owner, uint256 _tokenId, string memory _name, string memory _description, string memory _imageURI) public {
        require(msg.sender == tokenContract, "Only the token contract can mint tokens");
        require(tokenBalance[_owner] == 0, "Owner already has a token");

        tokenBalance[_owner] = _tokenId;
        tokenMetadata[_tokenId] = TokenMetadata(_name, _description, _imageURI);
        totalSupply = totalSupply.add(1);

        emit NewToken(_owner, _tokenId);
    }

    /**
     * @dev Make a donation to the charity
     * @param _amount Amount of the donation
     */
    function makeDonation(uint256 _amount) public {
        require(msg.sender != address(0), "Donor address cannot be zero");
        require(_amount > 0, "Donation amount must be greater than zero");

        donationHistory[msg.sender].push(Donation(msg.sender, _amount));
        payable(charityWallet).transfer(_amount);

        emit DonationMade(msg.sender, _amount);
    }

    /**
     * @dev Add a prize wallet
     * @param _wallet Address of the prize wallet
     */
    function addPrizeWallet(address _wallet) public {
        require(msg.sender == charityWallet, "Only the charity wallet can add prize wallets");
        require(_wallet != address(0), "Prize wallet address cannot be zero");

        prizeWallets[_wallet] = true;
    }

    /**
     * @dev Remove a prize wallet
     * @param _wallet Address of the prize wallet
     */
    function removePrizeWallet(address _wallet) public {
        require(msg.sender == charityWallet, "Only the charity wallet can remove prize wallets");
        require(prizeWallets[_wallet], "Prize wallet does not exist");

        delete prizeWallets[_wallet];
    }

    /**
     * @dev Get the token metadata
     * @param _tokenId ID of the token
     * @return TokenMetadata struct containing the token metadata
     */
    function getTokenMetadata(uint256 _tokenId) public view returns (TokenMetadata memory) {
        return tokenMetadata[_tokenId];
    }

    /**
     * @dev Get the donation history
     * @param _donor Address of the donor
     * @return Donation[] array containing the donation history
     */
    function getDonationHistory(address _donor) public view returns (Donation[] memory) {
        return donationHistory[_donor];
    }
}
```
