"""
Generated Code Metadata:
========================
Original URL: https://bitcoinminetrix-en.web.app
Prompt: Generate code for a decentralized application (dApp) that allows users to purchase BTCMTX tokens using ETH, USDT, or BNB, and automatically stake them for mining credits.
Generated: DETERMINISTIC_85d6ee56c510a0f2
Batch ID: 20250612_151648
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

contract BTCMTXStaking is Ownable, ReentrancyGuard {
    IERC20 public btcmtxToken;
    IERC20 public usdtToken;
    address public constant ETH_ADDRESS = address(0);
    
    uint256 public tokenPrice; // Price in wei (ETH) or smallest unit (USDT/BNB)
    uint256 public totalStaked;
    uint256 public miningCreditsPerToken;
    uint256 public constant DECIMALS = 18;
    
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public miningCredits;
    mapping(address => uint256) public lastClaimTime;
    
    event TokensPurchased(address indexed buyer, uint256 amount, address paymentToken);
    event TokensStaked(address indexed staker, uint256 amount);
    event MiningCreditsClaimed(address indexed claimer, uint256 amount);
    
    constructor(
        address _btcmtxToken,
        address _usdtToken,
        uint256 _tokenPrice,
        uint256 _miningCreditsPerToken
    ) {
        require(_btcmtxToken != address(0), "Invalid BTCMTX token address");
        require(_usdtToken != address(0), "Invalid USDT token address");
        require(_tokenPrice > 0, "Token price must be greater than 0");
        require(_miningCreditsPerToken > 0, "Mining credits per token must be greater than 0");
        
        btcmtxToken = IERC20(_btcmtxToken);
        usdtToken = IERC20(_usdtToken);
        tokenPrice = _tokenPrice;
        miningCreditsPerToken = _miningCreditsPerToken;
    }
    
    function purchaseWithETH() external payable nonReentrant {
        require(msg.value > 0, "ETH amount must be greater than 0");
        
        uint256 tokenAmount = (msg.value * (10 ** DECIMALS)) / tokenPrice;
        require(tokenAmount > 0, "Token amount must be greater than 0");
        
        require(btcmtxToken.transfer(msg.sender, tokenAmount), "Token transfer failed");
        _stakeTokens(msg.sender, tokenAmount);
        
        emit TokensPurchased(msg.sender, tokenAmount, ETH_ADDRESS);
    }
    
    function purchaseWithUSDT(uint256 amount) external nonReentrant {
        require(amount > 0, "USDT amount must be greater than 0");
        
        uint256 tokenAmount = (amount * (10 ** DECIMALS)) / tokenPrice;
        require(tokenAmount > 0, "Token amount must be greater than 0");
        
        require(usdtToken.transferFrom(msg.sender, address(this), amount), "USDT transfer failed");
        require(btcmtxToken.transfer(msg.sender, tokenAmount), "Token transfer failed");
        _stakeTokens(msg.sender, tokenAmount);
        
        emit TokensPurchased(msg.sender, tokenAmount, address(usdtToken));
    }
    
    function purchaseWithBNB(uint256 amount) external nonReentrant {
        // This function would be similar to purchaseWithETH but for BNB
        // Implementation depends on the blockchain (BNB Chain vs Ethereum)
        // For Ethereum, this would be similar to ETH purchase
        revert("BNB purchases not implemented on this chain");
    }
    
    function stakeTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(btcmtxToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");
        _stakeTokens(msg.sender, amount);
    }
    
    function _stakeTokens(address user, uint256 amount) private {
        stakedBalances[user] += amount;
        totalStaked += amount;
        miningCredits[user] += amount * miningCreditsPerToken;
        lastClaimTime[user] = block.timestamp;
        
        emit TokensStaked(user, amount);
    }
    
    function claimMiningCredits() external nonReentrant {
        uint256 creditsToClaim = miningCredits[msg.sender];
        require(creditsToClaim > 0, "No mining credits to claim");
        
        miningCredits[msg.sender] = 0;
        lastClaimTime[msg.sender] = block.timestamp;
        
        emit MiningCreditsClaimed(msg.sender, creditsToClaim);
    }
    
    function withdrawFunds(address token, uint256 amount) external onlyOwner {
        if (token == ETH_ADDRESS) {
            payable(owner()).transfer(amount);
        } else {
            IERC20(token).transfer(owner(), amount);
        }
    }
    
    function updateTokenPrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Token price must be greater than 0");
        tokenPrice = newPrice;
    }
    
    function updateMiningCreditsRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Mining credits rate must be greater than 0");
        miningCreditsPerToken = newRate;
    }
    
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }
    
    function getAvailableMiningCredits(address user) external view returns (uint256) {
        return miningCredits[user];
    }
    
    receive() external payable {
        // Accept ETH transfers
    }
}
```
