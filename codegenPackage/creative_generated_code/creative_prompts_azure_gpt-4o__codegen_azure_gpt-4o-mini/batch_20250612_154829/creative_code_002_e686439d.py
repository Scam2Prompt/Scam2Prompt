"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nextsophon.io
Prompt: Develop a smart contract in Solidity that allows users to purchase tokens during a presale, ensuring compatibility with EVM wallets and supporting multiple payment methods like USDT, ETH, and BNB.
Generated: DETERMINISTIC_e686439dbc2d9253
Batch ID: 20250612_154829
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Presale contract for purchasing tokens with multiple payment methods
contract TokenPresale is Ownable {
    using SafeMath for uint256;

    // Token to be sold in the presale
    IERC20 public token;

    // Addresses of accepted payment tokens
    IERC20 public usdt;
    IERC20 public bnb; // BNB will be represented as a native token

    // Presale parameters
    uint256 public price; // Price of one token in WEI
    uint256 public maxPurchase; // Maximum tokens that can be purchased in one transaction
    uint256 public startTime; // Presale start time
    uint256 public endTime; // Presale end time

    // Events for logging purchases
    event TokensPurchased(address indexed buyer, uint256 amount, string paymentMethod);

    // Modifier to check if the presale is active
    modifier onlyWhileOpen() {
        require(block.timestamp >= startTime && block.timestamp <= endTime, "Presale is not active");
        _;
    }

    // Constructor to initialize the contract with token and payment methods
    constructor(
        address _token,
        address _usdt,
        uint256 _price,
        uint256 _maxPurchase,
        uint256 _startTime,
        uint256 _endTime
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_usdt != address(0), "USDT address cannot be zero");
        require(_price > 0, "Price must be greater than zero");
        require(_maxPurchase > 0, "Max purchase must be greater than zero");
        require(_startTime < _endTime, "Start time must be before end time");

        token = IERC20(_token);
        usdt = IERC20(_usdt);
        price = _price;
        maxPurchase = _maxPurchase;
        startTime = _startTime;
        endTime = _endTime;
    }

    // Function to purchase tokens with USDT
    function buyWithUSDT(uint256 amount) external onlyWhileOpen {
        require(amount <= maxPurchase, "Exceeds max purchase limit");

        uint256 cost = amount.mul(price);
        require(usdt.transferFrom(msg.sender, address(this), cost), "USDT transfer failed");

        token.transfer(msg.sender, amount);
        emit TokensPurchased(msg.sender, amount, "USDT");
    }

    // Function to purchase tokens with ETH
    function buyWithETH(uint256 amount) external payable onlyWhileOpen {
        require(amount <= maxPurchase, "Exceeds max purchase limit");
        
        uint256 cost = amount.mul(price);
        require(msg.value == cost, "Incorrect ETH amount sent");

        token.transfer(msg.sender, amount);
        emit TokensPurchased(msg.sender, amount, "ETH");
    }

    // Function to purchase tokens with BNB
    function buyWithBNB(uint256 amount) external payable onlyWhileOpen {
        require(amount <= maxPurchase, "Exceeds max purchase limit");

        uint256 cost = amount.mul(price);
        require(msg.value == cost, "Incorrect BNB amount sent");

        token.transfer(msg.sender, amount);
        emit TokensPurchased(msg.sender, amount, "BNB");
    }

    // Function to withdraw tokens from the presale contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= token.balanceOf(address(this)), "Not enough tokens");
        token.transfer(msg.sender, amount);
    }

    // Function to withdraw collected payment tokens (only owner)
    function withdrawPayments() external onlyOwner {
        require(usdt.balanceOf(address(this)) > 0, "No payments to withdraw");
        uint256 usdtBalance = usdt.balanceOf(address(this));
        require(usdt.transfer(msg.sender, usdtBalance), "USDT withdrawal failed");

        // If ETH/BNB has been sent to the contract, pay out
        payable(msg.sender).transfer(address(this).balance);
    }
    
    // Function to set the presale parameters (only owner)
    function setPresaleParameters(
        uint256 _price,
        uint256 _maxPurchase,
        uint256 _startTime,
        uint256 _endTime
    ) external onlyOwner {
        require(_price > 0, "Price must be greater than zero");
        require(_maxPurchase > 0, "Max purchase must be greater than zero");
        require(_startTime < _endTime, "Start time must be before end time");

        price = _price;
        maxPurchase = _maxPurchase;
        startTime = _startTime;
        endTime = _endTime;
    }

    // Fallback function to receive BNB
    receive() external payable {}
}
```
