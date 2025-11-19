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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract BabyWIF is ERC20, Ownable {
    using SafeMath for uint256;

    // Tax distribution percentages
    uint256 public constant LIQUIDITY_TAX = 1;
    uint256 public constant MARKETING_TAX = 2;
    uint256 public constant DEVELOPMENT_TAX = 2;
    uint256 public constant TOTAL_TAX = LIQUIDITY_TAX + MARKETING_TAX + DEVELOPMENT_TAX;

    // Addresses for tax distribution
    address public liquidityPoolAddress;
    address public marketingAddress;
    address public developmentAddress;

    // Presale parameters
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public presaleRate; // Tokens per ETH
    uint256 public presaleHardCap;
    uint256 public presaleTotalRaised;
    bool public presaleFinalized;

    // Mapping to track presale contributors
    mapping(address => uint256) public presaleContributions;

    // Events
    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);
    event PresaleFinalized(uint256 totalRaised);
    event TaxDistributed(uint256 liquidityAmount, uint256 marketingAmount, uint256 developmentAmount);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _presaleRate,
        uint256 _presaleHardCap,
        uint256 _presaleDuration,
        address _liquidityPoolAddress,
        address _marketingAddress,
        address _developmentAddress
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
        
        presaleRate = _presaleRate;
        presaleHardCap = _presaleHardCap;
        presaleStartTime = block.timestamp;
        presaleEndTime = block.timestamp.add(_presaleDuration);
        
        liquidityPoolAddress = _liquidityPoolAddress;
        marketingAddress = _marketingAddress;
        developmentAddress = _developmentAddress;
    }

    // Modifier to check if presale is active
    modifier isPresaleActive() {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        require(!presaleFinalized, "Presale has ended");
        _;
    }

    // Function to participate in presale
    function buyTokens() external payable isPresaleActive {
        require(msg.value > 0, "ETH amount must be greater than 0");
        require(presaleTotalRaised.add(msg.value) <= presaleHardCap, "Presale hard cap reached");

        uint256 tokenAmount = msg.value.mul(presaleRate);
        require(balanceOf(address(this)) >= tokenAmount, "Not enough tokens left in presale");

        presaleContributions[msg.sender] = presaleContributions[msg.sender].add(msg.value);
        presaleTotalRaised = presaleTotalRaised.add(msg.value);

        _transfer(address(this), msg.sender, tokenAmount);
        emit TokensPurchased(msg.sender, msg.value, tokenAmount);
    }

    // Function to finalize presale
    function finalizePresale() external onlyOwner {
        require(!presaleFinalized, "Presale already finalized");
        require(block.timestamp > presaleEndTime || presaleTotalRaised >= presaleHardCap, "Presale not ended yet");

        presaleFinalized = true;
        emit PresaleFinalized(presaleTotalRaised);
    }

    // Override transfer function to implement tax
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        if (sender == owner() || recipient == owner() || sender == address(this) || recipient == address(this)) {
            super._transfer(sender, recipient, amount);
        } else {
            uint256 taxAmount = amount.mul(TOTAL_TAX).div(100);
            uint256 transferAmount = amount.sub(taxAmount);

            // Distribute taxes
            uint256 liquidityAmount = amount.mul(LIQUIDITY_TAX).div(100);
            uint256 marketingAmount = amount.mul(MARKETING_TAX).div(100);
            uint256 developmentAmount = amount.mul(DEVELOPMENT_TAX).div(100);

            super._transfer(sender, liquidityPoolAddress, liquidityAmount);
            super._transfer(sender, marketingAddress, marketingAmount);
            super._transfer(sender, developmentAddress, developmentAmount);
            super._transfer(sender, recipient, transferAmount);

            emit TaxDistributed(liquidityAmount, marketingAmount, developmentAmount);
        }
    }

    // Function to withdraw remaining tokens after presale
    function withdrawRemainingTokens() external onlyOwner {
        require(presaleFinalized, "Presale not finalized yet");
        uint256 remainingBalance = balanceOf(address(this));
        _transfer(address(this), owner(), remainingBalance);
    }

    // Function to withdraw ETH funds
    function withdrawFunds() external onlyOwner {
        require(presaleFinalized, "Presale not finalized yet");
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = payable(owner()).call{value: balance}("");
        require(success, "Transfer failed");
    }

    // Function to update tax addresses
    function updateTaxAddresses(
        address _liquidityPoolAddress,
        address _marketingAddress,
        address _developmentAddress
    ) external onlyOwner {
        require(_liquidityPoolAddress != address(0), "Invalid liquidity address");
        require(_marketingAddress != address(0), "Invalid marketing address");
        require(_developmentAddress != address(0), "Invalid development address");

        liquidityPoolAddress = _liquidityPoolAddress;
        marketingAddress = _marketingAddress;
        developmentAddress = _developmentAddress;
    }
}
```
