"""
Generated Code Metadata:
========================
Original URL: https://pulse-defi.pages.dev
Prompt: Compare the features and benefits of ERC20 and PRC20 tokens on PulseChain, and explain how to use a balance checker for these tokens.
Generated: DETERMINISTIC_319cff0f97b93b0f
Batch ID: 20250622_210914
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
 * @title TokenBalanceChecker
 * @dev A utility contract to check balances of ERC20 and PRC20 tokens on PulseChain
 */
contract TokenBalanceChecker {
    /**
     * @dev ERC20 Token Interface
     */
    interface IERC20 {
        function balanceOf(address account) external view returns (uint256);
        function decimals() external view returns (uint8);
    }

    /**
     * @dev PRC20 Token Interface (PulseChain's version of ERC20)
     */
    interface IPRC20 {
        function balanceOf(address account) external view returns (uint256);
        function decimals() external view returns (uint8);
    }

    /**
     * @notice Get the balance of an ERC20 token for a given address
     * @param tokenAddress The address of the ERC20 token contract
     * @param userAddress The address to check balance for
     * @return The token balance with decimals
     */
    function getERC20Balance(
        address tokenAddress,
        address userAddress
    ) public view returns (uint256) {
        require(tokenAddress != address(0), "Token address cannot be zero");
        require(userAddress != address(0), "User address cannot be zero");

        IERC20 token = IERC20(tokenAddress);
        return token.balanceOf(userAddress);
    }

    /**
     * @notice Get the balance of a PRC20 token for a given address
     * @param tokenAddress The address of the PRC20 token contract
     * @param userAddress The address to check balance for
     * @return The token balance with decimals
     */
    function getPRC20Balance(
        address tokenAddress,
        address userAddress
    ) public view returns (uint256) {
        require(tokenAddress != address(0), "Token address cannot be zero");
        require(userAddress != address(0), "User address cannot be zero");

        IPRC20 token = IPRC20(tokenAddress);
        return token.balanceOf(userAddress);
    }

    /**
     * @notice Get formatted balance (adjusted for decimals) of an ERC20 token
     * @param tokenAddress The address of the ERC20 token contract
     * @param userAddress The address to check balance for
     * @return The formatted token balance
     */
    function getFormattedERC20Balance(
        address tokenAddress,
        address userAddress
    ) public view returns (uint256) {
        uint256 balance = getERC20Balance(tokenAddress, userAddress);
        IERC20 token = IERC20(tokenAddress);
        uint8 decimals = token.decimals();
        return balance / (10 ** decimals);
    }

    /**
     * @notice Get formatted balance (adjusted for decimals) of a PRC20 token
     * @param tokenAddress The address of the PRC20 token contract
     * @param userAddress The address to check balance for
     * @return The formatted token balance
     */
    function getFormattedPRC20Balance(
        address tokenAddress,
        address userAddress
    ) public view returns (uint256) {
        uint256 balance = getPRC20Balance(tokenAddress, userAddress);
        IPRC20 token = IPRC20(tokenAddress);
        uint8 decimals = token.decimals();
        return balance / (10 ** decimals);
    }
}
```

```javascript
// JavaScript implementation for checking token balances on PulseChain

/**
 * ERC20/PRC20 Token Balance Checker Utility
 */
class PulseChainTokenChecker {
  /**
   * @param {Object} provider - Web3 provider (e.g., from MetaMask)
   */
  constructor(provider) {
    this.web3 = new Web3(provider);
  }

  /**
   * Get ERC20 token balance
   * @param {string} tokenAddress - Token contract address
   * @param {string} userAddress - User wallet address
   * @returns {Promise<string>} Formatted token balance
   */
  async getERC20Balance(tokenAddress, userAddress) {
    if (!this.web3.utils.isAddress(tokenAddress)) {
      throw new Error('Invalid token address');
    }
    if (!this.web3.utils.isAddress(userAddress)) {
      throw new Error('Invalid user address');
    }

    const abi = [
      {
        constant: true,
        inputs: [{ name: "_owner", type: "address" }],
        name: "balanceOf",
        outputs: [{ name: "balance", type: "uint256" }],
        type: "function",
      },
      {
        constant: true,
        inputs: [],
        name: "decimals",
        outputs: [{ name: "", type: "uint8" }],
        type: "function",
      },
    ];

    const contract = new this.web3.eth.Contract(abi, tokenAddress);
    const [balance, decimals] = await Promise.all([
      contract.methods.balanceOf(userAddress).call(),
      contract.methods.decimals().call(),
    ]);

    return (balance / 10 ** decimals).toString();
  }

  /**
   * Get PRC20 token balance (same as ERC20 on PulseChain)
   * @param {string} tokenAddress - Token contract address
   * @param {string} userAddress - User wallet address
   * @returns {Promise<string>} Formatted token balance
   */
  async getPRC20Balance(tokenAddress, userAddress) {
    // PRC20 uses the same interface as ERC20 on PulseChain
    return this.getERC20Balance(tokenAddress, userAddress);
  }
}
```
