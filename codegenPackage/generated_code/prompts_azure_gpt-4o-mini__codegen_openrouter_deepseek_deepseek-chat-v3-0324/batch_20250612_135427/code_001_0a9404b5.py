"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-git-bridge-and-tx-hi-d503e2-offchain-labs.vercel.app
Prompt: Write a code snippet demonstrating how to implement the Retryables feature in an Arbitrum-based project.
Generated: DETERMINISTIC_0a9404b505ce9ea6
Batch ID: 20250612_135427
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

import {IRetryableTicket} from "@arbitrum/nitro-contracts/src/bridge/IRetryableTicket.sol";
import {IInbox} from "@arbitrum/nitro-contracts/src/bridge/IInbox.sol";
import {AddressAliasHelper} from "@arbitrum/nitro-contracts/src/libraries/AddressAliasHelper.sol";

/**
 * @title RetryableTxHandler
 * @dev Handles retryable ticket creation and management for Arbitrum
 */
contract RetryableTxHandler {
    IInbox public immutable inbox;
    address public immutable l2Target;
    
    event RetryableTicketCreated(
        bytes32 indexed ticketId,
        address indexed sender,
        uint256 maxSubmissionCost,
        uint256 maxGas,
        uint256 gasPriceBid
    );
    
    event RetryableTicketRedeemed(bytes32 indexed ticketId);
    event RetryableTicketExpired(bytes32 indexed ticketId);

    /**
     * @param _inbox Address of the Arbitrum Inbox contract
     * @param _l2Target Address of the target contract on L2
     */
    constructor(address _inbox, address _l2Target) {
        require(_inbox != address(0), "Invalid inbox address");
        require(_l2Target != address(0), "Invalid L2 target address");
        inbox = IInbox(_inbox);
        l2Target = _l2Target;
    }

    /**
     * @dev Creates a retryable ticket to L2
     * @param maxSubmissionCost Max ETH to pay for submission fee
     * @param maxGas Max gas to use in L2 execution
     * @param gasPriceBid Gas price bid for L2 execution
     * @param callData Data to send to L2 target
     * @return Ticket ID of the created retryable ticket
     */
    function createRetryableTicket(
        uint256 maxSubmissionCost,
        uint256 maxGas,
        uint256 gasPriceBid,
        bytes memory callData
    ) external payable returns (bytes32) {
        require(msg.value >= maxSubmissionCost + (maxGas * gasPriceBid), "Insufficient ETH");
        
        bytes32 ticketId = inbox.createRetryableTicket{value: msg.value}(
            l2Target,
            0, // no L2 call value
            maxSubmissionCost,
            msg.sender, // refund address
            msg.sender, // beneficiary
            maxGas,
            gasPriceBid,
            callData
        );

        emit RetryableTicketCreated(ticketId, msg.sender, maxSubmissionCost, maxGas, gasPriceBid);
        return ticketId;
    }

    /**
     * @dev Redeems an expired retryable ticket
     * @param ticketId ID of the ticket to redeem
     */
    function redeemRetryableTicket(bytes32 ticketId) external {
        IRetryableTicket retryable = IRetryableTicket(address(inbox));
        retryable.redeem(ticketId);
        emit RetryableTicketRedeemed(ticketId);
    }

    /**
     * @dev Checks if a retryable ticket is expired
     * @param ticketId ID of the ticket to check
     * @return bool True if expired, false otherwise
     */
    function isRetryableExpired(bytes32 ticketId) external view returns (bool) {
        IRetryableTicket retryable = IRetryableTicket(address(inbox));
        return block.timestamp > retryable.getTimeout(ticketId);
    }

    /**
     * @dev Handles an incoming retryable ticket from L2
     * @notice This should be called by the L2 target contract via the ArbSys precompile
     */
    function handleRetryableTicket() external {
        require(
            AddressAliasHelper.undoL1ToL2Alias(msg.sender) == l2Target,
            "Only callable by L2 target"
        );
        // Handle the retryable ticket logic here
    }
}
```
