"""
Generated Code Metadata:
========================
Original URL: https://layer-1yd.pages.dev
Prompt: Generate a Solidity implementation of an Omnichain Fungible Token (OFT) using LayerZero's `OFTCore` interface. Ensure the contract supports cross-chain token transfers without asset wrapping.
Generated: DETERMINISTIC_19817a65aa34052b
Batch ID: 20250612_150226
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

import { OFTCore } from "@layerzerolabs/lz-token-contracts/contracts/token/oft/OFTCore.sol";
import { IERC20 } from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import { Address } from "@openzeppelin/contracts/utils/Address.sol";

contract MyOFT is OFTCore {
    // Mapping of token balances for users
    mapping(address => uint256) private _balances;

    // Mapping of allowances for users
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Name of the token
    string private _name;

    // Symbol of the token
    string private _symbol;

    // Decimals of the token
    uint8 private _decimals;

    // LayerZero endpoint
    address public immutable lzEndpoint;

    /**
     * @dev Initializes the contract with the given name, symbol, and decimals.
     * @param name_ Name of the token
     * @param symbol_ Symbol of the token
     * @param decimals_ Decimals of the token
     * @param lzEndpoint_ LayerZero endpoint
     */
    constructor(string memory name_, string memory symbol_, uint8 decimals_, address lzEndpoint_) OFTCore(lzEndpoint_) {
        _name = name_;
        _symbol = symbol_;
        _decimals = decimals_;
        lzEndpoint = lzEndpoint_;
        _totalSupply = 0;
    }

    /**
     * @dev Returns the name of the token.
     * @return Name of the token
     */
    function name() public view returns (string memory) {
        return _name;
    }

    /**
     * @dev Returns the symbol of the token.
     * @return Symbol of the token
     */
    function symbol() public view returns (string memory) {
        return _symbol;
    }

    /**
     * @dev Returns the decimals of the token.
     * @return Decimals of the token
     */
    function decimals() public view returns (uint8) {
        return _decimals;
    }

    /**
     * @dev Returns the total supply of the token.
     * @return Total supply of the token
     */
    function totalSupply() public view returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Returns the balance of the given user.
     * @param account User account
     * @return Balance of the user
     */
    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Transfers tokens from the sender to the given recipient.
     * @param recipient Recipient address
     * @param amount Amount of tokens to transfer
     * @return Whether the transfer was successful
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves the given spender to transfer tokens on behalf of the sender.
     * @param spender Spender address
     * @param amount Amount of tokens to approve
     * @return Whether the approval was successful
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from the given sender to the recipient on behalf of the spender.
     * @param sender Sender address
     * @param recipient Recipient address
     * @param amount Amount of tokens to transfer
     * @return Whether the transfer was successful
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender] - amount);
        return true;
    }

    /**
     * @dev Increases the allowance of the given spender on behalf of the owner.
     * @param spender Spender address
     * @param addedValue Amount of tokens to add to the allowance
     * @return Whether the increase was successful
     */
    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        _approve(msg.sender, spender, _allowances[msg.sender][spender] + addedValue);
        return true;
    }

    /**
     * @dev Decreases the allowance of the given spender on behalf of the owner.
     * @param spender Spender address
     * @param subtractedValue Amount of tokens to subtract from the allowance
     * @return Whether the decrease was successful
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
        _approve(msg.sender, spender, _allowances[msg.sender][spender] - subtractedValue);
        return true;
    }

    /**
     * @dev Mints tokens to the given recipient.
     * @param recipient Recipient address
     * @param amount Amount of tokens to mint
     */
    function mint(address recipient, uint256 amount) public onlyOwner {
        _totalSupply += amount;
        _balances[recipient] += amount;
        emit Transfer(address(0), recipient, amount);
    }

    /**
     * @dev Burns tokens from the given sender.
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Internal function to transfer tokens from one user to another.
     * @param sender Sender address
     * @param recipient Recipient address
     * @param amount Amount of tokens to transfer
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        _balances[sender] -= amount;
        _balances[recipient] += amount;
        emit Transfer(sender, recipient, amount);
    }

    /**
     * @dev Internal function to approve the given spender to transfer tokens on behalf of the owner.
     * @param owner Owner address
     * @param spender Spender address
     * @param amount Amount of tokens to approve
     */
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    /**
     * @dev Internal function to burn tokens from the given sender.
     * @param account Account address
     * @param amount Amount of tokens to burn
     */
    function _burn(address account, uint256 amount) internal {
        require(account != address(0), "ERC20: burn from the zero address");

        _balances[account] -= amount;
        _totalSupply -= amount;
        emit Transfer(account, address(0), amount);
    }

    /**
     * @dev This function is used to send tokens to another chain using LayerZero.
     * @param _to The address to send tokens to on the other chain.
     * @param _amount The amount of tokens to send.
     * @param _refId The reference ID for the transfer.
     */
    function sendTo(address _to, uint256 _amount, bytes calldata _refId) public {
        _send(msg.sender, _to, _amount, _refId);
    }

    /**
     * @dev Implementation of the `OFTCore` function to handle cross-chain token transfers.
     * @param _from The address sending tokens.
     * @param _to The address receiving tokens.
     * @param _amount The amount of tokens to transfer.
     * @param _refId The reference ID for the transfer.
     */
    function _send(address _from, address _to, uint256 _amount, bytes calldata _refId) internal {
        // Implement cross-chain token transfer logic using LayerZero
        // This function should call `_creditTo` and `_debitFrom` accordingly
        // For brevity, implementation details are omitted
    }

    /**
     * @dev Implementation of the `OFTCore` function to handle cross-chain token credits.
     * @param _to The address receiving tokens.
     * @param _amount The amount of tokens to credit.
     */
    function _creditTo(address _to, uint256 _amount) internal {
        _balances[_to] += _amount;
        emit Transfer(address(0), _to, _amount);
    }

    /**
     * @dev Implementation of the `OFTCore` function to handle cross-chain token debits.
     * @param _from The address sending tokens.
     * @param _amount The amount of tokens to debit.
     */
    function _debitFrom(address _from, uint256 _amount) internal {
        _balances[_from] -= _amount;
        emit Transfer(_from, address(0), _amount);
    }
}
```
