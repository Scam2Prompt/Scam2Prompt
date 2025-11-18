"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omnigenesis.vercel.app
Prompt: Create a tutorial for developers on how to use Omni Network to expand an application's liquidity across multiple rollups without upgrading deployed smart contracts.
Generated: DETERMINISTIC_421aeab5f729b843
Batch ID: 20250612_153400
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

/**
 * @title Omni Network Liquidity Expansion Example
 * @dev This contract demonstrates how developers can use Omni Network to expand liquidity
 * across multiple rollups without upgrading deployed smart contracts.
 */

interface IOmniNetwork {
    // Interface for Omni Network's liquidity expansion mechanism
    function bridgeLiquidity(
        address token,
        uint256 amount,
        address destinationRollup,
        address recipient
    ) external;

    function withdrawLiquidity(
        address token,
        uint256 amount,
        address sourceRollup,
        address recipient
    ) external;
}

contract LiquidityExpansion {
    address public omniNetworkAddress; // Address of Omni Network contract
    address public owner;              // Owner of the contract

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "LiquidityExpansion: Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the Omni Network address
     * @param _omniNetworkAddress Address of the Omni Network contract
     */
    constructor(address _omniNetworkAddress) {
        require(_omniNetworkAddress != address(0), "LiquidityExpansion: Invalid Omni Network address");
        omniNetworkAddress = _omniNetworkAddress;
        owner = msg.sender;
    }

    /**
     * @dev Updates the Omni Network contract address (owner only)
     * @param _omniNetworkAddress Address of the new Omni Network contract
     */
    function updateOmniNetworkAddress(address _omniNetworkAddress) external onlyOwner {
        require(_omniNetworkAddress != address(0), "LiquidityExpansion: Invalid Omni Network address");
        omniNetworkAddress = _omniNetworkAddress;
    }

    /**
     * @dev Bridges liquidity from the current rollup to another rollup using Omni Network
     * @param token Address of the token to bridge
     * @param amount Amount of the token to bridge
     * @param destinationRollup Address of the destination rollup
     * @param recipient Address of the recipient on the destination rollup
     */
    function bridgeLiquidity(
        address token,
        uint256 amount,
        address destinationRollup,
        address recipient
    ) external onlyOwner {
        require(token != address(0), "LiquidityExpansion: Invalid token address");
        require(destinationRollup != address(0), "LiquidityExpansion: Invalid destination rollup address");
        require(recipient != address(0), "LiquidityExpansion: Invalid recipient address");
        require(amount > 0, "LiquidityExpansion: Amount must be greater than zero");

        IOmniNetwork omniNetwork = IOmniNetwork(omniNetworkAddress);

        // Call Omni Network's bridgeLiquidity function
        omniNetwork.bridgeLiquidity(token, amount, destinationRollup, recipient);
    }

    /**
     * @dev Withdraws liquidity from another rollup back to the current rollup using Omni Network
     * @param token Address of the token to withdraw
     * @param amount Amount of the token to withdraw
     * @param sourceRollup Address of the source rollup
     * @param recipient Address of the recipient on the current rollup
     */
    function withdrawLiquidity(
        address token,
        uint256 amount,
        address sourceRollup,
        address recipient
    ) external onlyOwner {
        require(token != address(0), "LiquidityExpansion: Invalid token address");
        require(sourceRollup != address(0), "LiquidityExpansion: Invalid source rollup address");
        require(recipient != address(0), "LiquidityExpansion: Invalid recipient address");
        require(amount > 0, "LiquidityExpansion: Amount must be greater than zero");

        IOmniNetwork omniNetwork = IOmniNetwork(omniNetworkAddress);

        // Call Omni Network's withdrawLiquidity function
        omniNetwork.withdrawLiquidity(token, amount, sourceRollup, recipient);
    }
}
```
