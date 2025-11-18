"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remoteprocurator.pages.dev
Prompt: Write a smart contract that utilizes Multichain's MPC (Multi-Party Computation) for secure cross-chain bridging of tokens.
Generated: DETERMINISTIC_cfd0d36bf5f0c99d
Batch ID: 20250612_145821
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
 * @title CrossChainBridge
 * @notice A secure cross-chain bridge leveraging Multichain's MPC (Multi-Party Computation)
 * for token bridging across multiple blockchains.
 */
contract CrossChainBridge {
    // Address of the Multichain MPC wallet
    address public mpcWallet;

    // Event emitted when tokens are bridged to another chain
    event TokensBridged(
        address indexed sender,
        address indexed token,
        uint256 amount,
        uint256 destinationChainId,
        string recipientAddress
    );

    // Event emitted when tokens are received from another chain
    event TokensReceived(
        address indexed recipient,
        address indexed token,
        uint256 amount,
        uint256 sourceChainId
    );

    // Error for unauthorized operations
    error Unauthorized();

    // Modifier to restrict access to the MPC wallet
    modifier onlyMPC() {
        if (msg.sender != mpcWallet) revert Unauthorized();
        _;
    }

    /**
     * @notice Constructor to initialize the MPC wallet address.
     * @param _mpcWallet Address of the Multichain MPC wallet.
     */
    constructor(address _mpcWallet) {
        require(_mpcWallet != address(0), "Invalid MPC wallet address");
        mpcWallet = _mpcWallet;
    }

    /**
     * @notice Function to bridge tokens to another chain.
     * @param token Address of the token to be bridged.
     * @param amount Amount of tokens to bridge.
     * @param destinationChainId Chain ID of the destination chain.
     * @param recipientAddress Address of the recipient on the destination chain.
     */
    function bridgeTokens(
        address token,
        uint256 amount,
        uint256 destinationChainId,
        string calldata recipientAddress
    ) external {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        require(bytes(recipientAddress).length > 0, "Invalid recipient address");

        // Transfer tokens from the sender to the contract
        bool success = IERC20(token).transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Emit event for bridging tokens
        emit TokensBridged(msg.sender, token, amount, destinationChainId, recipientAddress);
    }

    /**
     * @notice Function to receive tokens from another chain. Can only be called by the MPC wallet.
     * @param token Address of the token being received.
     * @param recipient Address of the recipient on this chain.
     * @param amount Amount of tokens received.
     * @param sourceChainId Chain ID of the source chain.
     */
    function receiveTokens(
        address token,
        address recipient,
        uint256 amount,
        uint256 sourceChainId
    ) external onlyMPC {
        require(token != address(0), "Invalid token address");
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the contract to the recipient
        bool success = IERC20(token).transfer(recipient, amount);
        require(success, "Token transfer failed");

        // Emit event for receiving tokens
        emit TokensReceived(recipient, token, amount, sourceChainId);
    }

    /**
     * @notice Updates the MPC wallet address. Can only be called by the existing MPC wallet.
     * @param newMPCWallet Address of the new MPC wallet.
     */
    function updateMPCWallet(address newMPCWallet) external onlyMPC {
        require(newMPCWallet != address(0), "Invalid MPC wallet address");
        mpcWallet = newMPCWallet;
    }
}

/**
 * @dev Minimal ERC20 interface for token interaction.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
