"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-git-bridge-and-tx-hi-d503e2-offchain-labs.vercel.app
Prompt: Generate an example of a transaction that utilizes L2 gas savings when using the Arbitrum Bridge.
Generated: DETERMINISTIC_0214d71a5011b0d3
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

// Import Arbitrum's L1 Gateway Router interface
import {IL1GatewayRouter} from "@arbitrum/nitro-contracts/src/bridge/IL1GatewayRouter.sol";
import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract ArbitrumBridgeExample {
    // Mainnet L1 Gateway Router address (Arbitrum One)
    address public constant L1_GATEWAY_ROUTER = 0x72Ce9c846789fdB6fC1f34aC4AD25Dd9ef7031ef;
    
    // Token to bridge (example: USDC on Ethereum mainnet)
    address public constant L1_TOKEN = 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48;
    
    // Recipient address on Arbitrum
    address public recipient;
    
    // Event to track bridging
    event TokensBridged(
        address indexed sender,
        address indexed recipient,
        address indexed token,
        uint256 amount,
        uint256 maxSubmissionCost,
        uint256 maxGas,
        uint256 gasPriceBid
    );

    constructor(address _recipient) {
        recipient = _recipient;
    }

    /**
     * @notice Bridges tokens from L1 to L2 using Arbitrum's Gateway Router
     * @param _amount Amount of tokens to bridge
     * @param _maxSubmissionCost Max submission cost for L2 retryable ticket
     * @param _maxGas Max gas for L2 transaction
     * @param _gasPriceBid Gas price bid for L2 transaction
     */
    function bridgeTokens(
        uint256 _amount,
        uint256 _maxSubmissionCost,
        uint256 _maxGas,
        uint256 _gasPriceBid
    ) external payable {
        // Approve the Gateway Router to spend tokens
        IERC20(L1_TOKEN).approve(L1_GATEWAY_ROUTER, _amount);
        
        // Encode the extra data for L2 transaction
        bytes memory data = abi.encode(_maxSubmissionCost, _maxGas, _gasPriceBid, recipient);
        
        // Call outboundTransfer on the Gateway Router
        IL1GatewayRouter(L1_GATEWAY_ROUTER).outboundTransfer{value: msg.value}(
            L1_TOKEN,
            recipient,
            _amount,
            _maxGas,
            _gasPriceBid,
            data
        );
        
        emit TokensBridged(
            msg.sender,
            recipient,
            L1_TOKEN,
            _amount,
            _maxSubmissionCost,
            _maxGas,
            _gasPriceBid
        );
    }

    /**
     * @notice Helper function to estimate the total ETH needed for bridging
     * @param _maxSubmissionCost Max submission cost for L2 retryable ticket
     * @param _maxGas Max gas for L2 transaction
     * @param _gasPriceBid Gas price bid for L2 transaction
     * @return Total ETH needed (submission cost + L2 gas cost)
     */
    function estimateBridgeCost(
        uint256 _maxSubmissionCost,
        uint256 _maxGas,
        uint256 _gasPriceBid
    ) external pure returns (uint256) {
        return _maxSubmissionCost + (_maxGas * _gasPriceBid);
    }
}
```
