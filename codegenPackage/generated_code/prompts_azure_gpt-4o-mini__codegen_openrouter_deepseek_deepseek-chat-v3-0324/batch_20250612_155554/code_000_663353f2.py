"""
Generated Code Metadata:
========================
Original URL: https://op-enocean.github.io
Prompt: Explain how to implement Open Ocean patterns in Ethereum smart contracts to enhance security and composability.
Generated: DETERMINISTIC_663353f28f97c345
Batch ID: 20250612_155554
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
 * @title OpenOceanPatterns
 * @dev A collection of patterns inspired by OpenOcean to enhance security and composability in Ethereum smart contracts
 */
library OpenOceanPatterns {
    // Error declarations
    error InvalidAddress();
    error InsufficientBalance();
    error TransferFailed();
    error Unauthorized();
    error ReentrancyAttempt();

    /**
     * @dev Checks if an address is a contract (not EOAs)
     * @param addr The address to check
     */
    modifier onlyContract(address addr) {
        if (addr.code.length == 0) revert InvalidAddress();
        _;
    }

    /**
     * @dev Checks if an address is not zero address
     * @param addr The address to check
     */
    modifier notZeroAddress(address addr) {
        if (addr == address(0)) revert InvalidAddress();
        _;
    }

    /**
     * @dev Checks if the caller is the contract owner
     * @param owner The owner address to check against
     */
    modifier onlyOwner(address owner) {
        if (msg.sender != owner) revert Unauthorized();
        _;
    }

    /**
     * @dev Reentrancy guard pattern
     */
    modifier nonReentrant() {
        // Mappings are more gas efficient than storage variables for single use
        uint256 _status;
        assembly {
            _status := sload(0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef)
        }
        if (_status == 1) revert ReentrancyAttempt();
        
        assembly {
            sstore(0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef, 1)
        }
        _;
        assembly {
            sstore(0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef, 0)
        }
    }

    /**
     * @dev Safe transfer helper for ERC20 tokens
     * @param token The token contract address
     * @param to The recipient address
     * @param value The amount to transfer
     */
    function safeTransfer(
        address token,
        address to,
        uint256 value
    ) internal {
        (bool success, bytes memory data) = token.call(
            abi.encodeWithSelector(0xa9059cbb, to, value)
        );
        if (!success || (data.length > 0 && !abi.decode(data, (bool)))) {
            revert TransferFailed();
        }
    }

    /**
     * @dev Safe transferFrom helper for ERC20 tokens
     * @param token The token contract address
     * @param from The sender address
     * @param to The recipient address
     * @param value The amount to transfer
     */
    function safeTransferFrom(
        address token,
        address from,
        address to,
        uint256 value
    ) internal {
        (bool success, bytes memory data) = token.call(
            abi.encodeWithSelector(0x23b872dd, from, to, value)
        );
        if (!success || (data.length > 0 && !abi.decode(data, (bool)))) {
            revert TransferFailed();
        }
    }

    /**
     * @dev Safe ETH transfer helper
     * @param to The recipient address
     * @param value The amount to transfer
     */
    function safeTransferETH(address to, uint256 value) internal {
        (bool success, ) = to.call{value: value}("");
        if (!success) revert TransferFailed();
    }

    /**
     * @dev Batch call helper for composability
     * @param targets Array of target addresses
     * @param data Array of call data
     * @param values Array of ETH values to send
     */
    function batchCall(
        address[] calldata targets,
        bytes[] calldata data,
        uint256[] calldata values
    ) internal {
        require(
            targets.length == data.length && targets.length == values.length,
            "Array length mismatch"
        );

        for (uint256 i = 0; i < targets.length; i++) {
            (bool success, ) = targets[i].call{value: values[i]}(data[i]);
            require(success, "Batch call failed");
        }
    }

    /**
     * @dev Checks balance before operation
     * @param token The token contract address
     * @param owner The owner address
     * @param required The required balance
     */
    function checkBalance(
        address token,
        address owner,
        uint256 required
    ) internal view {
        (bool success, bytes memory data) = token.staticcall(
            abi.encodeWithSelector(0x70a08231, owner)
        );
        require(success, "Balance check failed");
        uint256 balance = abi.decode(data, (uint256));
        if (balance < required) revert InsufficientBalance();
    }
}

/**
 * @title ExampleUsage
 * @dev Example contract demonstrating OpenOcean patterns usage
 */
contract ExampleUsage {
    using OpenOceanPatterns for address;

    address public owner;
    uint256 private _status; // For reentrancy guard

    constructor() {
        owner = msg.sender;
    }

    receive() external payable {}

    /**
     * @dev Withdraw tokens using safe transfer pattern
     * @param token The token contract address
     * @param amount The amount to withdraw
     */
    function withdrawTokens(address token, uint256 amount)
        external
        OpenOceanPatterns.nonReentrant
        OpenOceanPatterns.onlyOwner(owner)
        OpenOceanPatterns.notZeroAddress(token)
    {
        token.safeTransfer(msg.sender, amount);
    }

    /**
     * @dev Execute batch operations
     * @param targets Array of target addresses
     * @param data Array of call data
     * @param values Array of ETH values to send
     */
    function executeBatch(
        address[] calldata targets,
        bytes[] calldata data,
        uint256[] calldata values
    ) external OpenOceanPatterns.onlyOwner(owner) {
        OpenOceanPatterns.batchCall(targets, data, values);
    }

    /**
     * @dev Check token balance
     * @param token The token contract address
     * @param user The user address
     * @param required The required balance
     */
    function verifyBalance(
        address token,
        address user,
        uint256 required
    ) external view OpenOceanPatterns.onlyContract(token) {
        OpenOceanPatterns.checkBalance(token, user, required);
    }
}
```
