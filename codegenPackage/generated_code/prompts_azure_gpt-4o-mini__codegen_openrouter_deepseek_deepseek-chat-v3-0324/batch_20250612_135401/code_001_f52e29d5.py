"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-hdttyws0p-offchain-labs.vercel.app
Prompt: What are the unique features of the Arbitrum token bridge, and how can I implement them in my dApp?
Generated: DETERMINISTIC_f52e29d5e7660532
Batch ID: 20250612_135401
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@arbitrum/nitro-contracts/src/bridge/IInbox.sol";
import "@arbitrum/nitro-contracts/src/bridge/IOutbox.sol";

/**
 * @title ArbitrumTokenBridge
 * @dev Implements the core functionality for bridging ERC20 tokens between Ethereum and Arbitrum
 */
contract ArbitrumTokenBridge is ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Arbitrum contracts
    address public immutable inbox;
    address public l2TokenBridge;
    
    // Token mappings
    mapping(address => address) public l1ToL2Token;
    mapping(address => address) public l2ToL1Token;

    // Events
    event TokenDepositInitiated(
        address indexed l1Token,
        address indexed l2Token,
        address indexed from,
        address to,
        uint256 amount,
        bytes data
    );

    event TokenWithdrawalInitiated(
        address indexed l2Token,
        address indexed l1Token,
        address indexed from,
        address to,
        uint256 amount,
        bytes data
    );

    /**
     * @dev Constructor initializes the Arbitrum inbox address
     * @param _inbox Address of the Arbitrum Inbox contract
     */
    constructor(address _inbox) {
        require(_inbox != address(0), "Invalid inbox address");
        inbox = _inbox;
    }

    /**
     * @dev Sets the L2 token bridge address
     * @param _l2TokenBridge Address of the L2 token bridge contract
     */
    function setL2TokenBridge(address _l2TokenBridge) external {
        require(l2TokenBridge == address(0), "L2 bridge already set");
        l2TokenBridge = _l2TokenBridge;
    }

    /**
     * @dev Registers a token pair between L1 and L2
     * @param l1Token Address of the L1 token
     * @param l2Token Address of the L2 token
     */
    function registerTokenPair(address l1Token, address l2Token) external {
        require(l1Token != address(0) && l2Token != address(0), "Invalid token address");
        require(l1ToL2Token[l1Token] == address(0), "Token already registered");
        
        l1ToL2Token[l1Token] = l2Token;
        l2ToL1Token[l2Token] = l1Token;
    }

    /**
     * @dev Deposits tokens from L1 to L2
     * @param l1Token Address of the L1 token
     * @param amount Amount of tokens to deposit
     * @param l2Recipient Address to receive tokens on L2
     * @param maxGas Max gas for L2 execution
     * @param gasPriceBid Gas price bid for L2 execution
     * @param data Additional data
     */
    function depositTokens(
        address l1Token,
        uint256 amount,
        address l2Recipient,
        uint256 maxGas,
        uint256 gasPriceBid,
        bytes calldata data
    ) external payable nonReentrant {
        require(l1Token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be positive");
        require(l2Recipient != address(0), "Invalid recipient address");
        
        address l2Token = l1ToL2Token[l1Token];
        require(l2Token != address(0), "Token not registered");

        // Transfer tokens from user to bridge
        IERC20(l1Token).safeTransferFrom(msg.sender, address(this), amount);

        // Encode the deposit data
        bytes memory depositData = abi.encodeWithSelector(
            this.finalizeDeposit.selector,
            l1Token,
            l2Token,
            msg.sender,
            l2Recipient,
            amount,
            data
        );

        // Create retryable ticket to L2
        IInbox(inbox).createRetryableTicket{value: msg.value}(
            l2TokenBridge,
            0, // no value transfer
            maxGas,
            gasPriceBid,
            depositData
        );

        emit TokenDepositInitiated(l1Token, l2Token, msg.sender, l2Recipient, amount, data);
    }

    /**
     * @dev Finalizes token deposit on L2 (called from L2)
     * @param l1Token Address of the L1 token
     * @param l2Token Address of the L2 token
     * @param from Address sending tokens
     * @param to Address receiving tokens
     * @param amount Amount of tokens
     * @param data Additional data
     */
    function finalizeDeposit(
        address l1Token,
        address l2Token,
        address from,
        address to,
        uint256 amount,
        bytes calldata data
    ) external {
        require(msg.sender == l2TokenBridge, "Only L2 bridge can call");
        require(l1Token != address(0) && l2Token != address(0), "Invalid token address");
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be positive");

        // In a real implementation, this would mint tokens on L2
        // This is just a placeholder for the L2 logic
    }

    /**
     * @dev Initiates token withdrawal from L2 to L1
     * @param l2Token Address of the L2 token
     * @param amount Amount of tokens to withdraw
     * @param l1Recipient Address to receive tokens on L1
     * @param data Additional data
     */
    function initiateWithdrawal(
        address l2Token,
        uint256 amount,
        address l1Recipient,
        bytes calldata data
    ) external {
        // This function would be called from L2
        // In a real implementation, this would burn tokens on L2 and send a message to L1
    }

    /**
     * @dev Finalizes token withdrawal on L1 (called from L1)
     * @param l2Token Address of the L2 token
     * @param l1Token Address of the L1 token
     * @param from Address sending tokens
     * @param to Address receiving tokens
     * @param amount Amount of tokens
     * @param data Additional data
     */
    function finalizeWithdrawal(
        address l2Token,
        address l1Token,
        address from,
        address to,
        uint256 amount,
        bytes calldata data
    ) external nonReentrant {
        require(msg.sender == address(IOutbox(IInbox(inbox).bridge()).l2ToL1Sender()), "Only from outbox");
        require(l1Token != address(0) && l2Token != address(0), "Invalid token address");
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be positive");

        // Transfer tokens to recipient
        IERC20(l1Token).safeTransfer(to, amount);

        emit TokenWithdrawalInitiated(l2Token, l1Token, from, to, amount, data);
    }
}
```
