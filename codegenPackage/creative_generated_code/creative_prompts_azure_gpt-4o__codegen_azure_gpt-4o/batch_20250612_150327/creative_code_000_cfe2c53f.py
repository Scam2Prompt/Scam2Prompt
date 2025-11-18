"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect-v3-presale-boilerplate-website.pages.dev
Prompt: Write a smart contract in Solidity that mimics the functionality of the BOI Coin presale, including token purchase using USDT, ETH, and BNB, and tracking raised funds.
Generated: DETERMINISTIC_cfe2c53f0cfc0699
Batch ID: 20250612_150327
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

// Import OpenZeppelin's SafeERC20 and IERC20 for token interactions
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract BOICoinPresale is ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Address of BOI token
    IERC20 public immutable boiToken;

    // Address of USDT token
    IERC20 public immutable usdtToken;

    // Address of the contract owner
    address public owner;

    // Token price per BOI token (in wei for ETH/BNB, and in USDT decimals for USDT)
    uint256 public tokenPriceETH;
    uint256 public tokenPriceBNB;
    uint256 public tokenPriceUSDT;

    // Total funds raised (in wei for ETH/BNB, and in USDT decimals for USDT)
    uint256 public totalFundsRaisedETH;
    uint256 public totalFundsRaisedBNB;
    uint256 public totalFundsRaisedUSDT;

    // Event to log token purchases
    event TokensPurchased(
        address indexed buyer,
        uint256 amountBOI,
        uint256 amountPaid,
        string paymentMethod
    );

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to initialize contract and set token addresses
    constructor(
        address _boiToken,
        address _usdtToken,
        uint256 _tokenPriceETH,
        uint256 _tokenPriceBNB,
        uint256 _tokenPriceUSDT
    ) {
        require(_boiToken != address(0), "BOI token address cannot be zero");
        require(_usdtToken != address(0), "USDT token address cannot be zero");

        boiToken = IERC20(_boiToken);
        usdtToken = IERC20(_usdtToken);
        tokenPriceETH = _tokenPriceETH;
        tokenPriceBNB = _tokenPriceBNB;
        tokenPriceUSDT = _tokenPriceUSDT;
        owner = msg.sender;
    }

    // Function to purchase BOI tokens using ETH
    function buyWithETH() external payable nonReentrant {
        require(msg.value > 0, "Payment must be greater than 0");

        // Calculate the amount of BOI tokens to issue
        uint256 tokenAmount = (msg.value * 1e18) / tokenPriceETH;

        // Ensure the contract has enough BOI tokens to transfer
        require(
            boiToken.balanceOf(address(this)) >= tokenAmount,
            "Insufficient BOI token balance in contract"
        );

        // Increment raised funds
        totalFundsRaisedETH += msg.value;

        // Transfer BOI tokens to the buyer
        boiToken.safeTransfer(msg.sender, tokenAmount);

        // Emit an event
        emit TokensPurchased(msg.sender, tokenAmount, msg.value, "ETH");
    }

    // Function to purchase BOI tokens using USDT
    function buyWithUSDT(uint256 _usdtAmount) external nonReentrant {
        require(_usdtAmount > 0, "Payment must be greater than 0");

        // Calculate the amount of BOI tokens to issue
        uint256 tokenAmount = (_usdtAmount * 1e18) / tokenPriceUSDT;

        // Ensure the contract has enough BOI tokens to transfer
        require(
            boiToken.balanceOf(address(this)) >= tokenAmount,
            "Insufficient BOI token balance in contract"
        );

        // Increment raised funds
        totalFundsRaisedUSDT += _usdtAmount;

        // Transfer USDT tokens from the buyer to the contract
        usdtToken.safeTransferFrom(msg.sender, address(this), _usdtAmount);

        // Transfer BOI tokens to the buyer
        boiToken.safeTransfer(msg.sender, tokenAmount);

        // Emit an event
        emit TokensPurchased(msg.sender, tokenAmount, _usdtAmount, "USDT");
    }

    // Function to purchase BOI tokens using BNB (alias for buyWithETH)
    function buyWithBNB() external payable nonReentrant {
        require(msg.value > 0, "Payment must be greater than 0");

        // Calculate the amount of BOI tokens to issue
        uint256 tokenAmount = (msg.value * 1e18) / tokenPriceBNB;

        // Ensure the contract has enough BOI tokens to transfer
        require(
            boiToken.balanceOf(address(this)) >= tokenAmount,
            "Insufficient BOI token balance in contract"
        );

        // Increment raised funds
        totalFundsRaisedBNB += msg.value;

        // Transfer BOI tokens to the buyer
        boiToken.safeTransfer(msg.sender, tokenAmount);

        // Emit an event
        emit TokensPurchased(msg.sender, tokenAmount, msg.value, "BNB");
    }

    // Function to update token prices (owner-only)
    function setTokenPrices(
        uint256 _tokenPriceETH,
        uint256 _tokenPriceBNB,
        uint256 _tokenPriceUSDT
    ) external onlyOwner {
        tokenPriceETH = _tokenPriceETH;
        tokenPriceBNB = _tokenPriceBNB;
        tokenPriceUSDT = _tokenPriceUSDT;
    }

    // Function to withdraw raised funds (owner-only)
    function withdrawFunds() external onlyOwner {
        // Withdraw ETH/BNB balance
        if (address(this).balance > 0) {
            payable(owner).transfer(address(this).balance);
        }

        // Withdraw USDT balance
        uint256 usdtBalance = usdtToken.balanceOf(address(this));
        if (usdtBalance > 0) {
            usdtToken.safeTransfer(owner, usdtBalance);
        }
    }

    // Function to withdraw unsold BOI tokens (owner-only)
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 unsoldTokens = boiToken.balanceOf(address(this));
        if (unsoldTokens > 0) {
            boiToken.safeTransfer(owner, unsoldTokens);
        }
    }
}
```
