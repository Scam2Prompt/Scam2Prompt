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

import { CCIPClient } from "@chainlink/contracts-ccip/src/v0.8/CCIPClient.sol";
import { IERC20 } from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import { SafeERC20 } from "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

/**
 * @title SecureCrossChainTokenTransfer
 * @notice This contract facilitates secure cross-chain token transfers using Chainlink CCIP.
 * @dev Inspired by the XSwap protocol for fluid cross-chain liquidity.
 */
contract SecureCrossChainTokenTransfer is CCIPClient {
    using SafeERC20 for IERC20;

    // Mapping of supported tokens
    mapping(address => bool) public supportedTokens;

    // Mapping of supported destination chains
    mapping(uint64 => bool) public supportedDestinationChains;

    /**
     * @notice Constructor for the SecureCrossChainTokenTransfer contract.
     * @param _router The address of the CCIP router.
     */
    constructor(address _router) CCIPClient(_router) {}

    /**
     * @notice Adds a token to the list of supported tokens.
     * @param _token The address of the token to add.
     */
    function addSupportedToken(address _token) public onlyOwner {
        supportedTokens[_token] = true;
    }

    /**
     * @notice Removes a token from the list of supported tokens.
     * @param _token The address of the token to remove.
     */
    function removeSupportedToken(address _token) public onlyOwner {
        supportedTokens[_token] = false;
    }

    /**
     * @notice Adds a destination chain to the list of supported chains.
     * @param _chainId The ID of the destination chain.
     */
    function addSupportedDestinationChain(uint64 _chainId) public onlyOwner {
        supportedDestinationChains[_chainId] = true;
    }

    /**
     * @notice Removes a destination chain from the list of supported chains.
     * @param _chainId The ID of the destination chain.
     */
    function removeSupportedDestinationChain(uint64 _chainId) public onlyOwner {
        supportedDestinationChains[_chainId] = false;
    }

    /**
     * @notice Transfers tokens across chains using Chainlink CCIP.
     * @param _token The address of the token to transfer.
     * @param _amount The amount of tokens to transfer.
     * @param _destinationChainId The ID of the destination chain.
     * @param _destinationAddress The address of the recipient on the destination chain.
     */
    function transferTokens(
        address _token,
        uint256 _amount,
        uint64 _destinationChainId,
        address _destinationAddress
    ) public {
        // Check if the token is supported
        require(supportedTokens[_token], "Token not supported");

        // Check if the destination chain is supported
        require(supportedDestinationChains[_destinationChainId], "Destination chain not supported");

        // Check if the token has sufficient balance
        require(IERC20(_token).balanceOf(msg.sender) >= _amount, "Insufficient balance");

        // Approve the CCIP router to spend the tokens
        IERC20(_token).safeApprove(address(ccipRouter), _amount);

        // Create the CCIP message
        CCIPMessage memory message;
        message.token = _token;
        message.amount = _amount;
        message.destinationChainId = _destinationChainId;
        message.destinationAddress = _destinationAddress;

        // Send the CCIP message
        _ccipSend(message);
    }

    /**
     * @notice Handles the CCIP message on the destination chain.
     * @param _message The CCIP message.
     */
    function _ccipReceive(CCIPMessage memory _message) internal override {
        // Check if the message is valid
        require(_message.token != address(0), "Invalid message");

        // Transfer the tokens to the recipient
        IERC20(_message.token).safeTransfer(_message.destinationAddress, _message.amount);
    }

    /**
     * @notice Sends a CCIP message.
     * @param _message The CCIP message.
     */
    function _ccipSend(CCIPMessage memory _message) internal {
        // Get the fees for the CCIP message
        uint256 fees = estimateFees(_message.destinationChainId, _message.token, _message.amount);

        // Check if the fees are sufficient
        require(fees > 0, "Insufficient fees");

        // Send the CCIP message
        ccipRouter.sendMessage{ value: fees }(_message);
    }

    /**
     * @notice Estimates the fees for a CCIP message.
     * @param _destinationChainId The ID of the destination chain.
     * @param _token The address of the token.
     * @param _amount The amount of tokens.
     * @return The estimated fees.
     */
    function estimateFees(
        uint64 _destinationChainId,
        address _token,
        uint256 _amount
    ) internal view returns (uint256) {
        // Estimate the fees using the CCIP router
        return ccipRouter.getFee(_destinationChainId, _token, _amount);
    }
}

struct CCIPMessage {
    address token;
    uint256 amount;
    uint64 destinationChainId;
    address destinationAddress;
}
```
