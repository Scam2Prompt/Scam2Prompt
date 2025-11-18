"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dikmansdeli.ru
Prompt: Write a Solidity contract to automate the repayment of loans on Venus Protocol when a specific token price threshold is met.
Generated: DETERMINISTIC_4c41365fa4b1eb02
Batch ID: 20250612_155048
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

// Import necessary interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IVenus {
    function repayBorrow(uint repayAmount) external returns (uint);
    function getAccountLiquidity(address account) external view returns (uint, uint, uint);
}

interface IPriceOracle {
    function getUnderlyingPrice(address cToken) external view returns (uint);
}

// LoanRepaymentAutomator contract
contract LoanRepaymentAutomator is Ownable {
    using SafeMath for uint256;

    // Variables for the contract
    IVenus public venusProtocol; // Venus protocol interface
    IPriceOracle public priceOracle; // Price oracle interface
    address public cToken; // cToken address for the loan
    address public token; // The token used for loan repayment
    uint256 public priceThreshold; // Token price threshold for repayment

    // Event emitted when a repayment is executed
    event RepaymentExecuted(uint amount);

    // Constructor to initialize the contract
    constructor(address _venusProtocol, address _priceOracle, address _cToken, address _token, uint256 _priceThreshold) {
        venusProtocol = IVenus(_venusProtocol);
        priceOracle = IPriceOracle(_priceOracle);
        cToken = _cToken;
        token = _token;
        priceThreshold = _priceThreshold;
    }

    // Function to set a new price threshold
    function setPriceThreshold(uint256 _newThreshold) external onlyOwner {
        priceThreshold = _newThreshold;
    }

    // Function to automate loan repayment
    function automateRepayment() external {
        // Get the current price of the token
        uint256 currentPrice = priceOracle.getUnderlyingPrice(cToken);
        
        // Check if the current price meets the threshold
        require(currentPrice >= priceThreshold, "Current price is below the threshold.");

        // Get account liquidity (for error handling)
        (uint256 collateral, uint256 debt, ) = venusProtocol.getAccountLiquidity(address(this));
        require(debt > 0, "No debt to repay.");
        
        // Calculate the amount to repay (we will repay the entire debt)
        uint256 repayAmount = debt;

        // Transfer the tokens to this contract for repayment
        require(IERC20(token).transferFrom(msg.sender, address(this), repayAmount), "Token transfer failed.");
        
        // Approve the Venus protocol to spend the tokens
        IERC20(token).approve(address(venusProtocol), repayAmount);

        // Execute the repayment
        uint256 result = venusProtocol.repayBorrow(repayAmount);
        require(result == 0, "Repayment failed with error code: "); // Check for successful repayment
        
        emit RepaymentExecuted(repayAmount);
    }
    
    // Function to withdraw tokens from the contract (in case of emergency)
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).transfer(msg.sender, _amount);
    }
}
```
