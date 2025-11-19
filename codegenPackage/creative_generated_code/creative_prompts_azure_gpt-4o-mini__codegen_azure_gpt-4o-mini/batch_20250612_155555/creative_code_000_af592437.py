"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staderlabss.github.io
Prompt: Write a smart contract for a permissionless investment strategy on Staderlabs that allows users to define asset allocation and risk management parameters.
Generated: DETERMINISTIC_af592437a1aa7152
Batch ID: 20250612_155555
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

// Importing the necessary interfaces for interacting with ERC20 tokens and Staderlabs
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for a permissionless investment strategy on Staderlabs
contract PermissionlessInvestmentStrategy is Ownable {
    // Struct to hold asset allocation and risk management parameters
    struct InvestmentStrategy {
        address asset;          // ERC20 asset address
        uint256 allocation;     // Percentage allocation (in basis points, e.g., 10000 = 100%)
        uint256 riskLimit;      // Maximum risk limit (in basis points)
    }

    // Mapping to store user strategies
    mapping(address => InvestmentStrategy[]) private userStrategies;

    // Event emitted when a new investment strategy is created
    event StrategyCreated(address indexed user, address asset, uint256 allocation, uint256 riskLimit);

    // Event emitted when an investment strategy is updated
    event StrategyUpdated(address indexed user, address asset, uint256 allocation, uint256 riskLimit);

    /**
     * @notice Creates a new investment strategy for the user.
     * @param _asset The address of the ERC20 asset.
     * @param _allocation The percentage allocation of the asset (in basis points).
     * @param _riskLimit The risk limit of the strategy (in basis points).
     */
    function createStrategy(address _asset, uint256 _allocation, uint256 _riskLimit) external {
        require(_allocation > 0 && _allocation <= 10000, "Invalid allocation");
        require(_riskLimit >= 0 && _riskLimit <= 10000, "Invalid risk limit");

        // Create and store the user's investment strategy
        InvestmentStrategy memory newStrategy = InvestmentStrategy({
            asset: _asset,
            allocation: _allocation,
            riskLimit: _riskLimit
        });
        
        userStrategies[msg.sender].push(newStrategy);
        
        emit StrategyCreated(msg.sender, _asset, _allocation, _riskLimit);
    }

    /**
     * @notice Updates an existing investment strategy for the user.
     * @param _index The index of the strategy to update.
     * @param _allocation The new percentage allocation of the asset (in basis points).
     * @param _riskLimit The new risk limit of the strategy (in basis points).
     */
    function updateStrategy(uint256 _index, uint256 _allocation, uint256 _riskLimit) external {
        require(_index < userStrategies[msg.sender].length, "Strategy does not exist");
        require(_allocation > 0 && _allocation <= 10000, "Invalid allocation");
        require(_riskLimit >= 0 && _riskLimit <= 10000, "Invalid risk limit");

        // Update the user's investment strategy
        InvestmentStrategy storage strategy = userStrategies[msg.sender][_index];
        strategy.allocation = _allocation;
        strategy.riskLimit = _riskLimit;

        emit StrategyUpdated(msg.sender, strategy.asset, _allocation, _riskLimit);
    }

    /**
     * @notice Retrieves the investment strategies of the user.
     * @return An array of investment strategies for the user.
     */
    function getUserStrategies() external view returns (InvestmentStrategy[] memory) {
        return userStrategies[msg.sender];
    }

    /**
     * @notice Fallback function to prevent accidental ether deposits.
     */
    receive() external payable {
        revert("This contract does not accept Ether");
    }
}
```
