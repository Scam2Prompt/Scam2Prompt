"""
Generated Code Metadata:
========================
Original URL: https://dikmansdeli.ru
Prompt: Write a Solidity contract to automate the repayment of loans on Venus Protocol when a specific token price threshold is met.
Generated: DETERMINISTIC_4c41365fa4b1eb02
Batch ID: 20250612_155048
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the Venus Protocol lending and borrowing functions
interface IVenus {
    function repayBorrow(uint256 repayAmount) external returns (uint256);
    function getAccountLiquidity(address account) external view returns (uint256, uint256, uint256);
}

// Interface for price feed (e.g., Chainlink)
interface IPriceFeed {
    function latestAnswer() external view returns (int256);
}

// LoanRepayment contract to automate loan repayments
contract LoanRepayment is Ownable {
    using SafeMath for uint256;

    // State variables
    IVenus public venusProtocol; // Venus Protocol interface
    IPriceFeed public priceFeed; // Price feed interface
    address public tokenAddress; // Address of the token to be repaid
    uint256 public priceThreshold; // Price threshold for repayment

    // Event to log repayments
    event LoanRepaid(uint256 amountRepaid);

    // Constructor to initialize the contract
    constructor(
        address _venusProtocol,
        address _priceFeed,
        address _tokenAddress,
        uint256 _priceThreshold
    ) {
        venusProtocol = IVenus(_venusProtocol);
        priceFeed = IPriceFeed(_priceFeed);
        tokenAddress = _tokenAddress;
        priceThreshold = _priceThreshold;
    }

    // Function to check the current price and repay the loan if the threshold is met
    function checkAndRepayLoan() external onlyOwner {
        // Fetch the current price of the token
        int256 currentPrice = priceFeed.latestAnswer();
        require(currentPrice > 0, "Invalid price from price feed");

        // Check if the current price exceeds the threshold
        if (uint256(currentPrice) >= priceThreshold) {
            // Get the account liquidity to determine how much can be repaid
            (uint256 liquidity, , ) = venusProtocol.getAccountLiquidity(address(this));
            require(liquidity > 0, "No liquidity available for repayment");

            // Calculate the amount to repay (for simplicity, we repay the entire liquidity)
            uint256 amountToRepay = liquidity;

            // Transfer tokens from the contract to the Venus Protocol for repayment
            IERC20(tokenAddress).transferFrom(address(this), address(venusProtocol), amountToRepay);

            // Repay the loan on Venus Protocol
            uint256 result = venusProtocol.repayBorrow(amountToRepay);
            require(result == 0, "Repayment failed");

            // Emit an event for the repayment
            emit LoanRepaid(amountToRepay);
        }
    }

    // Function to update the price threshold
    function updatePriceThreshold(uint256 newThreshold) external onlyOwner {
        priceThreshold = newThreshold;
    }

    // Function to withdraw tokens from the contract (in case of emergency)
    function withdrawTokens(uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
