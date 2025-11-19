"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Implement a cross-chain settlement mechanism for tokenized assets using Chainlink CCIP in Solidity.
Generated: DETERMINISTIC_952e4b17348f7db3
Batch ID: 20250612_152249
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

import { CCIPClient } from "@chainlink/contracts/src/v0.8/CCIPClient.sol";
import { IERC20 } from "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title CrossChainSettlement
 * @notice This contract facilitates cross-chain settlement of tokenized assets using Chainlink CCIP.
 */
contract CrossChainSettlement is CCIPClient {
    // Mapping of token addresses to their respective settlement statuses
    mapping(address => mapping(address => bool)) public settlementStatus;

    // Mapping of token addresses to their respective CCIP Router addresses
    mapping(address => address) public ccipRouters;

    // Event emitted when a cross-chain settlement is initiated
    event CrossChainSettlementInitiated(address indexed token, address indexed toChain, address indexed toAddress);

    // Event emitted when a cross-chain settlement is completed
    event CrossChainSettlementCompleted(address indexed token, address indexed toChain, address indexed toAddress);

    /**
     * @notice Constructor for the CrossChainSettlement contract.
     * @param _defaultAdmin The default admin address for the contract.
     * @param _ccipRouter The CCIP Router address.
     */
    constructor(address _defaultAdmin, address _ccipRouter) CCIPClient(_ccipRouter) {
        // Set the default admin
        _grantRole(DEFAULT_ADMIN_ROLE, _defaultAdmin);
    }

    /**
     * @notice Initiates a cross-chain settlement for a tokenized asset.
     * @param _token The address of the token to settle.
     * @param _toChain The chain ID of the destination chain.
     * @param _toAddress The address of the recipient on the destination chain.
     * @param _amount The amount of tokens to settle.
     */
    function initiateCrossChainSettlement(address _token, uint64 _toChain, address _toAddress, uint256 _amount) public {
        // Check if the token is supported
        require(ccipRouters[_token] != address(0), "Token not supported");

        // Check if the recipient address is valid
        require(_toAddress != address(0), "Invalid recipient address");

        // Get the CCIP Router address for the token
        address _ccipRouter = ccipRouters[_token];

        // Encode the settlement data
        bytes memory _data = abi.encode(_toAddress);

        // Get the CCIP message
        CCIPMessage memory _message = CCIPMessage(
            _ccipRouter,
            _toChain,
            _data,
            _amount
        );

        // Send the CCIP message
        _sendMessage(_message);

        // Update the settlement status
        settlementStatus[_token][_toAddress] = true;

        // Emit the CrossChainSettlementInitiated event
        emit CrossChainSettlementInitiated(_token, _toChain, _toAddress);
    }

    /**
     * @notice Completes a cross-chain settlement for a tokenized asset.
     * @param _message The CCIP message.
     */
    function _ccipReceive(CCIPMessage memory _message) internal override {
        // Get the token address from the CCIP message
        address _token = _message.sourceToken;

        // Get the recipient address from the CCIP message
        address _toAddress = abi.decode(_message.data, (address));

        // Check if the settlement is not already completed
        require(!settlementStatus[_token][_toAddress], "Settlement already completed");

        // Update the settlement status
        settlementStatus[_token][_toAddress] = false;

        // Transfer the tokens to the recipient
        IERC20(_token).transfer(_toAddress, _message.amount);

        // Emit the CrossChainSettlementCompleted event
        emit CrossChainSettlementCompleted(_token, _message.destinationChainSelector, _toAddress);
    }

    /**
     * @notice Adds a token to the list of supported tokens.
     * @param _token The address of the token to add.
     * @param _ccipRouter The CCIP Router address for the token.
     */
    function addToken(address _token, address _ccipRouter) public onlyRole(DEFAULT_ADMIN_ROLE) {
        // Check if the token is not already supported
        require(ccipRouters[_token] == address(0), "Token already supported");

        // Add the token to the list of supported tokens
        ccipRouters[_token] = _ccipRouter;
    }

    /**
     * @notice Removes a token from the list of supported tokens.
     * @param _token The address of the token to remove.
     */
    function removeToken(address _token) public onlyRole(DEFAULT_ADMIN_ROLE) {
        // Check if the token is supported
        require(ccipRouters[_token] != address(0), "Token not supported");

        // Remove the token from the list of supported tokens
        delete ccipRouters[_token];
    }
}
```
