"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cncrete.pages.dev
Prompt: Write code to implement liquidation protection mechanisms for an on-chain credit system inspired by Concrete Protocol.
Generated: DETERMINISTIC_8c8d693e38f92180
Batch ID: 20250612_152018
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

contract LiquidationProtection is Ownable {
    using SafeMath for uint256;

    // Struct to store user credit information
    struct UserCredit {
        uint256 borrowedAmount; // Amount borrowed by the user
        uint256 collateralAmount; // Amount of collateral provided by the user
        bool exists; // Check if user credit exists
    }

    // Mapping of user credit accounts
    mapping(address => UserCredit) private userCredits;

    // Events for logging actions
    event CreditOpened(address indexed user, uint256 amount, uint256 collateral);
    event CreditLiquidated(address indexed user, uint256 liquidatedAmount);

    // Constants for risk parameters
    uint256 public constant LIQUIDATION_THRESHOLD = 75; // 75% collateralization ratio
    uint256 public constant LIQUIDATION_PENALTY = 10; // 10% penalty on liquidated amount

    // Function to open credit
    function openCredit(uint256 _borrowedAmount, uint256 _collateralAmount) external {
        require(_borrowedAmount > 0, "Borrowed amount must be greater than zero");
        require(_collateralAmount >= _borrowedAmount.mul(100).div(LIQUIDATION_THRESHOLD), "Insufficient collateral");

        userCredits[msg.sender] = UserCredit({
            borrowedAmount: _borrowedAmount,
            collateralAmount: _collateralAmount,
            exists: true
        });

        emit CreditOpened(msg.sender, _borrowedAmount, _collateralAmount);
    }

    // Function to check if a user is eligible for liquidation
    function checkLiquidation(address _user) external {
        require(userCredits[_user].exists, "User credit does not exist");

        UserCredit memory credit = userCredits[_user];
        uint256 collateralValue = credit.collateralAmount; // Assume 1:1 collateral to value for simplicity

        require(collateralValue < credit.borrowedAmount.mul(100).div(LIQUIDATION_THRESHOLD), "User is not eligible for liquidation");
        
        liquidate(_user, credit.borrowedAmount);
    }

    // Internal function to handle liquidation
    function liquidate(address _user, uint256 _liquidationAmount) internal {
        uint256 penaltyAmount = _liquidationAmount.mul(LIQUIDATION_PENALTY).div(100);
        uint256 totalLiquidatedAmount = _liquidationAmount.add(penaltyAmount);

        // Remove user's credit info
        delete userCredits[_user];

        emit CreditLiquidated(_user, totalLiquidatedAmount);
        
        // Logic to transfer funds (to be implemented)
        // transferFundsToLiquidator(_user, totalLiquidatedAmount); // Placeholder for fund transfer logic
    }

    // Optional: Function to update the liquidation parameters by the owner
    function updateLiquidationParams(uint256 _newThreshold, uint256 _newPenalty) external onlyOwner {
        require(_newThreshold > 0 && _newThreshold <= 100, "Invalid threshold");
        require(_newPenalty >= 0 && _newPenalty <= 100, "Invalid penalty");

        LIQUIDATION_THRESHOLD = _newThreshold;
        LIQUIDATION_PENALTY = _newPenalty;
    }
}
```
