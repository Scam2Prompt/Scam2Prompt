"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rusfanat.ru
Prompt: Write a smart contract that integrates Hop Protocol for enabling automated cross-chain token swaps between ERC-20 tokens.
Generated: DETERMINISTIC_e6b0ffd3e42bfa82
Batch ID: 20250612_153809
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
 * @title CrossChainSwap
 * @dev This smart contract uses the Hop Protocol to perform automated cross-chain ERC-20 token swaps.
 * Users can deposit tokens on one chain and receive tokens on another chain using Hop Protocol bridges.
 */

interface IHopBridge {
    function sendToL2(
        uint256 amount,
        uint256 minAmountOut,
        address recipient,
        uint256 deadline,
        address relayer,
        uint256 relayerFee
    ) external;
    
    function sendToL1(
        uint256 amount,
        uint256 minAmountOut,
        address recipient,
        uint256 deadline
    ) external;
}

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract CrossChainSwap {
    address public owner;

    // Mapping of Hop Bridge contract addresses by token and chain
    mapping(address => mapping(uint256 => address)) public hopBridges;

    event CrossChainSwapInitiated(
        address indexed sender,
        address indexed token,
        uint256 amount,
        uint256 destinationChainId,
        address recipient
    );

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Adds or updates the Hop Bridge address for a specific token and chain.
     * @param token The ERC-20 token address.
     * @param chainId The destination chain ID.
     * @param bridge The Hop Bridge contract address.
     */
    function setHopBridge(
        address token,
        uint256 chainId,
        address bridge
    ) external onlyOwner {
        require(bridge != address(0), "Invalid bridge address");
        hopBridges[token][chainId] = bridge;
    }

    /**
     * @dev Initiates a cross-chain token swap using the Hop Protocol.
     * @param token The ERC-20 token address.
     * @param amount The amount of tokens to swap.
     * @param destinationChainId The destination chain ID.
     * @param recipient The recipient address on the destination chain.
     * @param minAmountOut The minimum amount of tokens to receive on the destination chain.
     * @param deadline The deadline for the swap.
     * @param relayer The relayer address (optional; can be set to address(0)).
     * @param relayerFee The relayer fee (optional; can be set to 0).
     */
    function swapToChain(
        address token,
        uint256 amount,
        uint256 destinationChainId,
        address recipient,
        uint256 minAmountOut,
        uint256 deadline,
        address relayer,
        uint256 relayerFee
    ) external {
        // Validate inputs
        require(hopBridges[token][destinationChainId] != address(0), "Bridge not set for token and chain");
        require(amount > 0, "Invalid amount");
        require(recipient != address(0), "Invalid recipient");

        // Get the Hop Bridge contract
        address bridge = hopBridges[token][destinationChainId];

        // Transfer tokens from the sender to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Approve the Hop Bridge contract to spend tokens
        IERC20(token).approve(bridge, amount);

        // Send tokens to the destination chain via Hop Protocol
        if (relayer != address(0)) {
            IHopBridge(bridge).sendToL2(
                amount,
                minAmountOut,
                recipient,
                deadline,
                relayer,
                relayerFee
            );
        } else {
            IHopBridge(bridge).sendToL1(
                amount,
                minAmountOut,
                recipient,
                deadline
            );
        }

        emit CrossChainSwapInitiated(msg.sender, token, amount, destinationChainId, recipient);
    }

    /**
     * @dev Withdraws ERC-20 tokens accidentally sent to the contract.
     * @param token The ERC-20 token address.
     * @param recipient The recipient address for the tokens.
     */
    function withdrawTokens(address token, address recipient) external onlyOwner {
        uint256 balance = IERC20(token).balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        IERC20(token).transfer(recipient, balance);
    }
}
```
