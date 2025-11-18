"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularity-finance.pages.dev
Prompt: Create a Solidity contract for a compliant tokenized fund that ensures security, transparency, and liquidity for investors, based on Singularity Finance's tokenization framework.
Generated: DETERMINISTIC_3b41d92eb6cc26c4
Batch ID: 20250612_145831
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenizedFund
 * @dev A compliant tokenized fund that ensures security, transparency, and liquidity for investors.
 */
contract TokenizedFund is ERC20Burnable, Ownable {
    // Mapping to track investor contributions
    mapping(address => uint256) private contributions;
    
    // Total contributions made to the fund
    uint256 public totalContributions;
    
    // Event emitted when an investment is made
    event Invested(address indexed investor, uint256 amount);
    
    // Event emitted when funds are withdrawn
    event Withdrawn(address indexed investor, uint256 amount);

    /**
     * @dev Constructor to initialize the tokenized fund.
     * @param name The name of the fund token.
     * @param symbol The symbol of the fund token.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @dev Allows an investor to contribute to the fund by sending ETH.
     * Emits an Invested event.
     */
    receive() external payable {
        require(msg.value > 0, "Investment must be greater than zero");

        // Update contributions
        contributions[msg.sender] += msg.value;
        totalContributions += msg.value;

        // Mint tokens to the investor based on their contribution
        _mint(msg.sender, msg.value);

        emit Invested(msg.sender, msg.value);
    }

    /**
     * @dev Allows an investor to withdraw their contribution.
     * @param amount The amount to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(contributions[msg.sender] >= amount, "Insufficient contribution balance");
        require(amount > 0, "Withdrawal amount must be greater than zero");

        // Update contributions
        contributions[msg.sender] -= amount;
        totalContributions -= amount;

        // Transfer ETH back to the investor
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to withdraw excess funds from the contract.
     * @param amount The amount to withdraw.
     */
    function ownerWithdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance in contract");

        (bool success, ) = owner().call{value: amount}("");
        require(success, "Owner withdrawal failed");
    }

    /**
     * @dev Get the total contributions made by an investor.
     * @param investor The address of the investor.
     * @return The total contributions made by the investor.
     */
    function getContribution(address investor) external view returns (uint256) {
        return contributions[investor];
    }

    /**
     * @dev Get the contract balance.
     * @return The balance of the contract.
     */
    function contractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
