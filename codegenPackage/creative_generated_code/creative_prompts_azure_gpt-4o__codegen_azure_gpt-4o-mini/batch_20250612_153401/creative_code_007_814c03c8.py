"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etfswap-in.pages.dev
Prompt: Create a Solidity contract for token presale management, including bonus calculations (e.g., "ETFS18" promo) and token distribution, as described in ETFSwap's presale stage.
Generated: DETERMINISTIC_814c03c8918f7b2a
Batch ID: 20250612_153401
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

// Interface for the token to be sold
interface IToken is IERC20 {
    function mint(address to, uint256 amount) external;
}

// Presale contract for token distribution
contract TokenPresale is Ownable {
    // State variables
    IToken public token; // The token being sold
    uint256 public presaleStart; // Start time of presale
    uint256 public presaleEnd; // End time of presale
    uint256 public tokenPrice; // Price per token in wei
    uint256 public bonusRate; // Bonus tokens for promo "ETFS18"
    address public treasury; // Address to collect funds

    // Mapping to track contributions
    mapping(address => uint256) public contributions;

    // Events for logging
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 tokensReceived);
    event PresaleStarted(uint256 start, uint256 end);
    event PresaleEnded();

    // Modifiers
    modifier onlyDuringPresale() {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        _;
    }

    // Constructor to initialize the presale
    constructor(IToken _token, uint256 _tokenPrice, uint256 _bonusRate, address _treasury) {
        token = _token;
        tokenPrice = _tokenPrice;
        bonusRate = _bonusRate;
        treasury = _treasury;
    }

    // Start the presale
    function startPresale(uint256 durationInDays) external onlyOwner {
        presaleStart = block.timestamp;
        presaleEnd = block.timestamp + (durationInDays * 1 days);
        emit PresaleStarted(presaleStart, presaleEnd);
    }

    // Buy tokens during the presale
    function buyTokens() external payable onlyDuringPresale {
        require(msg.value > 0, "Send ETH to purchase tokens");

        // Calculate amount of tokens to be minted
        uint256 tokensToMint = (msg.value / tokenPrice) * (1 + bonusRate / 100);
        contributions[msg.sender] += msg.value;

        // Mint tokens and transfer to buyer
        token.mint(msg.sender, tokensToMint);
        
        // Emit event for logging
        emit TokensPurchased(msg.sender, msg.value, tokensToMint);
    }

    // Withdraw funds to the treasury
    function withdrawFunds() external onlyOwner {
        require(address(this).balance > 0, "No funds to withdraw");

        payable(treasury).transfer(address(this).balance);
    }

    // End the presale
    function endPresale() external onlyOwner {
        require(block.timestamp >= presaleEnd, "Presale not yet ended");
        emit PresaleEnded();
    }

    // Fallback function to prevent accidental ether transfers
    receive() external payable {
        revert("Direct ETH transfer not allowed, use buyTokens() instead");
    }
}
```
