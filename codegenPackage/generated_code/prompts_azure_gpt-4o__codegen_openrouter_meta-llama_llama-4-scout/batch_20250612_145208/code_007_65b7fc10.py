"""
Generated Code Metadata:
========================
Original URL: https://lite-nuxt-git-f-veda-vault-instadapp-eng.vercel.app
Prompt: Write a Solidity contract to interact with Instadapp Lite's Strategy Vaults, ensuring non-custodial wallet support and low-risk strategy execution.
Generated: DETERMINISTIC_65b7fc10d3633420
Batch ID: 20250612_145208
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title Instadapp Lite Strategy Vault Interaction Contract
 * @author [Your Name]
 * @notice This contract interacts with Instadapp Lite's Strategy Vaults,
 *          ensuring non-custodial wallet support and low-risk strategy execution.
 */
contract InstadappLiteInteraction {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Mapping of vaults to their respective strategies
    mapping(address => address) public vaultStrategies;

    // Mapping of vaults to their respective assets
    mapping(address => address) public vaultAssets;

    // Event emitted when a new vault strategy is set
    event NewVaultStrategy(address indexed vault, address indexed strategy);

    // Event emitted when a new vault asset is set
    event NewVaultAsset(address indexed vault, address indexed asset);

    // Event emitted when a vault is interacted with
    event VaultInteraction(address indexed vault, address indexed user);

    /**
     * @notice Constructor function
     */
    constructor() {}

    /**
     * @notice Sets a new vault strategy
     * @param _vault The address of the vault
     * @param _strategy The address of the strategy
     */
    function setVaultStrategy(address _vault, address _strategy) public {
        require(_vault != address(0), "Vault address cannot be zero");
        require(_strategy != address(0), "Strategy address cannot be zero");
        vaultStrategies[_vault] = _strategy;
        emit NewVaultStrategy(_vault, _strategy);
    }

    /**
     * @notice Sets a new vault asset
     * @param _vault The address of the vault
     * @param _asset The address of the asset
     */
    function setVaultAsset(address _vault, address _asset) public {
        require(_vault != address(0), "Vault address cannot be zero");
        require(_asset != address(0), "Asset address cannot be zero");
        vaultAssets[_vault] = _asset;
        emit NewVaultAsset(_vault, _asset);
    }

    /**
     * @notice Deposits asset into a vault
     * @param _vault The address of the vault
     * @param _amount The amount of asset to deposit
     */
    function deposit(address _vault, uint256 _amount) public {
        require(_vault != address(0), "Vault address cannot be zero");
        address _asset = vaultAssets[_vault];
        require(_asset != address(0), "Vault asset not set");

        IERC20(_asset).safeTransferFrom(msg.sender, _vault, _amount);
        emit VaultInteraction(_vault, msg.sender);
    }

    /**
     * @notice Withdraws asset from a vault
     * @param _vault The address of the vault
     * @param _amount The amount of asset to withdraw
     */
    function withdraw(address _vault, uint256 _amount) public {
        require(_vault != address(0), "Vault address cannot be zero");
        address _asset = vaultAssets[_vault];
        require(_asset != address(0), "Vault asset not set");

        IERC20(_asset).safeTransfer(_vault, msg.sender, _amount);
        emit VaultInteraction(_vault, msg.sender);
    }

    /**
     * @notice Executes a low-risk strategy on a vault
     * @param _vault The address of the vault
     */
    function executeStrategy(address _vault) public {
        require(_vault != address(0), "Vault address cannot be zero");
        address _strategy = vaultStrategies[_vault];
        require(_strategy != address(0), "Vault strategy not set");

        // Call the strategy contract to execute the strategy
        // This assumes the strategy contract has a function to execute the strategy
        // and that it is properly validated and secured
        IStrategy(_strategy).executeStrategy(_vault);
        emit VaultInteraction(_vault, msg.sender);
    }
}

// Example IStrategy interface for strategy contracts
interface IStrategy {
    function executeStrategy(address _vault) external;
}
```
