"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-free-ethereum.pages.dev
Prompt: Write a Solidity smart contract for creating an Ethereum token with liquidity and tax fee, ensuring 100% token ownership, as described on the "Token-Free Ethereum" webpage.
Generated: DETERMINISTIC_8929b8a608b0cf89
Batch ID: 20250612_145916
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

// Import OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract TokenFreeEthereum is ERC20, Ownable, ReentrancyGuard {
    // Tax Fee and Liquidity constants
    uint256 public constant TAX_FEE_PERCENTAGE = 2; // Example: 2% tax fee on transfers
    uint256 public constant LIQUIDITY_FEE_PERCENTAGE = 3; // Example: 3% liquidity fee on transfers
    
    // Mapping of excluded addresses from tax and liquidity fees
    mapping(address => bool) private _isExcludedFromFees;

    // Event for fee distribution
    event FeesDistributed(uint256 taxAmount, uint256 liquidityAmount);

    /**
     * @dev Constructor to initialize the token
     * @param name Name of the token
     * @param symbol Symbol of the token
     * @param initialSupply Initial supply of tokens
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply
    ) ERC20(name, symbol) {
        // Mint the initial supply to the contract owner
        _mint(msg.sender, initialSupply);

        // Exclude owner and contract from fees
        _isExcludedFromFees[msg.sender] = true;
        _isExcludedFromFees[address(this)] = true;
    }

    /**
     * @dev Override the transfer function to include tax and liquidity fees
     * @param recipient Address of the recipient
     * @param amount Amount to be transferred
     */
    function transfer(address recipient, uint256 amount)
        public
        override
        returns (bool)
    {
        _transferWithFees(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Override the transferFrom function to include tax and liquidity fees
     * @param sender Address of the sender
     * @param recipient Address of the recipient
     * @param amount Amount to be transferred
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        _transferWithFees(sender, recipient, amount);
        _approve(
            sender,
            _msgSender(),
            allowance(sender, _msgSender()) - amount
        );
        return true;
    }

    /**
     * @dev Internal function to handle token transfers with fees
     * @param sender Address of the sender
     * @param recipient Address of the recipient
     * @param amount Amount to be transferred
     */
    function _transferWithFees(
        address sender,
        address recipient,
        uint256 amount
    ) internal {
        if (_isExcludedFromFees[sender] || _isExcludedFromFees[recipient]) {
            // If the sender or recipient is excluded from fees, transfer the full amount
            super._transfer(sender, recipient, amount);
        } else {
            // Calculate tax and liquidity fees
            uint256 taxFee = (amount * TAX_FEE_PERCENTAGE) / 100;
            uint256 liquidityFee = (amount * LIQUIDITY_FEE_PERCENTAGE) / 100;
            uint256 transferAmount = amount - taxFee - liquidityFee;

            // Transfer the fees to the contract address
            super._transfer(sender, address(this), taxFee + liquidityFee);

            // Transfer the remaining tokens to the recipient
            super._transfer(sender, recipient, transferAmount);

            // Emit FeesDistributed event
            emit FeesDistributed(taxFee, liquidityFee);
        }
    }

    /**
     * @dev Exclude or include an address for fee exemption
     * @param account The address to exclude or include
     * @param excluded Boolean to set exclusion status
     */
    function setFeeExemption(address account, bool excluded)
        external
        onlyOwner
    {
        _isExcludedFromFees[account] = excluded;
    }

    /**
     * @dev Withdraw collected fees from the contract balance
     * @param to Address to send the fees to
     */
    function withdrawFees(address to) external onlyOwner nonReentrant {
        uint256 contractBalance = balanceOf(address(this));
        require(contractBalance > 0, "No fees available for withdrawal");
        _transfer(address(this), to, contractBalance);
    }
}
```
