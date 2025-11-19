"""
Generated Code Metadata:
========================
Original URL: https://etuktuk-io-web.pages.dev
Prompt: Write a smart contract in Solidity that enables users to purchase $TUK tokens using multiple cryptocurrencies like BNB, ETH, and USDT, as described in the eTukTuk presale process.
Generated: DETERMINISTIC_c7e753cf8c36f05c
Batch ID: 20250612_145837
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

contract TukTokenPresale is Ownable, ReentrancyGuard {
    IERC20 public tukToken;
    IERC20 public usdtToken;
    
    uint256 public tokenPriceInBNB;
    uint256 public tokenPriceInETH;
    uint256 public tokenPriceInUSDT;
    
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    
    uint256 public totalTokensSold;
    uint256 public totalRaisedBNB;
    uint256 public totalRaisedETH;
    uint256 public totalRaisedUSDT;
    
    mapping(address => uint256) public contributions;
    
    event TokensPurchased(
        address indexed buyer,
        uint256 amount,
        string currency,
        uint256 value
    );
    
    constructor(
        address _tukToken,
        address _usdtToken,
        uint256 _tokenPriceInBNB,
        uint256 _tokenPriceInETH,
        uint256 _tokenPriceInUSDT,
        uint256 _presaleDuration
    ) {
        tukToken = IERC20(_tukToken);
        usdtToken = IERC20(_usdtToken);
        
        tokenPriceInBNB = _tokenPriceInBNB;
        tokenPriceInETH = _tokenPriceInETH;
        tokenPriceInUSDT = _tokenPriceInUSDT;
        
        presaleStartTime = block.timestamp;
        presaleEndTime = block.timestamp + _presaleDuration;
    }
    
    function buyWithBNB() external payable nonReentrant {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        require(msg.value > 0, "BNB amount must be greater than 0");
        
        uint256 tokenAmount = (msg.value * 1e18) / tokenPriceInBNB;
        require(tukToken.balanceOf(address(this)) >= tokenAmount, "Not enough tokens in presale");
        
        tukToken.transfer(msg.sender, tokenAmount);
        
        totalTokensSold += tokenAmount;
        totalRaisedBNB += msg.value;
        contributions[msg.sender] += tokenAmount;
        
        emit TokensPurchased(msg.sender, tokenAmount, "BNB", msg.value);
    }
    
    function buyWithETH() external payable nonReentrant {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        require(msg.value > 0, "ETH amount must be greater than 0");
        
        uint256 tokenAmount = (msg.value * 1e18) / tokenPriceInETH;
        require(tukToken.balanceOf(address(this)) >= tokenAmount, "Not enough tokens in presale");
        
        tukToken.transfer(msg.sender, tokenAmount);
        
        totalTokensSold += tokenAmount;
        totalRaisedETH += msg.value;
        contributions[msg.sender] += tokenAmount;
        
        emit TokensPurchased(msg.sender, tokenAmount, "ETH", msg.value);
    }
    
    function buyWithUSDT(uint256 amount) external nonReentrant {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        require(amount > 0, "USDT amount must be greater than 0");
        
        uint256 tokenAmount = (amount * 1e18) / tokenPriceInUSDT;
        require(tukToken.balanceOf(address(this)) >= tokenAmount, "Not enough tokens in presale");
        
        usdtToken.transferFrom(msg.sender, address(this), amount);
        tukToken.transfer(msg.sender, tokenAmount);
        
        totalTokensSold += tokenAmount;
        totalRaisedUSDT += amount;
        contributions[msg.sender] += tokenAmount;
        
        emit TokensPurchased(msg.sender, tokenAmount, "USDT", amount);
    }
    
    function withdrawFunds() external onlyOwner {
        uint256 bnbBalance = address(this).balance;
        uint256 ethBalance = address(this).balance;
        uint256 usdtBalance = usdtToken.balanceOf(address(this));
        
        if (bnbBalance > 0) {
            payable(owner()).transfer(bnbBalance);
        }
        
        if (ethBalance > 0) {
            payable(owner()).transfer(ethBalance);
        }
        
        if (usdtBalance > 0) {
            usdtToken.transfer(owner(), usdtBalance);
        }
    }
    
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale has not ended yet");
        uint256 unsoldTokens = tukToken.balanceOf(address(this));
        tukToken.transfer(owner(), unsoldTokens);
    }
    
    function setTokenPriceInBNB(uint256 _newPrice) external onlyOwner {
        tokenPriceInBNB = _newPrice;
    }
    
    function setTokenPriceInETH(uint256 _newPrice) external onlyOwner {
        tokenPriceInETH = _newPrice;
    }
    
    function setTokenPriceInUSDT(uint256 _newPrice) external onlyOwner {
        tokenPriceInUSDT = _newPrice;
    }
    
    function extendPresale(uint256 _additionalTime) external onlyOwner {
        presaleEndTime += _additionalTime;
    }
    
    function getPresaleStatus() external view returns (bool) {
        return block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime;
    }
    
    function getRemainingTime() external view returns (uint256) {
        if (block.timestamp >= presaleEndTime) {
            return 0;
        }
        return presaleEndTime - block.timestamp;
    }
}
```
