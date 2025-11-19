"""
Generated Code Metadata:
========================
Original URL: https://web-bugresolver.pages.dev
Prompt: Create a smart contract example that utilizes Multichain's no-slippage bridge for transferring tokens between chains.
Generated: DETERMINISTIC_8c4a8f2be7415342
Batch ID: 20250612_145917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MultichainBridgeAdapter
 * @dev A smart contract that facilitates cross-chain token transfers using Multichain's no-slippage bridge
 */
contract MultichainBridgeAdapter is Ownable {
    using SafeERC20 for IERC20;

    // Multichain router contract address
    address public multichainRouter;

    // Mapping of supported tokens and their corresponding destination chain IDs
    mapping(address => mapping(uint256 => bool)) public supportedTokens;

    event TokenBridged(
        address indexed token,
        address indexed sender,
        uint256 amount,
        uint256 destChainId,
        address recipient
    );

    event TokenSupportUpdated(
        address indexed token,
        uint256 indexed chainId,
        bool supported
    );

    event RouterUpdated(address indexed newRouter);

    /**
     * @dev Constructor initializes the Multichain router address
     * @param _multichainRouter Address of the Multichain router contract
     */
    constructor(address _multichainRouter) {
        require(_multichainRouter != address(0), "Invalid router address");
        multichainRouter = _multichainRouter;
    }

    /**
     * @dev Updates the Multichain router address
     * @param _newRouter New router address
     */
    function updateRouter(address _newRouter) external onlyOwner {
        require(_newRouter != address(0), "Invalid router address");
        multichainRouter = _newRouter;
        emit RouterUpdated(_newRouter);
    }

    /**
     * @dev Adds or removes token support for a specific chain
     * @param _token Token address
     * @param _chainId Destination chain ID
     * @param _supported Whether the token is supported for the chain
     */
    function setTokenSupport(
        address _token,
        uint256 _chainId,
        bool _supported
    ) external onlyOwner {
        supportedTokens[_token][_chainId] = _supported;
        emit TokenSupportUpdated(_token, _chainId, _supported);
    }

    /**
     * @dev Bridges tokens to another chain using Multichain's no-slippage bridge
     * @param _token Token to bridge
     * @param _amount Amount to bridge
     * @param _destChainId Destination chain ID
     * @param _recipient Recipient address on destination chain
     */
    function bridgeTokens(
        address _token,
        uint256 _amount,
        uint256 _destChainId,
        address _recipient
    ) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(_recipient != address(0), "Invalid recipient address");
        require(
            supportedTokens[_token][_destChainId],
            "Token not supported for this chain"
        );

        IERC20 token = IERC20(_token);
        uint256 balanceBefore = token.balanceOf(address(this));
        token.safeTransferFrom(msg.sender, address(this), _amount);
        uint256 balanceAfter = token.balanceOf(address(this));
        require(
            balanceAfter - balanceBefore >= _amount,
            "Token transfer failed"
        );

        token.safeApprove(multichainRouter, _amount);

        // The actual bridge call would be here, but implementation depends on Multichain's router interface
        // This is a placeholder for the bridge functionality
        // In production, you would call the appropriate Multichain router function
        // Example: IMultichainRouter(multichainRouter).anySwapOut(_token, _recipient, _amount, _destChainId);

        emit TokenBridged(_token, msg.sender, _amount, _destChainId, _recipient);
    }

    /**
     * @dev Emergency function to withdraw tokens stuck in the contract
     * @param _token Token to withdraw
     */
    function emergencyWithdraw(address _token) external onlyOwner {
        IERC20 token = IERC20(_token);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        token.safeTransfer(owner(), balance);
    }
}
```
