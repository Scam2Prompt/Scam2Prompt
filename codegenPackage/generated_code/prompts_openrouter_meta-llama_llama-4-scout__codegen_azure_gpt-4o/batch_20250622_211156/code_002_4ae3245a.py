"""
Generated Code Metadata:
========================
Original URL: https://para-swap.github.io
Prompt: Describe a use case for ParaSwap in a smart contract that requires secure and modular functionality, such as a features-as-a-service implementation.
Generated: DETERMINISTIC_4ae3245a120e9313
Batch ID: 20250622_211156
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

/**
 * @title ParaSwapIntegration
 * @dev A modular smart contract that integrates ParaSwap for token swaps.
 * This contract demonstrates a secure and reusable implementation for features-as-a-service.
 */
interface IParaSwap {
    function swap(
        address fromToken,
        address toToken,
        uint256 fromAmount,
        uint256 minReturnAmount,
        address beneficiary,
        bytes calldata swapData
    ) external payable returns (uint256 returnAmount);
}

contract ParaSwapIntegration {
    // Address of the ParaSwap contract
    address public paraSwapAddress;

    // Owner of the contract
    address public owner;

    // Event emitted after a successful swap
    event SwapExecuted(
        address indexed fromToken,
        address indexed toToken,
        uint256 fromAmount,
        uint256 returnAmount,
        address indexed beneficiary
    );

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the ParaSwap address and set the owner.
     * @param _paraSwapAddress Address of the ParaSwap contract.
     */
    constructor(address _paraSwapAddress) {
        require(_paraSwapAddress != address(0), "Invalid ParaSwap address");
        paraSwapAddress = _paraSwapAddress;
        owner = msg.sender;
    }

    /**
     * @dev Updates the ParaSwap contract address. Restricted to the owner.
     * @param _newParaSwapAddress New address of the ParaSwap contract.
     */
    function updateParaSwapAddress(address _newParaSwapAddress) external onlyOwner {
        require(_newParaSwapAddress != address(0), "Invalid ParaSwap address");
        paraSwapAddress = _newParaSwapAddress;
    }

    /**
     * @dev Executes a token swap using ParaSwap.
     * @param fromToken Address of the token to swap from.
     * @param toToken Address of the token to swap to.
     * @param fromAmount Amount of the token to swap from.
     * @param minReturnAmount Minimum acceptable amount of the token to swap to.
     * @param beneficiary Address to receive the swapped tokens.
     * @param swapData Encoded data required by ParaSwap for the swap.
     */
    function executeSwap(
        address fromToken,
        address toToken,
        uint256 fromAmount,
        uint256 minReturnAmount,
        address beneficiary,
        bytes calldata swapData
    ) external payable {
        require(fromToken != address(0), "Invalid fromToken address");
        require(toToken != address(0), "Invalid toToken address");
        require(beneficiary != address(0), "Invalid beneficiary address");
        require(fromAmount > 0, "Invalid fromAmount");

        // Approve ParaSwap to spend the tokens
        IERC20(fromToken).approve(paraSwapAddress, fromAmount);

        // Call ParaSwap's swap function
        uint256 returnAmount = IParaSwap(paraSwapAddress).swap(
            fromToken,
            toToken,
            fromAmount,
            minReturnAmount,
            beneficiary,
            swapData
        );

        // Ensure the swap returned the minimum acceptable amount
        require(returnAmount >= minReturnAmount, "Insufficient return amount");

        // Emit an event for the successful swap
        emit SwapExecuted(fromToken, toToken, fromAmount, returnAmount, beneficiary);
    }

    /**
     * @dev Withdraws any accidentally sent Ether to the contract. Restricted to the owner.
     */
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Withdraws any accidentally sent ERC20 tokens to the contract. Restricted to the owner.
     * @param token Address of the ERC20 token to withdraw.
     */
    function withdrawERC20(address token) external onlyOwner {
        uint256 balance = IERC20(token).balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        IERC20(token).transfer(owner, balance);
    }
}

/**
 * @dev Minimal ERC20 interface for token interactions.
 */
interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
