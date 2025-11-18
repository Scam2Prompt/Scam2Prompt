"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roostcoinclaim.pages.dev
Prompt: Write a Solidity contract that mimics the presale breakdown of $ROOST, ensuring 50% of the raise goes to LP and 50% to expenses, development, and distribution.
Generated: DETERMINISTIC_90d6d56275fd9e10
Batch ID: 20250612_152710
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
 * @title ROOSTPresale
 * @dev This contract handles the presale breakdown of $ROOST tokens,
 * ensuring 50% of the raise goes to liquidity pool (LP) and 50% to expenses, development, and distribution.
 */
contract ROOSTPresale {
    // Address of the liquidity pool manager
    address public liquidityPoolAddress;

    // Address for expense, development, and distribution funds
    address public expensesAddress;

    // Total funds raised during presale
    uint256 public totalFundsRaised;

    // Flag to indicate whether presale is active
    bool public presaleActive;

    // Event emitted when funds are distributed
    event FundsDistributed(uint256 toLiquidityPool, uint256 toExpenses);

    // Modifier to ensure a function is called only when presale is active
    modifier onlyWhilePresaleActive() {
        require(presaleActive, "Presale is not active");
        _;
    }

    /**
     * @dev Constructor to initialize the contract addresses.
     * @param _liquidityPoolAddress Address where LP funds will be sent.
     * @param _expensesAddress Address where expense funds will be sent.
     */
    constructor(address _liquidityPoolAddress, address _expensesAddress) {
        require(_liquidityPoolAddress != address(0), "Invalid liquidity pool address");
        require(_expensesAddress != address(0), "Invalid expenses address");

        liquidityPoolAddress = _liquidityPoolAddress;
        expensesAddress = _expensesAddress;
        presaleActive = true;
    }

    /**
     * @dev Function to contribute funds during the presale.
     * @notice Only callable while presale is active.
     */
    function contribute() external payable onlyWhilePresaleActive {
        require(msg.value > 0, "Contribution must be greater than zero");

        totalFundsRaised += msg.value;
    }

    /**
     * @dev Function to end the presale and distribute funds.
     * @notice Only callable by the contract owner.
     */
    function endPresale() external {
        require(presaleActive, "Presale is already ended");
        require(address(this).balance > 0, "No funds to distribute");

        presaleActive = false;

        uint256 halfFunds = address(this).balance / 2;

        // Transfer 50% of raised funds to liquidity pool address
        (bool lpSuccess, ) = liquidityPoolAddress.call{value: halfFunds}("");
        require(lpSuccess, "Transfer to liquidity pool failed");

        // Transfer 50% of raised funds to expenses address
        (bool expensesSuccess, ) = expensesAddress.call{value: halfFunds}("");
        require(expensesSuccess, "Transfer to expenses address failed");

        emit FundsDistributed(halfFunds, halfFunds);
    }

    /**
     * @dev Fallback function to receive Ether contributions.
     */
    receive() external payable onlyWhilePresaleActive {
        totalFundsRaised += msg.value;
    }

    /**
     * @dev Function to retrieve contract balance.
     * @return Contract balance in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
