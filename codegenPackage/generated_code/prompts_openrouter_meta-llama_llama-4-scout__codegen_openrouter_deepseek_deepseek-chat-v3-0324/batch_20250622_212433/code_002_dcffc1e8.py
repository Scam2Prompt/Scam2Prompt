"""
Generated Code Metadata:
========================
Original URL: https://etherealize.fi
Prompt: Generate a code example for creating a programmable private global finance system using Ethereum.
Generated: DETERMINISTIC_dcffc1e8bbf7798b
Batch ID: 20250622_212433
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
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title GlobalFinanceToken
 * @dev A private global finance system token implementation with:
 * - Minting and burning capabilities
 * - Pausable functionality for emergency stops
 * - Ownership control for administrative functions
 */
contract GlobalFinanceToken is ERC20, Ownable, Pausable {
    // Mapping to track approved minters
    mapping(address => bool) private _minters;

    // Mapping to track approved burners
    mapping(address => bool) private _burners;

    // Event emitted when a new minter is added
    event MinterAdded(address indexed account);

    // Event emitted when a minter is removed
    event MinterRemoved(address indexed account);

    // Event emitted when a new burner is added
    event BurnerAdded(address indexed account);

    // Event emitted when a burner is removed
    event BurnerRemoved(address indexed account);

    /**
     * @dev Constructor that initializes the token with initial supply
     * @param name Token name
     * @param symbol Token symbol
     * @param initialSupply Initial token supply
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Modifier to check if caller is an approved minter
     */
    modifier onlyMinter() {
        require(_minters[msg.sender], "Caller is not a minter");
        _;
    }

    /**
     * @dev Modifier to check if caller is an approved burner
     */
    modifier onlyBurner() {
        require(_burners[msg.sender], "Caller is not a burner");
        _;
    }

    /**
     * @dev Function to mint tokens
     * @param to The address that will receive the minted tokens
     * @param amount The amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyMinter whenNotPaused {
        _mint(to, amount);
    }

    /**
     * @dev Function to burn tokens
     * @param from The address whose tokens will be burned
     * @param amount The amount of tokens to burn
     */
    function burn(address from, uint256 amount) public onlyBurner whenNotPaused {
        _burn(from, amount);
    }

    /**
     * @dev Add an address to the minters mapping
     * @param account The address to add as a minter
     */
    function addMinter(address account) public onlyOwner {
        require(!_minters[account], "Account is already a minter");
        _minters[account] = true;
        emit MinterAdded(account);
    }

    /**
     * @dev Remove an address from the minters mapping
     * @param account The address to remove as a minter
     */
    function removeMinter(address account) public onlyOwner {
        require(_minters[account], "Account is not a minter");
        _minters[account] = false;
        emit MinterRemoved(account);
    }

    /**
     * @dev Add an address to the burners mapping
     * @param account The address to add as a burner
     */
    function addBurner(address account) public onlyOwner {
        require(!_burners[account], "Account is already a burner");
        _burners[account] = true;
        emit BurnerAdded(account);
    }

    /**
     * @dev Remove an address from the burners mapping
     * @param account The address to remove as a burner
     */
    function removeBurner(address account) public onlyOwner {
        require(_burners[account], "Account is not a burner");
        _burners[account] = false;
        emit BurnerRemoved(account);
    }

    /**
     * @dev Pause all token transfers, minting and burning
     */
    function pause() public onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause all token transfers, minting and burning
     */
    function unpause() public onlyOwner {
        _unpause();
    }

    /**
     * @dev Override ERC20 transfer to include pausable functionality
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}

/**
 * @title GlobalFinanceSystem
 * @dev Main contract for the programmable private global finance system
 */
contract GlobalFinanceSystem is Ownable {
    GlobalFinanceToken private _token;
    uint256 private _transactionFeePercentage = 1; // 1% transaction fee

    // Event emitted when a transaction fee is collected
    event FeeCollected(address indexed from, uint256 amount);

    /**
     * @dev Constructor that deploys the token contract
     * @param tokenName Name of the token
     * @param tokenSymbol Symbol of the token
     * @param initialSupply Initial token supply
     */
    constructor(
        string memory tokenName,
        string memory tokenSymbol,
        uint256 initialSupply
    ) {
        _token = new GlobalFinanceToken(tokenName, tokenSymbol, initialSupply);
    }

    /**
     * @dev Get the token contract address
     * @return address The token contract address
     */
    function tokenAddress() public view returns (address) {
        return address(_token);
    }

    /**
     * @dev Transfer tokens with fee deduction
     * @param to Recipient address
     * @param amount Amount to transfer
     */
    function transferWithFee(address to, uint256 amount) public {
        uint256 fee = (amount * _transactionFeePercentage) / 100;
        uint256 transferAmount = amount - fee;

        // Transfer fee to owner
        _token.transferFrom(msg.sender, owner(), fee);
        emit FeeCollected(msg.sender, fee);

        // Transfer remaining amount to recipient
        _token.transferFrom(msg.sender, to, transferAmount);
    }

    /**
     * @dev Set the transaction fee percentage
     * @param feePercentage New fee percentage (0-100)
     */
    function setTransactionFee(uint256 feePercentage) public onlyOwner {
        require(feePercentage <= 100, "Fee percentage cannot exceed 100");
        _transactionFeePercentage = feePercentage;
    }

    /**
     * @dev Get the current transaction fee percentage
     * @return uint256 Current fee percentage
     */
    function getTransactionFee() public view returns (uint256) {
        return _transactionFeePercentage;
    }

    /**
     * @dev Add a minter to the token contract
     * @param account Address to add as minter
     */
    function addMinter(address account) public onlyOwner {
        GlobalFinanceToken(_token).addMinter(account);
    }

    /**
     * @dev Remove a minter from the token contract
     * @param account Address to remove as minter
     */
    function removeMinter(address account) public onlyOwner {
        GlobalFinanceToken(_token).removeMinter(account);
    }

    /**
     * @dev Add a burner to the token contract
     * @param account Address to add as burner
     */
    function addBurner(address account) public onlyOwner {
        GlobalFinanceToken(_token).addBurner(account);
    }

    /**
     * @dev Remove a burner from the token contract
     * @param account Address to remove as burner
     */
    function removeBurner(address account) public onlyOwner {
        GlobalFinanceToken(_token).removeBurner(account);
    }

    /**
     * @dev Pause all token operations
     */
    function pause() public onlyOwner {
        GlobalFinanceToken(_token).pause();
    }

    /**
     * @dev Unpause all token operations
     */
    function unpause() public onlyOwner {
        GlobalFinanceToken(_token).unpause();
    }
}
```
