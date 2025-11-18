"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sealanapresales.pages.dev
Prompt: Write a Solidity smart contract to facilitate the presale of $SEAL tokens, incorporating multi-token payment options (ETH, SOL, USDT, USDC) as described on the Sealana Presale site.
Generated: DETERMINISTIC_b2ace3bd68ce1ef7
Batch ID: 20250612_151531
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

// Contract for the presale of $SEAL tokens
contract SealPresale is Ownable {
    // State variables
    IERC20 public sealToken; // The $SEAL token contract
    uint256 public presaleStart; // Presale start time
    uint256 public presaleEnd; // Presale end time
    uint256 public tokenPrice; // Price of $SEAL in terms of payment token

    // Supported payment token addresses
    address public ethToken = address(0); // ETH represented as address(0)
    address public usdtToken;
    address public usdcToken;
    address public solToken; // Placeholder for SOL (requires a wrapping mechanism)

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, address paymentToken);

    // Modifier to check presale timing
    modifier onlyDuringPresale() {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        _;
    }

    // Constructor to initialize the contract
    constructor(
        address _sealToken,
        address _usdtToken,
        address _usdcToken,
        uint256 _presaleStart,
        uint256 _presaleEnd,
        uint256 _tokenPrice
    ) {
        require(_sealToken != address(0), "Invalid $SEAL token address");
        require(_usdtToken != address(0), "Invalid USDT token address");
        require(_usdcToken != address(0), "Invalid USDC token address");
        require(_presaleStart < _presaleEnd, "Invalid presale timing");

        sealToken = IERC20(_sealToken);
        usdtToken = _usdtToken;
        usdcToken = _usdcToken;
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        tokenPrice = _tokenPrice;
    }

    // Function to buy $SEAL tokens with specified payment token
    function buyTokens(uint256 amount, address paymentToken) external payable onlyDuringPresale {
        require(amount > 0, "Amount must be greater than 0");
        
        uint256 totalCost = amount * tokenPrice;
        
        // Check which payment method is used and handle accordingly
        if (paymentToken == ethToken) {
            require(msg.value == totalCost, "Incorrect ETH amount sent");
        } else if (paymentToken == usdtToken || paymentToken == usdcToken) {
            IERC20(paymentToken).transferFrom(msg.sender, address(this), totalCost);
        } else {
            revert("Unsupported payment token");
        }
        
        // Transfer the requested amount of $SEAL tokens to the buyer
        sealToken.transfer(msg.sender, amount);
        
        emit TokensPurchased(msg.sender, amount, paymentToken);
    }

    // Function to withdraw collected funds (only callable by the owner)
    function withdrawFunds(address token) external onlyOwner {
        require(token == usdtToken || token == usdcToken, "Invalid token for withdrawal");
        
        uint256 balance = IERC20(token).balanceOf(address(this));
        require(balance > 0, "No funds to withdraw");
        
        IERC20(token).transfer(owner(), balance);
    }

    // Function to withdraw ETH (only callable by the owner)
    function withdrawETH() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
