"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cowswap.cc
Prompt: Provide a Solidity example for integrating CoW Swap's Vault Relayer v1.3.1 into a smart contract to facilitate token swaps for supported cryptocurrencies like AAVE and LINK.
Generated: DETERMINISTIC_f2d502bdaa21eb3f
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title CoWSwapIntegration
 * @dev A smart contract to facilitate token swaps using CoW Swap's Vault Relayer v1.3.1.
 */
interface IVaultRelayer {
    /**
     * @dev Executes a token swap through CoW Swap's Vault Relayer.
     * @param sender Address initiating the swap.
     * @param recipient Address receiving the swapped tokens.
     * @param sellToken Address of the token being sold.
     * @param buyToken Address of the token being bought.
     * @param sellAmount Amount of sellToken being sold.
     * @param minBuyAmount Minimum amount of buyToken expected.
     * @param metadata Additional metadata (e.g., order or swap details).
     */
    function swap(
        address sender,
        address recipient,
        address sellToken,
        address buyToken,
        uint256 sellAmount,
        uint256 minBuyAmount,
        bytes calldata metadata
    ) external;
}

contract CoWSwapIntegration {
    address public owner; // Owner of the contract
    address public vaultRelayerAddress; // Address of CoW Swap's Vault Relayer
    
    event TokenSwapped(
        address indexed sender,
        address indexed recipient,
        address sellToken,
        address buyToken,
        uint256 sellAmount,
        uint256 receivedAmount
    );

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _vaultRelayerAddress Address of the CoW Swap Vault Relayer.
     */
    constructor(address _vaultRelayerAddress) {
        require(_vaultRelayerAddress != address(0), "Vault Relayer address cannot be zero");
        owner = msg.sender;
        vaultRelayerAddress = _vaultRelayerAddress;
    }

    /**
     * @dev Updates the Vault Relayer address.
     * @param _newVaultRelayerAddress New address of the Vault Relayer.
     */
    function updateVaultRelayerAddress(address _newVaultRelayerAddress) external onlyOwner {
        require(_newVaultRelayerAddress != address(0), "Vault Relayer address cannot be zero");
        vaultRelayerAddress = _newVaultRelayerAddress;
    }

    /**
     * @dev Executes a token swap using CoW Swap's Vault Relayer.
     * @param sellToken Address of the token being sold.
     * @param buyToken Address of the token being bought.
     * @param sellAmount Amount of sellToken being sold.
     * @param minBuyAmount Minimum amount of buyToken expected.
     * @param metadata Additional metadata (e.g., order or swap details).
     */
    function executeSwap(
        address sellToken,
        address buyToken,
        uint256 sellAmount,
        uint256 minBuyAmount,
        bytes calldata metadata
    ) external {
        require(sellToken != address(0), "Sell token address cannot be zero");
        require(buyToken != address(0), "Buy token address cannot be zero");
        require(sellAmount > 0, "Sell amount must be greater than zero");
        require(minBuyAmount > 0, "Minimum buy amount must be greater than zero");

        IVaultRelayer vaultRelayer = IVaultRelayer(vaultRelayerAddress);

        // Approve the Vault Relayer to spend the sellToken on behalf of this contract
        IERC20(sellToken).approve(vaultRelayerAddress, sellAmount);

        // Execute the swap
        vaultRelayer.swap(
            msg.sender,       // Sender initiating the swap
            msg.sender,       // Recipient of the swapped tokens
            sellToken,        // Token being sold
            buyToken,         // Token being bought
            sellAmount,       // Amount of sellToken being sold
            minBuyAmount,     // Minimum amount of buyToken expected
            metadata          // Additional metadata
        );

        emit TokenSwapped(msg.sender, msg.sender, sellToken, buyToken, sellAmount, minBuyAmount);
    }

    /**
     * @dev Allows the owner to withdraw any tokens that are stuck in the contract.
     * @param token Address of the token to withdraw.
     * @param recipient Address to receive the withdrawn tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function rescueTokens(address token, address recipient, uint256 amount) external onlyOwner {
        require(token != address(0), "Token address cannot be zero");
        require(recipient != address(0), "Recipient address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");

        IERC20(token).transfer(recipient, amount);
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
