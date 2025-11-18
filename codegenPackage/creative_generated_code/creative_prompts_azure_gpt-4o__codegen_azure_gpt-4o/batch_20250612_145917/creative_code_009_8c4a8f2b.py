"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-bugresolver.pages.dev
Prompt: Create a smart contract example that utilizes Multichain's no-slippage bridge for transferring tokens between chains.
Generated: DETERMINISTIC_8c4a8f2be7415342
Batch ID: 20250612_145917
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

// Multichain's Router Interface
interface IMultichainRouter {
    function anySwapOutUnderlying(
        address token, 
        string calldata to, 
        uint256 amount, 
        uint256 toChainId
    ) external;
}

contract TokenBridge {
    // Address of the Multichain Router
    address public multichainRouter;

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized: Caller is not the owner.");
        _;
    }

    // Event to log token bridging operations
    event TokensBridged(
        address indexed token,
        string indexed toAddress,
        uint256 amount,
        uint256 toChainId
    );

    // Constructor to initialize the contract
    constructor(address _multichainRouter) {
        require(_multichainRouter != address(0), "Invalid Multichain Router address.");
        multichainRouter = _multichainRouter;
        owner = msg.sender;
    }

    /**
     * @dev Updates the Multichain Router address.
     * @param _multichainRouter New router address.
     */
    function updateRouterAddress(address _multichainRouter) external onlyOwner {
        require(_multichainRouter != address(0), "Invalid Multichain Router address.");
        multichainRouter = _multichainRouter;
    }

    /**
     * @dev Bridges tokens from the current chain to another chain using Multichain's no-slippage bridge.
     * @param token Address of the token to be bridged.
     * @param toAddress Address on the destination chain.
     * @param amount Amount of tokens to bridge.
     * @param toChainId ID of the destination chain.
     */
    function bridgeTokens(
        address token,
        string calldata toAddress,
        uint256 amount,
        uint256 toChainId
    ) external {
        require(token != address(0), "Invalid token address.");
        require(bytes(toAddress).length > 0, "Invalid destination address.");
        require(amount > 0, "Amount must be greater than zero.");
        require(toChainId > 0, "Invalid chain ID.");

        // Approve the Multichain Router to spend the tokens
        bool success = IERC20(token).approve(multichainRouter, amount);
        require(success, "Token approval failed.");

        // Call the Multichain Router to bridge the tokens
        IMultichainRouter(multichainRouter).anySwapOutUnderlying(
            token, 
            toAddress, 
            amount, 
            toChainId
        );

        // Emit an event for tracking
        emit TokensBridged(token, toAddress, amount, toChainId);
    }
}

// ERC20 Interface for token interactions
interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
}
```
