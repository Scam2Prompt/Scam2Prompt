"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m-wisemonkey.pages.dev
Prompt: Develop a smart contract template for swapping $monky tokens on a decentralized exchange.
Generated: DETERMINISTIC_0b2b164b0babb8b1
Batch ID: 20250612_150024
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
 * @title MonkyTokenSwap
 * @dev This smart contract facilitates swapping $MONKY tokens on a decentralized exchange.
 * Ensure the token uses the ERC20 standard.
 */
contract MonkyTokenSwap {
    // Address of the $MONKY token contract
    address public monkyTokenAddress;

    // Address of the decentralized exchange (DEX) router
    address public dexRouterAddress;

    // Owner of the contract
    address public owner;

    // Event emitted whenever a token swap is successfully performed
    event TokenSwapped(
        address indexed user,
        uint256 amountIn,
        uint256 amountOut,
        address indexed tokenOut
    );

    /**
     * @dev Modifier to restrict certain functionality to the owner of the contract.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor initializes the contract with $MONKY token and DEX router addresses.
     * @param _monkyTokenAddress Address of the $MONKY token (ERC20 token contract).
     * @param _dexRouterAddress Address of the decentralized exchange router.
     */
    constructor(address _monkyTokenAddress, address _dexRouterAddress) {
        require(
            _monkyTokenAddress != address(0),
            "Invalid $MONKY token address"
        );
        require(_dexRouterAddress != address(0), "Invalid DEX router address");

        monkyTokenAddress = _monkyTokenAddress;
        dexRouterAddress = _dexRouterAddress;
        owner = msg.sender;
    }

    /**
     * @dev Function to swap $MONKY tokens for another token.
     * Assumes the DEX router has an appropriate swap implementation.
     * @param tokenOut The address of the token to receive after the swap.
     * @param amountIn The amount of $MONKY tokens to swap.
     * @param amountOutMin Minimum amount of `tokenOut` to receive from the swap.
     * @param path The swap path (typically [$MONKY, tokenOut]).
     * @param deadline The deadline for the swap transaction (Unix timestamp).
     */
    function swapTokens(
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        uint256 deadline
    ) external {
        require(tokenOut != address(0), "Invalid tokenOut address");
        require(amountIn > 0, "AmountIn must be greater than zero");
        require(path[0] == monkyTokenAddress, "Path must start with $MONKY");

        // Transfer $MONKY tokens from the sender to this contract
        bool success = IERC20(monkyTokenAddress).transferFrom(
            msg.sender,
            address(this),
            amountIn
        );
        require(success, "$MONKY token transfer failed");

        // Approve the DEX router to spend $MONKY tokens
        success = IERC20(monkyTokenAddress).approve(dexRouterAddress, amountIn);
        require(success, "Approval to DEX router failed");

        // Perform the token swap on the DEX router
        try IDEXRouter(dexRouterAddress).swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        ) returns (uint256[] memory amounts) {
            // Emit the swap event
            emit TokenSwapped(msg.sender, amountIn, amounts[1], tokenOut);
        } catch {
            revert("Token swap failed");
        }
    }

    /**
     * @dev Change the address of the DEX router.
     * @param _newDexRouterAddress New DEX router address.
     */
    function updateDexRouterAddress(address _newDexRouterAddress)
        external
        onlyOwner
    {
        require(_newDexRouterAddress != address(0), "Invalid DEX router address");
        dexRouterAddress = _newDexRouterAddress;
    }

    /**
     * @dev Change the address of the $MONKY token.
     * @param _newMonkyTokenAddress New $MONKY token address.
     */
    function updateMonkyTokenAddress(address _newMonkyTokenAddress)
        external
        onlyOwner
    {
        require(
            _newMonkyTokenAddress != address(0),
            "Invalid $MONKY token address"
        );
        monkyTokenAddress = _newMonkyTokenAddress;
    }

    /**
     * @dev Withdraw accidentally sent tokens to the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount to withdraw.
     */
    function withdrawTokens(address token, uint256 amount)
        external
        onlyOwner
    {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        bool success = IERC20(token).transfer(owner, amount);
        require(success, "Token withdrawal failed");
    }
}

// Interface for interacting with ERC20 tokens
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function approve(address spender, uint256 amount) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}

// Interface for interacting with a DEX router
interface IDEXRouter {
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts);
}
```
