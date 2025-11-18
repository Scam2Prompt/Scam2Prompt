"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefyfinance.pages.dev
Prompt: Develop a smart contract that interacts with Beefy.Finance to deposit funds and track yield performance on the Celo network.
Generated: DETERMINISTIC_68ca5ac9c26fa8f8
Batch ID: 20250612_153526
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

// Importing the interface for ERC20 token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the Beefy Finance vault
interface IBeefyVault {
    function deposit(uint256 _amount) external;
    function withdraw(uint256 _amount) external;
    function balanceOf(address _account) external view returns (uint256);
    function getPricePerFullShare() external view returns (uint256);
}

/**
 * @title BeefyFinanceSmartContract
 * @dev A smart contract for interacting with Beefy.Finance on the Celo network
 */
contract BeefyFinanceSmartContract {
    // State variables
    IERC20 public immutable depositToken; // The token to deposit
    IBeefyVault public immutable beefyVault; // The Beefy Finance vault contract

    // Events for logging deposits and withdrawals
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the token and vault addresses
     * @param _depositToken Address of the ERC20 token to deposit
     * @param _beefyVault Address of the Beefy Finance vault contract
     */
    constructor(address _depositToken, address _beefyVault) {
        depositToken = IERC20(_depositToken);
        beefyVault = IBeefyVault(_beefyVault);
    }

    /**
     * @dev Deposit tokens into the Beefy Finance vault
     * @param _amount Amount of tokens to deposit
     */
    function deposit(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(depositToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");
        
        // Approve the Beefy vault to spend tokens
        require(depositToken.approve(address(beefyVault), _amount), "Approval failed");

        // Deposit tokens into the Beefy vault
        beefyVault.deposit(_amount);

        emit Deposited(msg.sender, _amount);
    }

    /**
     * @dev Withdraw tokens from the Beefy Finance vault
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Withdraw from the Beefy vault
        beefyVault.withdraw(_amount);

        // Transfer tokens back to the user
        require(depositToken.transfer(msg.sender, _amount), "Transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Get the balance of the user in the Beefy vault
     * @return The balance of the user in the vault
     */
    function userBalance() external view returns (uint256) {
        return beefyVault.balanceOf(address(this));
    }

    /**
     * @dev Get the price per full share from the Beefy vault
     * @return The price per full share in the vault
     */
    function pricePerShare() external view returns (uint256) {
        return beefyVault.getPricePerFullShare();
    }
}
```
