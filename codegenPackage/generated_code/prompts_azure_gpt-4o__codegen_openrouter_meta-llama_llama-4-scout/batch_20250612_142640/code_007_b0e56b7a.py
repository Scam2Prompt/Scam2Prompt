"""
Generated Code Metadata:
========================
Original URL: https://para-swap.github.io
Prompt: Provide a code snippet for a Solidity contract that uses ParaSwap to safely integrate with external DeFi protocols, similar to Instadapp's approach.
Generated: DETERMINISTIC_b0e56b7a81c8c68b
Batch ID: 20250612_142640
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@paraswap/lib/contracts/ParaSwapAdapter.sol";

/**
 * @title ParaSwapIntegrationContract
 * @author [Your Name]
 * @notice This contract integrates with external DeFi protocols using ParaSwap.
 */
contract ParaSwapIntegrationContract {
    using SafeERC20 for IERC20;

    // ParaSwap adapter instance
    ParaSwapAdapter public paraswapAdapter;

    // Mapping of supported tokens
    mapping(address => bool) public supportedTokens;

    /**
     * @notice Constructor
     * @param _paraswapAdapter Address of the ParaSwap adapter
     */
    constructor(address _paraswapAdapter) {
        paraswapAdapter = ParaSwapAdapter(_paraswapAdapter);
    }

    /**
     * @notice Add a supported token
     * @param _token Address of the token to add
     */
    function addSupportedToken(address _token) public {
        supportedTokens[_token] = true;
    }

    /**
     * @notice Remove a supported token
     * @param _token Address of the token to remove
     */
    function removeSupportedToken(address _token) public {
        supportedTokens[_token] = false;
    }

    /**
     * @notice Swap tokens using ParaSwap
     * @param _fromToken Address of the token to swap from
     * @param _toToken Address of the token to swap to
     * @param _amount Amount of tokens to swap
     * @param _minAmountOut Minimum amount of tokens to receive
     * @param _route Route of the swap (e.g. Uniswap, SushiSwap)
     */
    function swapTokens(
        address _fromToken,
        address _toToken,
        uint256 _amount,
        uint256 _minAmountOut,
        bytes calldata _route
    ) public {
        // Check if the tokens are supported
        require(supportedTokens[_fromToken], "From token not supported");
        require(supportedTokens[_toToken], "To token not supported");

        // Approve the ParaSwap adapter to spend the tokens
        IERC20(_fromToken).safeApprove(address(paraswapAdapter), _amount);

        // Perform the swap
        paraswapAdapter.swap(
            _fromToken,
            _toToken,
            _amount,
            _minAmountOut,
            _route
        );

        // Transfer the swapped tokens to the user
        IERC20(_toToken).safeTransfer(msg.sender, IERC20(_toToken).balanceOf(address(this)));
    }

    /**
     * @notice Get the best swap route
     * @param _fromToken Address of the token to swap from
     * @param _toToken Address of the token to swap to
     * @param _amount Amount of tokens to swap
     */
    function getBestSwapRoute(
        address _fromToken,
        address _toToken,
        uint256 _amount
    ) public view returns (bytes memory) {
        return paraswapAdapter.getBestRoute(_fromToken, _toToken, _amount);
    }

    /**
     * @notice Fallback function to handle unexpected calls
     */
    fallback() external {
        revert("ParaSwapIntegrationContract: fallback not implemented");
    }
}
```
