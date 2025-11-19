"""
Generated Code Metadata:
========================
Original URL: https://soniclaqs.com
Prompt: "Create a simple Vyper contract that takes advantage of SonicVM's lightning-fast execution and 100% EVM compatibility for a decentralized finance (DeFi) application."
Generated: DETERMINISTIC_e79eeda007efabd7
Batch ID: 20250622_210054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# @version ^0.3.9

"""
@title Fast DeFi Token Swap
@notice A simple token swap contract leveraging SonicVM's performance
@dev Fully compatible with EVM, optimized for speed and gas efficiency
"""

from vyper.interfaces import ERC20

interface IUniswapV2Router:
    def swapExactTokensForTokens(
        amountIn: uint256,
        amountOutMin: uint256,
        path: address[20],
        to: address,
        deadline: uint256
    ) -> uint256[2]: view

event TokenSwap:
    sender: indexed(address)
    tokenIn: indexed(address)
    tokenOut: indexed(address)
    amountIn: uint256
    amountOut: uint256

# Address of UniswapV2Router
router: public(IUniswapV2Router)

@external
def __init__(_router: address):
    """
    @notice Initialize the contract with Uniswap router address
    @param _router Address of the UniswapV2Router contract
    """
    self.router = IUniswapV2Router(_router)

@external
@nonreentrant('lock')
def swap_tokens(
    tokenIn: address,
    tokenOut: address,
    amountIn: uint256,
    amountOutMin: uint256,
    deadline: uint256,
    path: address[20]
) -> uint256:
    """
    @notice Execute a token swap with minimal gas usage
    @dev Requires prior ERC20 approval for tokenIn
    @param tokenIn Address of input token
    @param tokenOut Address of output token
    @param amountIn Amount of input tokens to swap
    @param amountOutMin Minimum amount of output tokens expected
    @param deadline Unix timestamp after which swap will fail
    @param path Array of token addresses representing swap path
    @return amountOut Actual amount of output tokens received
    """
    # Transfer tokens from sender to this contract
    assert ERC20(tokenIn).transferFrom(msg.sender, self, amountIn), "Transfer failed"
    
    # Approve router to spend tokens
    assert ERC20(tokenIn).approve(self.router.address, amountIn), "Approval failed"
    
    # Execute swap
    amounts: uint256[2] = self.router.swapExactTokensForTokens(
        amountIn,
        amountOutMin,
        path,
        msg.sender,
        deadline
    )
    
    amountOut: uint256 = amounts[1]
    
    # Verify minimum output
    assert amountOut >= amountOutMin, "Insufficient output amount"
    
    log TokenSwap(msg.sender, tokenIn, tokenOut, amountIn, amountOut)
    
    return amountOut

@external
@view
def get_estimated_output(
    tokenIn: address,
    tokenOut: address,
    amountIn: uint256,
    path: address[20]
) -> uint256:
    """
    @notice Estimate output amount for a given swap
    @param tokenIn Address of input token
    @param tokenOut Address of output token
    @param amountIn Amount of input tokens
    @param path Array of token addresses representing swap path
    @return Estimated amount of output tokens
    """
    amounts: uint256[2] = self.router.swapExactTokensForTokens(
        amountIn,
        0,
        path,
        self,  # Using self as to address since this is just a view call
        2**256 - 1  # Max deadline for estimation
    )
    return amounts[1]
```
