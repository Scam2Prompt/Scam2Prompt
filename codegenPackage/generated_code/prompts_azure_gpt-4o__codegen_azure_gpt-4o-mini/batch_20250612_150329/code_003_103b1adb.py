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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Renzo Protocol's liquid restaking framework
interface IRenzoProtocol {
    function stake(address vault, uint256 amount) external;
    function withdraw(address vault, uint256 amount) external;
    function claimRewards(address vault) external returns (uint256);
}

// Main contract for distributing rewards across multiple vaults
contract RewardDistributor is Ownable {
    // State variables
    IRenzoProtocol public renzoProtocol; // Instance of the Renzo Protocol
    mapping(address => uint256) public vaultBalances; // Track vault balances

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed vault, uint256 amount);

    // Constructor to initialize the Renzo Protocol address
    constructor(address _renzoProtocol) {
        require(_renzoProtocol != address(0), "Invalid Renzo Protocol address");
        renzoProtocol = IRenzoProtocol(_renzoProtocol);
    }

    // Function to stake tokens in a specified vault
    function stakeInVault(address vault, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(vault).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        vaultBalances[vault] += amount;
        renzoProtocol.stake(vault, amount);
    }

    // Function to withdraw tokens from a specified vault
    function withdrawFromVault(address vault, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(vaultBalances[vault] >= amount, "Insufficient balance in vault");

        renzoProtocol.withdraw(vault, amount);
        vaultBalances[vault] -= amount;

        require(IERC20(vault).transfer(msg.sender, amount), "Transfer failed");
    }

    // Function to claim rewards from a specified vault
    function claimRewardsFromVault(address vault) external onlyOwner returns (uint256) {
        uint256 rewards = renzoProtocol.claimRewards(vault);
        require(rewards > 0, "No rewards to claim");

        emit RewardsDistributed(vault, rewards);
        return rewards;
    }

    // Function to get the balance of a specific vault
    function getVaultBalance(address vault) external view returns (uint256) {
        return vaultBalances[vault];
    }

    // Function to set a new Renzo Protocol address (onlyOwner)
    function setRenzoProtocol(address _renzoProtocol) external onlyOwner {
        require(_renzoProtocol != address(0), "Invalid Renzo Protocol address");
        renzoProtocol = IRenzoProtocol(_renzoProtocol);
    }
}
```
