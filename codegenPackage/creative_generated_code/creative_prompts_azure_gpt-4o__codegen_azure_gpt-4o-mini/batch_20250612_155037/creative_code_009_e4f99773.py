"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakeflarre.com
Prompt: Generate a smart contract that demonstrates cross-chain NFT purchases on stakeflarre using tokens from another blockchain, leveraging both the FTSO and Data Connector protocols.
Generated: DETERMINISTIC_e4f997733d2b6dfb
Batch ID: 20250612_155037
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the FTSO protocol
interface IFTSO {
    function getLatestPrice() external view returns (uint256);
}

// Interface for the Data Connector protocol
interface IDataConnector {
    function getData(string calldata key) external view returns (uint256);
}

// Smart contract for cross-chain NFT purchases
contract CrossChainNFTMarket is Ownable {
    // Variables to store the NFT, token, and price feeds
    IERC721 public nftContract;  // The NFT contract
    IERC20 public paymentToken;   // The token used for purchases
    IFTSO public ftso;           // The FTSO price feed
    IDataConnector public dataConnector; // The data connector for off-chain data

    // Event emitted when an NFT is purchased
    event NFTPurchased(address indexed buyer, uint256 indexed tokenId, uint256 price);

    // Constructor to initialize contract parameters
    constructor(
        address _nftContract,
        address _paymentToken,
        address _ftso,
        address _dataConnector
    ) {
        nftContract = IERC721(_nftContract);
        paymentToken = IERC20(_paymentToken);
        ftso = IFTSO(_ftso);
        dataConnector = IDataConnector(_dataConnector);
    }

    // Function to purchase an NFT
    function purchaseNFT(uint256 tokenId) external {
        // Check if the NFT exists and is available for purchase
        require(nftContract.ownerOf(tokenId) != address(0), "NFT does not exist");

        // Get the latest price from FTSO
        uint256 price = ftso.getLatestPrice();
        require(price > 0, "Invalid price fetched");

        // Convert the price (assuming it’s in the base unit compatible with the payment token)
        uint256 priceInTokens = price; // Adjust conversion logic if necessary

        // Ensure buyer has enough tokens
        require(paymentToken.balanceOf(msg.sender) >= priceInTokens, "Insufficient token balance");
        
        // Transfer the tokens from buyer to the contract owner
        bool success = paymentToken.transferFrom(msg.sender, owner(), priceInTokens);
        require(success, "Token transfer failed");

        // Transfer the NFT to the buyer
        nftContract.safeTransferFrom(owner(), msg.sender, tokenId);
        
        // Emit an event for the purchase
        emit NFTPurchased(msg.sender, tokenId, priceInTokens);
    }
    
    // Function to withdraw tokens from the contract (for the owner only)
    function withdrawTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");
        
        uint256 contractBalance = paymentToken.balanceOf(address(this));
        require(amount <= contractBalance, "Insufficient contract balance");
        
        // Transfer tokens to the specified address
        bool success = paymentToken.transfer(to, amount);
        require(success, "Token withdrawal failed");
    }

    // Function to update FTSO address (onlyOwner)
    function updateFTSO(address newFTSO) external onlyOwner {
        require(newFTSO != address(0), "Invalid FTSO address");
        ftso = IFTSO(newFTSO);
    }

    // Function to update Data Connector address (onlyOwner)
    function updateDataConnector(address newDataConnector) external onlyOwner {
        require(newDataConnector != address(0), "Invalid Data Connector address");
        dataConnector = IDataConnector(newDataConnector);
    }
}
```
