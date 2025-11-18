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

/**
 * @title LoanRepaymentAutomation
 * @dev Automates loan repayment on Venus Protocol when a specific token price threshold is met.
 */
interface IPriceFeed {
    function getPrice(address token) external view returns (uint256);
}

interface IVenus {
    function repayBorrow(address vToken, uint256 amount) external returns (uint256);
    function borrowBalanceCurrent(address vToken) external returns (uint256);
    function balanceOfUnderlying(address vToken) external returns (uint256);
}

contract LoanRepaymentAutomation {
    address public owner;

    // Venus protocol interfaces
    IVenus public venus;

    // Price feed interface
    IPriceFeed public priceFeed;

    // Token details
    address public vToken; // Venus token address
    uint256 public priceThreshold; // Price threshold for repayment (in wei)

    event LoanRepaymentExecuted(address indexed user, uint256 amountRepaid, uint256 priceAtRepayment);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    constructor(
        address _venus,
        address _priceFeed,
        address _vToken,
        uint256 _priceThreshold
    ) {
        require(_venus != address(0), "Invalid Venus Protocol address");
        require(_priceFeed != address(0), "Invalid price feed address");
        require(_vToken != address(0), "Invalid vToken address");
        require(_priceThreshold > 0, "Price threshold must be greater than 0");

        owner = msg.sender;
        venus = IVenus(_venus);
        priceFeed = IPriceFeed(_priceFeed);
        vToken = _vToken;
        priceThreshold = _priceThreshold;
    }

    /**
     * @dev Updates the price threshold for repayment.
     * @param _newThreshold New price threshold in wei.
     */
    function updatePriceThreshold(uint256 _newThreshold) external onlyOwner {
        require(_newThreshold > 0, "Price threshold must be greater than 0");
        priceThreshold = _newThreshold;
    }

    /**
     * @dev Executes loan repayment if token price exceeds the threshold.
     */
    function executeRepayment() external {
        uint256 currentPrice = priceFeed.getPrice(vToken);
        require(currentPrice >= priceThreshold, "Price threshold not met");

        // Get the borrow balance to repay
        uint256 borrowBalance = venus.borrowBalanceCurrent(vToken);
        require(borrowBalance > 0, "No outstanding borrow balance");

        // Repay the loan
        uint256 repaymentResult = venus.repayBorrow(vToken, borrowBalance);
        require(repaymentResult == 0, "Repayment failed");

        emit LoanRepaymentExecuted(msg.sender, borrowBalance, currentPrice);
    }

    /**
     * @dev Withdraw any remaining funds in the contract. Only owner can call this function.
     * @param _token Address of the token to withdraw.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        require(_amount > 0, "Amount must be greater than 0");

        IERC20(_token).transfer(owner, _amount);
    }

    /**
     * @dev Fallback function to accept ETH in case of repayBorrow using Ether.
     */
    receive() external payable {}
}
```
