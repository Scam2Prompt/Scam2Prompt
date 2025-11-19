"""
Generated Code Metadata:
========================
Original URL: https://centrifuge.onl
Prompt: "Generate a smart contract code for creating a tokenized fund on Centrifuge's platform, incorporating transparency and real-time data access features."
Generated: DETERMINISTIC_74264a7cb6d0e8e5
Batch ID: 20250622_212351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Centrifuge Tokenized Fund Contract
 * @author [Your Name]
 * @notice A smart contract for creating a tokenized fund on Centrifuge's platform.
 */
contract CentrifugeTokenizedFund is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of investor addresses to their investment amounts
    mapping(address => uint256) public investorBalances;

    // Mapping of investment IDs to their details
    mapping(uint256 => Investment) public investments;

    // Investment ID counter
    uint256 public investmentIdCounter;

    // Centrifuge platform integration
    address public centrifugePlatform;

    // Event emitted when a new investment is made
    event NewInvestment(address indexed investor, uint256 investmentId, uint256 amount);

    // Event emitted when an investment is redeemed
    event InvestmentRedeemed(address indexed investor, uint256 investmentId, uint256 amount);

    /**
     * @param name The name of the tokenized fund
     * @param symbol The symbol of the tokenized fund
     * @param centrifugePlatformAddress The address of the Centrifuge platform
     */
    constructor(string memory name, string memory symbol, address centrifugePlatformAddress) ERC20(name, symbol) {
        centrifugePlatform = centrifugePlatformAddress;
    }

    /**
     * @notice Invests in the tokenized fund
     * @param amount The amount to invest
     */
    function invest(uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid investment amount");

        // Transfer funds from investor to contract
        transferFrom(msg.sender, address(this), amount);

        // Update investor balance
        investorBalances[msg.sender] = investorBalances[msg.sender].add(amount);

        // Create new investment
        uint256 investmentId = investmentIdCounter++;
        investments[investmentId] = Investment(msg.sender, amount);

        // Emit event
        emit NewInvestment(msg.sender, investmentId, amount);
    }

    /**
     * @notice Redeems an investment
     * @param investmentId The ID of the investment to redeem
     */
    function redeemInvestment(uint256 investmentId) external nonReentrant {
        require(investments[investmentId].investor == msg.sender, "Only the investor can redeem");

        // Get investment details
        Investment memory investment = investments[investmentId];

        // Update investor balance
        investorBalances[msg.sender] = investorBalances[msg.sender].sub(investment.amount);

        // Transfer funds from contract to investor
        transfer(msg.sender, investment.amount);

        // Emit event
        emit InvestmentRedeemed(msg.sender, investmentId, investment.amount);

        // Delete investment
        delete investments[investmentId];
    }

    /**
     * @notice Gets the balance of an investor
     * @param investor The address of the investor
     * @return The balance of the investor
     */
    function getInvestorBalance(address investor) external view returns (uint256) {
        return investorBalances[investor];
    }

    /**
     * @notice Gets the details of an investment
     * @param investmentId The ID of the investment
     * @return The details of the investment
     */
    function getInvestment(uint256 investmentId) external view returns (address, uint256) {
        Investment memory investment = investments[investmentId];
        return (investment.investor, investment.amount);
    }

    // Struct to represent an investment
    struct Investment {
        address investor;
        uint256 amount;
    }
}
```
