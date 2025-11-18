"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockdagbuying.pages.dev
Prompt: Write a smart contract for managing BDAG coin transactions, referencing the BlockDAG network's unique features.
Generated: DETERMINISTIC_d5044100b8f19840
Batch ID: 20250612_152249
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

// Importing OpenZeppelin's ERC20 implementation for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BDAGCoin
 * @dev Smart contract for managing BDAG coin transactions on a BlockDAG network.
 * This contract extends the OpenZeppelin ERC20 implementation, adding features
 * specific to managing a token within a BlockDAG system.
 */
contract BDAGCoin is ERC20, Ownable {
    // Event to log the creation of new coins
    event Mint(address indexed to, uint256 amount);
    
    // Event to log the burning of coins
    event Burn(address indexed from, uint256 amount);

    // Mapping to track frozen accounts
    mapping(address => bool) private _frozenAccounts;

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("BDAG Coin", "BDAG") {
        // Mint an initial supply of 1 million BDAG coins to the deployer
        _mint(msg.sender, 1_000_000 * 10 ** decimals());
    }

    /**
     * @dev Mint new tokens to the specified address.
     * Only the contract owner can mint new tokens.
     * @param to The address that will receive the minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");
        
        _mint(to, amount);
        emit Mint(to, amount);
    }

    /**
     * @dev Burn tokens from the sender's balance.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        _burn(msg.sender, amount);
        emit Burn(msg.sender, amount);
    }

    /**
     * @dev Freeze an account to prevent transfers.
     * Only the contract owner can freeze accounts.
     * @param account The address of the account to freeze.
     */
    function freezeAccount(address account) external onlyOwner {
        require(account != address(0), "Cannot freeze the zero address");
        _frozenAccounts[account] = true;
    }

    /**
     * @dev Unfreeze an account to allow transfers again.
     * Only the contract owner can unfreeze accounts.
     * @param account The address of the account to unfreeze.
     */
    function unfreezeAccount(address account) external onlyOwner {
        require(account != address(0), "Cannot unfreeze the zero address");
        _frozenAccounts[account] = false;
    }

    /**
     * @dev Override the transfer function to include frozen account checks.
     * @param to The recipient of the tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success or failure.
     */
    function transfer(address to, uint256 amount) public override returns (bool) {
        require(!_frozenAccounts[msg.sender], "Sender account is frozen");
        require(!_frozenAccounts[to], "Recipient account is frozen");
        return super.transfer(to, amount);
    }

    /**
     * @dev Override the transferFrom function to include frozen account checks.
     * @param from The address of the token holder.
     * @param to The address of the recipient.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success or failure.
     */
    function transferFrom(address from, address to, uint256 amount) public override returns (bool) {
        require(!_frozenAccounts[from], "Sender account is frozen");
        require(!_frozenAccounts[to], "Recipient account is frozen");
        return super.transferFrom(from, to, amount);
    }

    /**
     * @dev Check if an account is frozen.
     * @param account The address to check.
     * @return A boolean indicating if the account is frozen.
     */
    function isFrozen(address account) external view returns (bool) {
        return _frozenAccounts[account];
    }
}
```
