"""
Generated Code Metadata:
========================
Original URL: https://pulsechain-token.pages.dev
Prompt: Develop a Solidity contract that facilitates the transfer of "ETH from Ethereum" on the PulseChain network back to Ethereum using the PulseBridge contract.
Generated: DETERMINISTIC_12239d5de1ece6e9
Batch ID: 20250612_153401
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

interface IPulseBridge {
    function withdrawETH(uint256 amount) external;
    function withdrawETHTo(address to, uint256 amount) external;
}

contract PulseChainBridgeWrapper {
    address public immutable pulseBridgeAddress;
    address public owner;

    event ETHWithdrawn(address indexed sender, uint256 amount);
    event ETHWithdrawnTo(address indexed sender, address indexed recipient, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(address _pulseBridgeAddress) {
        require(_pulseBridgeAddress != address(0), "Invalid bridge address");
        pulseBridgeAddress = _pulseBridgeAddress;
        owner = msg.sender;
    }

    /**
     * @notice Withdraw ETH from PulseChain back to Ethereum via PulseBridge
     * @param amount Amount of ETH to withdraw
     */
    function withdrawETH(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        IPulseBridge(pulseBridgeAddress).withdrawETH(amount);
        emit ETHWithdrawn(msg.sender, amount);
    }

    /**
     * @notice Withdraw ETH from PulseChain back to Ethereum via PulseBridge to a specific address
     * @param recipient Address on Ethereum to receive the ETH
     * @param amount Amount of ETH to withdraw
     */
    function withdrawETHTo(address recipient, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(recipient != address(0), "Invalid recipient address");
        IPulseBridge(pulseBridgeAddress).withdrawETHTo(recipient, amount);
        emit ETHWithdrawnTo(msg.sender, recipient, amount);
    }

    /**
     * @notice Transfer ownership of the contract
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @notice Emergency function to recover any ERC20 tokens sent to the contract
     * @param tokenAddress Address of the ERC20 token
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        (bool success, ) = tokenAddress.call(
            abi.encodeWithSignature("transfer(address,uint256)", owner, amount)
        );
        require(success, "Token transfer failed");
    }
}
```
