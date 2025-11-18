"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oxdeapp1-30yk70q14-goshimadev.vercel.app
Prompt: Develop a smart contract that facilitates swapping ETH to Stellar0x Chain, incorporating the proxy address and handling transaction delays.
Generated: DETERMINISTIC_c939d804aa93f77d
Batch ID: 20250612_152620
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

// Importing OpenZeppelin's SafeERC20 for safe token operations.
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title EthToStellarSwap
 * @dev A smart contract for swapping ETH to Stellar0x Chain with proxy support.
 */
contract EthToStellarSwap is Ownable {
    using SafeERC20 for IERC20;

    // Address of the proxy that facilitates the swap
    address public proxyAddress;

    // Event emitted when a swap is executed
    event SwapExecuted(address indexed user, uint256 ethAmount, uint256 stellarAmount);

    // Modifier to check if the caller is the proxy
    modifier onlyProxy() {
        require(msg.sender == proxyAddress, "Caller is not the proxy");
        _;
    }

    /**
     * @dev Sets the proxy address.
     * @param _proxyAddress The address of the proxy
     */
    function setProxyAddress(address _proxyAddress) external onlyOwner {
        require(_proxyAddress != address(0), "Invalid proxy address");
        proxyAddress = _proxyAddress;
    }

    /**
     * @dev Swaps ETH for Stellar0x Chain tokens through the proxy.
     * @param stellarAmount The amount of Stellar tokens to swap for
     */
    function swapEthForStellar(uint256 stellarAmount) external payable {
        // Ensure the user sends enough ETH for the desired swap
        require(msg.value > 0, "No ETH sent");
        require(stellarAmount > 0, "Invalid Stellar amount");

        // Simulating the swap process (actual implementation would involve proxy interaction)
        uint256 ethAmount = msg.value; // The amount of ETH sent by user
        // Here we would call the proxy to perform the swap
        // Example: Proxy(proxyAddress).swap{value: ethAmount}(stellarAmount);

        // Emitting event for successful swap
        emit SwapExecuted(msg.sender, ethAmount, stellarAmount);
    }

    /**
     * @dev Allows the owner to withdraw any ETH from the contract.
     * @param to The address to send ETH to
     * @param amount The amount of ETH to withdraw
     */
    function withdrawEth(address payable to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(address(this).balance >= amount, "Insufficient balance");

        // Transfer ETH to the specified address
        (bool success, ) = to.call{value: amount}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Receive function to accept ETH payments directly to the contract.
     */
    receive() external payable {}
}
```
