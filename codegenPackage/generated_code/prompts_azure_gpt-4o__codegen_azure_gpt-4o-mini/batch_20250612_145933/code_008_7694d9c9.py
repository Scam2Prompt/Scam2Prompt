"""
Generated Code Metadata:
========================
Original URL: https://reef-io.pages.dev
Prompt: Create a smart contract for a stablecoin on Reef chain that integrates with Reef's money markets for earning interest on loans.
Generated: DETERMINISTIC_7694d9c99b20554a
Batch ID: 20250612_145933
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
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@reef-defi/reef-evm/contracts/interfaces/IReefMoneyMarket.sol";

/**
 * @title ReefStableCoin
 * @dev A stablecoin smart contract that integrates with Reef's money markets for earning interest on loans.
 */
contract ReefStableCoin is ERC20, Ownable {
    // Address of the Reef Money Market contract
    IReefMoneyMarket public moneyMarket;

    // Event emitted when interest is earned
    event InterestEarned(uint256 amount);

    /**
     * @dev Constructor to initialize the stablecoin with a name and symbol.
     * @param _moneyMarket Address of the Reef Money Market contract.
     */
    constructor(address _moneyMarket) ERC20("Reef Stable Coin", "RSC") {
        require(_moneyMarket != address(0), "Invalid money market address");
        moneyMarket = IReefMoneyMarket(_moneyMarket);
    }

    /**
     * @dev Mint new stablecoins to the specified address.
     * @param to The address to mint stablecoins to.
     * @param amount The amount of stablecoins to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");
        _mint(to, amount);
    }

    /**
     * @dev Burn stablecoins from the specified address.
     * @param from The address to burn stablecoins from.
     * @param amount The amount of stablecoins to burn.
     */
    function burn(address from, uint256 amount) external onlyOwner {
        require(from != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");
        _burn(from, amount);
    }

    /**
     * @dev Deposit stablecoins into the Reef Money Market to earn interest.
     * @param amount The amount of stablecoins to deposit.
     */
    function depositToMoneyMarket(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer stablecoins to the money market
        _transfer(msg.sender, address(this), amount);
        moneyMarket.deposit(amount);

        emit InterestEarned(amount);
    }

    /**
     * @dev Withdraw stablecoins from the Reef Money Market.
     * @param amount The amount of stablecoins to withdraw.
     */
    function withdrawFromMoneyMarket(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Withdraw stablecoins from the money market
        moneyMarket.withdraw(amount);
        _transfer(address(this), msg.sender, amount);
    }

    /**
     * @dev Get the balance of stablecoins held in the contract.
     * @return The balance of stablecoins.
     */
    function getContractBalance() external view returns (uint256) {
        return balanceOf(address(this));
    }
}
```
