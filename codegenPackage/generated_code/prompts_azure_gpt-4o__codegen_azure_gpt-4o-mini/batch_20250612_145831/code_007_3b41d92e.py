"""
Generated Code Metadata:
========================
Original URL: https://singularity-finance.pages.dev
Prompt: Create a Solidity contract for a compliant tokenized fund that ensures security, transparency, and liquidity for investors, based on Singularity Finance's tokenization framework.
Generated: DETERMINISTIC_3b41d92eb6cc26c4
Batch ID: 20250612_145831
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// TokenizedFund contract that implements a compliant tokenized fund
contract TokenizedFund is ERC20, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Fund structure to hold fund details
    struct Fund {
        string name;
        string description;
        uint256 totalInvestment;
        uint256 totalShares;
        bool isActive;
    }

    // Mapping of fund ID to Fund details
    mapping(uint256 => Fund) public funds;
    uint256 public fundCount;

    // Events for logging
    event FundCreated(uint256 indexed fundId, string name, string description);
    event InvestmentMade(uint256 indexed fundId, address indexed investor, uint256 amount);
    event FundClosed(uint256 indexed fundId);

    // Modifier to check if fund is active
    modifier onlyActiveFund(uint256 fundId) {
        require(funds[fundId].isActive, "Fund is not active");
        _;
    }

    // Constructor to initialize the token
    constructor() ERC20("TokenizedFundToken", "TFT") {}

    // Function to create a new fund
    function createFund(string memory name, string memory description) external onlyOwner {
        fundCount++;
        funds[fundCount] = Fund(name, description, 0, 0, true);
        emit FundCreated(fundCount, name, description);
    }

    // Function to invest in a fund
    function investInFund(uint256 fundId) external payable onlyActiveFund(fundId) nonReentrant {
        require(msg.value > 0, "Investment must be greater than 0");

        Fund storage fund = funds[fundId];
        fund.totalInvestment = fund.totalInvestment.add(msg.value);
        fund.totalShares = fund.totalShares.add(msg.value); // 1:1 share to investment ratio

        // Mint new tokens to the investor
        _mint(msg.sender, msg.value);
        
        emit InvestmentMade(fundId, msg.sender, msg.value);
    }

    // Function to close a fund
    function closeFund(uint256 fundId) external onlyOwner onlyActiveFund(fundId) {
        funds[fundId].isActive = false;
        emit FundClosed(fundId);
    }

    // Function to withdraw funds from the contract
    function withdraw(uint256 fundId) external onlyOwner onlyActiveFund(fundId) {
        Fund storage fund = funds[fundId];
        require(fund.totalInvestment > 0, "No funds to withdraw");

        uint256 amountToWithdraw = fund.totalInvestment;
        fund.totalInvestment = 0; // Reset investment to prevent re-entrancy

        // Transfer the funds to the owner
        payable(owner()).transfer(amountToWithdraw);
    }

    // Function to get fund details
    function getFundDetails(uint256 fundId) external view returns (string memory, string memory, uint256, uint256, bool) {
        Fund storage fund = funds[fundId];
        return (fund.name, fund.description, fund.totalInvestment, fund.totalShares, fund.isActive);
    }
}
```
