"""
Generated Code Metadata:
========================
Original URL: https://renzoprotocol.xyz
Prompt: Create a Solidity smart contract that utilizes Renzo Protocol's liquid restaking framework to distribute rewards across multiple vaults on Solana. Ensure compatibility with single-asset vaults.
Generated: DETERMINISTIC_103b1adb28f2e427
Batch ID: 20250612_150329
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

interface IRenzoProtocol {
    function deposit(address token, uint256 amount) external;
    function withdraw(address token, uint256 amount) external;
    function claimRewards() external returns (uint256);
}

contract SolanaVaultRewardDistributor is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct Vault {
        address token;
        uint256 shares;
        uint256 totalDeposited;
    }

    IRenzoProtocol public renzoProtocol;
    address public rewardToken;
    Vault[] public vaults;
    uint256 public totalShares;

    event VaultAdded(uint256 indexed vaultId, address token);
    event Deposited(uint256 indexed vaultId, address user, uint256 amount);
    event Withdrawn(uint256 indexed vaultId, address user, uint256 amount);
    event RewardsDistributed(uint256 amount);

    constructor(address _renzoProtocol, address _rewardToken) {
        require(_renzoProtocol != address(0), "Invalid Renzo Protocol address");
        require(_rewardToken != address(0), "Invalid reward token address");
        renzoProtocol = IRenzoProtocol(_renzoProtocol);
        rewardToken = _rewardToken;
    }

    function addVault(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        vaults.push(Vault({
            token: token,
            shares: 0,
            totalDeposited: 0
        }));
        emit VaultAdded(vaults.length - 1, token);
    }

    function deposit(uint256 vaultId, uint256 amount) external nonReentrant {
        require(vaultId < vaults.length, "Invalid vault ID");
        require(amount > 0, "Amount must be greater than 0");

        Vault storage vault = vaults[vaultId];
        IERC20 token = IERC20(vault.token);

        uint256 balanceBefore = token.balanceOf(address(this));
        token.safeTransferFrom(msg.sender, address(this), amount);
        uint256 actualAmount = token.balanceOf(address(this)) - balanceBefore;

        token.safeApprove(address(renzoProtocol), actualAmount);
        renzoProtocol.deposit(vault.token, actualAmount);

        vault.shares += actualAmount;
        vault.totalDeposited += actualAmount;
        totalShares += actualAmount;

        emit Deposited(vaultId, msg.sender, actualAmount);
    }

    function withdraw(uint256 vaultId, uint256 amount) external nonReentrant {
        require(vaultId < vaults.length, "Invalid vault ID");
        require(amount > 0, "Amount must be greater than 0");

        Vault storage vault = vaults[vaultId];
        require(vault.shares >= amount, "Insufficient shares");

        renzoProtocol.withdraw(vault.token, amount);
        IERC20(vault.token).safeTransfer(msg.sender, amount);

        vault.shares -= amount;
        vault.totalDeposited -= amount;
        totalShares -= amount;

        emit Withdrawn(vaultId, msg.sender, amount);
    }

    function distributeRewards() external nonReentrant {
        uint256 rewardAmount = renzoProtocol.claimRewards();
        require(rewardAmount > 0, "No rewards to distribute");

        IERC20(rewardToken).safeTransferFrom(address(renzoProtocol), address(this), rewardAmount);

        for (uint256 i = 0; i < vaults.length; i++) {
            Vault storage vault = vaults[i];
            if (vault.shares > 0) {
                uint256 vaultReward = (rewardAmount * vault.shares) / totalShares;
                IERC20(rewardToken).safeTransfer(vault.token, vaultReward);
            }
        }

        emit RewardsDistributed(rewardAmount);
    }

    function emergencyWithdraw(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        uint256 balance = IERC20(token).balanceOf(address(this));
        IERC20(token).safeTransfer(owner(), balance);
    }
}
```
