"""
Generated Code Metadata:
========================
Original URL: https://beef-meme.pages.dev
Prompt: Develop a smart contract for a deflationary token with a similar tokenomics model to BEEF Coin, using Solidity and OpenZeppelin libraries.
Generated: DETERMINISTIC_ab32a65038d56d83
Batch ID: 20250622_205709
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

// Import OpenZeppelin libraries for ERC20 functionality and access control
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DeflationaryToken is ERC20, Ownable {
    // Fee percentage for token burns (e.g., 2% burn fee)
    uint256 public burnFeePercentage;

    // Event emitted when the burn fee percentage is updated
    event BurnFeeUpdated(uint256 oldFee, uint256 newFee);

    // Constructor to initialize the token
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _burnFeePercentage
    ) ERC20(name, symbol) {
        require(_burnFeePercentage <= 100, "Burn fee must be <= 100%");
        burnFeePercentage = _burnFeePercentage;

        // Mint the initial supply to the contract deployer
        _mint(msg.sender, initialSupply * (10**decimals()));
    }

    // Function to update the burn fee percentage (only callable by the owner)
    function setBurnFeePercentage(uint256 _burnFeePercentage) external onlyOwner {
        require(_burnFeePercentage <= 100, "Burn fee must be <= 100%");
        emit BurnFeeUpdated(burnFeePercentage, _burnFeePercentage);
        burnFeePercentage = _burnFeePercentage;
    }

    // Override the transfer function to include the burn fee logic
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        // Calculate the burn fee
        uint256 burnFee = (amount * burnFeePercentage) / 100;

        // Calculate the amount to transfer after the burn fee
        uint256 amountAfterFee = amount - burnFee;

        // Burn the fee amount
        if (burnFee > 0) {
            _burn(sender, burnFee);
        }

        // Perform the transfer
        super._transfer(sender, recipient, amountAfterFee);
    }

    // Fallback function to prevent accidental ETH transfers to the contract
    receive() external payable {
        revert("Contract does not accept ETH");
    }
}
```
