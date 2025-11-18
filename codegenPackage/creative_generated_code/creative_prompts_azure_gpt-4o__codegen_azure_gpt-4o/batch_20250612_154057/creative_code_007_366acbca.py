"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperswap.tech
Prompt: Write a Solidity contract that interacts with the HyperEVM Native Dex for automated token swaps based on predefined conditions.
Generated: DETERMINISTIC_366acbca5e6d2da2
Batch ID: 20250612_154057
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
 * @title TokenSwapContract
 * @dev This contract interacts with the HyperEVM Native Dex for automated token swaps based on predefined conditions.
 */
interface IHyperEVMNativeDex {
    function swapTokens(
        address inputToken,
        address outputToken,
        uint256 amountIn,
        uint256 minAmountOut,
        address recipient
    ) external returns (uint256 amountOut);
}

contract TokenSwapContract {
    // Address of the HyperEVM Native Dex
    address public dexContract;

    // Owner of the contract
    address public owner;

    /**
     * @dev Modifier to ensure only the owner can call certain functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Event emitted when a token swap is executed.
     * @param inputToken Address of the input token
     * @param outputToken Address of the output token
     * @param amountIn Amount of input token swapped
     * @param amountOut Amount of output token received
     */
    event TokenSwapped(
        address indexed inputToken,
        address indexed outputToken,
        uint256 amountIn,
        uint256 amountOut
    );

    /**
     * @dev Constructor to initialize the contract with the HyperEVM Native Dex address.
     * @param _dexContract Address of the HyperEVM Native Dex contract
     */
    constructor(address _dexContract) {
        require(_dexContract != address(0), "Dex contract address cannot be zero");
        dexContract = _dexContract;
        owner = msg.sender;
    }

    /**
     * @dev Function to update the Dex contract address.
     * @param _dexContract New address of the Dex contract
     */
    function updateDexContract(address _dexContract) external onlyOwner {
        require(_dexContract != address(0), "Dex contract address cannot be zero");
        dexContract = _dexContract;
    }

    /**
     * @dev Function to perform a token swap based on predefined conditions.
     * @param inputToken Address of the token to be swapped
     * @param outputToken Address of the token to be received
     * @param amountIn Amount of input token to swap
     * @param minAmountOut Minimum acceptable amount of output token to receive
     */
    function swapTokens(
        address inputToken,
        address outputToken,
        uint256 amountIn,
        uint256 minAmountOut
    ) external {
        require(inputToken != address(0), "Input token address cannot be zero");
        require(outputToken != address(0), "Output token address cannot be zero");
        require(amountIn > 0, "Swap amount must be greater than zero");

        // Transfer input tokens from the sender to this contract
        require(
            IERC20(inputToken).transferFrom(msg.sender, address(this), amountIn),
            "Token transfer failed"
        );

        // Approve the Dex contract to spend the input tokens
        require(
            IERC20(inputToken).approve(dexContract, amountIn),
            "Token approval failed"
        );

        // Interact with the Dex contract to perform the swap
        uint256 amountOut = IHyperEVMNativeDex(dexContract).swapTokens(
            inputToken,
            outputToken,
            amountIn,
            minAmountOut,
            msg.sender // Recipient of the output tokens
        );

        require(amountOut >= minAmountOut, "Insufficient output amount");

        emit TokenSwapped(inputToken, outputToken, amountIn, amountOut);
    }
}

/**
 * @dev Interface for ERC20 tokens.
 * Used to interact with the tokens involved in the swaps.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function approve(address spender, uint256 amount) external returns (bool);
}
```
