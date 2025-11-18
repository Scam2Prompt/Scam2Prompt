"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthr.pages.dev
Prompt: Provide an example of how to implement SYNTHR's governance features, including influencing gauge weights for syASSET/ASSET LP farming rewards and submitting syASSET listing proposals.
Generated: DETERMINISTIC_acc6ae0cd047b0ad
Batch ID: 20250612_152439
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

// Import relevant interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the SYNTHR governance contract
interface ISynthGovernance {
    function setGaugeWeights(address asset, uint256 weight) external;
    function proposeListing(address asset) external;
}

// Governance contract for SYNTHR
contract SynthGovernance is ISynthGovernance, Ownable {
    // Struct to hold gauge information
    struct Gauge {
        uint256 weight;
        bool isListed;
    }

    // Mapping of assets to their respective gauges
    mapping(address => Gauge) public gauges;

    // Event emitted when gauge weights are updated
    event GaugeWeightUpdated(address indexed asset, uint256 weight);

    // Event emitted when a new asset is proposed for listing
    event AssetListed(address indexed asset);

    // Modifier to check if the asset is already listed
    modifier onlyListedAsset(address asset) {
        require(gauges[asset].isListed, "Asset not listed");
        _;
    }

    // Function to set gauge weights for farming rewards
    function setGaugeWeights(address asset, uint256 weight) external override onlyOwner {
        require(weight >= 0, "Weight must be non-negative");

        // Update the gauge weight for the specified asset
        gauges[asset].weight = weight;

        // Emit an event to log the weight update
        emit GaugeWeightUpdated(asset, weight);
    }

    // Function to propose a new asset for listing
    function proposeListing(address asset) external override onlyOwner {
        require(asset != address(0), "Asset address cannot be zero");
        require(!gauges[asset].isListed, "Asset already listed");

        // Mark the asset as listed
        gauges[asset].isListed = true;

        // Emit an event to log the proposed listing
        emit AssetListed(asset);
    }

    // Function to get the current gauge weight of an asset
    function getGaugeWeight(address asset) external view returns (uint256) {
        return gauges[asset].weight;
    }

    // Function to check if an asset is listed
    function isAssetListed(address asset) external view returns (bool) {
        return gauges[asset].isListed;
    }
}
```
