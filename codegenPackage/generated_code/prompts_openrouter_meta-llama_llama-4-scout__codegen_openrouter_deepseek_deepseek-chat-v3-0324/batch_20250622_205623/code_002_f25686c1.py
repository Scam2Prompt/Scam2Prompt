"""
Generated Code Metadata:
========================
Original URL: https://claim-brc20.pages.dev
Prompt: Generate a smart contract code in Solidity for a token sale similar to BRC-20 DEX public sale, accepting multiple currencies like ETH, BSC, BUSD, and USDT.
Generated: DETERMINISTIC_f25686c1452502a8
Batch ID: 20250622_205623
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract TokenSale is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token being sold
    IERC20 public saleToken;

    // Sale parameters
    uint256 public saleStartTime;
    uint256 public saleEndTime;
    uint256 public tokenPrice; // Price per token in wei or equivalent for stablecoins
    uint256 public minPurchase;
    uint256 public maxPurchase;
    uint256 public totalTokensForSale;
    uint256 public tokensSold;

    // Accepted payment tokens
    address public constant ETH = address(0);
    address public BSC;
    address public BUSD;
    address public USDT;

    // Token to USD rate (1 token = X USD)
    mapping(address => uint256) public tokenToUsdRate;

    // Whitelist
    mapping(address => bool) public whitelist;
    bool public whitelistEnabled;

    // User contributions
    mapping(address => uint256) public contributions;

    // Events
    event TokensPurchased(address indexed purchaser, address indexed paymentToken, uint256 amount, uint256 tokens);
    event SaleExtended(uint256 newEndTime);
    event WhitelistUpdated(address[] addresses, bool status);
    event TokensWithdrawn(address indexed owner, uint256 amount);
    event FundsWithdrawn(address indexed owner, address indexed token, uint256 amount);

    constructor(
        address _saleToken,
        uint256 _saleStartTime,
        uint256 _saleEndTime,
        uint256 _tokenPrice,
        uint256 _minPurchase,
        uint256 _maxPurchase,
        uint256 _totalTokensForSale,
        address _bsc,
        address _busd,
        address _usdt,
        uint256 _bscRate,
        uint256 _busdRate,
        uint256 _usdtRate
    ) {
        require(_saleToken != address(0), "TokenSale: invalid token address");
        require(_saleEndTime > _saleStartTime, "TokenSale: invalid sale period");
        require(_tokenPrice > 0, "TokenSale: token price must be > 0");
        require(_minPurchase > 0, "TokenSale: min purchase must be > 0");
        require(_maxPurchase > _minPurchase, "TokenSale: max purchase must be > min");
        require(_totalTokensForSale > 0, "TokenSale: total tokens must be > 0");

        saleToken = IERC20(_saleToken);
        saleStartTime = _saleStartTime;
        saleEndTime = _saleEndTime;
        tokenPrice = _tokenPrice;
        minPurchase = _minPurchase;
        maxPurchase = _maxPurchase;
        totalTokensForSale = _totalTokensForSale;

        BSC = _bsc;
        BUSD = _busd;
        USDT = _usdt;

        tokenToUsdRate[BSC] = _bscRate;
        tokenToUsdRate[BUSD] = _busdRate;
        tokenToUsdRate[USDT] = _usdtRate;
    }

    modifier whenSaleActive() {
        require(block.timestamp >= saleStartTime && block.timestamp <= saleEndTime, "TokenSale: sale not active");
        _;
    }

    modifier whenSaleEnded() {
        require(block.timestamp > saleEndTime, "TokenSale: sale not ended");
        _;
    }

    function buyWithETH() external payable nonReentrant whenSaleActive {
        require(!whitelistEnabled || whitelist[msg.sender], "TokenSale: not whitelisted");
        uint256 amount = msg.value;
        _buyTokens(ETH, amount);
    }

    function buyWithToken(address paymentToken, uint256 amount) external nonReentrant whenSaleActive {
        require(!whitelistEnabled || whitelist[msg.sender], "TokenSale: not whitelisted");
        require(paymentToken == BSC || paymentToken == BUSD || paymentToken == USDT, "TokenSale: invalid payment token");
        
        IERC20(paymentToken).transferFrom(msg.sender, address(this), amount);
        _buyTokens(paymentToken, amount);
    }

    function _buyTokens(address paymentToken, uint256 amount) private {
        require(amount >= minPurchase, "TokenSale: amount below minimum");
        
        uint256 usdAmount = paymentToken == ETH ? 
            amount.mul(1e18).div(tokenPrice) : 
            amount.mul(tokenToUsdRate[paymentToken]).div(tokenPrice);
        
        uint256 tokens = usdAmount;
        require(tokens > 0, "TokenSale: insufficient payment");
        require(tokensSold.add(tokens) <= totalTokensForSale, "TokenSale: insufficient tokens remaining");
        require(contributions[msg.sender].add(tokens) <= maxPurchase, "TokenSale: exceeds max purchase");

        contributions[msg.sender] = contributions[msg.sender].add(tokens);
        tokensSold = tokensSold.add(tokens);

        saleToken.transfer(msg.sender, tokens);
        emit TokensPurchased(msg.sender, paymentToken, amount, tokens);
    }

    function extendSale(uint256 newEndTime) external onlyOwner {
        require(newEndTime > saleEndTime, "TokenSale: new end time must be later");
        saleEndTime = newEndTime;
        emit SaleExtended(newEndTime);
    }

    function setWhitelist(address[] calldata addresses, bool status) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            whitelist[addresses[i]] = status;
        }
        emit WhitelistUpdated(addresses, status);
    }

    function toggleWhitelist() external onlyOwner {
        whitelistEnabled = !whitelistEnabled;
    }

    function withdrawTokens() external onlyOwner whenSaleEnded {
        uint256 balance = saleToken.balanceOf(address(this));
        require(balance > 0, "TokenSale: no tokens to withdraw");
        saleToken.transfer(owner(), balance);
        emit TokensWithdrawn(owner(), balance);
    }

    function withdrawFunds(address token) external onlyOwner nonReentrant {
        uint256 balance;
        if (token == ETH) {
            balance = address(this).balance;
            payable(owner()).transfer(balance);
        } else {
            balance = IERC20(token).balanceOf(address(this));
            IERC20(token).transfer(owner(), balance);
        }
        emit FundsWithdrawn(owner(), token, balance);
    }

    function updateTokenRates(address token, uint256 rate) external onlyOwner {
        require(token == BSC || token == BUSD || token == USDT, "TokenSale: invalid token");
        tokenToUsdRate[token] = rate;
    }

    function remainingTokens() external view returns (uint256) {
        return totalTokensForSale.sub(tokensSold);
    }

    function getContribution(address user) external view returns (uint256) {
        return contributions[user];
    }

    function isWhitelisted(address user) external view returns (bool) {
        return whitelist[user];
    }
}
```
