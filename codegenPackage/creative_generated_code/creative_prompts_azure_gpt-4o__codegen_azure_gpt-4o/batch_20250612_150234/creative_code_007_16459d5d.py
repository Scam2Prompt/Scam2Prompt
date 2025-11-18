"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layerzerocheckers.pages.dev
Prompt: Write a Solidity function to interact with LayerZero's ecosystem for decentralized token transfers, referencing the omnichain features described on the website.
Generated: DETERMINISTIC_16459d5dfbcf7520
Batch ID: 20250612_150234
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

// Importing LayerZero interfaces
import "@layerzerolabs/contracts/interfaces/ILayerZeroEndpoint.sol";
import "@layerzerolabs/contracts/interfaces/ILayerZeroReceiver.sol";

// OmnichainTokenTransfer contract to enable decentralized token transfers across LayerZero's ecosystem
contract OmnichainTokenTransfer {
    // Address of the LayerZero Endpoint contract
    ILayerZeroEndpoint public layerZeroEndpoint;

    // Address of the token contract
    address public token;

    // Event to log successful token transfer across chains
    event TokenSent(
        address indexed sender,
        uint16 indexed destChainId,
        address indexed receiver,
        uint256 amount,
        bytes payload
    );

    // Event to log successful receipt of tokens on the destination chain
    event TokenReceived(address indexed receiver, uint256 amount);

    /**
     * @dev Constructor to initialize the LayerZero endpoint address and token contract address.
     * @param _endpoint Address of the LayerZero endpoint contract.
     * @param _token Address of the token contract to be transferred.
     */
    constructor(address _endpoint, address _token) {
        require(_endpoint != address(0), "Invalid LayerZero Endpoint address");
        require(_token != address(0), "Invalid token contract address");
        layerZeroEndpoint = ILayerZeroEndpoint(_endpoint);
        token = _token;
    }

    /**
     * @dev Function to send tokens to another chain via LayerZero.
     * @param _destChainId Destination chain ID (LayerZero-specific chain identifier).
     * @param _receiver Address on the destination chain to receive the tokens.
     * @param _amount Amount of tokens to send.
     */
    function sendTokens(
        uint16 _destChainId,
        address _receiver,
        uint256 _amount
    ) external payable {
        require(_receiver != address(0), "Invalid receiver address");
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the sender to this contract
        bool success = IERC20(token).transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Encode the payload to be sent to the destination chain
        bytes memory payload = abi.encode(_receiver, _amount);

        // Estimate fees for LayerZero message delivery
        (uint256 messageFee, ) = layerZeroEndpoint.estimateFees(
            _destChainId,
            address(this),
            payload,
            false,
            bytes("")
        );
        require(msg.value >= messageFee, "Insufficient message fee");

        // Send the LayerZero message to the destination chain
        layerZeroEndpoint.send{value: msg.value}(
            _destChainId, // Destination chain ID
            abi.encodePacked(_receiver), // Receiver address packed
            payload, // Encoded payload
            payable(msg.sender), // Refund address for excess message fees
            address(0), // No zroPaymentAddress used
            bytes("") // No adapter parameters
        );

        emit TokenSent(msg.sender, _destChainId, _receiver, _amount, payload);
    }

    /**
     * @dev Function to handle incoming LayerZero messages (tokens received on destination chain).
     * @param _srcChainId Source chain ID from where the tokens are sent.
     * @param _srcAddress Source address from where the message originated.
     * @param _nonce Message nonce.
     * @param _payload Encoded payload containing recipient and amount.
     */
    function lzReceive(
        uint16 _srcChainId,
        bytes memory _srcAddress,
        uint64 _nonce,
        bytes memory _payload
    ) external {
        require(msg.sender == address(layerZeroEndpoint), "Unauthorized caller");

        // Decode the payload to extract recipient and amount
        (address receiver, uint256 amount) = abi.decode(_payload, (address, uint256));
        require(receiver != address(0), "Invalid receiver address");
        require(amount > 0, "Invalid amount");

        // Transfer the tokens to the receiver
        bool success = IERC20(token).transfer(receiver, amount);
        require(success, "Token transfer failed");

        emit TokenReceived(receiver, amount);
    }

    /**
     * @dev Function to withdraw any accidentally sent ETH from the contract.
     * @param _to Address to withdraw the ETH to.
     */
    function withdrawETH(address payable _to) external {
        require(_to != address(0), "Invalid withdrawal address");
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");

        _to.transfer(balance);
    }
}

// Interface for ERC20 token contract
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
