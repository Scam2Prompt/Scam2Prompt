"""
Generated Code Metadata:
========================
Original URL: https://predelin.ru
Prompt: Generate code in Solidity to create a custom liquidity pool on Beethoven X with specific token ratios and automated market-making functionality.
Generated: DETERMINISTIC_4b787d898b0ce50f
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

import "@balancer-labs/v2-vault/contracts/interfaces/IVault.sol";
import "@balancer-labs/v2-vault/contracts/interfaces/IAsset.sol";
import "@balancer-labs/v2-pool-utils/contracts/interfaces/IPoolSwapStructs.sol";

contract BeethovenXCustomPool {
    IVault private immutable vault;
    bytes32 private poolId;
    address[] private tokens;
    uint256[] private balances;
    uint256[] private weights;

    event PoolCreated(bytes32 indexed poolId, address[] tokens, uint256[] weights);
    event SwapExecuted(address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    /**
     * @dev Initialize the contract with Balancer Vault address
     * @param _vault Address of the Balancer Vault contract
     */
    constructor(address _vault) {
        require(_vault != address(0), "Invalid vault address");
        vault = IVault(_vault);
    }

    /**
     * @dev Create a new liquidity pool with specified tokens and weights
     * @param _tokens Array of token addresses to include in the pool
     * @param _initialBalances Initial balances for each token
     * @param _weights Normalized weights for each token (sum to 1e18)
     * @param _swapFeePercentage Swap fee percentage (1e16 = 1%)
     */
    function createPool(
        address[] memory _tokens,
        uint256[] memory _initialBalances,
        uint256[] memory _weights,
        uint256 _swapFeePercentage
    ) external {
        require(_tokens.length >= 2, "Minimum 2 tokens required");
        require(_tokens.length == _initialBalances.length, "Mismatched tokens/balances");
        require(_tokens.length == _weights.length, "Mismatched tokens/weights");

        uint256 totalWeight;
        for (uint256 i = 0; i < _weights.length; i++) {
            totalWeight += _weights[i];
            require(_weights[i] > 0, "Zero weight not allowed");
        }
        require(totalWeight == 1e18, "Weights must sum to 1e18");

        tokens = _tokens;
        balances = _initialBalances;
        weights = _weights;

        // Approve vault to spend tokens
        for (uint256 i = 0; i < _tokens.length; i++) {
            IERC20(_tokens[i]).approve(address(vault), _initialBalances[i]);
        }

        // Create pool
        IVault.PoolSpecialization specialization = IVault.PoolSpecialization.GENERAL;
        bytes memory userData = abi.encode(IVault.JoinKind.INIT, _initialBalances);
        IVault.JoinPoolRequest memory request = IVault.JoinPoolRequest({
            assets: _convertToIAsset(_tokens),
            maxAmountsIn: _initialBalances,
            userData: userData,
            fromInternalBalance: false
        });

        poolId = vault.registerPool(specialization);
        vault.joinPool(poolId, address(this), address(this), request);

        emit PoolCreated(poolId, _tokens, _weights);
    }

    /**
     * @dev Execute a swap between tokens in the pool
     * @param _tokenIn Address of the input token
     * @param _tokenOut Address of the output token
     * @param _amount Amount of input token to swap
     * @param _minAmountOut Minimum amount of output token to receive
     */
    function swap(
        address _tokenIn,
        address _tokenOut,
        uint256 _amount,
        uint256 _minAmountOut
    ) external returns (uint256 amountOut) {
        require(poolId != bytes32(0), "Pool not initialized");
        require(_tokenIn != _tokenOut, "Cannot swap same token");
        require(_amount > 0, "Amount must be positive");

        IERC20(_tokenIn).transferFrom(msg.sender, address(this), _amount);
        IERC20(_tokenIn).approve(address(vault), _amount);

        IVault.SingleSwap memory singleSwap = IVault.SingleSwap({
            poolId: poolId,
            kind: IVault.SwapKind.GIVEN_IN,
            assetIn: IAsset(_tokenIn),
            assetOut: IAsset(_tokenOut),
            amount: _amount,
            userData: ""
        });

        IVault.FundManagement memory funds = IVault.FundManagement({
            sender: address(this),
            fromInternalBalance: false,
            recipient: payable(msg.sender),
            toInternalBalance: false
        });

        amountOut = vault.swap(singleSwap, funds, _minAmountOut, block.timestamp);
        emit SwapExecuted(_tokenIn, _tokenOut, _amount, amountOut);
    }

    /**
     * @dev Internal helper to convert address array to IAsset array
     */
    function _convertToIAsset(address[] memory _addresses) private pure returns (IAsset[] memory assets) {
        assets = new IAsset[](_addresses.length);
        for (uint256 i = 0; i < _addresses.length; i++) {
            assets[i] = IAsset(_addresses[i]);
        }
    }

    /**
     * @dev Get the pool ID
     */
    function getPoolId() external view returns (bytes32) {
        return poolId;
    }

    /**
     * @dev Get the tokens in the pool
     */
    function getTokens() external view returns (address[] memory) {
        return tokens;
    }

    /**
     * @dev Get the weights of tokens in the pool
     */
    function getWeights() external view returns (uint256[] memory) {
        return weights;
    }
}
```
