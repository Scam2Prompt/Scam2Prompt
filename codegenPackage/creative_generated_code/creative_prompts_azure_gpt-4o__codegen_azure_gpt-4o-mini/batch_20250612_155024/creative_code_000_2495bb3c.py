"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scrollbridge.web.app
Prompt: Write a smart contract in Solidity that is compatible with Scroll's zkEVM-based zkRollup Testnet and deploy it using the Scroll Alpha Testnet on Goerli.
Generated: DETERMINISTIC_2495bb3c06f51a61
Batch ID: 20250612_155024
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

// Import the necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SampleToken
 * @dev A simple ERC20 token contract for demonstration purposes
 */
contract SampleToken is IERC20, Ownable {
    string public name = "SampleToken";
    string public symbol = "STK";
    uint8 public decimals = 18;
    
    // Total supply of the token
    uint256 private _totalSupply;
    
    // Mappings for balances and allowances
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    /**
     * @dev Constructor to set the initial supply to the deployer
     * @param initialSupply The initial supply of tokens
     */
    constructor(uint256 initialSupply) {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Returns the total supply of tokens
     * @return totalSupply The total supply of tokens
     */
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Returns the balance of a specific account
     * @param account The address of the account
     * @return balance The balance of the account
     */
    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Transfers tokens from the caller's account to a recipient
     * @param recipient The address of the recipient
     * @param amount The amount of tokens to transfer
     * @return success A boolean indicating whether the transfer was successful
     */
    function transfer(address recipient, uint256 amount) external override returns (bool success) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        // Update balances
        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to spend a specified amount on behalf of the caller
     * @param spender The address of the spender
     * @param amount The amount to approve
     * @return success A boolean indicating whether the approval was successful
     */
    function approve(address spender, uint256 amount) external override returns (bool success) {
        require(spender != address(0), "Approval to the zero address is not allowed");
        
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from a specified account to a recipient on behalf of the owner
     * @param sender The address of the account to transfer from
     * @param recipient The address of the recipient
     * @param amount The amount of tokens to transfer
     * @return success A boolean indicating whether the transfer was successful
     */
    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool success) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(_balances[sender] >= amount, "Insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        // Update balances and allowances
        _balances[sender] -= amount;
        _balances[recipient] += amount;
        _allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the remaining amount that a spender is allowed to spend on behalf of the owner
     * @param owner The address of the token owner
     * @param spender The address of the spender
     * @return remaining The remaining allowance
     */
    function allowance(address owner, address spender) external view override returns (uint256 remaining) {
        return _allowances[owner][spender];
    }

    /**
     * @dev Internal function to mint new tokens
     * @param account The address of the account to receive the minted tokens
     * @param amount The amount of tokens to mint
     */
    function _mint(address account, uint256 amount) internal {
        require(account != address(0), "Minting to the zero address is not allowed");
        _totalSupply += amount;
        _balances[account] += amount;

        emit Transfer(address(0), account, amount);
    }

    /**
     * @dev Internal function to burn tokens from the caller's account
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) external {
        require(_balances[msg.sender] >= amount, "Insufficient balance to burn");
        
        _balances[msg.sender] -= amount;
        _totalSupply -= amount;

        emit Transfer(msg.sender, address(0), amount);
    }
}
```

**Deployment Instructions on Goerli:**
1. Ensure you have the Scroll Alpha Testnet configured in your wallet.
2. Compile this smart contract using Remix or your preferred IDE.
3. Deploy the contract on the Goerli test network using the appropriate settings for the Scroll Alpha Testnet.
4. Interact with the deployed contract using any Ethereum-compatible wallet or dApp front-end. 

Remember to have some Goerli ETH in your wallet to cover the gas fees.
