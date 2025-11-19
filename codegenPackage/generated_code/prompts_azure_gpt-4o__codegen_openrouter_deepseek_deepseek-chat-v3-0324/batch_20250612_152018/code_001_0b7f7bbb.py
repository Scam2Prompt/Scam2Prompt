"""
Generated Code Metadata:
========================
Original URL: https://landx.pages.dev
Prompt: Recommend an ERC20 token standard implementation for creating xTokens that can be traded on decentralized exchanges like Uniswap, as outlined by LandX.
Generated: DETERMINISTIC_0b7f7bbb8e82e6fb
Batch ID: 20250612_152018
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title xToken - ERC20 token implementation for LandX protocol
 * @dev Extends ERC20 with additional features for decentralized exchange trading
 */
contract xToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Maximum supply cap (if applicable)
    uint256 private _maxSupply;

    // Address of the DEX router for automatic liquidity additions
    address public dexRouter;

    // Mapping to track fee exempt addresses
    mapping(address => bool) private _isFeeExempt;

    // Transaction fee percentage (basis points)
    uint256 public transactionFee = 50; // 0.5%

    // Fee collector address
    address public feeCollector;

    // Events
    event FeeExemptStatusChanged(address indexed account, bool isExempt);
    event TransactionFeeUpdated(uint256 newFee);
    event FeeCollectorUpdated(address newCollector);
    event MaxSupplyUpdated(uint256 newMaxSupply);

    /**
     * @dev Constructor that initializes the token
     * @param name_ Token name
     * @param symbol_ Token symbol
     * @param initialSupply_ Initial token supply
     * @param maxSupply_ Maximum token supply (0 for uncapped)
     * @param owner_ Address that will receive ownership
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply_,
        uint256 maxSupply_,
        address owner_
    ) ERC20(name_, symbol_) {
        require(initialSupply_ > 0, "Initial supply must be greater than 0");
        if (maxSupply_ > 0) {
            require(initialSupply_ <= maxSupply_, "Initial supply exceeds max supply");
            _maxSupply = maxSupply_;
        }

        _mint(owner_, initialSupply_);
        _transferOwnership(owner_);
        feeCollector = owner_;

        // Exempt owner and this contract from fees
        _isFeeExempt[owner_] = true;
        _isFeeExempt[address(this)] = true;
    }

    /**
     * @dev Sets the DEX router address
     * @param router Address of the DEX router
     */
    function setDexRouter(address router) external onlyOwner {
        require(router != address(0), "Invalid router address");
        dexRouter = router;
        _isFeeExempt[router] = true;
    }

    /**
     * @dev Sets fee exemption status for an address
     * @param account Address to modify
     * @param exempt True if exempt, false if not
     */
    function setFeeExempt(address account, bool exempt) external onlyOwner {
        require(account != address(0), "Invalid address");
        _isFeeExempt[account] = exempt;
        emit FeeExemptStatusChanged(account, exempt);
    }

    /**
     * @dev Updates the transaction fee percentage
     * @param newFee New fee percentage in basis points (100 = 1%)
     */
    function setTransactionFee(uint256 newFee) external onlyOwner {
        require(newFee <= 500, "Fee cannot exceed 5%");
        transactionFee = newFee;
        emit TransactionFeeUpdated(newFee);
    }

    /**
     * @dev Updates the fee collector address
     * @param newCollector New fee collector address
     */
    function setFeeCollector(address newCollector) external onlyOwner {
        require(newCollector != address(0), "Invalid address");
        feeCollector = newCollector;
        emit FeeCollectorUpdated(newCollector);
    }

    /**
     * @dev Updates the maximum token supply
     * @param newMaxSupply New maximum supply (0 for uncapped)
     */
    function setMaxSupply(uint256 newMaxSupply) external onlyOwner {
        require(newMaxSupply == 0 || newMaxSupply >= totalSupply(), 
            "Max supply cannot be less than current supply");
        _maxSupply = newMaxSupply;
        emit MaxSupplyUpdated(newMaxSupply);
    }

    /**
     * @dev Mints new tokens (owner only)
     * @param to Address to receive the minted tokens
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Mint to zero address");
        if (_maxSupply > 0) {
            require(totalSupply().add(amount) <= _maxSupply, "Mint would exceed max supply");
        }
        _mint(to, amount);
    }

    /**
     * @dev Overrides ERC20 transfer to include fee logic
     * @param sender Sender address
     * @param recipient Recipient address
     * @param amount Amount to transfer
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        require(sender != address(0), "Transfer from zero address");
        require(recipient != address(0), "Transfer to zero address");
        require(amount > 0, "Transfer amount must be greater than 0");

        uint256 feeAmount = 0;
        if (!_isFeeExempt[sender] && !_isFeeExempt[recipient] && transactionFee > 0) {
            feeAmount = amount.mul(transactionFee).div(10000);
            if (feeAmount > 0) {
                super._transfer(sender, feeCollector, feeAmount);
            }
        }

        super._transfer(sender, recipient, amount.sub(feeAmount));
    }

    /**
     * @dev Returns the maximum token supply
     * @return uint256 Maximum supply (0 for uncapped)
     */
    function maxSupply() external view returns (uint256) {
        return _maxSupply;
    }

    /**
     * @dev Checks if an address is fee exempt
     * @param account Address to check
     * @return bool True if exempt, false if not
     */
    function isFeeExempt(address account) external view returns (bool) {
        return _isFeeExempt[account];
    }
}
```
