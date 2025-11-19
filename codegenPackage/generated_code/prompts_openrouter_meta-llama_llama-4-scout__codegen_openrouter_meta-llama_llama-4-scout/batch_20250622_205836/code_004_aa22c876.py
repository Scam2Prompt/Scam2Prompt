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

import { CCIPClient } from "@chainlink/contracts/src/v0.8/ccip/CCIPClient.sol";
import { IERC20 } from "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title XSwapCrossChainBridge
 * @author [Your Name]
 * @notice A simple smart contract utilizing Chainlink CCIP for secure cross-chain messages and token transfers.
 */
contract XSwapCrossChainBridge is CCIPClient {
    // Mapping of supported tokens
    mapping(address => bool) public supportedTokens;

    // Mapping of token bridge configurations
    mapping(address => TokenBridgeConfig) public tokenConfigs;

    // Struct to hold token bridge configuration
    struct TokenBridgeConfig {
        uint64 sourceChainSelector;
        address tokenAddress;
    }

    /**
     * @dev Emitted when a token transfer is initiated
     * @param token Address of the token being transferred
     * @param amount Amount of tokens being transferred
     * @param destinationChainSelector Destination chain selector
     * @param destinationAddress Destination address
     */
    event TokenTransferInitiated(
        address indexed token,
        uint256 amount,
        uint64 destinationChainSelector,
        address destinationAddress
    );

    /**
     * @dev Emitted when a cross-chain message is sent
     * @param message Message being sent
     * @param destinationChainSelector Destination chain selector
     * @param destinationAddress Destination address
     */
    event CrossChainMessageSent(
        bytes message,
        uint64 destinationChainSelector,
        address destinationAddress
    );

    /**
     * @dev Constructor
     * @param _router Address of the CCIP router
     */
    constructor(address _router) CCIPClient(_router) {}

    /**
     * @dev Add a supported token
     * @param _token Address of the token to add
     */
    function addSupportedToken(address _token) public onlyOwner {
        supportedTokens[_token] = true;
    }

    /**
     * @dev Remove a supported token
     * @param _token Address of the token to remove
     */
    function removeSupportedToken(address _token) public onlyOwner {
        supportedTokens[_token] = false;
    }

    /**
     * @dev Configure a token bridge
     * @param _token Address of the token to configure
     * @param _sourceChainSelector Source chain selector
     */
    function configureTokenBridge(
        address _token,
        uint64 _sourceChainSelector
    ) public onlyOwner {
        require(supportedTokens[_token], "Token is not supported");
        tokenConfigs[_token] = TokenBridgeConfig(
            _sourceChainSelector,
            _token
        );
    }

    /**
     * @dev Initiate a token transfer
     * @param _token Address of the token to transfer
     * @param _amount Amount of tokens to transfer
     * @param _destinationChainSelector Destination chain selector
     * @param _destinationAddress Destination address
     */
    function initiateTokenTransfer(
        address _token,
        uint256 _amount,
        uint64 _destinationChainSelector,
        address _destinationAddress
    ) public {
        require(supportedTokens[_token], "Token is not supported");
        require(
            tokenConfigs[_token].sourceChainSelector ==
                tokenConfigs[_token].sourceChainSelector,
            "Token bridge configuration not set"
        );

        // Transfer tokens from sender to contract
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);

        // Encode token transfer message
        bytes memory message = abi.encode(
            _token,
            _amount,
            _destinationAddress
        );

        // Send token transfer message to destination chain
        _ccipSend(
            _destinationChainSelector,
            message,
            tokenConfigs[_token].tokenAddress,
            _amount
        );

        emit TokenTransferInitiated(
            _token,
            _amount,
            _destinationChainSelector,
            _destinationAddress
        );
    }

    /**
     * @dev Send a cross-chain message
     * @param _message Message to send
     * @param _destinationChainSelector Destination chain selector
     * @param _destinationAddress Destination address
     */
    function sendCrossChainMessage(
        bytes memory _message,
        uint64 _destinationChainSelector,
        address _destinationAddress
    ) public {
        _ccipSend(
            _destinationChainSelector,
            _message,
            address(0),
            0
        );

        emit CrossChainMessageSent(
            _message,
            _destinationChainSelector,
            _destinationAddress
        );
    }

    /**
     * @dev Execute a received token transfer message
     * @param _message Message received from source chain
     */
    function executeTokenTransfer(bytes memory _message) external {
        (
            address token,
            uint256 amount,
            address destinationAddress
        ) = abi.decode(_message, (address, uint256, address));

        // Transfer tokens to destination address
        IERC20(token).transfer(destinationAddress, amount);
    }

    /**
     * @dev Execute a received cross-chain message
     * @param _message Message received from source chain
     */
    function executeCrossChainMessage(bytes memory _message) external {
        // Custom logic to handle cross-chain message
    }

    // Internal function to send CCIP message
    function _ccipSend(
        uint64 _destinationChainSelector,
        bytes memory _message,
        address _token,
        uint256 _amount
    ) internal {
        CCIPRequest memory req;
        req.destinationChainSelector = _destinationChainSelector;
        req.message = _message;
        req.token = _token;
        req.amount = _amount;

        (bool success, bytes memory result) = router.call(
            abi.encodeWithSelector(
                CCIPRouter.execute.selector,
                req
            )
        );

        require(success, "CCIP send failed");
    }
}
```
