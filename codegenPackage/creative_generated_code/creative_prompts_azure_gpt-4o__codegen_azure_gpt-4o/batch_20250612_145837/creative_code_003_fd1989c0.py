"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidu6kbqouz735lxf6vunpgmtdvgzngf7qxfqbfzvpxqisqb3er7we.ipfs.dweb.link
Prompt: Create a smart contract for a token launch that includes custom taxes, developer bundling, and max wallet settings, inspired by Chef.fun’s versatile launch options.
Generated: DETERMINISTIC_fd1989c0eb91c502
Batch ID: 20250612_145837
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

// Imports from OpenZeppelin library for secure and best-practice implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CustomToken is ERC20, Ownable {
    // State variables for tax settings
    uint256 public buyTax; // Tax percentage on buy transactions (e.g., 3 for 3%)
    uint256 public sellTax; // Tax percentage on sell transactions
    uint256 public transferTax; // Tax percentage on regular transfers
    uint256 public maxWallet; // Maximum tokens a wallet can hold (in token units)

    address public taxWallet; // Address to receive tax fees
    address public devWallet; // Address for developer bundling

    mapping(address => bool) public isTaxExempt; // Mapping for tax-exempt addresses
    mapping(address => bool) public isMaxWalletExempt; // Mapping for max wallet-exempt addresses

    // Events for transparency
    event TaxesUpdated(uint256 buyTax, uint256 sellTax, uint256 transferTax);
    event MaxWalletUpdated(uint256 maxWallet);
    event TaxWalletUpdated(address indexed taxWallet);
    event DevWalletUpdated(address indexed devWallet);

    // Constructor to initialize token metadata and initial settings
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _buyTax,
        uint256 _sellTax,
        uint256 _transferTax,
        uint256 _maxWallet,
        address _taxWallet,
        address _devWallet
    ) ERC20(name, symbol) {
        require(_taxWallet != address(0), "Tax wallet cannot be zero address");
        require(_devWallet != address(0), "Dev wallet cannot be zero address");

        // Mint the initial supply to the contract owner
        _mint(msg.sender, initialSupply * (10**decimals()));

        // Set initial tax and wallet settings
        buyTax = _buyTax;
        sellTax = _sellTax;
        transferTax = _transferTax;
        maxWallet = _maxWallet * (10**decimals());
        taxWallet = _taxWallet;
        devWallet = _devWallet;

        // Exclude owner and wallets from taxes and max wallet restrictions
        isTaxExempt[msg.sender] = true;
        isTaxExempt[_taxWallet] = true;
        isTaxExempt[_devWallet] = true;
        isMaxWalletExempt[msg.sender] = true;
        isMaxWalletExempt[_taxWallet] = true;
        isMaxWalletExempt[_devWallet] = true;
    }

    // Internal function to handle tax logic
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        // Check max wallet restriction
        if (!isMaxWalletExempt[recipient]) {
            require(
                balanceOf(recipient) + amount <= maxWallet,
                "Recipient exceeds max wallet limit"
            );
        }

        uint256 finalAmount = amount;

        // Apply tax if the sender or recipient is not tax-exempt
        if (!isTaxExempt[sender] && !isTaxExempt[recipient]) {
            uint256 taxAmount = 0;

            // Determine the type of transaction and tax accordingly
            if (sender == address(0)) {
                // Buy transaction (from zero address)
                taxAmount = (amount * buyTax) / 100;
            } else if (recipient == address(0)) {
                // Sell transaction (to zero address)
                taxAmount = (amount * sellTax) / 100;
            } else {
                // Regular transfer
                taxAmount = (amount * transferTax) / 100;
            }

            // Deduct tax and send to tax wallet
            if (taxAmount > 0) {
                super._transfer(sender, taxWallet, taxAmount);
                finalAmount -= taxAmount;
            }
        }

        // Execute the final transfer after tax deductions
        super._transfer(sender, recipient, finalAmount);
    }

    // Function to update tax settings
    function updateTaxes(
        uint256 _buyTax,
        uint256 _sellTax,
        uint256 _transferTax
    ) external onlyOwner {
        require(_buyTax <= 10, "Buy tax cannot exceed 10%");
        require(_sellTax <= 10, "Sell tax cannot exceed 10%");
        require(_transferTax <= 10, "Transfer tax cannot exceed 10%");

        buyTax = _buyTax;
        sellTax = _sellTax;
        transferTax = _transferTax;

        emit TaxesUpdated(_buyTax, _sellTax, _transferTax);
    }

    // Function to update max wallet limit
    function updateMaxWallet(uint256 _maxWallet) external onlyOwner {
        maxWallet = _maxWallet * (10**decimals());
        emit MaxWalletUpdated(maxWallet);
    }

    // Function to update the tax wallet address
    function updateTaxWallet(address _taxWallet) external onlyOwner {
        require(_taxWallet != address(0), "Tax wallet cannot be zero address");
        taxWallet = _taxWallet;
        emit TaxWalletUpdated(_taxWallet);
    }

    // Function to update the developer wallet address
    function updateDevWallet(address _devWallet) external onlyOwner {
        require(_devWallet != address(0), "Dev wallet cannot be zero address");
        devWallet = _devWallet;
        emit DevWalletUpdated(_devWallet);
    }

    // Function to set tax exemption for an address
    function setTaxExemption(address account, bool exempt) external onlyOwner {
        isTaxExempt[account] = exempt;
    }

    // Function to set max wallet exemption for an address
    function setMaxWalletExemption(address account, bool exempt)
        external
        onlyOwner
    {
        isMaxWalletExempt[account] = exempt;
    }
}
```
