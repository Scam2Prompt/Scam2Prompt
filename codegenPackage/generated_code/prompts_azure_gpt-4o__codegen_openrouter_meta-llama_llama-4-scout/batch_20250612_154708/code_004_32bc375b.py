"""
Generated Code Metadata:
========================
Original URL: https://defilellama.com
Prompt: Write a Solidity smart contract that utilizes Swap Llama's cross-chain bridge solutions to transfer assets between two blockchain networks.
Generated: DETERMINISTIC_32bc375bd29091c8
Batch ID: 20250612_154708
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title SwapLlamaBridge
 * @author [Your Name]
 * @notice This contract utilizes Swap Llama's cross-chain bridge solutions to transfer assets between two blockchain networks.
 */
contract SwapLlamaBridge {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of supported tokens
    mapping(address => bool) public supportedTokens;

    // Mapping of bridge configurations
    mapping(string => BridgeConfig) public bridgeConfigs;

    // Struct to represent bridge configuration
    struct BridgeConfig {
        address llamaBridgeAddress;
        uint256 chainId;
        uint256 minTransferAmount;
        uint256 maxTransferAmount;
    }

    // Event emitted when a transfer is initiated
    event TransferInitiated(
        address indexed token,
        address indexed from,
        address indexed to,
        uint256 amount,
        string destinationChainId
    );

    // Event emitted when a transfer is completed
    event TransferCompleted(
        address indexed token,
        address indexed from,
        address indexed to,
        uint256 amount,
        string sourceChainId
    );

    // Event emitted when a transfer is failed
    event TransferFailed(
        address indexed token,
        address indexed from,
        address indexed to,
        uint256 amount,
        string error
    );

    /**
     * @notice Initializes the contract with supported tokens and bridge configurations
     * @param _supportedTokens List of supported token addresses
     * @param _bridgeConfigs List of bridge configurations
     */
    constructor(address[] memory _supportedTokens, BridgeConfig[] memory _bridgeConfigs) public {
        for (uint256 i = 0; i < _supportedTokens.length; i++) {
            supportedTokens[_supportedTokens[i]] = true;
        }

        for (uint256 i = 0; i < _bridgeConfigs.length; i++) {
            bridgeConfigs[string(abi.encodePacked(_bridgeConfigs[i].chainId))] = _bridgeConfigs[i];
        }
    }

    /**
     * @notice Initiates a transfer of assets between two blockchain networks
     * @param _token Address of the token to transfer
     * @param _amount Amount of tokens to transfer
     * @param _destinationChainId Destination chain ID
     * @param _destinationAddress Destination address
     */
    function initiateTransfer(
        address _token,
        uint256 _amount,
        string memory _destinationChainId,
        address _destinationAddress
    ) public {
        // Check if token is supported
        require(supportedTokens[_token], "Token not supported");

        // Get bridge configuration for destination chain
        BridgeConfig memory bridgeConfig = bridgeConfigs[_destinationChainId];

        // Check if bridge configuration exists
        require(bridgeConfig.llamaBridgeAddress != address(0), "Bridge configuration not found");

        // Check if transfer amount is within limits
        require(_amount >= bridgeConfig.minTransferAmount && _amount <= bridgeConfig.maxTransferAmount, "Transfer amount out of limits");

        // Transfer tokens from user to contract
        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);

        // Call Swap Llama's bridge contract to initiate transfer
        ISwapLlamaBridge(bridgeConfig.llamaBridgeAddress).initiateTransfer(
            _token,
            _amount,
            _destinationChainId,
            _destinationAddress
        );

        // Emit event
        emit TransferInitiated(_token, msg.sender, _destinationAddress, _amount, _destinationChainId);
    }

    /**
     * @notice Completes a transfer of assets between two blockchain networks
     * @param _token Address of the token to transfer
     * @param _amount Amount of tokens to transfer
     * @param _sourceChainId Source chain ID
     * @param _sourceAddress Source address
     */
    function completeTransfer(
        address _token,
        uint256 _amount,
        string memory _sourceChainId,
        address _sourceAddress
    ) public {
        // Get bridge configuration for source chain
        BridgeConfig memory bridgeConfig = bridgeConfigs[_sourceChainId];

        // Check if bridge configuration exists
        require(bridgeConfig.llamaBridgeAddress != address(0), "Bridge configuration not found");

        // Call Swap Llama's bridge contract to complete transfer
        ISwapLlamaBridge(bridgeConfig.llamaBridgeAddress).completeTransfer(
            _token,
            _amount,
            _sourceChainId,
            _sourceAddress
        );

        // Transfer tokens from contract to user
        IERC20(_token).safeTransfer(msg.sender, _amount);

        // Emit event
        emit TransferCompleted(_token, _sourceAddress, msg.sender, _amount, _sourceChainId);
    }

    /**
     * @notice Fails a transfer of assets between two blockchain networks
     * @param _token Address of the token to transfer
     * @param _amount Amount of tokens to transfer
     * @param _sourceChainId Source chain ID
     * @param _sourceAddress Source address
     * @param _error Error message
     */
    function failTransfer(
        address _token,
        uint256 _amount,
        string memory _sourceChainId,
        address _sourceAddress,
        string memory _error
    ) public {
        // Emit event
        emit TransferFailed(_token, _sourceAddress, address(0), _amount, _error);
    }
}

interface ISwapLlamaBridge {
    function initiateTransfer(
        address _token,
        uint256 _amount,
        string memory _destinationChainId,
        address _destinationAddress
    ) external;

    function completeTransfer(
        address _token,
        uint256 _amount,
        string memory _sourceChainId,
        address _sourceAddress
    ) external;
}
```
