"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cowswap-finance.medium.com
Prompt: Develop a smart contract that supports fair token launches, inspired by CowSwap's "Fair Sales" concept.
Generated: DETERMINISTIC_8bd312333bf812a1
Batch ID: 20250612_150858
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title FairToken
 * @dev A simple ERC20 token contract that supports fair token launches.
 */
contract FairToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Variables for managing the sale
    uint256 public saleStartTime;
    uint256 public saleEndTime;
    uint256 public tokenPrice; // in wei
    uint256 public tokensSold;
    uint256 public maxTokensForSale;

    // Events for logging
    event TokensPurchased(address indexed buyer, uint256 amount);
    event SaleStarted(uint256 startTime, uint256 endTime);
    event SaleEnded(uint256 endTime);

    // Modifier to check if the sale is active
    modifier saleActive() {
        require(block.timestamp >= saleStartTime && block.timestamp <= saleEndTime, "Sale is not active");
        _;
    }

    // Constructor to initialize the token
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _maxTokensForSale, uint256 _tokenPrice) 
        ERC20(name, symbol) {
        _mint(address(this), initialSupply);
        maxTokensForSale = _maxTokensForSale;
        tokenPrice = _tokenPrice;
    }

    /**
     * @dev Start the token sale
     * @param duration Duration of the sale in seconds
     */
    function startSale(uint256 duration) external onlyOwner {
        saleStartTime = block.timestamp;
        saleEndTime = block.timestamp.add(duration);
        emit SaleStarted(saleStartTime, saleEndTime);
    }

    /**
     * @dev Purchase tokens during the sale
     * @param amount Amount of tokens to purchase
     */
    function purchaseTokens(uint256 amount) external payable saleActive {
        require(amount > 0, "Amount should be greater than 0");
        require(msg.value >= amount.mul(tokenPrice), "Insufficient funds sent");
        require(tokensSold.add(amount) <= maxTokensForSale, "Not enough tokens left for sale");

        tokensSold = tokensSold.add(amount);
        _transfer(address(this), msg.sender, amount);

        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev End the sale
     */
    function endSale() external onlyOwner {
        require(block.timestamp > saleEndTime, "Sale is still active");
        saleEndTime = block.timestamp;
        emit SaleEnded(saleEndTime);
    }

    /**
     * @dev Withdraw collected Ether from the sale
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Transfer failed");
    }

    /**
     * @dev Fallback function to prevent Ether from being sent directly to the contract
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }

    /**
     * @dev Get the current price of the token in wei
     */
    function getTokenPrice() external view returns (uint256) {
        return tokenPrice;
    }
}
```
