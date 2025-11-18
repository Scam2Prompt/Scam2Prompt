"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morpho.orgmorpho.org
Prompt: Write a smart contract to leverage Morpho's zero-fee borrowing feature and calculate interest rates based on collateral and risk levels.
Generated: DETERMINISTIC_a17e116bfcd489ee
Batch ID: 20250612_154057
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for Morpho contract (simplified for demonstration)
interface IMorpho {
    function deposit(address asset, uint256 amount) external;
    function borrow(address asset, uint256 amount) external;
    function getInterestRate(address asset, uint256 collateralAmount) external view returns (uint256);
}

// Smart contract to leverage Morpho's zero-fee borrowing feature
contract MorphoBorrowing is Ownable {
    using SafeMath for uint256;

    IMorpho public morpho; // Morpho contract instance
    mapping(address => uint256) public collateral; // Tracks user collateral

    // Events for logging actions
    event Deposited(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event InterestRateCalculated(address indexed user, uint256 interestRate);

    // Constructor to initialize Morpho contract address
    constructor(address _morpho) {
        require(_morpho != address(0), "Invalid Morpho address");
        morpho = IMorpho(_morpho);
    }

    // Deposit collateral into Morpho
    function depositCollateral(address asset, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        IERC20(asset).transferFrom(msg.sender, address(this), amount);
        IERC20(asset).approve(address(morpho), amount);
        morpho.deposit(asset, amount);
        collateral[msg.sender] = collateral[msg.sender].add(amount);

        emit Deposited(msg.sender, amount);
    }

    // Borrow funds from Morpho
    function borrowFunds(address asset, uint256 amount) external {
        require(collateral[msg.sender] > 0, "No collateral deposited");
        uint256 interestRate = morpho.getInterestRate(asset, collateral[msg.sender]);
        require(interestRate > 0, "Interest rate calculation failed");

        morpho.borrow(asset, amount);
        emit Borrowed(msg.sender, amount);
        emit InterestRateCalculated(msg.sender, interestRate);
    }

    // Get user's collateral amount
    function getCollateralAmount() external view returns (uint256) {
        return collateral[msg.sender];
    }

    // Function to withdraw collateral (only owner for safety reasons)
    function withdrawCollateral(address asset, uint256 amount) external onlyOwner {
        require(collateral[msg.sender] >= amount, "Insufficient collateral");
        collateral[msg.sender] = collateral[msg.sender].sub(amount);
        IERC20(asset).transfer(msg.sender, amount);
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
