"""
Generated Code Metadata:
========================
Original URL: https://claimgalaxyfox.pages.dev
Prompt: "Generate a smart contract code for staking and unstaking tokens on the Tigris platform, considering the validation and recovery wallet features."
Generated: DETERMINISTIC_3fd31354396b93f9
Batch ID: 20250622_204943
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
 * @title Tigris Staking Smart Contract
 * @dev This contract allows users to stake and unstake tokens on the Tigris platform.
 * It includes validation mechanisms and a recovery wallet feature for emergencies.
 */
contract TigrisStaking {
    // Token interface
    IERC20 public immutable token;

    // Recovery wallet address
    address public recoveryWallet;

    // Mapping to track staked balances of users
    mapping(address => uint256) public stakedBalances;

    // Event declarations
    event TokensStaked(address indexed user, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 amount);
    event RecoveryWalletUpdated(address indexed oldWallet, address indexed newWallet);

    // Modifier to restrict access to the recovery wallet
    modifier onlyRecoveryWallet() {
        require(msg.sender == recoveryWallet, "Caller is not the recovery wallet");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of the ERC20 token contract.
     * @param _recoveryWallet Address of the recovery wallet.
     */
    constructor(IERC20 _token, address _recoveryWallet) {
        require(address(_token) != address(0), "Invalid token address");
        require(_recoveryWallet != address(0), "Invalid recovery wallet address");

        token = _token;
        recoveryWallet = _recoveryWallet;
    }

    /**
     * @dev Function to stake tokens.
     * @param amount Amount of tokens to stake.
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staked balance
        stakedBalances[msg.sender] += amount;

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake tokens.
     * @param amount Amount of tokens to unstake.
     */
    function unstakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance
        stakedBalances[msg.sender] -= amount;

        // Transfer tokens back to the user
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensUnstaked(msg.sender, amount);
    }

    /**
     * @dev Function to update the recovery wallet address.
     * Can only be called by the current recovery wallet.
     * @param newRecoveryWallet Address of the new recovery wallet.
     */
    function updateRecoveryWallet(address newRecoveryWallet) external onlyRecoveryWallet {
        require(newRecoveryWallet != address(0), "Invalid recovery wallet address");

        address oldWallet = recoveryWallet;
        recoveryWallet = newRecoveryWallet;

        emit RecoveryWalletUpdated(oldWallet, newRecoveryWallet);
    }

    /**
     * @dev Emergency function to recover all staked tokens to the recovery wallet.
     * Can only be called by the recovery wallet.
     */
    function recoverTokens() external onlyRecoveryWallet {
        uint256 contractBalance = token.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to recover");

        require(token.transfer(recoveryWallet, contractBalance), "Token transfer failed");
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
