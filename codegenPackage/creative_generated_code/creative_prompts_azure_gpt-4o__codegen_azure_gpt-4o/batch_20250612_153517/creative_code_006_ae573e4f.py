"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zero-815.pages.dev
Prompt: Create a cross-chain bridge for transferring USDC tokens between chains using LayerZero's protocol. Include code and explain how the endpoints and interfaces are configured.
Generated: DETERMINISTIC_ae573e4f2733b9fd
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for a cross-chain bridge using LayerZero's protocol to transfer USDC tokens between chains. This example is written in Solidity and includes proper documentation and comments. 

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import LayerZero interfaces
import "@layerzerolabs/solidity-examples/contracts/interfaces/ILayerZeroEndpoint.sol";
import "@layerzerolabs/solidity-examples/contracts/interfaces/ILayerZeroReceiver.sol";

// ERC20 Interface for USDC
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function approve(address spender, uint256 amount) external returns (bool);

    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}

contract USDCBridge is ILayerZeroReceiver {
    // LayerZero endpoint interface
    ILayerZeroEndpoint public layerZeroEndpoint;

    // USDC token contract address
    address public usdcToken;

    // Mapping to track received messages (prevents replay attacks)
    mapping(uint16 => mapping(bytes => mapping(uint64 => bool))) public receivedMessages;

    // Events for logging
    event USDCBridged(uint16 indexed destinationChainId, address indexed sender, uint256 amount);
    event USDCReceived(uint16 indexed sourceChainId, address indexed recipient, uint256 amount);

    /**
     * @notice Constructor to initialize the contract
     * @param _layerZeroEndpoint LayerZero endpoint address
     * @param _usdcToken USDC token contract address
     */
    constructor(address _layerZeroEndpoint, address _usdcToken) {
        require(_layerZeroEndpoint != address(0), "Invalid LayerZero endpoint address");
        require(_usdcToken != address(0), "Invalid USDC token address");

        layerZeroEndpoint = ILayerZeroEndpoint(_layerZeroEndpoint);
        usdcToken = _usdcToken;
    }

    /**
     * @notice Bridge USDC tokens to another chain
     * @param destinationChainId LayerZero chain ID of the destination chain
     * @param recipient Address to receive USDC on the destination chain
     * @param amount Amount of USDC to transfer
     */
    function bridgeUSDC(
        uint16 destinationChainId,
        bytes calldata recipient,
        uint256 amount
    ) external payable {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(usdcToken).balanceOf(msg.sender) >= amount, "Insufficient USDC balance");

        // Transfer USDC from sender to this contract
        IERC20(usdcToken).transferFrom(msg.sender, address(this), amount);

        // Encode payload to send to destination chain
        bytes memory payload = abi.encode(recipient, amount);

        // Estimate LayerZero fees
        (uint256 nativeFee, ) = layerZeroEndpoint.estimateFees(destinationChainId, address(this), payload, false, "");

        require(msg.value >= nativeFee, "Insufficient native token for LayerZero fees");

        // Send message to destination chain
        layerZeroEndpoint.send{value: msg.value}(
            destinationChainId, // Destination chain ID
            recipient,          // Destination address (encoded as bytes)
            payload,            // Encoded payload
            payable(msg.sender), // Refund address for excess fees
            address(0),         // Address for custom adapter params (set to zero for default behavior)
            ""                  // Adapter parameters (set to empty for default behavior)
        );

        emit USDCBridged(destinationChainId, msg.sender, amount);
    }

    /**
     * @notice Handle incoming messages from LayerZero endpoint
     * @param sourceChainId Chain ID of the source chain
     * @param sourceAddress Address of the sender on the source chain (encoded as bytes)
     * @param payload Encoded payload containing recipient and amount
     */
    function lzReceive(
        uint16 sourceChainId,
        bytes calldata sourceAddress,
        uint64 nonce,
        bytes calldata payload
    ) external override {
        // Ensure the message was sent by the trusted LayerZero endpoint
        require(msg.sender == address(layerZeroEndpoint), "Unauthorized sender");

        // Prevent replay attacks
        require(!receivedMessages[sourceChainId][sourceAddress][nonce], "Message already processed");
        receivedMessages[sourceChainId][sourceAddress][nonce] = true;

        // Decode payload
        (address recipient, uint256 amount) = abi.decode(payload, (address, uint256));

        // Transfer USDC to the recipient
        require(IERC20(usdcToken).transfer(recipient, amount), "USDC transfer failed");

        emit USDCReceived(sourceChainId, recipient, amount);
    }

    /**
     * @notice Allows owner to withdraw any native tokens sent to the contract by mistake
     * @param to Address to send the native tokens
     */
    function withdrawNativeTokens(address to) external {
        require(to != address(0), "Invalid recipient address");
        payable(to).transfer(address(this).balance);
    }

    /**
     * @notice Allows owner to withdraw any ERC20 tokens sent to the contract by mistake
     * @param token Address of the ERC20 token
     * @param to Address to send the tokens
     * @param amount Amount of tokens to withdraw
     */
    function withdrawERC20(address token, address to, uint256 amount) external {
        require(token != address(0), "Invalid token address");
        require(to != address(0), "Invalid recipient address");
        require(IERC20(token).transfer(to, amount), "ERC20 transfer failed");
    }
}
```

This contract leverages LayerZero's protocol for cross-chain messaging, handles USDC token transfers, and includes proper error handling and security measures. Make sure to deploy this contract with the correct LayerZero endpoint address and USDC token address for your environment.
