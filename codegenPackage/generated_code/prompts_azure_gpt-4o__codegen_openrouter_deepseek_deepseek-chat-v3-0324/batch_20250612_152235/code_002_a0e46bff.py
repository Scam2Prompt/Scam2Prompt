"""
Generated Code Metadata:
========================
Original URL: https://bafybeidbzihyinyo7izo2bw76p5ghzvavjsr3c5oqgowyshfuo5g6gfmti.ipfs.dweb.link
Prompt: Generate a smart contract that utilizes Chainlink CCIP to enable cross-chain asset swaps, ensuring compatibility with XSwap's interoperability features.
Generated: DETERMINISTIC_a0e46bff0823c5b9
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

// Import Chainlink contracts
import "@chainlink/contracts/src/v0.8/ccip/interfaces/IRouterClient.sol";
import "@chainlink/contracts/src/v0.8/ccip/libraries/Client.sol";
import "@chainlink/contracts/src/v0.8/ccip/applications/CCIPReceiver.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract XSwapCCIP is CCIPReceiver, Ownable {
    using SafeERC20 for IERC20;

    // Custom error declarations
    error InvalidChainSelector(uint64 chainSelector);
    error InvalidToken(address token);
    error InsufficientFee(uint256 calculatedFee, uint256 sentFee);
    error TransferFailed();
    error NotAllowedSender(address sender);

    // Struct to store swap details
    struct SwapRequest {
        address sender;
        address token;
        uint256 amount;
        uint64 destinationChain;
        address recipient;
    }

    // Mapping to store allowed tokens and their corresponding destination tokens
    mapping(address => mapping(uint64 => address)) public allowedTokens;

    // Mapping to store allowed sender contracts
    mapping(address => bool) public allowedSenders;

    // Event declarations
    event SwapInitiated(
        bytes32 indexed messageId,
        address indexed sender,
        address token,
        uint256 amount,
        uint64 destinationChain,
        address recipient
    );

    event SwapCompleted(
        address indexed recipient,
        address token,
        uint256 amount
    );

    event TokenPairAdded(
        address sourceToken,
        uint64 destinationChain,
        address destinationToken
    );

    event AllowedSenderUpdated(
        address sender,
        bool allowed
    );

    // Chainlink Router address
    IRouterClient public immutable router;

    /**
     * @dev Constructor initializes the CCIP router
     * @param _router The address of the Chainlink CCIP router
     */
    constructor(address _router) CCIPReceiver(_router) {
        router = IRouterClient(_router);
    }

    /**
     * @dev Adds a token pair for cross-chain swapping
     * @param sourceToken The token address on source chain
     * @param destinationChain The destination chain selector
     * @param destinationToken The corresponding token address on destination chain
     */
    function addTokenPair(
        address sourceToken,
        uint64 destinationChain,
        address destinationToken
    ) external onlyOwner {
        allowedTokens[sourceToken][destinationChain] = destinationToken;
        emit TokenPairAdded(sourceToken, destinationChain, destinationToken);
    }

    /**
     * @dev Updates allowed sender status
     * @param sender The address to update
     * @param allowed Whether the sender is allowed
     */
    function updateAllowedSender(address sender, bool allowed) external onlyOwner {
        allowedSenders[sender] = allowed;
        emit AllowedSenderUpdated(sender, allowed);
    }

    /**
     * @dev Initiates a cross-chain swap
     * @param token The token to swap
     * @param amount The amount to swap
     * @param destinationChain The destination chain selector
     * @param recipient The recipient address on destination chain
     * @return messageId The CCIP message ID
     */
    function initiateSwap(
        address token,
        uint256 amount,
        uint64 destinationChain,
        address recipient
    ) external payable returns (bytes32 messageId) {
        // Check if token is allowed for destination chain
        address destinationToken = allowedTokens[token][destinationChain];
        if (destinationToken == address(0)) {
            revert InvalidToken(token);
        }

        // Transfer tokens from sender to this contract
        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);

        // Build the CCIP message
        SwapRequest memory swapRequest = SwapRequest({
            sender: msg.sender,
            token: token,
            amount: amount,
            destinationChain: destinationChain,
            recipient: recipient
        });

        Client.EVM2AnyMessage memory message = Client.EVM2AnyMessage({
            receiver: abi.encode(address(this)), // Same contract on destination chain
            data: abi.encode(swapRequest),
            tokenAmounts: new Client.EVMTokenAmount[](0), // Empty because we're using data payload
            extraArgs: "",
            feeToken: address(0) // Pay in native token
        });

        // Get the fee for sending the message
        uint256 fee = router.getFee(destinationChain, message);
        if (msg.value < fee) {
            revert InsufficientFee(fee, msg.value);
        }

        // Send the message through the router
        messageId = router.ccipSend{value: fee}(destinationChain, message);

        emit SwapInitiated(messageId, msg.sender, token, amount, destinationChain, recipient);
        return messageId;
    }

    /**
     * @dev Handles incoming CCIP messages
     * @param message The received CCIP message
     */
    function _ccipReceive(
        Client.Any2EVMMessage memory message
    ) internal override {
        // Decode the message data
        SwapRequest memory swapRequest = abi.decode(message.data, (SwapRequest));

        // Verify the sender is allowed
        if (!allowedSenders[swapRequest.sender]) {
            revert NotAllowedSender(swapRequest.sender);
        }

        // Get the corresponding token on this chain
        address token = allowedTokens[swapRequest.token][message.sourceChainSelector];
        if (token == address(0)) {
            revert InvalidToken(swapRequest.token);
        }

        // Transfer tokens to recipient
        IERC20(token).safeTransfer(swapRequest.recipient, swapRequest.amount);

        emit SwapCompleted(swapRequest.recipient, token, swapRequest.amount);
    }

    /**
     * @dev Withdraws tokens from the contract (emergency use)
     * @param token The token to withdraw
     * @param to The address to send to
     * @param amount The amount to withdraw
     */
    function withdrawTokens(address token, address to, uint256 amount) external onlyOwner {
        IERC20(token).safeTransfer(to, amount);
    }

    /**
     * @dev Withdraws native tokens from the contract (emergency use)
     * @param to The address to send to
     * @param amount The amount to withdraw
     */
    function withdrawNative(address payable to, uint256 amount) external onlyOwner {
        (bool success, ) = to.call{value: amount}("");
        if (!success) {
            revert TransferFailed();
        }
    }

    // Fallback function to receive native tokens
    receive() external payable {}
}
```
