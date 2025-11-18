"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teset123214.pages.dev
Prompt: Develop a smart contract that facilitates swapping Ethereum for $TIMI tokens, ensuring compliance with the tokenomics (1B supply, 0/0 tax) mentioned on the Timi Claim Airdrop page.
Generated: DETERMINISTIC_b6c471ab5109352d
Batch ID: 20250612_152658
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
 * @title TIMISwapContract
 * @dev A smart contract to facilitate swapping ETH for $TIMI tokens.
 * $TIMI tokenomics: 1 billion token supply, no transaction tax (0/0 tax).
 * This contract assumes $TIMI is an ERC20 token.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function totalSupply() external view returns (uint256);
}

contract TIMISwapContract {
    // Address of the $TIMI token contract
    IERC20 public timiToken;

    // Owner of the contract
    address public owner;

    // ETH to TIMI exchange rate (e.g., 1 ETH = 1000 TIMI)
    uint256 public ethToTimiRate;

    /**
     * @dev Ensures only the contract owner can call certain functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor for the TIMISwapContract.
     * @param _timiToken Address of the $TIMI token contract.
     * @param _ethToTimiRate ETH to TIMI exchange rate.
     */
    constructor(IERC20 _timiToken, uint256 _ethToTimiRate) {
        require(address(_timiToken) != address(0), "Invalid token address");
        require(_ethToTimiRate > 0, "Exchange rate must be greater than 0");

        timiToken = _timiToken;
        ethToTimiRate = _ethToTimiRate;
        owner = msg.sender;
    }

    /**
     * @dev Swaps ETH for $TIMI tokens.
     * Transfers $TIMI tokens to the sender based on the ETH sent.
     * Reverts if the contract does not have enough tokens to fulfill the swap.
     */
    function swapETHForTimi() external payable {
        require(msg.value > 0, "ETH amount must be greater than 0");

        // Calculate the amount of $TIMI tokens to transfer
        uint256 timiAmount = msg.value * ethToTimiRate;

        // Check if the contract has enough $TIMI tokens for the swap
        require(timiToken.balanceOf(address(this)) >= timiAmount, "Insufficient $TIMI tokens in contract");

        // Transfer $TIMI tokens to the sender
        require(timiToken.transfer(msg.sender, timiAmount), "Token transfer failed");
    }

    /**
     * @dev Allows the owner to update the ETH to TIMI exchange rate.
     * @param _newRate New ETH to TIMI exchange rate.
     */
    function updateExchangeRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Exchange rate must be greater than 0");
        ethToTimiRate = _newRate;
    }

    /**
     * @dev Allows the owner to withdraw ETH collected in the contract.
     */
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");

        // Transfer ETH to the owner
        (bool success,) = owner.call{value: balance}("");
        require(success, "ETH withdrawal failed");
    }

    /**
     * @dev Allows the owner to withdraw any remaining $TIMI tokens in the contract.
     */
    function withdrawTimiTokens() external onlyOwner {
        uint256 balance = timiToken.balanceOf(address(this));
        require(balance > 0, "No $TIMI tokens to withdraw");

        // Transfer $TIMI tokens to the owner
        require(timiToken.transfer(owner, balance), "Token withdrawal failed");
    }

    /**
     * @dev Fallback function to accept ETH sent directly to the contract.
     */
    receive() external payable {}

    /**
     * @dev Prevent accidental ETH transfers to non-payable functions.
     */
    fallback() external payable {
        revert("Invalid function call");
    }
}
```
