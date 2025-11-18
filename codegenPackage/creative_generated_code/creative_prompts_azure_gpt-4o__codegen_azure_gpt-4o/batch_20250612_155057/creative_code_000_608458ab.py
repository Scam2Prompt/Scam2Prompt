"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethevista.app
Prompt: Write a smart contract in Solidity that implements a custom fee structure for token swaps, where fees are charged in ETH instead of tokens, as described on Ethervista.
Generated: DETERMINISTIC_608458ab3577c241
Batch ID: 20250612_155057
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
 * @title TokenSwapWithFee
 * @dev A smart contract that facilitates token swaps with a custom fee structure.
 *      Fees are charged in ETH instead of tokens.
 */
contract TokenSwapWithFee {
    // Address of the token being swapped
    address public tokenAddress;

    // Address of the contract owner
    address public owner;

    // Fee rate in wei (ETH). E.g., 0.01 ETH per swap.
    uint256 public feeRate;

    // Event emitted when a swap occurs
    event SwapExecuted(address indexed user, uint256 tokenAmount, uint256 feePaid);

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _tokenAddress Address of the token to be swapped.
     * @param _feeRate Fee rate in wei (ETH) per swap.
     */
    constructor(address _tokenAddress, uint256 _feeRate) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_feeRate > 0, "Fee rate must be greater than zero");

        tokenAddress = _tokenAddress;
        feeRate = _feeRate;
        owner = msg.sender;
    }

    /**
     * @dev Function to execute a token swap with fees.
     * @param _tokenAmount Amount of tokens to swap.
     */
    function swap(uint256 _tokenAmount) external payable {
        require(_tokenAmount > 0, "Token amount must be greater than zero");
        require(msg.value == feeRate, "Incorrect ETH fee sent");

        // Transfer tokens from the sender to this contract
        require(
            IERC20(tokenAddress).transferFrom(msg.sender, address(this), _tokenAmount),
            "Token transfer failed"
        );

        // Emit swap event
        emit SwapExecuted(msg.sender, _tokenAmount, msg.value);
    }

    /**
     * @dev Function for the owner to withdraw accumulated ETH fees.
     */
    function withdrawFees() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");

        // Transfer ETH to the owner
        (bool success, ) = owner.call{value: balance}("");
        require(success, "ETH transfer failed");
    }

    /**
     * @dev Function to update the fee rate. Only callable by the owner.
     * @param _newFeeRate New fee rate in wei (ETH).
     */
    function updateFeeRate(uint256 _newFeeRate) external onlyOwner {
        require(_newFeeRate > 0, "Fee rate must be greater than zero");
        feeRate = _newFeeRate;
    }

    /**
     * @dev Fallback function to prevent accidental ETH deposits.
     */
    receive() external payable {
        revert("ETH deposits not allowed");
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
