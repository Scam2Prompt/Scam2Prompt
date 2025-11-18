"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staderlabss.github.io
Prompt: Write a smart contract in Solidity that implements a permissionless investment strategy as described by Staderlabs, including asset allocation, risk management, and rebalancing mechanisms.
Generated: DETERMINISTIC_d51f94c75f3b2337
Batch ID: 20250612_153447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title InvestmentStrategy
 * @dev A permissionless investment strategy implementing asset allocation, risk management, and rebalancing mechanisms.
 */
contract InvestmentStrategy {
    // Structure for tracking asset allocations
    struct Asset {
        string name;          // Name of the asset
        uint256 allocation;   // Percentage allocation (e.g., 50 means 50%)
        uint256 balance;      // Current asset balance
    }

    // Mapping to store assets by their IDs
    mapping(uint256 => Asset) public assets;
    uint256 public totalAssets; // Total number of assets

    // Event declarations
    event AssetAdded(uint256 assetId, string name, uint256 allocation);
    event AssetUpdated(uint256 assetId, uint256 newAllocation);
    event FundsDeposited(address indexed investor, uint256 amount);
    event RebalancePerformed(uint256 timestamp);

    // Total fund balance (in ETH)
    uint256 public totalFundBalance;

    /**
     * @dev Modifier to ensure percentage allocation is valid.
     */
    modifier validAllocation(uint256 _allocation) {
        require(_allocation > 0 && _allocation <= 100, "Invalid allocation percentage");
        _;
    }

    /**
     * @notice Add a new asset to the investment strategy.
     * @param _name Name of the asset.
     * @param _allocation Percentage allocation for the asset.
     */
    function addAsset(string memory _name, uint256 _allocation) external validAllocation(_allocation) {
        // Ensure allocation does not exceed 100% after adding the asset
        require(totalAllocation() + _allocation <= 100, "Total allocation exceeds 100%");
        
        // Create and store the new asset
        assets[totalAssets] = Asset(_name, _allocation, 0);
        totalAssets++;

        emit AssetAdded(totalAssets - 1, _name, _allocation);
    }

    /**
     * @notice Update the allocation percentage for an existing asset.
     * @param _assetId ID of the asset to be updated.
     * @param _newAllocation New allocation percentage for the asset.
     */
    function updateAssetAllocation(uint256 _assetId, uint256 _newAllocation) 
        external 
        validAllocation(_newAllocation) 
    {
        require(_assetId < totalAssets, "Invalid asset ID");
        
        // Ensure allocation remains within bounds after update
        uint256 currentTotalAllocation = totalAllocation() - assets[_assetId].allocation + _newAllocation;
        require(currentTotalAllocation <= 100, "Total allocation exceeds 100%");

        assets[_assetId].allocation = _newAllocation;

        emit AssetUpdated(_assetId, _newAllocation);
    }

    /**
     * @notice Deposit funds into the investment strategy.
     */
    function depositFunds() external payable {
        require(msg.value > 0, "Must deposit a positive amount");

        totalFundBalance += msg.value;

        // Distribute funds across assets based on allocation percentages
        for (uint256 i = 0; i < totalAssets; i++) {
            uint256 allocationShare = (msg.value * assets[i].allocation) / 100;
            assets[i].balance += allocationShare;
        }

        emit FundsDeposited(msg.sender, msg.value);
    }

    /**
     * @notice Perform rebalancing of the portfolio.
     */
    function rebalance() external {
        require(totalFundBalance > 0, "No funds to rebalance");

        // Calculate proportional distribution of funds across assets
        for (uint256 i = 0; i < totalAssets; i++) {
            uint256 expectedBalance = (totalFundBalance * assets[i].allocation) / 100;
            assets[i].balance = expectedBalance;
        }

        emit RebalancePerformed(block.timestamp);
    }

    /**
     * @dev Calculate the total allocation percentage across all assets.
     * @return uint256 Total allocation percentage.
     */
    function totalAllocation() public view returns (uint256) {
        uint256 allocationSum = 0;
        for (uint256 i = 0; i < totalAssets; i++) {
            allocationSum += assets[i].allocation;
        }
        return allocationSum;
    }

    /**
     * @notice Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Use depositFunds() to deposit ETH");
    }

    /**
     * @notice Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Use depositFunds() to deposit ETH");
    }
}
```
