"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iziswap.fi
Prompt: Write a smart contract in Solidity for a liquidity-mining-based bond like iUSD, ensuring it is 100% collateralized and avoids impermanent loss for LP farming.
Generated: DETERMINISTIC_a3659dc8e4072cb0
Batch ID: 20250612_153424
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

// Import the necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract BondLiquidityMining is Ownable, ReentrancyGuard {
    // Struct to hold bond details
    struct Bond {
        uint256 amount;          // Amount of collateral
        uint256 maturity;        // Maturity timestamp
        bool isActive;           // Active status of the bond
    }

    // Mapping to keep track of user bonds
    mapping(address => Bond) public bonds;

    // Event emitted for bond creation
    event BondCreated(address indexed user, uint256 amount, uint256 maturity);
    
    // Event emitted for bond redemption
    event BondRedeemed(address indexed user, uint256 amount);

    // Collateral token used for bonding
    IERC20 public collateralToken;
    
    // Total collateral locked in the contract
    uint256 public totalCollateral;

    // Constructor to initialize the contract with the collateral token address
    constructor(address _collateralToken) {
        require(_collateralToken != address(0), "Invalid token address");
        collateralToken = IERC20(_collateralToken);
    }

    // Function to create a bond
    function createBond(uint256 _amount, uint256 _maturity) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        require(_maturity > block.timestamp, "Maturity must be in the future");

        // Transfer collateral from user to contract
        require(collateralToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update bond details
        bonds[msg.sender] = Bond({
            amount: _amount,
            maturity: _maturity,
            isActive: true
        });

        totalCollateral += _amount;

        emit BondCreated(msg.sender, _amount, _maturity);
    }

    // Function to redeem a bond
    function redeemBond() external nonReentrant {
        Bond storage userBond = bonds[msg.sender];
        
        require(userBond.isActive, "No active bond");
        require(block.timestamp >= userBond.maturity, "Bond has not matured yet");

        uint256 amountToRedeem = userBond.amount;

        // Reset bond details
        userBond.amount = 0;
        userBond.isActive = false;

        // Transfer the collateral back to the user
        require(collateralToken.transfer(msg.sender, amountToRedeem), "Transfer failed");

        totalCollateral -= amountToRedeem;

        emit BondRedeemed(msg.sender, amountToRedeem);
    }

    // Function to check the bond details
    function getBondDetails(address _user) external view returns (Bond memory) {
        return bonds[_user];
    }

    // Function to withdraw collateral in case of emergencies (only owner)
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount <= totalCollateral, "Insufficient collateral");
        totalCollateral -= _amount;
        require(collateralToken.transfer(msg.sender, _amount), "Transfer failed");
    }
}
```
