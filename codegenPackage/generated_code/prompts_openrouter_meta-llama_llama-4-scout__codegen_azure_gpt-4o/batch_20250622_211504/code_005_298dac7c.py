"""
Generated Code Metadata:
========================
Original URL: https://iqnetwork.io
Prompt: Create a code snippet in Solidity to interact with the IQ Token's smart contract on the Ethereum blockchain.
Generated: DETERMINISTIC_298dac7cdac0d268
Batch ID: 20250622_211504
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
 * @title IQTokenInteractor
 * @dev A contract to interact with the IQ Token smart contract on the Ethereum blockchain.
 * This contract allows querying balances and transferring IQ tokens.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract IQTokenInteractor {
    // Address of the IQ Token contract
    address public iqTokenAddress;

    // Event emitted when tokens are successfully transferred
    event TokensTransferred(address indexed from, address indexed to, uint256 amount);

    /**
     * @dev Constructor to set the IQ Token contract address.
     * @param _iqTokenAddress The address of the IQ Token contract.
     */
    constructor(address _iqTokenAddress) {
        require(_iqTokenAddress != address(0), "Invalid token address");
        iqTokenAddress = _iqTokenAddress;
    }

    /**
     * @dev Get the balance of IQ tokens for a specific address.
     * @param account The address to query the balance for.
     * @return The balance of IQ tokens.
     */
    function getBalance(address account) external view returns (uint256) {
        require(account != address(0), "Invalid account address");
        IERC20 iqToken = IERC20(iqTokenAddress);
        return iqToken.balanceOf(account);
    }

    /**
     * @dev Transfer IQ tokens to a recipient.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return success True if the transfer was successful, false otherwise.
     */
    function transferTokens(address recipient, uint256 amount) external returns (bool success) {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Transfer amount must be greater than zero");

        IERC20 iqToken = IERC20(iqTokenAddress);
        bool result = iqToken.transfer(recipient, amount);
        require(result, "Token transfer failed");

        emit TokensTransferred(msg.sender, recipient, amount);
        return result;
    }
}
```
