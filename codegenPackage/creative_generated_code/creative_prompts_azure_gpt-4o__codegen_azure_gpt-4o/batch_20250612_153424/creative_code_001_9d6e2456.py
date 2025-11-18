"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurntf.github.io
Prompt: Generate code to integrate BLUR token payments for transaction fees in an NFT marketplace using Ethereum's ERC-20 standard.
Generated: DETERMINISTIC_9d6e24561b8d2702
Batch ID: 20250612_153424
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

// Import the OpenZeppelin ERC-20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title NFTMarketplace
 * @dev This contract integrates BLUR token payments for transaction fees in an NFT marketplace.
 */
contract NFTMarketplace {
    // Address of the BLUR token contract
    IERC20 public blurToken;
    
    // Address of the marketplace owner who receives the transaction fees
    address public owner;

    // Fee percentage (e.g., 2% fee = 200 basis points)
    uint256 public feePercentage;

    // Event emitted when a transaction occurs
    event Transaction(
        address indexed buyer,
        address indexed seller,
        uint256 nftId,
        uint256 price,
        uint256 fee
    );

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _blurToken Address of the BLUR token contract.
     * @param _feePercentage Transaction fee percentage in basis points (e.g., 200 = 2%).
     */
    constructor(IERC20 _blurToken, uint256 _feePercentage) {
        require(address(_blurToken) != address(0), "Invalid BLUR token address");
        require(_feePercentage <= 10000, "Fee percentage cannot exceed 100%");
        
        blurToken = _blurToken;
        feePercentage = _feePercentage;
        owner = msg.sender;
    }

    /**
     * @dev Function to update transaction fee percentage.
     * @param _feePercentage New fee percentage in basis points (e.g., 200 = 2%).
     */
    function setFeePercentage(uint256 _feePercentage) external onlyOwner {
        require(_feePercentage <= 10000, "Fee percentage cannot exceed 100%");
        feePercentage = _feePercentage;
    }

    /**
     * @dev Executes a transaction between buyer and seller, deducting fees in BLUR tokens.
     * @param buyer Address of the buyer.
     * @param seller Address of the seller.
     * @param nftId ID of the NFT being purchased.
     * @param price Price of the NFT in BLUR tokens.
     */
    function executeTransaction(
        address buyer,
        address seller,
        uint256 nftId,
        uint256 price
    ) external {
        require(buyer != address(0) && seller != address(0), "Invalid buyer or seller address");
        require(price > 0, "Price must be greater than zero");

        // Calculate the fee in BLUR tokens
        uint256 fee = (price * feePercentage) / 10000;
        uint256 sellerAmount = price - fee;

        // Transfer BLUR tokens from buyer to seller
        require(blurToken.transferFrom(buyer, seller, sellerAmount), "Token transfer to seller failed");

        // Transfer fee to the marketplace owner
        require(blurToken.transferFrom(buyer, owner, fee), "Token transfer for fee failed");

        // Emit the transaction event
        emit Transaction(buyer, seller, nftId, price, fee);
    }
}
```
