"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://puffmypanda.pages.dev
Prompt: Generate a smart contract for minting ERC-721A tokens for the Puff Puff Pandas NFT collection, including features for greenlist access and airdrop of $PUFFS tokens.
Generated: DETERMINISTIC_10782a560f74cd1f
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title Puff Puff Pandas ERC-721A Smart Contract
 * @dev This contract implements minting with ERC-721A, greenlist access, and token airdrop functionality.
 */
import "erc721a/contracts/ERC721A.sol"; // Import the ERC-721A implementation
import "@openzeppelin/contracts/access/Ownable.sol"; // Import for ownership management
import "@openzeppelin/contracts/token/ERC20/IERC20.sol"; // Import for ERC-20 interaction

contract PuffPuffPandas is ERC721A, Ownable {
    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Price per NFT in wei
    uint256 public constant MINT_PRICE = 0.05 ether;

    // Maximum number of NFTs per wallet
    uint256 public constant MAX_MINT_PER_WALLET = 20;

    // Greenlist mapping for addresses allowed to mint early
    mapping(address => bool) public greenlist;

    // $PUFFS token for airdrop functionality
    IERC20 public puffsToken;

    // Track the number of NFTs minted by each wallet
    mapping(address => uint256) public walletMintedCount;

    // Events
    event Minted(address indexed minter, uint256 quantity);
    event AirdropExecuted(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor to initialize the NFT collection details and $PUFFS token contract.
     * @param _name NFT collection name.
     * @param _symbol NFT collection symbol.
     * @param _puffsToken Address of the $PUFFS token contract.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        address _puffsToken
    ) ERC721A(_name, _symbol) {
        puffsToken = IERC20(_puffsToken);
    }

    /**
     * @dev Mint function for greenlisted and public users.
     * @param quantity Number of NFTs to mint.
     */
    function mint(uint256 quantity) external payable {
        require(quantity > 0, "Mint quantity must be greater than zero");
        require(totalSupply() + quantity <= MAX_SUPPLY, "Exceeds maximum supply");
        require(msg.value >= quantity * MINT_PRICE, "Insufficient ETH sent");

        if (greenlist[msg.sender]) {
            // Greenlist access - bypass wallet limit
            _mint(msg.sender, quantity);
        } else {
            require(
                walletMintedCount[msg.sender] + quantity <= MAX_MINT_PER_WALLET,
                "Exceeds max mint limit per wallet"
            );
            _mint(msg.sender, quantity);
            walletMintedCount[msg.sender] += quantity;
        }

        emit Minted(msg.sender, quantity);
    }

    /**
     * @dev Owner-only function to set greenlist access.
     * @param accounts Array of addresses to be added to the greenlist.
     * @param status Boolean indicating whether to add or remove greenlist access.
     */
    function setGreenlist(address[] calldata accounts, bool status) external onlyOwner {
        for (uint256 i = 0; i < accounts.length; i++) {
            greenlist[accounts[i]] = status;
        }
    }

    /**
     * @dev Airdrop $PUFFS tokens to specific wallet addresses.
     * @param recipients Array of recipient addresses.
     * @param amounts Array of amounts to airdrop to each recipient.
     */
    function airdrop(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Airdrop amount must be greater than zero");

            puffsToken.transfer(recipients[i], amounts[i]);
            emit AirdropExecuted(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Withdraw contract balance to the owner's wallet.
     */
    function withdraw() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");
        payable(owner()).transfer(contractBalance);
    }

    /**
     * @dev Update the $PUFFS token contract address.
     * @param _puffsToken New $PUFFS token contract address.
     */
    function setPuffsToken(address _puffsToken) external onlyOwner {
        require(_puffsToken != address(0), "Invalid token address");
        puffsToken = IERC20(_puffsToken);
    }
}
```
