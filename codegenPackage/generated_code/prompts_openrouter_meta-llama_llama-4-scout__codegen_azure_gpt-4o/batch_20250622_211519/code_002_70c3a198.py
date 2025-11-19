"""
Generated Code Metadata:
========================
Original URL: https://asdasdaw123122.pages.dev
Prompt: Design a smart contract on Ethereum that utilizes Multichain's Router protocol to swap tokens between Ethereum and Binance Smart Chain.
Generated: DETERMINISTIC_70c3a198d1ca8267
Batch ID: 20250622_211519
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

/**
 * @title CrossChainTokenSwap
 * @dev A smart contract to swap tokens between Ethereum and Binance Smart Chain using Multichain's Router protocol.
 */
interface IMultichainRouter {
    function anySwapOut(
        address token,
        string calldata to,
        uint256 amount,
        uint256 toChainID
    ) external;

    function anySwapOutUnderlying(
        address token,
        string calldata to,
        uint256 amount,
        uint256 toChainID
    ) external;
}

contract CrossChainTokenSwap {
    // Address of the Multichain Router contract
    address public multichainRouter;

    // Event emitted when a token swap is initiated
    event TokenSwapInitiated(
        address indexed sender,
        address indexed token,
        string to,
        uint256 amount,
        uint256 toChainID
    );

    /**
     * @dev Constructor to set the Multichain Router address.
     * @param _multichainRouter Address of the Multichain Router contract.
     */
    constructor(address _multichainRouter) {
        require(_multichainRouter != address(0), "Invalid router address");
        multichainRouter = _multichainRouter;
    }

    /**
     * @dev Initiates a token swap to another chain using Multichain's Router protocol.
     * @param token Address of the token to be swapped.
     * @param to Address on the destination chain to receive the tokens (as a string).
     * @param amount Amount of tokens to swap.
     * @param toChainID Chain ID of the destination chain.
     */
    function swapTokens(
        address token,
        string calldata to,
        uint256 amount,
        uint256 toChainID
    ) external {
        require(token != address(0), "Invalid token address");
        require(bytes(to).length > 0, "Invalid destination address");
        require(amount > 0, "Amount must be greater than zero");
        require(toChainID > 0, "Invalid destination chain ID");

        // Transfer tokens from the sender to this contract
        require(
            IERC20(token).transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Approve the Multichain Router to spend the tokens
        require(
            IERC20(token).approve(multichainRouter, amount),
            "Token approval failed"
        );

        // Call Multichain's Router to initiate the swap
        IMultichainRouter(multichainRouter).anySwapOut(
            token,
            to,
            amount,
            toChainID
        );

        // Emit an event for the swap
        emit TokenSwapInitiated(msg.sender, token, to, amount, toChainID);
    }

    /**
     * @dev Fallback function to receive ETH (if needed for gas fees on the destination chain).
     */
    receive() external payable {}

    /**
     * @dev Withdraw any accidentally sent ETH to the contract.
     * @param to Address to send the ETH to.
     */
    function withdrawETH(address payable to) external {
        require(to != address(0), "Invalid address");
        require(address(this).balance > 0, "No ETH to withdraw");

        to.transfer(address(this).balance);
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function approve(address spender, uint256 amount) external returns (bool);
}
```
