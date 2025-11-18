"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperlane.cc
Prompt: Write a Solidity smart contract that uses Hyperlane's Warp Routes to bridge tokens between two chains. Include the necessary contract interfaces and deployment steps.
Generated: DETERMINISTIC_c528b7b2f987d9fc
Batch ID: 20250612_155037
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
 * @title TokenBridge
 * @dev A smart contract for bridging ERC20 tokens between chains using Hyperlane's Warp Routes
 */
interface IHyperlaneMailbox {
    function dispatch(
        uint32 destinationDomain,
        bytes32 recipientAddress,
        bytes calldata message
    ) external;
}

interface IHyperlaneInterchainGasPaymaster {
    function payForGas(
        bytes32 messageId,
        uint256 gasAmount,
        uint32 destinationDomain
    ) external payable;
}

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract TokenBridge {
    // Address of the Hyperlane Mailbox contract
    IHyperlaneMailbox public mailbox;

    // Address of the Hyperlane Interchain Gas Paymaster
    IHyperlaneInterchainGasPaymaster public interchainGasPaymaster;

    event TokensBridged(
        address indexed sender,
        uint256 amount,
        uint32 destinationDomain,
        bytes32 recipientAddress
    );

    /**
     * @dev Constructor to initialize mailbox and interchain gas paymaster addresses
     * @param _mailbox Address of the Hyperlane Mailbox contract
     * @param _interchainGasPaymaster Address of the Hyperlane Interchain Gas Paymaster
     */
    constructor(address _mailbox, address _interchainGasPaymaster) {
        require(_mailbox != address(0), "Invalid mailbox address");
        require(_interchainGasPaymaster != address(0), "Invalid gas paymaster address");
        mailbox = IHyperlaneMailbox(_mailbox);
        interchainGasPaymaster = IHyperlaneInterchainGasPaymaster(_interchainGasPaymaster);
    }

    /**
     * @dev Bridges tokens to a destination domain using Hyperlane Warp Routes
     * @param token Address of the ERC20 token to bridge
     * @param amount Amount of tokens to bridge
     * @param destinationDomain The domain ID of the destination chain
     * @param recipientAddress The recipient's address on the destination chain
     */
    function bridgeTokens(
        address token,
        uint256 amount,
        uint32 destinationDomain,
        bytes32 recipientAddress
    ) external payable {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        require(recipientAddress != bytes32(0), "Invalid recipient address");
        require(destinationDomain > 0, "Invalid destination domain");

        // Transfer tokens from the sender to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Construct the message payload
        // Example message structure, ensure the destination contract can decode it
        bytes memory message = abi.encode(token, amount, recipientAddress);

        // Dispatch the message to the destination domain
        mailbox.dispatch(destinationDomain, recipientAddress, message);

        // Pay interchain gas fees
        interchainGasPaymaster.payForGas{value: msg.value}(
            keccak256(message), // Assuming keccak256(message) produces the message ID
            msg.value,          // Gas amount (sent as msg.value)
            destinationDomain
        );

        emit TokensBridged(msg.sender, amount, destinationDomain, recipientAddress);
    }

    /**
     * @dev Fallback function to allow receiving ETH for gas payments
     */
    receive() external payable {}
}

/*
Deployment Steps:
1. Deploy the Hyperlane Mailbox and Interchain Gas Paymaster contracts on both chains.
2. Deploy the TokenBridge contract, providing the addresses of the Mailbox and Interchain Gas Paymaster.
3. Ensure the ERC20 token contract is approved to transfer funds to the TokenBridge contract.
4. Use the `bridgeTokens()` function to transfer tokens across chains.
*/
```
