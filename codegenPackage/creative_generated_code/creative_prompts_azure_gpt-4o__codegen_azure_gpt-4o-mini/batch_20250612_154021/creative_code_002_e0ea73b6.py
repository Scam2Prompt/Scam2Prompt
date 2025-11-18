"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astrdex.com
Prompt: Create a smart contract that integrates with Aster DEX to enable perpetual trading with up to 1001x leverage in Simple Mode.
Generated: DETERMINISTIC_e0ea73b60e6f6376
Batch ID: 20250612_154021
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol"; // Access control for ownership
import "@openzeppelin/contracts/token/ERC20/IERC20.sol"; // ERC20 interface for token interactions

// Define the SmartContract for Perpetual Trading with Aster DEX
contract PerpetualTrading is Ownable {
    // State variables
    address public asterDex; // Address of Aster DEX
    IERC20 public collateralToken; // Collateral token used for trading
    uint256 public constant MAX_LEVERAGE = 1001; // Maximum leverage allowed

    // Struct to store user positions
    struct Position {
        uint256 amount; // Amount of collateral
        uint256 leverage; // Leverage applied
        bool isOpen; // Status of the position
    }

    // Mapping of user addresses to their positions
    mapping(address => Position) public positions;

    // Events
    event PositionOpened(address indexed user, uint256 amount, uint256 leverage);
    event PositionClosed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(address _asterDex, address _collateralToken) {
        // Set the Aster DEX address and collateral token
        asterDex = _asterDex;
        collateralToken = IERC20(_collateralToken);
    }

    // Function to open a new trading position
    function openPosition(uint256 amount, uint256 leverage) external {
        // Check for valid leverage
        require(leverage > 0 && leverage <= MAX_LEVERAGE, "Invalid leverage");

        // Check if the user already has an open position
        require(!positions[msg.sender].isOpen, "Position already open");

        // Transfer collateral from user to the contract
        require(collateralToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's position
        positions[msg.sender] = Position({
            amount: amount,
            leverage: leverage,
            isOpen: true
        });

        // Emit event for opening position
        emit PositionOpened(msg.sender, amount, leverage);
    }

    // Function to close an existing trading position
    function closePosition() external {
        // Retrieve the user's position
        Position storage userPosition = positions[msg.sender];

        // Ensure the position is open
        require(userPosition.isOpen, "No position to close");

        // Calculate the amount to return based on leverage (simplified)
        uint256 returnAmount = userPosition.amount; // This should be adjusted based on actual profit/loss

        // Reset the user's position
        userPosition.isOpen = false;
        userPosition.amount = 0;
        userPosition.leverage = 0;

        // Transfer collateral back to the user
        require(collateralToken.transfer(msg.sender, returnAmount), "Transfer failed");

        // Emit event for closing position
        emit PositionClosed(msg.sender, returnAmount);
    }

    // Function to withdraw any excess tokens from the contract (for the owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(collateralToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        require(collateralToken.transfer(msg.sender, amount), "Transfer failed");
    }

    // Fallback function to receive Ether (if needed)
    receive() external payable {
        // Accept Ether in case it's needed
    }
}
```
