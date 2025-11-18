"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kodiak-finance.app
Prompt: Generate Solidity code for a smart contract that utilizes Kodiak Finance's automated yield farming strategies tailored to different risk levels.
Generated: DETERMINISTIC_48c91fcb146f4e98
Batch ID: 20250612_153925
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

// Import necessary interfaces for interacting with the Kodiak Finance protocol
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the YieldFarming contract
contract YieldFarming is Ownable {
    // Define a struct to hold information about each farming strategy
    struct Strategy {
        string name;                // Name of the strategy
        address tokenAddress;       // Address of the ERC20 token to farm
        uint256 riskLevel;         // Risk level (1-5, where 5 is highest risk)
        uint256 yield;             // Current yield percentage
        bool isActive;             // Status of the strategy
    }

    // State variables
    mapping(uint256 => Strategy) public strategies;   // Mapping of strategy ID to Strategy
    uint256 public strategyCount;                      // Total number of strategies

    // Event to log the addition of a new strategy
    event StrategyAdded(uint256 strategyId, string name, address tokenAddress, uint256 riskLevel, uint256 yield);
    
    // Event to log the activation or deactivation of a strategy
    event StrategyStatusUpdated(uint256 strategyId, bool isActive);

    // Modifier to check if strategy exists
    modifier strategyExists(uint256 strategyId) {
        require(strategyId < strategyCount, "Strategy does not exist");
        _;
    }

    // Function to add a new yield farming strategy
    function addStrategy(string memory _name, address _tokenAddress, uint256 _riskLevel, uint256 _yield) external onlyOwner {
        require(_riskLevel >= 1 && _riskLevel <= 5, "Risk level must be between 1 and 5");
        require(_tokenAddress != address(0), "Invalid token address");

        strategies[strategyCount] = Strategy({
            name: _name,
            tokenAddress: _tokenAddress,
            riskLevel: _riskLevel,
            yield: _yield,
            isActive: true
        });

        emit StrategyAdded(strategyCount, _name, _tokenAddress, _riskLevel, _yield);
        strategyCount++;
    }

    // Function to update the status of an existing strategy
    function updateStrategyStatus(uint256 strategyId, bool _isActive) external onlyOwner strategyExists(strategyId) {
        strategies[strategyId].isActive = _isActive;
        emit StrategyStatusUpdated(strategyId, _isActive);
    }

    // Function to retrieve strategy details
    function getStrategy(uint256 strategyId) external view strategyExists(strategyId) returns (string memory, address, uint256, uint256, bool) {
        Strategy memory strategy = strategies[strategyId];
        return (strategy.name, strategy.tokenAddress, strategy.riskLevel, strategy.yield, strategy.isActive);
    }

    // Function to calculate yield for a given amount based on the strategy's yield percentage
    function calculateYield(uint256 strategyId, uint256 amount) external view strategyExists(strategyId) returns (uint256) {
        Strategy memory strategy = strategies[strategyId];
        require(strategy.isActive, "Strategy is inactive");
        return (amount * strategy.yield) / 100; // Returns yield based on the yield percentage
    }
}
```
