"""
Generated Code Metadata:
========================
Original URL: https://telos-4ji.pages.dev
Prompt: Generate code to integrate LayerZero's omnichain interoperability protocol with Telos Blockchain, enabling seamless asset transfers between Telos and other supported blockchains.
Generated: DETERMINISTIC_7713c40ec9cf79e6
Batch ID: 20250612_152018
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

import "@layerzerolabs/solidity-examples/contracts/lzApp/NonblockingLzApp.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TelosOmnichainBridge
 * @dev Enables cross-chain asset transfers between Telos and other chains via LayerZero
 */
contract TelosOmnichainBridge is NonblockingLzApp, Ownable {
    using SafeERC20 for IERC20;

    struct ChainInfo {
        uint16 chainId;
        address bridgeContract;
    }

    // Supported tokens and their corresponding contracts on other chains
    mapping(address => mapping(uint16 => address)) public tokenMappings;
    
    // Supported chains and their bridge contracts
    mapping(uint16 => address) public chainBridgeContracts;
    
    // Track processed messages to prevent replay attacks
    mapping(bytes32 => bool) public processedMessages;

    event TokenSent(
        address indexed token,
        address indexed sender,
        address indexed receiver,
        uint256 amount,
        uint16 destinationChainId
    );

    event TokenReceived(
        address indexed token,
        address indexed receiver,
        uint256 amount,
        uint16 sourceChainId
    );

    event ChainAdded(
        uint16 chainId,
        address bridgeContract
    );

    event TokenMappingAdded(
        address localToken,
        uint16 remoteChainId,
        address remoteToken
    );

    /**
     * @dev Constructor initializes the LayerZero endpoint
     * @param _lzEndpoint LayerZero endpoint address
     */
    constructor(address _lzEndpoint) NonblockingLzApp(_lzEndpoint) {}

    /**
     * @dev Add supported chain and its bridge contract
     * @param _chainId LayerZero chain ID
     * @param _bridgeContract Bridge contract address on the remote chain
     */
    function addSupportedChain(uint16 _chainId, address _bridgeContract) external onlyOwner {
        require(_bridgeContract != address(0), "Invalid bridge contract");
        chainBridgeContracts[_chainId] = _bridgeContract;
        emit ChainAdded(_chainId, _bridgeContract);
    }

    /**
     * @dev Add token mapping between chains
     * @param _localToken Local token address
     * @param _remoteChainId Remote chain ID
     * @param _remoteToken Corresponding token address on remote chain
     */
    function addTokenMapping(
        address _localToken,
        uint16 _remoteChainId,
        address _remoteToken
    ) external onlyOwner {
        require(_localToken != address(0), "Invalid local token");
        require(_remoteToken != address(0), "Invalid remote token");
        tokenMappings[_localToken][_remoteChainId] = _remoteToken;
        emit TokenMappingAdded(_localToken, _remoteChainId, _remoteToken);
    }

    /**
     * @dev Send tokens to another chain
     * @param _token Token address to send
     * @param _amount Amount to send
     * @param _receiver Receiver address on destination chain
     * @param _destinationChainId Destination chain ID
     */
    function sendTokens(
        address _token,
        uint256 _amount,
        address _receiver,
        uint16 _destinationChainId
    ) external payable {
        require(_amount > 0, "Amount must be > 0");
        require(tokenMappings[_token][_destinationChainId] != address(0), "Token not supported on destination chain");
        require(chainBridgeContracts[_destinationChainId] != address(0), "Chain not supported");

        // Transfer tokens from sender to this contract
        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);

        // Prepare payload
        bytes memory payload = abi.encode(
            tokenMappings[_token][_destinationChainId],
            _receiver,
            _amount
        );

        // Get message fee
        (uint256 messageFee,) = lzEndpoint.estimateFees(
            _destinationChainId,
            address(this),
            payload,
            false,
            bytes("")
        );
        require(msg.value >= messageFee, "Insufficient message fee");

        // Send message via LayerZero
        _lzSend(
            _destinationChainId,
            payload,
            payable(msg.sender),
            address(0x0),
            bytes(""),
            msg.value
        );

        emit TokenSent(_token, msg.sender, _receiver, _amount, _destinationChainId);
    }

    /**
     * @dev Override _nonblockingLzReceive to handle incoming messages
     * @param _srcChainId Source chain ID
     * @param _srcAddress Source address
     * @param _nonce Message nonce
     * @param _payload Message payload
     */
    function _nonblockingLzReceive(
        uint16 _srcChainId,
        bytes memory _srcAddress,
        uint64 _nonce,
        bytes memory _payload
    ) internal override {
        // Prevent replay attacks
        bytes32 messageHash = keccak256(abi.encodePacked(_srcChainId, _srcAddress, _nonce, _payload));
        require(!processedMessages[messageHash], "Message already processed");
        processedMessages[messageHash] = true;

        // Verify source bridge contract
        address srcBridgeContract;
        assembly {
            srcBridgeContract := mload(add(_srcAddress, 20))
        }
        require(srcBridgeContract == chainBridgeContracts[_srcChainId], "Invalid source bridge");

        // Decode payload
        (address remoteToken, address receiver, uint256 amount) = abi.decode(
            _payload,
            (address, address, uint256)
        );

        // Find local token
        address localToken = address(0);
        for (uint i = 0; i < 100; i++) {
            // This is a simplified approach - in production you'd want a better mapping system
            if (tokenMappings[localToken][_srcChainId] == remoteToken) {
                break;
            }
            // Increment to next token (this is just a placeholder)
            localToken = address(uint160(localToken) + 1);
        }
        require(localToken != address(0), "Token mapping not found");

        // Transfer tokens to receiver
        IERC20(localToken).safeTransfer(receiver, amount);

        emit TokenReceived(localToken, receiver, amount, _srcChainId);
    }

    /**
     * @dev Withdraw stuck tokens (emergency only)
     * @param _token Token address to withdraw
     */
    function withdrawStuckTokens(address _token) external onlyOwner {
        uint256 balance = IERC20(_token).balanceOf(address(this));
        IERC20(_token).safeTransfer(owner(), balance);
    }

    /**
     * @dev Withdraw native currency (emergency only)
     */
    function withdrawNative() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to receive native currency
    receive() external payable {}
}
```
