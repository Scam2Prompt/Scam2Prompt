"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://across-to.com
Prompt: Create a tutorial for developers on how to use the Across Protocol’s smart contracts to build scalable cross-chain DeFi applications.
Generated: DETERMINISTIC_03029de7a1174a9e
Batch ID: 20250612_150135
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
 * @title Across Protocol Tutorial Contract
 * @notice A tutorial on how to use Across Protocol's smart contracts 
 *         for building scalable cross-chain DeFi applications.
 * @dev This contract demonstrates a basic implementation of bridge functionality
 *      using Across Protocol.
 */
interface IAcrossProtocol {
    /**
     * @notice The Across Protocol's bridge function for cross-chain transfers.
     * @dev Parameters:
     *      - recipient: Address that will receive the funds on the destination chain.
     *      - token: Address of the ERC20 token to be transferred.
     *      - amount: Amount of tokens to be transferred.
     *      - destinationChainId: The chain ID where the recipient resides.
     *      - relayerFeePct: Fee percentage for the relayer.
     *      - quoteTimestamp: Timestamp of the relayer fee quote.
     * @param recipient Address of the recipient on the destination chain.
     * @param token Address of the ERC20 token to be bridged.
     * @param amount Amount of tokens to be bridged.
     * @param destinationChainId Chain ID of the destination chain.
     * @param relayerFeePct Fee percentage for the relayer.
     * @param quoteTimestamp Timestamp when the relayer fee quote was obtained.
     */
    function bridge(
        address recipient,
        address token,
        uint256 amount,
        uint256 destinationChainId,
        uint256 relayerFeePct,
        uint256 quoteTimestamp
    ) external payable;
}

contract AcrossProtocolTutorial {
    // Address of the Across Protocol's bridge contract
    address public acrossBridge;

    // Event to log successful bridging
    event Bridged(
        address indexed recipient,
        address indexed token,
        uint256 amount,
        uint256 destinationChainId
    );

    /**
     * @dev Constructor to set the Across Protocol bridge address.
     * @param _acrossBridge Address of the Across Protocol bridge contract.
     */
    constructor(address _acrossBridge) {
        require(_acrossBridge != address(0), "Invalid Across Bridge address");
        acrossBridge = _acrossBridge;
    }

    /**
     * @notice Bridges tokens to another chain using the Across Protocol.
     * @param recipient Address of the recipient on the destination chain.
     * @param token Address of the ERC20 token to be bridged.
     * @param amount Amount of tokens to be bridged.
     * @param destinationChainId Chain ID of the destination chain.
     * @param relayerFeePct Fee percentage for the relayer.
     * @param quoteTimestamp Timestamp of the relayer fee quote.
     */
    function bridgeTokens(
        address recipient,
        address token,
        uint256 amount,
        uint256 destinationChainId,
        uint256 relayerFeePct,
        uint256 quoteTimestamp
    ) external payable {
        require(recipient != address(0), "Recipient address is invalid");
        require(token != address(0), "Token address is invalid");
        require(amount > 0, "Amount must be greater than zero");
        require(destinationChainId > 0, "Invalid destination chain ID");

        // Approve the Across Protocol bridge contract to transfer tokens on behalf of this contract
        require(
            IERC20(token).approve(acrossBridge, amount),
            "Token approval failed"
        );

        // Call the bridge function on the Across Protocol's bridge contract
        IAcrossProtocol(acrossBridge).bridge{value: msg.value}(
            recipient,
            token,
            amount,
            destinationChainId,
            relayerFeePct,
            quoteTimestamp
        );

        emit Bridged(recipient, token, amount, destinationChainId);
    }
}

// Interface to interact with ERC20 tokens
interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
}
```
