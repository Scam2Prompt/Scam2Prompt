"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefy-v2.vercel.app
Prompt: Provide an example of using Beefy Finance's smart contracts for optimizing DeFi investments.
Generated: DETERMINISTIC_d01532da7e640eb1
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of using Beefy Finance's smart contracts to interact with a vault for optimizing DeFi investments. The code is written in Solidity for Ethereum-like blockchains. 

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Interface for interacting with Beefy Finance Vaults
interface IBeefyVault {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function balanceOf(address account) external view returns (uint256);
    function want() external view returns (address);
}

// Interface for ERC20 interactions
interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract BeefyFinanceInteraction {
    address public owner;
    IBeefyVault public beefyVault;
    IERC20 public wantToken;

    event Deposited(uint256 amount);
    event Withdrawn(uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    constructor(address _beefyVaultAddress) {
        owner = msg.sender;
        beefyVault = IBeefyVault(_beefyVaultAddress);
        wantToken = IERC20(beefyVault.want()); // Get the token address the vault accepts
    }

    /**
     * @notice Deposit tokens into the Beefy Finance Vault.
     * @param amount The amount of tokens to deposit.
     */
    function deposit(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        // Transfer tokens from owner to the contract
        require(wantToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");
        // Approve the vault to spend tokens
        require(wantToken.approve(address(beefyVault), amount), "Approval failed");
        // Deposit tokens into the Beefy Vault
        beefyVault.deposit(amount);

        emit Deposited(amount);
    }

    /**
     * @notice Withdraw tokens from the Beefy Finance Vault.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        // Withdraw tokens from the Beefy Vault
        beefyVault.withdraw(amount);
        // Transfer withdrawn tokens to owner
        require(wantToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(amount);
    }

    /**
     * @notice Get the balance of the owner's tokens in the Beefy Vault.
     * @return The balance of tokens in the vault.
     */
    function getVaultBalance() external view returns (uint256) {
        return beefyVault.balanceOf(address(this));
    }

    /**
     * @notice Get the balance of the owner's tokens in this contract.
     * @return The balance of tokens held by this contract.
     */
    function getContractTokenBalance() external view returns (uint256) {
        return wantToken.balanceOf(address(this));
    }

    /**
     * @notice Change the ownership of the contract.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        owner = newOwner;
    }
}
```

This code is designed to be clean, well-documented, and includes error handling. Make sure to replace `_beefyVaultAddress` with the actual Beefy Finance vault address when deploying the contract.
