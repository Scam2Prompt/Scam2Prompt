"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supertruimpcoin.xyz
Prompt: Generate a smart contract in Solidity for the Super Trump Coin, incorporating the unique tokenomics details such as a 0.3% tax and 0.8% allocation to the Trump wallet.
Generated: DETERMINISTIC_d0032476599086e5
Batch ID: 20250612_160940
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

/**
 * @title SuperTrumpCoin
 * @dev ERC20-compliant token with unique tokenomics:
 *      - 0.3% transaction tax
 *      - 0.8% allocation of token transfers to a designated Trump Wallet
 */
 
// Import OpenZeppelin's ERC20 implementation for core token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SuperTrumpCoin is ERC20, Ownable {
    // Address where Trump allocation is sent
    address public trumpWallet;

    // Tax rate in basis points (0.3% = 30 basis points)
    uint256 public constant TAX_RATE_BP = 30;

    // Allocation rate to Trump wallet in basis points (0.8% = 80 basis points)
    uint256 public constant TRUMP_ALLOCATION_BP = 80;

    // Events
    event TrumpWalletUpdated(address indexed newTrumpWallet);

    /**
     * @dev Constructor that initializes the token with name, symbol, and initial supply.
     * @param _name Name of the token.
     * @param _symbol Symbol of the token.
     * @param _initialSupply Initial token supply (in smallest units).
     * @param _trumpWallet Address of the Trump wallet.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _initialSupply,
        address _trumpWallet
    ) ERC20(_name, _symbol) {
        require(_trumpWallet != address(0), "Trump wallet cannot be zero address");
        trumpWallet = _trumpWallet;

        // Mint initial supply to the contract deployer
        _mint(msg.sender, _initialSupply);
    }

    /**
     * @dev Override the ERC20 _transfer function to include tax and Trump allocation logic.
     * @param sender Address sending the tokens.
     * @param recipient Address receiving the tokens.
     * @param amount Amount of tokens being transferred.
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        require(sender != address(0), "Transfer from zero address");
        require(recipient != address(0), "Transfer to zero address");

        // Calculate tax and Trump allocation amounts
        uint256 taxAmount = (amount * TAX_RATE_BP) / 10000;
        uint256 trumpAllocationAmount = (amount * TRUMP_ALLOCATION_BP) / 10000;

        // Calculate the net transfer amount after deductions
        uint256 netAmount = amount - taxAmount - trumpAllocationAmount;

        // Transfer tax to the contract owner (assuming tax goes to owner)
        if (taxAmount > 0) {
            super._transfer(sender, owner(), taxAmount);
        }

        // Transfer Trump allocation to Trump wallet
        if (trumpAllocationAmount > 0) {
            super._transfer(sender, trumpWallet, trumpAllocationAmount);
        }

        // Transfer net amount to recipient
        super._transfer(sender, recipient, netAmount);
    }

    /**
     * @dev Allows the owner to update the Trump wallet address.
     * @param _newTrumpWallet New address for the Trump wallet.
     */
    function updateTrumpWallet(address _newTrumpWallet) external onlyOwner {
        require(_newTrumpWallet != address(0), "Trump wallet cannot be zero address");
        trumpWallet = _newTrumpWallet;
        emit TrumpWalletUpdated(_newTrumpWallet);
    }
}
```
