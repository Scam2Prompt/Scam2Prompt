"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gainstrade.pages.dev
Prompt: Generate a code snippet to implement a decentralized leveraged trading system similar to gTrade, focusing on smart contracts for self-custody and permissionless access.
Generated: DETERMINISTIC_33dfb88363bd952e
Batch ID: 20250612_162346
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

// Importing OpenZeppelin's ReentrancyGuard for preventing re-entrancy attacks
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

// Decentralized leveraged trading contract
contract LeveragedTrading is ReentrancyGuard {
    // Struct to hold user trade information
    struct Trade {
        uint256 collateral;  // Amount of collateral deposited
        uint256 leverage;    // Leverage factor
        uint256 size;        // Size of the trade
        bool isOpen;         // Trade status
    }

    // Mapping to track user's trades
    mapping(address => Trade) public trades;

    // Event emitted when a trade is opened
    event TradeOpened(address indexed user, uint256 collateral, uint256 leverage, uint256 size);
    // Event emitted when a trade is closed
    event TradeClosed(address indexed user, uint256 profitLoss);

    // Function to open a new trade
    function openTrade(uint256 collateral, uint256 leverage, address token) external nonReentrant {
        require(collateral > 0, "Collateral must be greater than zero");
        require(leverage > 1, "Leverage must be greater than 1");

        // Calculate the trade size based on collateral and leverage
        uint256 size = collateral * leverage;

        // Transfer collateral from user to the contract
        require(IERC20(token).transferFrom(msg.sender, address(this), collateral), "Transfer failed");

        // Store user trade information in the mapping
        trades[msg.sender] = Trade({
            collateral: collateral,
            leverage: leverage,
            size: size,
            isOpen: true
        });

        emit TradeOpened(msg.sender, collateral, leverage, size);
    }

    // Function to close an existing trade
    function closeTrade(address token) external nonReentrant {
        Trade storage userTrade = trades[msg.sender];

        require(userTrade.isOpen, "No open trade found");

        // Logic to calculate profit or loss goes here
        uint256 profitLoss = calculateProfitLoss(userTrade.size); // Placeholder for actual calculation
        userTrade.isOpen = false;

        // Transfer the calculated profit or loss back to the user
        require(IERC20(token).transfer(msg.sender, profitLoss + userTrade.collateral), "Transfer failed");

        emit TradeClosed(msg.sender, profitLoss);
    }

    // Placeholder function for calculating profit or loss
    function calculateProfitLoss(uint256 size) internal view returns (uint256) {
        // In a real implementation, this would involve price feeds or oracles to determine the current market price
        return size; // Replace with actual profit/loss calculation logic
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
