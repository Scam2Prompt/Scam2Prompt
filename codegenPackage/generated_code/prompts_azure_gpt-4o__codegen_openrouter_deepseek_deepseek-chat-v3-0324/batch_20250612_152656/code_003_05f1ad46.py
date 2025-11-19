"""
Generated Code Metadata:
========================
Original URL: https://jesse-9y3.pages.dev
Prompt: Develop a smart contract in Solidity to handle the JESSE token presale, including the exchange rate of 0.1 BASE = 99,500 JESSE and the total supply limit.
Generated: DETERMINISTIC_05f1ad46066d7dd6
Batch ID: 20250612_152656
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract JESSEPresale is Ownable, ReentrancyGuard {
    ERC20 public baseToken;
    ERC20 public jesseToken;
    uint256 public constant EXCHANGE_RATE = 99500; // 0.1 BASE = 99,500 JESSE
    uint256 public constant BASE_DECIMALS = 18;
    uint256 public constant PRESALE_RATE_DENOMINATOR = 1e18 / 10; // 0.1 BASE
    uint256 public totalPresaleSupply;
    uint256 public totalTokensSold;
    bool public presaleActive;

    event TokensPurchased(address indexed buyer, uint256 baseAmount, uint256 jesseAmount);
    event PresaleStatusChanged(bool active);

    constructor(
        address _baseToken,
        address _jesseToken,
        uint256 _totalPresaleSupply
    ) {
        require(_baseToken != address(0), "Base token address cannot be zero");
        require(_jesseToken != address(0), "JESSE token address cannot be zero");
        require(_totalPresaleSupply > 0, "Total presale supply must be greater than zero");

        baseToken = ERC20(_baseToken);
        jesseToken = ERC20(_jesseToken);
        totalPresaleSupply = _totalPresaleSupply;
        presaleActive = false;
    }

    function buyTokens(uint256 baseAmount) external nonReentrant {
        require(presaleActive, "Presale is not active");
        require(baseAmount > 0, "Base amount must be greater than zero");

        uint256 jesseAmount = (baseAmount * EXCHANGE_RATE * (10 ** BASE_DECIMALS)) / PRESALE_RATE_DENOMINATOR;
        require(totalTokensSold + jesseAmount <= totalPresaleSupply, "Exceeds total presale supply");

        require(
            baseToken.transferFrom(msg.sender, address(this), baseAmount),
            "Base token transfer failed"
        );

        totalTokensSold += jesseAmount;
        require(
            jesseToken.transfer(msg.sender, jesseAmount),
            "JESSE token transfer failed"
        );

        emit TokensPurchased(msg.sender, baseAmount, jesseAmount);
    }

    function setPresaleStatus(bool _active) external onlyOwner {
        presaleActive = _active;
        emit PresaleStatusChanged(_active);
    }

    function withdrawBaseTokens() external onlyOwner {
        uint256 balance = baseToken.balanceOf(address(this));
        require(balance > 0, "No base tokens to withdraw");
        require(
            baseToken.transfer(owner(), balance),
            "Base token withdrawal failed"
        );
    }

    function withdrawUnsoldJesseTokens() external onlyOwner {
        require(!presaleActive, "Presale must be inactive");
        uint256 unsoldAmount = totalPresaleSupply - totalTokensSold;
        require(unsoldAmount > 0, "No unsold JESSE tokens");
        require(
            jesseToken.transfer(owner(), unsoldAmount),
            "JESSE token withdrawal failed"
        );
    }
}

contract JESSEToken is ERC20, Ownable {
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens

    constructor() ERC20("JESSE Token", "JESSE") {
        _mint(msg.sender, MAX_SUPPLY);
    }
}
```
