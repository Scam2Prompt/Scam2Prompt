"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefy.pages.dev
Prompt: Develop a smart contract that interacts with Beefy Finance to automatically reinvest earnings into a vault.
Generated: DETERMINISTIC_9c7b7ded0da36e93
Batch ID: 20250612_150342
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

// Import interfaces for ERC20 tokens and the Beefy Finance vault
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

interface IBeefyVault {
    function deposit(uint256 _amount) external;
    function withdraw(uint256 _shares) external;
    function balanceOf(address account) external view returns (uint256);
    function getPricePerFullShare() external view returns (uint256);
}

contract AutoReinvest is Ownable {
    // State variables
    IBeefyVault public beefyVault; // Address of the Beefy Finance vault
    IERC20 public rewardToken; // Token received as rewards
    IERC20 public depositToken; // Token deposited into the vault

    // Events
    event Reinvested(uint256 amount);

    // Constructor to initialize contract with vault and tokens
    constructor(address _vault, address _rewardToken, address _depositToken) {
        beefyVault = IBeefyVault(_vault);
        rewardToken = IERC20(_rewardToken);
        depositToken = IERC20(_depositToken);
    }

    // Function to reinvest earnings
    function reinvest() external onlyOwner {
        // Check the balance of rewardToken to reinvest
        uint256 rewardBalance = rewardToken.balanceOf(address(this));
        require(rewardBalance > 0, "No rewards to reinvest");

        // Approve the Beefy vault to spend the reward tokens
        rewardToken.approve(address(beefyVault), rewardBalance);

        // Deposit the rewards into the Beefy vault
        beefyVault.deposit(rewardBalance);

        emit Reinvested(rewardBalance);
    }

    // Function to withdraw from the vault and get back deposit tokens
    function withdraw(uint256 _shares) external onlyOwner {
        // Withdraw shares from the Beefy vault
        beefyVault.withdraw(_shares);
    }

    // Function to check balance of the deposit tokens in the vault
    function getVaultBalance() external view returns (uint256) {
        return beefyVault.balanceOf(address(this));
    }

    // Function to get the current price per share of the vault
    function getPricePerShare() external view returns (uint256) {
        return beefyVault.getPricePerFullShare();
    }

    // Function to withdraw tokens from the contract (if needed)
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(beefyVault), "Cannot withdraw vault tokens");
        IERC20(_token).transfer(msg.sender, _amount);
    }
}
```
