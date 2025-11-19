"""
Generated Code Metadata:
========================
Original URL: https://quecko.com
Prompt: Generate a smart contract for a decentralized application (dApp) that integrates with a multichain wallet, as described by Quecko's blockchain development services.
Generated: DETERMINISTIC_970d2e57fc0c40b4
Batch ID: 20250612_163149
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MultiChainWalletIntegration
 * @dev A smart contract for decentralized applications (dApps) that integrates with multichain wallets.
 * Supports cross-chain transactions, token swaps, and wallet management.
 */
contract MultiChainWalletIntegration is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to store supported chain information
    struct ChainInfo {
        uint256 chainId;
        string chainName;
        bool isActive;
    }

    // Struct to store wallet information
    struct WalletInfo {
        address walletAddress;
        uint256[] supportedChainIds;
    }

    // Mapping from chain ID to ChainInfo
    mapping(uint256 => ChainInfo) public supportedChains;

    // Mapping from user address to WalletInfo
    mapping(address => WalletInfo) public userWallets;

    // Events
    event ChainAdded(uint256 chainId, string chainName);
    event ChainRemoved(uint256 chainId);
    event WalletRegistered(address indexed user, address walletAddress, uint256[] chainIds);
    event CrossChainTransfer(
        address indexed sender,
        address indexed recipient,
        uint256 amount,
        uint256 fromChainId,
        uint256 toChainId,
        address tokenAddress
    );

    /**
     * @dev Modifier to check if the chain is supported
     */
    modifier onlySupportedChain(uint256 chainId) {
        require(supportedChains[chainId].isActive, "Chain not supported");
        _;
    }

    /**
     * @dev Add a new supported chain
     * @param chainId The chain ID to add
     * @param chainName The name of the chain
     */
    function addSupportedChain(uint256 chainId, string memory chainName) external onlyOwner {
        require(!supportedChains[chainId].isActive, "Chain already supported");
        supportedChains[chainId] = ChainInfo(chainId, chainName, true);
        emit ChainAdded(chainId, chainName);
    }

    /**
     * @dev Remove a supported chain
     * @param chainId The chain ID to remove
     */
    function removeSupportedChain(uint256 chainId) external onlyOwner {
        require(supportedChains[chainId].isActive, "Chain not supported");
        supportedChains[chainId].isActive = false;
        emit ChainRemoved(chainId);
    }

    /**
     * @dev Register a multichain wallet for a user
     * @param walletAddress The wallet address to register
     * @param chainIds Array of supported chain IDs
     */
    function registerWallet(address walletAddress, uint256[] memory chainIds) external {
        require(walletAddress != address(0), "Invalid wallet address");
        require(chainIds.length > 0, "At least one chain must be supported");

        for (uint256 i = 0; i < chainIds.length; i++) {
            require(supportedChains[chainIds[i]].isActive, "Unsupported chain detected");
        }

        userWallets[msg.sender] = WalletInfo(walletAddress, chainIds);
        emit WalletRegistered(msg.sender, walletAddress, chainIds);
    }

    /**
     * @dev Execute a cross-chain transfer
     * @param recipient The recipient address on the destination chain
     * @param amount The amount to transfer
     * @param fromChainId The source chain ID
     * @param toChainId The destination chain ID
     * @param tokenAddress The ERC20 token address (address(0) for native token)
     */
    function crossChainTransfer(
        address recipient,
        uint256 amount,
        uint256 fromChainId,
        uint256 toChainId,
        address tokenAddress
    ) external payable nonReentrant onlySupportedChain(fromChainId) onlySupportedChain(toChainId) {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than 0");

        WalletInfo memory senderWallet = userWallets[msg.sender];
        require(senderWallet.walletAddress != address(0), "Wallet not registered");

        bool fromChainSupported = false;
        bool toChainSupported = false;

        for (uint256 i = 0; i < senderWallet.supportedChainIds.length; i++) {
            if (senderWallet.supportedChainIds[i] == fromChainId) {
                fromChainSupported = true;
            }
            if (senderWallet.supportedChainIds[i] == toChainId) {
                toChainSupported = true;
            }
        }

        require(fromChainSupported && toChainSupported, "Chain not supported by wallet");

        if (tokenAddress == address(0)) {
            require(msg.value == amount, "Incorrect ETH amount");
            // In a production environment, this would interact with a bridge contract
            // For this example, we just emit the event
        } else {
            IERC20 token = IERC20(tokenAddress);
            require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");
            // In a production environment, tokens would be locked/bridged here
        }

        emit CrossChainTransfer(msg.sender, recipient, amount, fromChainId, toChainId, tokenAddress);
    }

    /**
     * @dev Withdraw tokens from the contract (owner only)
     * @param tokenAddress The token contract address (address(0) for native token)
     * @param amount The amount to withdraw
     */
    function withdrawFunds(address tokenAddress, uint256 amount) external onlyOwner {
        if (tokenAddress == address(0)) {
            payable(owner()).transfer(amount);
        } else {
            IERC20 token = IERC20(tokenAddress);
            token.transfer(owner(), amount);
        }
    }
}
```
