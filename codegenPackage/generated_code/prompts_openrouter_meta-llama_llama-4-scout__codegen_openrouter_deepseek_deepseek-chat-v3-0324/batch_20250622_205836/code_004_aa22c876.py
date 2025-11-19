"""
Generated Code Metadata:
========================
Original URL: https://bafybeidbzihyinyo7izo2bw76p5ghzvavjsr3c5oqgowyshfuo5g6gfmti.ipfs.dweb.link
Prompt: Develop a simple smart contract using Solidity that utilizes Chainlink CCIP for secure cross-chain messages and token transfers, suitable for the XSwap protocol.
Generated: DETERMINISTIC_aa22c87600e7fec7
Batch ID: 20250622_205836
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

import "@chainlink/contracts/src/v0.8/ccip/CCIPReceiver.sol";
import "@chainlink/contracts/src/v0.8/ccip/interfaces/IRouterClient.sol";
import "@chainlink/contracts/src/v0.8/ccip/interfaces/IAny2EVMMessageReceiver.sol";
import "@chainlink/contracts/src/v0.8/ccip/libraries/Client.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract XSwapCCIP is CCIPReceiver, Ownable {
    using SafeERC20 for IERC20;

    // Custom errors
    error InvalidMessage(bytes32 messageId);
    error TransferFailed();
    error InsufficientFee();
    error UnsupportedChain(uint64 chainSelector);

    // Events
    event TokensSwapped(
        bytes32 indexed messageId,
        address indexed from,
        address indexed token,
        uint256 amount,
        uint64 destinationChain
    );
    event TokensReceived(
        bytes32 indexed messageId,
        address indexed to,
        address indexed token,
        uint256 amount,
        uint64 sourceChain
    );
    event ChainSupportUpdated(uint64 chainSelector, bool isSupported);

    // Chainlink CCIP Router
    IRouterClient public immutable router;

    // Supported chains for cross-chain swaps
    mapping(uint64 => bool) public supportedChains;

    // Message ID to token transfer details
    mapping(bytes32 => address) public messageToToken;
    mapping(bytes32 => address) public messageToRecipient;
    mapping(bytes32 => uint256) public messageToAmount;

    constructor(address _router) CCIPReceiver(_router) {
        router = IRouterClient(_router);
    }

    /**
     * @notice Swap tokens to another chain
     * @param destinationChainSelector The destination chain ID
     * @param recipient The recipient address on the destination chain
     * @param token The token address to swap
     * @param amount The amount of tokens to swap
     */
    function swapTokens(
        uint64 destinationChainSelector,
        address recipient,
        address token,
        uint256 amount
    ) external payable {
        if (!supportedChains[destinationChainSelector]) {
            revert UnsupportedChain(destinationChainSelector);
        }

        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);

        Client.EVMTokenAmount[] memory tokenAmounts = new Client.EVMTokenAmount[](1);
        tokenAmounts[0] = Client.EVMTokenAmount({
            token: token,
            amount: amount
        });

        Client.EVM2AnyMessage memory message = Client.EVM2AnyMessage({
            receiver: abi.encode(address(this)), // Same contract on destination chain
            data: abi.encode(recipient),
            tokenAmounts: tokenAmounts,
            extraArgs: "",
            feeToken: address(0), // Pay fees in native token
            feeAmount: msg.value
        });

        bytes32 messageId = router.ccipSend(destinationChainSelector, message);
        
        messageToToken[messageId] = token;
        messageToRecipient[messageId] = recipient;
        messageToAmount[messageId] = amount;

        emit TokensSwapped(messageId, msg.sender, token, amount, destinationChainSelector);
    }

    /**
     * @notice Handle a received message from CCIP
     * @param message The CCIP message
     */
    function _ccipReceive(
        Client.Any2EVMMessage memory message
    ) internal override {
        bytes32 messageId = message.messageId;
        uint64 sourceChainSelector = message.sourceChainSelector;

        if (!supportedChains[sourceChainSelector]) {
            revert UnsupportedChain(sourceChainSelector);
        }

        if (message.tokenAmounts.length == 0) {
            revert InvalidMessage(messageId);
        }

        address token = message.tokenAmounts[0].token;
        uint256 amount = message.tokenAmounts[0].amount;
        address recipient = abi.decode(message.data, (address));

        IERC20(token).safeTransfer(recipient, amount);

        emit TokensReceived(messageId, recipient, token, amount, sourceChainSelector);
    }

    /**
     * @notice Update supported chains
     * @param chainSelector The chain ID
     * @param isSupported Whether the chain is supported
     */
    function updateChainSupport(uint64 chainSelector, bool isSupported) external onlyOwner {
        supportedChains[chainSelector] = isSupported;
        emit ChainSupportUpdated(chainSelector, isSupported);
    }

    /**
     * @notice Withdraw tokens from the contract
     * @param token The token address to withdraw
     * @param amount The amount to withdraw
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).safeTransfer(owner(), amount);
    }

    /**
     * @notice Withdraw native tokens from the contract
     * @param amount The amount to withdraw
     */
    function withdrawNative(uint256 amount) external onlyOwner {
        payable(owner()).transfer(amount);
    }

    // Fallback function to receive native tokens
    receive() external payable {}
}
```
