"""
Generated Code Metadata:
========================
Original URL: https://bafybeidbzihyinyo7izo2bw76p5ghzvavjsr3c5oqgowyshfuo5g6gfmti.ipfs.dweb.link
Prompt: Write a code snippet using Chainlink CCIP to implement secure cross-chain token transfers, referencing the XSwap protocol for fluid cross-chain liquidity.
Generated: DETERMINISTIC_d68edc3ae2e54b31
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
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/ccip/CCIPReceiver.sol";
import "@chainlink/contracts/src/v0.8/ccip/interfaces/IAny2EVMMessageReceiver.sol";
import "@chainlink/contracts/src/v0.8/ccip/libraries/Client.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract XSwapCCIP is CCIPReceiver, Ownable {
    using SafeERC20 for IERC20;

    // Chainlink CCIP Router address
    address public ccipRouter;

    // Supported tokens mapping (chainId => tokenAddress => isSupported)
    mapping(uint64 => mapping(address => bool)) public supportedTokens;

    // XSwap protocol address for liquidity management
    address public xSwapProtocol;

    // Event emitted when tokens are sent cross-chain
    event TokensSent(
        uint64 destinationChainId,
        address token,
        address recipient,
        uint256 amount,
        bytes32 messageId
    );

    // Event emitted when tokens are received cross-chain
    event TokensReceived(
        uint64 sourceChainId,
        address token,
        address recipient,
        uint256 amount,
        bytes32 messageId
    );

    /**
     * @dev Constructor initializes the CCIP receiver and sets the router
     * @param _router The address of the CCIP router
     * @param _xSwapProtocol The address of the XSwap protocol
     */
    constructor(address _router, address _xSwapProtocol) CCIPReceiver(_router) {
        require(_router != address(0), "Invalid router address");
        require(_xSwapProtocol != address(0), "Invalid XSwap address");
        ccipRouter = _router;
        xSwapProtocol = _xSwapProtocol;
    }

    /**
     * @dev Adds a supported token for cross-chain transfers
     * @param chainId The destination chain ID
     * @param tokenAddress The token contract address
     */
    function addSupportedToken(uint64 chainId, address tokenAddress) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        supportedTokens[chainId][tokenAddress] = true;
    }

    /**
     * @dev Removes a supported token for cross-chain transfers
     * @param chainId The destination chain ID
     * @param tokenAddress The token contract address
     */
    function removeSupportedToken(uint64 chainId, address tokenAddress) external onlyOwner {
        require(supportedTokens[chainId][tokenAddress], "Token not supported");
        supportedTokens[chainId][tokenAddress] = false;
    }

    /**
     * @dev Initiates a cross-chain token transfer
     * @param destinationChainId The destination chain ID
     * @param token The token contract address
     * @param recipient The recipient address on the destination chain
     * @param amount The amount of tokens to transfer
     */
    function sendTokens(
        uint64 destinationChainId,
        address token,
        address recipient,
        uint256 amount
    ) external payable {
        require(supportedTokens[destinationChainId][token], "Token not supported on destination chain");
        require(amount > 0, "Amount must be greater than 0");
        require(recipient != address(0), "Invalid recipient address");

        // Transfer tokens from sender to this contract
        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);

        // Build CCIP message
        Client.EVM2AnyMessage memory message = Client.EVM2AnyMessage({
            receiver: abi.encode(address(this)), // This contract will receive on destination
            data: abi.encode(token, recipient, amount),
            tokenAmounts: new Client.EVMTokenAmount[](0), // Using data field instead for flexibility
            extraArgs: "",
            feeToken: address(0) // Paying fees in native token
        });

        // Get fee from router
        uint256 fee = IRouterClient(ccipRouter).getFee(destinationChainId, message);
        require(msg.value >= fee, "Insufficient fee");

        // Send message via CCIP
        bytes32 messageId = IRouterClient(ccipRouter).ccipSend{value: fee}(
            destinationChainId,
            message
        );

        emit TokensSent(destinationChainId, token, recipient, amount, messageId);
    }

    /**
     * @dev Handles incoming CCIP messages
     * @param message The received CCIP message
     */
    function _ccipReceive(Client.Any2EVMMessage memory message) internal override {
        // Decode the message data
        (address token, address recipient, uint256 amount) = abi.decode(
            message.data,
            (address, address, uint256)
        );

        require(supportedTokens[message.sourceChainId][token], "Token not supported");
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Invalid amount");

        // Transfer tokens to recipient
        IERC20(token).safeTransfer(recipient, amount);

        emit TokensReceived(
            message.sourceChainId,
            token,
            recipient,
            amount,
            message.messageId
        );
    }

    /**
     * @dev Withdraws tokens from the contract (emergency use)
     * @param token The token contract address
     * @param amount The amount to withdraw
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).safeTransfer(owner(), amount);
    }

    /**
     * @dev Updates the XSwap protocol address
     * @param _xSwapProtocol The new XSwap protocol address
     */
    function updateXSwapProtocol(address _xSwapProtocol) external onlyOwner {
        require(_xSwapProtocol != address(0), "Invalid XSwap address");
        xSwapProtocol = _xSwapProtocol;
    }

    // Fallback function to receive native tokens (for fee payments)
    receive() external payable {}
}
```
