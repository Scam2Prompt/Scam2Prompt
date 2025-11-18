"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimalvara.pages.dev
Prompt: Develop a function in Solidity to automatically rebalance the underlying assets of an ERC-7621 Basket Token based on predefined monthly schedules or discretionary DAO-controlled settings.
Generated: DETERMINISTIC_a43e2953d3f4a896
Batch ID: 20250612_154820
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

// Import ERC-20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the ERC-7621 Basket Token
interface IERC7621BasketToken {
    function getUnderlyingAssets() external view returns (address[] memory);
    function getAssetWeights() external view returns (uint256[] memory);
    function rebalance() external;
}

// Smart contract for automated rebalancing of an ERC-7621 Basket Token
contract Rebalancer {
    // Address of the Basket Token
    IERC7621BasketToken public basketToken;

    // Last rebalance timestamp
    uint256 public lastRebalance;

    // Rebalance interval in seconds (30 days)
    uint256 public constant REBALANCE_INTERVAL = 30 days;

    // Event emitted when rebalancing occurs
    event Rebalanced(uint256 timestamp);

    // Constructor to initialize the basket token address
    constructor(IERC7621BasketToken _basketToken) {
        basketToken = _basketToken;
        lastRebalance = block.timestamp;
    }

    // Function to initiate the rebalancing process
    function rebalance() external {
        // Check if the time since last rebalance exceeds the interval
        require(block.timestamp >= lastRebalance + REBALANCE_INTERVAL, "Rebalance not due");

        // Call the rebalance function of the basket token
        try basketToken.rebalance() {
            lastRebalance = block.timestamp;
            emit Rebalanced(lastRebalance);
        } catch {
            revert("Rebalance failed");
        }
    }

    // Function to manually set a new rebalance interval (only owner can call)
    function setRebalanceInterval(uint256 newInterval) external {
        // For the sake of example, we assume a modifier for owner restriction
        // _onlyOwner();
        require(newInterval > 0, "Interval must be positive");
        lastRebalance = block.timestamp - newInterval; // Allow immediate rebalance
    }

    // Function to get the current balance of a specified ERC-20 asset in the basket
    function getAssetBalance(address asset) external view returns (uint256) {
        return IERC20(asset).balanceOf(address(basketToken));
    }
}
```
