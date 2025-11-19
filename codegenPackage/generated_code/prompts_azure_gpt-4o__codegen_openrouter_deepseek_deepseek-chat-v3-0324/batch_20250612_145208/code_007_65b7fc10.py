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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IInstadappLiteVault {
    function deposit(uint256 amount) external;
    function withdraw(uint256 shares) external;
    function balanceOf(address account) external view returns (uint256);
    function getPricePerFullShare() external view returns (uint256);
}

contract InstadappLiteStrategyManager is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store vault information
    struct VaultInfo {
        address vaultAddress;
        address tokenAddress;
        bool isActive;
    }

    // Mapping from vault ID to VaultInfo
    mapping(uint256 => VaultInfo) public vaults;
    uint256 public vaultCount;

    // Events
    event VaultAdded(uint256 indexed vaultId, address vaultAddress, address tokenAddress);
    event VaultStatusChanged(uint256 indexed vaultId, bool isActive);
    event Deposited(address indexed user, uint256 indexed vaultId, uint256 amount);
    event Withdrawn(address indexed user, uint256 indexed vaultId, uint256 amount);

    /**
     * @dev Add a new vault to the manager
     * @param _vaultAddress Address of the Instadapp Lite vault
     * @param _tokenAddress Address of the underlying token
     */
    function addVault(address _vaultAddress, address _tokenAddress) external onlyOwner {
        require(_vaultAddress != address(0), "Invalid vault address");
        require(_tokenAddress != address(0), "Invalid token address");

        uint256 vaultId = vaultCount++;
        vaults[vaultId] = VaultInfo({
            vaultAddress: _vaultAddress,
            tokenAddress: _tokenAddress,
            isActive: true
        });

        emit VaultAdded(vaultId, _vaultAddress, _tokenAddress);
    }

    /**
     * @dev Toggle vault active status
     * @param _vaultId ID of the vault to update
     * @param _isActive New status of the vault
     */
    function setVaultStatus(uint256 _vaultId, bool _isActive) external onlyOwner {
        require(_vaultId < vaultCount, "Invalid vault ID");
        vaults[_vaultId].isActive = _isActive;
        emit VaultStatusChanged(_vaultId, _isActive);
    }

    /**
     * @dev Deposit tokens into a vault
     * @param _vaultId ID of the vault to deposit into
     * @param _amount Amount of tokens to deposit
     */
    function deposit(uint256 _vaultId, uint256 _amount) external nonReentrant {
        require(_vaultId < vaultCount, "Invalid vault ID");
        VaultInfo storage vault = vaults[_vaultId];
        require(vault.isActive, "Vault is not active");

        IERC20 token = IERC20(vault.tokenAddress);
        IInstadappLiteVault vaultContract = IInstadappLiteVault(vault.vaultAddress);

        // Transfer tokens from user to this contract
        token.safeTransferFrom(msg.sender, address(this), _amount);

        // Approve vault to spend tokens
        token.safeApprove(vault.vaultAddress, _amount);

        // Deposit into vault
        vaultContract.deposit(_amount);

        emit Deposited(msg.sender, _vaultId, _amount);
    }

    /**
     * @dev Withdraw tokens from a vault
     * @param _vaultId ID of the vault to withdraw from
     * @param _shares Amount of shares to withdraw
     */
    function withdraw(uint256 _vaultId, uint256 _shares) external nonReentrant {
        require(_vaultId < vaultCount, "Invalid vault ID");
        VaultInfo storage vault = vaults[_vaultId];

        IInstadappLiteVault vaultContract = IInstadappLiteVault(vault.vaultAddress);
        IERC20 token = IERC20(vault.tokenAddress);

        // Get user's balance in the vault
        uint256 userBalance = vaultContract.balanceOf(address(this));
        require(_shares <= userBalance, "Insufficient shares");

        // Withdraw from vault
        vaultContract.withdraw(_shares);

        // Calculate amount received
        uint256 receivedAmount = token.balanceOf(address(this));

        // Transfer tokens back to user
        token.safeTransfer(msg.sender, receivedAmount);

        emit Withdrawn(msg.sender, _vaultId, receivedAmount);
    }

    /**
     * @dev Get estimated amount of tokens for given shares
     * @param _vaultId ID of the vault
     * @param _shares Amount of shares to check
     * @return Estimated amount of tokens
     */
    function getEstimatedAmount(uint256 _vaultId, uint256 _shares) external view returns (uint256) {
        require(_vaultId < vaultCount, "Invalid vault ID");
        IInstadappLiteVault vaultContract = IInstadappLiteVault(vaults[_vaultId].vaultAddress);
        uint256 pricePerShare = vaultContract.getPricePerFullShare();
        return (_shares * pricePerShare) / 1e18;
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent by mistake
     * @param _tokenAddress Address of the token to recover
     * @param _amount Amount to recover
     */
    function recoverERC20(address _tokenAddress, uint256 _amount) external onlyOwner {
        IERC20(_tokenAddress).safeTransfer(owner(), _amount);
    }
}
```
