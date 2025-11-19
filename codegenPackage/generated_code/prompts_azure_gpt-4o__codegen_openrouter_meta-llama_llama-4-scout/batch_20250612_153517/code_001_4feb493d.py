"""
Generated Code Metadata:
========================
Original URL: https://babywif-io.pages.dev
Prompt: Generate a Solidity smart contract for a token presale that aligns with the tokenomics of Baby WIF ($BIF), including a 5% tax split into 1% liquidity pool, 2% marketing, and 2% development.
Generated: DETERMINISTIC_4feb493dcead7be3
Batch ID: 20250612_153517
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Baby WIF Presale Contract
 * @author [Your Name]
 * @notice Token presale contract for Baby WIF ($BIF) with 5% tax split into 1% liquidity pool, 2% marketing, and 2% development.
 */
contract BabyWIFPresale is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tax distribution
    uint256 public constant TAX_RATE = 5;
    uint256 public constant LIQUIDITY_TAX = 1;
    uint256 public constant MARKETING_TAX = 2;
    uint256 public constant DEVELOPMENT_TAX = 2;

    // Tax recipient addresses
    address public marketingRecipient;
    address public developmentRecipient;
    address public liquidityPool;

    // Presale settings
    uint256 public presaleStart;
    uint256 public presaleEnd;
    uint256 public presaleRate;
    bool public presaleActive;

    // Mapping of user contributions
    mapping(address => uint256) public userContributions;

    /**
     * @notice Constructor
     * @param _marketingRecipient Address to receive marketing tax
     * @param _developmentRecipient Address to receive development tax
     * @param _liquidityPool Address of the liquidity pool
     * @param _presaleRate Presale rate (1 $BIF = x wei)
     */
    constructor(
        address _marketingRecipient,
        address _developmentRecipient,
        address _liquidityPool,
        uint256 _presaleRate
    ) ERC20("Baby WIF", "BIF") {
        marketingRecipient = _marketingRecipient;
        developmentRecipient = _developmentRecipient;
        liquidityPool = _liquidityPool;
        presaleRate = _presaleRate;
        presaleActive = false;
    }

    /**
     * @notice Start presale
     * @param _presaleStart Presale start timestamp
     * @param _presaleEnd Presale end timestamp
     */
    function startPresale(uint256 _presaleStart, uint256 _presaleEnd) external onlyOwner {
        require(!presaleActive, "Presale already active");
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        presaleActive = true;
    }

    /**
     * @notice End presale
     */
    function endPresale() external onlyOwner {
        require(presaleActive, "Presale not active");
        presaleActive = false;
    }

    /**
     * @notice Buy tokens during presale
     * @param _amount Amount of wei to spend
     */
    function buyTokens(uint256 _amount) external nonReentrant {
        require(presaleActive, "Presale not active");
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale not in progress");
        require(_amount > 0, "Invalid amount");

        uint256 tokensToMint = _amount.mul(presaleRate);
        uint256 taxAmount = tokensToMint.mul(TAX_RATE).div(100);

        // Split tax
        uint256 liquidityTax = taxAmount.mul(LIQUIDITY_TAX).div(TAX_RATE);
        uint256 marketingTax = taxAmount.mul(MARKETING_TAX).div(TAX_RATE);
        uint256 developmentTax = taxAmount.mul(DEVELOPMENT_TAX).div(TAX_RATE);

        // Mint tokens
        _mint(msg.sender, tokensToMint.sub(taxAmount));
        _mint(marketingRecipient, marketingTax);
        _mint(developmentRecipient, developmentTax);
        _mint(liquidityPool, liquidityTax);

        // Update user contributions
        userContributions[msg.sender] = userContributions[msg.sender].add(_amount);
    }

    /**
     * @notice Burn tokens
     * @param _amount Amount of tokens to burn
     */
    function burn(uint256 _amount) public override {
        require(_amount > 0, "Invalid amount");
        _burn(msg.sender, _amount);
    }

    // OpenZeppelin's ERC20 _beforeTokenTransfer hook
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256[] memory ids
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, ids);
    }

    // OpenZeppelin's ERC20 _afterTokenTransfer hook
    function _afterTokenTransfer(
        address from,
        address to,
        uint256[] memory ids
    ) internal virtual override {
        super._afterTokenTransfer(from, to, ids);
    }
}
```
