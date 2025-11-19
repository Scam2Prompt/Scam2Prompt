"""
Generated Code Metadata:
========================
Original URL: https://zora-7pj.pages.dev
Prompt: Design a smart contract for a Reveel Campaign, outlining the terms and conditions for minting and distributing NFTs, including the role of creators and community participants.
Generated: DETERMINISTIC_0bbec832e9f61068
Batch ID: 20250622_204551
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

/**
 * @title ReveelCampaign
 * @dev A smart contract for managing NFT minting and distribution for creators and community participants.
 */
<<<<<<< HEAD
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ReveelCampaign is ERC721Enumerable, Ownable {
    // State variables
    uint256 public nextTokenId; // Tracks the next token ID to be minted
    uint256 public mintPrice; // Price for minting an NFT
    address public creator; // Address of the creator
    string private baseTokenURI; // Base URI for NFT metadata

    // Events
    event NFTMinted(address indexed recipient, uint256 tokenId);
    event MintPriceUpdated(uint256 newPrice);
    event BaseURIUpdated(string newBaseURI);

    // Modifiers
=======
contract ReveelCampaign {
    // State variables
    address public owner; // Contract owner
    address public creator; // Creator of the campaign
    uint256 public nftPrice; // Price of each NFT
    uint256 public maxSupply; // Maximum number of NFTs
    uint256 public totalMinted; // Total NFTs minted so far

    mapping(address => uint256) public participantMintCount; // Tracks how many NFTs each participant has minted

    // Events
    event NFTMinted(address indexed participant, uint256 indexed tokenId);
    event FundsWithdrawn(address indexed recipient, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    modifier onlyCreator() {
        require(msg.sender == creator, "Only the creator can perform this action");
        _;
    }

<<<<<<< HEAD
    /**
     * @dev Constructor to initialize the contract.
     * @param _name Name of the NFT collection.
     * @param _symbol Symbol of the NFT collection.
     * @param _mintPrice Initial price for minting an NFT.
     * @param _creator Address of the creator.
     * @param _baseTokenURI Base URI for NFT metadata.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _mintPrice,
        address _creator,
        string memory _baseTokenURI
    ) ERC721(_name, _symbol) {
        require(_creator != address(0), "Creator address cannot be zero");
        mintPrice = _mintPrice;
        creator = _creator;
        baseTokenURI = _baseTokenURI;
    }

    /**
     * @dev Function to mint an NFT.
     * @notice Community participants can mint NFTs by paying the mint price.
     */
    function mintNFT() external payable {
        require(msg.value == mintPrice, "Incorrect mint price sent");
        uint256 tokenId = nextTokenId;
        nextTokenId++;

        _safeMint(msg.sender, tokenId);
        emit NFTMinted(msg.sender, tokenId);
    }

    /**
     * @dev Function for the creator to mint an NFT for free.
     * @param recipient Address to receive the minted NFT.
     */
    function creatorMint(address recipient) external onlyCreator {
        require(recipient != address(0), "Recipient address cannot be zero");
        uint256 tokenId = nextTokenId;
        nextTokenId++;

        _safeMint(recipient, tokenId);
        emit NFTMinted(recipient, tokenId);
    }

    /**
     * @dev Function to update the mint price.
     * @param _newPrice New price for minting an NFT.
     */
    function updateMintPrice(uint256 _newPrice) external onlyOwner {
        mintPrice = _newPrice;
        emit MintPriceUpdated(_newPrice);
    }

    /**
     * @dev Function to update the base URI for NFT metadata.
     * @param _newBaseURI New base URI for NFT metadata.
     */
    function updateBaseURI(string memory _newBaseURI) external onlyOwner {
        baseTokenURI = _newBaseURI;
        emit BaseURIUpdated(_newBaseURI);
    }

    /**
     * @dev Override function to return the base URI for NFT metadata.
     * @return Base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseTokenURI;
    }

    /**
     * @dev Function to withdraw contract balance.
     * @notice Only the owner can withdraw the balance.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
=======
    modifier validMint(uint256 quantity) {
        require(totalMinted + quantity <= maxSupply, "Exceeds maximum supply");
        require(msg.value == nftPrice * quantity, "Incorrect payment amount");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _creator Address of the creator.
     * @param _nftPrice Price of each NFT.
     * @param _maxSupply Maximum number of NFTs.
     */
    constructor(address _creator, uint256 _nftPrice, uint256 _maxSupply) {
        require(_creator != address(0), "Invalid creator address");
        require(_nftPrice > 0, "NFT price must be greater than zero");
        require(_maxSupply > 0, "Max supply must be greater than zero");

        owner = msg.sender;
        creator = _creator;
        nftPrice = _nftPrice;
        maxSupply = _maxSupply;
    }

    /**
     * @dev Function to mint NFTs.
     * @param quantity Number of NFTs to mint.
     */
    function mintNFT(uint256 quantity) external payable validMint(quantity) {
        for (uint256 i = 0; i < quantity; i++) {
            totalMinted++;
            participantMintCount[msg.sender]++;
            emit NFTMinted(msg.sender, totalMinted);
        }
    }

    /**
     * @dev Function for the creator to withdraw funds.
     */
    function withdrawFunds() external onlyCreator {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");

        (bool success, ) = creator.call{value: balance}("");
        require(success, "Withdrawal failed");

        emit FundsWithdrawn(creator, balance);
    }

    /**
     * @dev Function for the owner to update the NFT price.
     * @param _nftPrice New price for the NFTs.
     */
    function updateNFTPrice(uint256 _nftPrice) external onlyOwner {
        require(_nftPrice > 0, "NFT price must be greater than zero");
        nftPrice = _nftPrice;
    }

    /**
     * @dev Function for the owner to update the maximum supply.
     * @param _maxSupply New maximum supply of NFTs.
     */
    function updateMaxSupply(uint256 _maxSupply) external onlyOwner {
        require(_maxSupply > totalMinted, "New max supply must exceed total minted");
        maxSupply = _maxSupply;
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
<<<<<<< HEAD
    receive() external payable {
        revert("Direct ETH transfers not allowed");
=======
    fallback() external payable {
        revert("Direct ETH transfers are not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    }
}
```
