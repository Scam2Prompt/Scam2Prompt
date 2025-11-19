"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamster-k.com
Prompt: Generate a code snippet for a smart contract that allows users to exchange NFTs for $HAM tokens in the Hamster Kombat ecosystem.
Generated: DETERMINISTIC_5c57c37d51c57906
Batch ID: 20250612_162813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title NFT to $HAM Token Exchange Contract
 * @author Hamster Kombat Team
 * @notice This contract allows users to exchange NFTs for $HAM tokens in the Hamster Kombat ecosystem.
 */
contract NFTTokenExchange {
    // State variables
    IERC721 public nftContract; // NFT contract interface
    IERC20 public hamToken;     // $HAM token contract interface
    address public owner;       // Contract owner address
    uint256 public exchangeRate; // Number of $HAM tokens per NFT

    // Events
    event OwnershipTransferred(address indexed oldOwner, address indexed newOwner);
    event NFTExchanged(address indexed user, uint256 indexed tokenId, uint256 hamAmount);

    // Constructor
    constructor(address _nftContract, address _hamToken, uint256 _exchangeRate) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        require(_hamToken != address(0), "Invalid $HAM token address");
        require(_exchangeRate > 0, "Exchange rate must be greater than zero");

        nftContract = IERC721(_nftContract);
        hamToken = IERC20(_hamToken);
        exchangeRate = _exchangeRate;
        owner = msg.sender;
    }

    // Modifier to restrict functions to only the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Function to transfer ownership
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @notice Exchange an NFT for $HAM tokens.
     * @param tokenId The ID of the NFT being exchanged.
     */
    function exchangeNFTForHam(uint256 tokenId) external {
        // Validate the sender owns the NFT
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own the specified NFT");

        // Transfer the NFT to the contract
        nftContract.transferFrom(msg.sender, address(this), tokenId);

        // Calculate the amount of $HAM tokens to transfer
        uint256 hamAmount = exchangeRate;

        // Validate the contract has enough $HAM tokens
        require(hamToken.balanceOf(address(this)) >= hamAmount, "Not enough $HAM tokens in contract");

        // Transfer $HAM tokens to the sender
        bool success = hamToken.transfer(msg.sender, hamAmount);
        require(success, "Failed to transfer $HAM tokens");

        // Emit the exchange event
        emit NFTExchanged(msg.sender, tokenId, hamAmount);
    }

    /**
     * @notice Withdraw all $HAM tokens from the contract (owner only).
     */
    function withdrawHamTokens() external onlyOwner {
        uint256 hamBalance = hamToken.balanceOf(address(this));
        require(hamBalance > 0, "No $HAM tokens to withdraw");

        bool success = hamToken.transfer(owner, hamBalance);
        require(success, "Failed to withdraw $HAM tokens");
    }

    /**
     * @notice Withdraw an NFT from the contract (owner only).
     * @param tokenId The ID of the NFT to withdraw.
     */
    function withdrawNFT(uint256 tokenId) external onlyOwner {
        require(nftContract.ownerOf(tokenId) == address(this), "Contract does not own the specified NFT");
        nftContract.transferFrom(address(this), owner, tokenId);
    }
}

// Interface for ERC-721 (NFT standard)
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
    function transferFrom(address from, address to, uint256 tokenId) external;
}

// Interface for ERC-20 ($HAM token standard)
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
