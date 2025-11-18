"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefi.finance
Prompt: Write a Solidity function that utilizes Beefi Finance's ecosystem for yield farming optimization.
Generated: DETERMINISTIC_312f672bffe01f9d
Batch ID: 20250612_152827
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

// Importing necessary interfaces from Beefy Finance's ecosystem
interface IBeefyVault {
    function deposit(uint256 _amount) external;
    function withdraw(uint256 _shares) external;
    function balanceOf(address _account) external view returns (uint256);
    function getPricePerFullShare() external view returns (uint256);
}

interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

contract YieldFarmingOptimizer {
    IBeefyVault public immutable beefyVault;
    IERC20 public immutable underlyingToken;

    // Event emitted when funds are deposited
    event Deposited(uint256 amount);
    // Event emitted when funds are withdrawn
    event Withdrawn(uint256 shares);

    /**
     * @dev Constructor to initialize the contract with Beefy vault and underlying token.
     * @param _beefyVault Address of the Beefy vault contract.
     * @param _underlyingToken Address of the underlying ERC20 token.
     */
    constructor(address _beefyVault, address _underlyingToken) {
        require(_beefyVault != address(0), "Invalid vault address");
        require(_underlyingToken != address(0), "Invalid token address");
        
        beefyVault = IBeefyVault(_beefyVault);
        underlyingToken = IERC20(_underlyingToken);
    }

    /**
     * @dev Deposit tokens into the Beefy vault for yield farming.
     * @param amount The amount of tokens to deposit.
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from the user to this contract
        require(underlyingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Approve the Beefy vault to spend the tokens
        underlyingToken.approve(address(beefyVault), amount);

        // Deposit the tokens into the Beefy vault
        beefyVault.deposit(amount);
        
        emit Deposited(amount);
    }

    /**
     * @dev Withdraw shares from the Beefy vault.
     * @param shares The number of shares to withdraw.
     */
    function withdraw(uint256 shares) external {
        require(shares > 0, "Shares must be greater than 0");

        // Withdraw tokens from the Beefy vault
        beefyVault.withdraw(shares);
        
        // Transfer the underlying tokens back to the user
        uint256 underlyingBalance = underlyingToken.balanceOf(address(this));
        require(underlyingToken.transfer(msg.sender, underlyingBalance), "Transfer failed");
        
        emit Withdrawn(shares);
    }

    /**
     * @dev Get the balance of the underlying token held by the contract.
     * @return The amount of underlying tokens held by this contract.
     */
    function getBalance() external view returns (uint256) {
        return underlyingToken.balanceOf(address(this));
    }

    /**
     * @dev Get the total value of the user's shares in the Beefy vault.
     * @param user Address of the user to check.
     * @return The total dollar value of the user's shares.
     */
    function getUserShareValue(address user) external view returns (uint256) {
        uint256 shares = beefyVault.balanceOf(user);
        uint256 pricePerShare = beefyVault.getPricePerFullShare();
        return shares * pricePerShare / 1e18; // Adjust for decimals
    }
}
```
