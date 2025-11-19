"""
Generated Code Metadata:
========================
Original URL: https://crop-6qi.pages.dev
Prompt: Write a smart contract in Solidity for a cross-game, cross-chain decentralized player network's token sale, with a first-come-first-served allocation mechanism.
Generated: DETERMINISTIC_23f67c1a11b205cb
Batch ID: 20250622_210443
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title CrossChainTokenSale
 * @dev A smart contract for a cross-game, cross-chain decentralized player network's token sale
 * with a first-come-first-served allocation mechanism.
 */
contract CrossChainTokenSale is Ownable {
    using SafeMath for uint256;

    // The token being sold
    IERC20 public token;

    // Sale parameters
    uint256 public tokenPrice; // Price per token in wei
    uint256 public tokensAvailable; // Total tokens available for sale
    uint256 public tokensSold; // Total tokens sold
    uint256 public saleStart; // Sale start time
    uint256 public saleEnd; // Sale end time

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event SaleStarted(uint256 startTime, uint256 endTime);
    event SaleEnded(uint256 totalTokensSold);

    // Modifier to check if the sale is active
    modifier saleActive() {
        require(block.timestamp >= saleStart && block.timestamp <= saleEnd, "Sale is not active");
        _;
    }

    // Modifier to check if the sale has ended
    modifier saleEnded() {
        require(block.timestamp > saleEnd, "Sale is still active");
        _;
    }

    /**
     * @dev Constructor to initialize the token sale
     * @param _token Address of the token being sold
     * @param _tokenPrice Price per token in wei
     * @param _tokensAvailable Total tokens available for sale
     */
    constructor(IERC20 _token, uint256 _tokenPrice, uint256 _tokensAvailable) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_tokensAvailable > 0, "Tokens available must be greater than zero");

        token = _token;
        tokenPrice = _tokenPrice;
        tokensAvailable = _tokensAvailable;
    }

    /**
     * @dev Start the token sale
     * @param _duration Duration of the sale in seconds
     */
    function startSale(uint256 _duration) external onlyOwner {
        require(saleStart == 0, "Sale already started");
        saleStart = block.timestamp;
        saleEnd = saleStart.add(_duration);
        emit SaleStarted(saleStart, saleEnd);
    }

    /**
     * @dev Purchase tokens during the sale
     * @param _amount Amount of tokens to purchase
     */
    function purchaseTokens(uint256 _amount) external payable saleActive {
        require(_amount > 0, "Amount must be greater than zero");
        require(msg.value == _amount.mul(tokenPrice), "Incorrect Ether value sent");
        require(tokensSold.add(_amount) <= tokensAvailable, "Not enough tokens available");

        tokensSold = tokensSold.add(_amount);
        token.transfer(msg.sender, _amount);
        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev End the token sale and withdraw remaining tokens
     */
    function endSale() external onlyOwner saleEnded {
        uint256 remainingTokens = tokensAvailable.sub(tokensSold);
        if (remainingTokens > 0) {
            token.transfer(owner(), remainingTokens);
        }
        emit SaleEnded(tokensSold);
        saleStart = 0; // Reset sale parameters
        saleEnd = 0;
    }

    /**
     * @dev Withdraw Ether from the contract
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
