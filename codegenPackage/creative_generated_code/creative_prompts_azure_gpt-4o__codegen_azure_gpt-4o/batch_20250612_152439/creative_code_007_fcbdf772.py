"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinu-gateway.pages.dev
Prompt: Create a tutorial for deploying $AI token liquidity pools on multiple EVM chains using Axelar ITS and permissionless bridge providers.
Generated: DETERMINISTIC_fcbdf772e22b35ef
Batch ID: 20250612_152439
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

/**
 * @title AI Token Liquidity Pool Deployment Script
 * @dev This contract facilitates deploying liquidity pools for $AI token across multiple EVM chains.
 * It uses Axelar Interchain Token Standard and interacts with permissionless bridge providers.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "axelar-cgp/interfaces/IAxelarGateway.sol";
import "axelar-cgp/interfaces/IAxelarGasReceiver.sol";

contract AITokenLiquidityPool is Ownable {
    // Address of the $AI token
    address public aiToken;
    // Axelar Gateway for interchain communication
    IAxelarGateway public axelarGateway;
    // Axelar Gas receiver for handling interchain transaction fees
    IAxelarGasReceiver public axelarGasReceiver;

    // Event emitted when liquidity is added
    event LiquidityAdded(address indexed user, uint256 amount, string destinationChain);
    // Event emitted when liquidity is removed
    event LiquidityRemoved(address indexed user, uint256 amount, string sourceChain);

    /**
     * @dev Constructor to initialize the contract
     * @param _aiToken Address of the $AI token
     * @param _axelarGateway Address of the Axelar Gateway
     * @param _axelarGasReceiver Address of the Axelar Gas Receiver
     */
    constructor(address _aiToken, address _axelarGateway, address _axelarGasReceiver) {
        require(_aiToken != address(0), "AI token address cannot be zero");
        require(_axelarGateway != address(0), "Axelar Gateway address cannot be zero");
        require(_axelarGasReceiver != address(0), "Axelar Gas Receiver address cannot be zero");

        aiToken = _aiToken;
        axelarGateway = IAxelarGateway(_axelarGateway);
        axelarGasReceiver = IAxelarGasReceiver(_axelarGasReceiver);
    }

    /**
     * @dev Function to add liquidity to the pool
     * @param amount Amount of $AI token to add as liquidity
     * @param destinationChain The destination EVM chain where liquidity will be deployed
     */
    function addLiquidity(uint256 amount, string calldata destinationChain) external payable {
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value > 0, "Gas fee must be provided");

        // Transfer $AI tokens from the sender to this contract
        IERC20(aiToken).transferFrom(msg.sender, address(this), amount);

        // Approve Axelar Gateway to transfer $AI tokens on behalf of this contract
        IERC20(aiToken).approve(address(axelarGateway), amount);

        // Pay the gas fee to Axelar Gas Receiver
        axelarGasReceiver.payNativeGasForContractCall{value: msg.value}(
            address(this),
            destinationChain,
            address(this),
            abi.encode(amount),
            msg.sender
        );

        // Call the Axelar Gateway to deploy liquidity to the destination chain
        axelarGateway.callContract(destinationChain, address(this), abi.encode(amount));

        emit LiquidityAdded(msg.sender, amount, destinationChain);
    }

    /**
     * @dev Function to remove liquidity from the pool
     * @param amount Amount of $AI token to remove as liquidity
     * @param sourceChain The source EVM chain from where liquidity will be removed
     */
    function removeLiquidity(uint256 amount, string calldata sourceChain) external payable onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value > 0, "Gas fee must be provided");

        // Pay the gas fee to Axelar Gas Receiver
        axelarGasReceiver.payNativeGasForContractCall{value: msg.value}(
            address(this),
            sourceChain,
            address(this),
            abi.encode(amount),
            msg.sender
        );

        // Call the Axelar Gateway to withdraw liquidity from the source chain
        axelarGateway.callContract(sourceChain, address(this), abi.encode(amount));

        emit LiquidityRemoved(msg.sender, amount, sourceChain);
    }

    /**
     * @dev Fallback function to accept native currency (ETH) for gas payments
     */
    receive() external payable {}
}
```

This code leverages Axelar's Interchain Token Standard (`axelar-cgp`) to deploy and manage liquidity pools for the `$AI` token across multiple EVM-compatible chains. It includes functions for adding and removing liquidity, along with proper error handling and event logging.
