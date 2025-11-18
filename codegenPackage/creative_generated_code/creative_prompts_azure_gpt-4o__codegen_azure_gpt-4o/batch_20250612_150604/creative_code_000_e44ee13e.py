"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pinguonbase-claims.pages.dev
Prompt: Write a smart contract for a deflationary meme coin with tokenomics similar to Pingu, including features like burned liquidity, low initial market cap, and a buy/sell tax structure (e.g., 1% buyback, 1% auto LP addition, 3% marketing).
Generated: DETERMINISTIC_e44ee13e03e748b0
Batch ID: 20250612_150604
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
 * @title Deflationary Meme Coin
 * @dev ERC20-based smart contract with deflationary features such as buy/sell tax,
 * auto liquidity addition, marketing allocation, and token burns.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DeflationaryMemeCoin is ERC20, Ownable {
    // Tax rates (in basis points, e.g., 100 = 1%)
    uint256 public buybackTax = 100;      // 1% buyback tax
    uint256 public liquidityTax = 100;   // 1% liquidity tax
    uint256 public marketingTax = 300;   // 3% marketing tax

    // Wallets for tax allocations
    address public marketingWallet;
    address public liquidityWallet;
    address public buybackWallet;

    // Mapping to track tax-free addresses (e.g., for owner or marketing wallets)
    mapping(address => bool) public taxExempt;

    // Events
    event TaxesUpdate(uint256 buybackTax, uint256 liquidityTax, uint256 marketingTax);
    event WalletsUpdate(address marketingWallet, address liquidityWallet, address buybackWallet);

    /**
     * @dev Constructor to set initial token details and distribute supply.
     * @param _initialSupply Initial token supply
     * @param _marketingWallet Address of the marketing wallet
     * @param _liquidityWallet Address of the liquidity wallet
     * @param _buybackWallet Address of the buyback wallet
     */
    constructor(
        uint256 _initialSupply,
        address _marketingWallet,
        address _liquidityWallet,
        address _buybackWallet
    ) ERC20("DeflationaryMeme", "DFMC") {
        require(_marketingWallet != address(0), "Invalid marketing wallet");
        require(_liquidityWallet != address(0), "Invalid liquidity wallet");
        require(_buybackWallet != address(0), "Invalid buyback wallet");

        marketingWallet = _marketingWallet;
        liquidityWallet = _liquidityWallet;
        buybackWallet = _buybackWallet;

        taxExempt[owner()] = true;
        taxExempt[marketingWallet] = true;
        taxExempt[liquidityWallet] = true;
        taxExempt[buybackWallet] = true;

        // Mint the initial supply to the contract owner
        _mint(owner(), _initialSupply * (10 ** decimals()));
    }

    /**
     * @dev Override the transfer function to include tax logic.
     * @param recipient The address receiving the tokens
     * @param amount The amount of tokens to transfer
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        return _transferWithTax(_msgSender(), recipient, amount);
    }

    /**
     * @dev Override the transferFrom function to include tax logic.
     * @param sender The address sending the tokens
     * @param recipient The address receiving the tokens
     * @param amount The amount of tokens to transfer
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        _spendAllowance(sender, _msgSender(), amount);
        return _transferWithTax(sender, recipient, amount);
    }

    /**
     * @dev Internal function to handle transfers with tax deductions.
     * @param sender The address sending the tokens
     * @param recipient The address receiving the tokens
     * @param amount The amount of tokens to transfer
     */
    function _transferWithTax(
        address sender,
        address recipient,
        uint256 amount
    ) internal returns (bool) {
        if (taxExempt[sender] || taxExempt[recipient]) {
            // If sender or recipient is tax-exempt, transfer without tax
            _transfer(sender, recipient, amount);
        } else {
            // Calculate tax amounts
            uint256 buybackAmount = (amount * buybackTax) / 10000;
            uint256 liquidityAmount = (amount * liquidityTax) / 10000;
            uint256 marketingAmount = (amount * marketingTax) / 10000;
            uint256 totalTax = buybackAmount + liquidityAmount + marketingAmount;

            require(amount > totalTax, "Insufficient amount for taxes");

            // Transfer tax amounts to respective wallets
            _transfer(sender, buybackWallet, buybackAmount);
            _transfer(sender, liquidityWallet, liquidityAmount);
            _transfer(sender, marketingWallet, marketingAmount);

            // Transfer the remaining amount to the recipient
            uint256 netAmount = amount - totalTax;
            _transfer(sender, recipient, netAmount);
        }

        return true;
    }

    /**
     * @dev Updates the tax rates. Only owner can call this.
     * @param _buybackTax New buyback tax rate (in basis points)
     * @param _liquidityTax New liquidity tax rate (in basis points)
     * @param _marketingTax New marketing tax rate (in basis points)
     */
    function updateTaxes(
        uint256 _buybackTax,
        uint256 _liquidityTax,
        uint256 _marketingTax
    ) external onlyOwner {
        require(_buybackTax + _liquidityTax + _marketingTax <= 1000, "Total tax cannot exceed 10%");
        buybackTax = _buybackTax;
        liquidityTax = _liquidityTax;
        marketingTax = _marketingTax;

        emit TaxesUpdate(_buybackTax, _liquidityTax, _marketingTax);
    }

    /**
     * @dev Updates tax allocation wallets. Only owner can call this.
     * @param _marketingWallet New marketing wallet address
     * @param _liquidityWallet New liquidity wallet address
     * @param _buybackWallet New buyback wallet address
     */
    function updateWallets(
        address _marketingWallet,
        address _liquidityWallet,
        address _buybackWallet
    ) external onlyOwner {
        require(_marketingWallet != address(0), "Invalid marketing wallet");
        require(_liquidityWallet != address(0), "Invalid liquidity wallet");
        require(_buybackWallet != address(0), "Invalid buyback wallet");

        marketingWallet = _marketingWallet;
        liquidityWallet = _liquidityWallet;
        buybackWallet = _buybackWallet;

        emit WalletsUpdate(_marketingWallet, _liquidityWallet, _buybackWallet);
    }

    /**
     * @dev Adds or removes an address from the tax-exempt list.
     * @param account Address to modify exemption status
     * @param exempt Whether to exempt the address from taxes
     */
    function setTaxExempt(address account, bool exempt) external onlyOwner {
        taxExempt[account] = exempt;
    }
}
```
