"""
Generated Code Metadata:
========================
Original URL: https://123-7bf.pages.dev
Prompt: How can I optimize the performance of a Web3 Dapp for buying and selling tokens, addressing issues like high gas fees, transaction delays, and liquidity challenges?
Generated: DETERMINISTIC_b1b4f2cca62c7e1b
Batch ID: 20250622_205836
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract OptimizedTokenExchange is Ownable, ReentrancyGuard {
    IERC20 public token;
    uint256 public minSwapAmount;
    uint256 public feePercentage; // Basis points (1/100th of a percent)
    uint256 public totalLiquidity;
    bool public isTradingEnabled;
    
    mapping(address => uint256) public liquidityProvided;
    mapping(address => uint256) public lastTransactionBlock;

    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);
    event TokensSold(address indexed seller, uint256 tokenAmount, uint256 ethAmount);
    event LiquidityAdded(address indexed provider, uint256 ethAmount, uint256 tokenAmount);
    event LiquidityRemoved(address indexed provider, uint256 ethAmount, uint256 tokenAmount);
    event TradingStatusChanged(bool status);

    constructor(IERC20 _token, uint256 _minSwapAmount, uint256 _feePercentage) {
        token = _token;
        minSwapAmount = _minSwapAmount;
        feePercentage = _feePercentage;
        isTradingEnabled = true;
    }

    modifier tradingEnabled() {
        require(isTradingEnabled, "Trading is currently disabled");
        _;
    }

    modifier noSameBlock(address user) {
        require(lastTransactionBlock[user] != block.number, "One transaction per block allowed");
        _;
        lastTransactionBlock[user] = block.number;
    }

    function setTradingStatus(bool _status) external onlyOwner {
        isTradingEnabled = _status;
        emit TradingStatusChanged(_status);
    }

    function updateFeePercentage(uint256 _feePercentage) external onlyOwner {
        require(_feePercentage <= 1000, "Fee cannot exceed 10%");
        feePercentage = _feePercentage;
    }

    function updateMinSwapAmount(uint256 _minSwapAmount) external onlyOwner {
        minSwapAmount = _minSwapAmount;
    }

    function getPrice(uint256 amount) public view returns (uint256) {
        require(totalLiquidity > 0, "No liquidity available");
        return (amount * address(this).balance) / totalLiquidity;
    }

    function addLiquidity(uint256 tokenAmount) external payable nonReentrant {
        require(msg.value > 0 && tokenAmount > 0, "Must provide both ETH and tokens");
        require(token.transferFrom(msg.sender, address(this), tokenAmount), "Token transfer failed");

        uint256 liquidityMinted;
        if (totalLiquidity == 0) {
            liquidityMinted = msg.value;
        } else {
            liquidityMinted = (msg.value * totalLiquidity) / address(this).balance;
        }

        liquidityProvided[msg.sender] += liquidityMinted;
        totalLiquidity += liquidityMinted;

        emit LiquidityAdded(msg.sender, msg.value, tokenAmount);
    }

    function removeLiquidity(uint256 liquidityAmount) external nonReentrant {
        require(liquidityAmount > 0, "Must withdraw more than 0");
        require(liquidityProvided[msg.sender] >= liquidityAmount, "Insufficient liquidity");

        uint256 ethAmount = (liquidityAmount * address(this).balance) / totalLiquidity;
        uint256 tokenAmount = (liquidityAmount * token.balanceOf(address(this))) / totalLiquidity;

        liquidityProvided[msg.sender] -= liquidityAmount;
        totalLiquidity -= liquidityAmount;

        (bool sent, ) = msg.sender.call{value: ethAmount}("");
        require(sent, "ETH transfer failed");
        require(token.transfer(msg.sender, tokenAmount), "Token transfer failed");

        emit LiquidityRemoved(msg.sender, ethAmount, tokenAmount);
    }

    function buyTokens() external payable tradingEnabled noSameBlock(msg.sender) nonReentrant {
        require(msg.value >= minSwapAmount, "Amount below minimum");
        require(totalLiquidity > 0, "No liquidity available");

        uint256 fee = (msg.value * feePercentage) / 10000;
        uint256 amountAfterFee = msg.value - fee;

        uint256 tokensToTransfer = (amountAfterFee * token.balanceOf(address(this))) / (address(this).balance - amountAfterFee);
        require(tokensToTransfer > 0, "Insufficient output amount");

        require(token.transfer(msg.sender, tokensToTransfer), "Token transfer failed");
        emit TokensPurchased(msg.sender, msg.value, tokensToTransfer);
    }

    function sellTokens(uint256 tokenAmount) external tradingEnabled noSameBlock(msg.sender) nonReentrant {
        require(tokenAmount >= minSwapAmount, "Amount below minimum");
        require(totalLiquidity > 0, "No liquidity available");

        uint256 ethToTransfer = (tokenAmount * address(this).balance) / (token.balanceOf(address(this)) + tokenAmount);
        require(ethToTransfer > 0, "Insufficient output amount");

        uint256 fee = (ethToTransfer * feePercentage) / 10000;
        uint256 amountAfterFee = ethToTransfer - fee;

        require(token.transferFrom(msg.sender, address(this), tokenAmount), "Token transfer failed");
        
        (bool sent, ) = msg.sender.call{value: amountAfterFee}("");
        require(sent, "ETH transfer failed");

        emit TokensSold(msg.sender, tokenAmount, amountAfterFee);
    }

    receive() external payable {
        // Accept ETH deposits
    }
}
```
