"""
Generated Code Metadata:
========================
Original URL: https://claimcrudoprotocol.pages.dev
Prompt: Provide an example of a smart contract on Binance Smart Chain that facilitates transparent and secure transactions for crude oil investments, as emphasized in the Crudo Protocol ecosystem.
Generated: DETERMINISTIC_9bb67fa0e637ad6a
Batch ID: 20250612_151141
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

/**
 * @title CrudoOilInvestment
 * @dev A smart contract for transparent and secure crude oil investments on Binance Smart Chain
 */
contract CrudoOilInvestment is Ownable, ReentrancyGuard {
    // Struct to represent an investment
    struct Investment {
        address investor;
        uint256 amount;
        uint256 oilAmount; // Amount of oil barrels represented
        uint256 timestamp;
        bool isActive;
    }

    // Token used for investments (BUSD, USDT, etc.)
    IERC20 public paymentToken;

    // Current price of crude oil per barrel in payment token decimals
    uint256 public oilPricePerBarrel;

    // Total oil supply available for investment
    uint256 public totalOilSupply;

    // Total oil invested
    uint256 public totalOilInvested;

    // Mapping of investor to their investments
    mapping(address => Investment[]) public investments;

    // Events
    event InvestmentMade(
        address indexed investor,
        uint256 amount,
        uint256 oilAmount,
        uint256 timestamp
    );
    event InvestmentWithdrawn(
        address indexed investor,
        uint256 amount,
        uint256 oilAmount,
        uint256 timestamp
    );
    event OilPriceUpdated(uint256 newPrice, uint256 timestamp);
    event OilSupplyUpdated(uint256 newSupply, uint256 timestamp);

    /**
     * @dev Constructor
     * @param _paymentToken Address of the payment token (BUSD, USDT, etc.)
     * @param _initialOilPrice Initial price of oil per barrel
     * @param _initialOilSupply Initial oil supply available
     */
    constructor(
        address _paymentToken,
        uint256 _initialOilPrice,
        uint256 _initialOilSupply
    ) {
        require(_paymentToken != address(0), "Invalid payment token address");
        paymentToken = IERC20(_paymentToken);
        oilPricePerBarrel = _initialOilPrice;
        totalOilSupply = _initialOilSupply;
    }

    /**
     * @dev Invest in crude oil
     * @param amount Amount of payment token to invest
     */
    function invest(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(
            paymentToken.balanceOf(msg.sender) >= amount,
            "Insufficient token balance"
        );

        uint256 oilAmount = (amount * (10 ** 18)) / oilPricePerBarrel;
        require(
            totalOilInvested + oilAmount <= totalOilSupply,
            "Not enough oil supply"
        );

        // Transfer tokens from investor to contract
        require(
            paymentToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Create new investment
        Investment memory newInvestment = Investment({
            investor: msg.sender,
            amount: amount,
            oilAmount: oilAmount,
            timestamp: block.timestamp,
            isActive: true
        });

        investments[msg.sender].push(newInvestment);
        totalOilInvested += oilAmount;

        emit InvestmentMade(
            msg.sender,
            amount,
            oilAmount,
            block.timestamp
        );
    }

    /**
     * @dev Withdraw investment
     * @param investmentIndex Index of the investment to withdraw
     */
    function withdrawInvestment(uint256 investmentIndex) external nonReentrant {
        require(
            investmentIndex < investments[msg.sender].length,
            "Invalid investment index"
        );

        Investment storage investment = investments[msg.sender][investmentIndex];
        require(investment.isActive, "Investment already withdrawn");

        uint256 currentValue = (investment.oilAmount * oilPricePerBarrel) / (10 ** 18);
        
        // Mark investment as withdrawn
        investment.isActive = false;
        totalOilInvested -= investment.oilAmount;

        // Transfer tokens back to investor
        require(
            paymentToken.transfer(msg.sender, currentValue),
            "Token transfer failed"
        );

        emit InvestmentWithdrawn(
            msg.sender,
            currentValue,
            investment.oilAmount,
            block.timestamp
        );
    }

    /**
     * @dev Update oil price (only owner)
     * @param newPrice New price per barrel
     */
    function updateOilPrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Price must be greater than 0");
        oilPricePerBarrel = newPrice;
        emit OilPriceUpdated(newPrice, block.timestamp);
    }

    /**
     * @dev Update total oil supply (only owner)
     * @param newSupply New total oil supply
     */
    function updateOilSupply(uint256 newSupply) external onlyOwner {
        require(newSupply >= totalOilInvested, "Supply cannot be less than invested");
        totalOilSupply = newSupply;
        emit OilSupplyUpdated(newSupply, block.timestamp);
    }

    /**
     * @dev Get investor's active investments count
     * @param investor Address of the investor
     * @return count Number of active investments
     */
    function getActiveInvestmentsCount(address investor) external view returns (uint256) {
        uint256 count = 0;
        for (uint256 i = 0; i < investments[investor].length; i++) {
            if (investments[investor][i].isActive) {
                count++;
            }
        }
        return count;
    }

    /**
     * @dev Get total invested amount by an investor
     * @param investor Address of the investor
     * @return total Total invested amount
     */
    function getTotalInvested(address investor) external view returns (uint256) {
        uint256 total = 0;
        for (uint256 i = 0; i < investments[investor].length; i++) {
            if (investments[investor][i].isActive) {
                total += investments[investor][i].amount;
            }
        }
        return total;
    }
}
```
