"""
Generated Code Metadata:
========================
Original URL: https://earns-pupstoken.pages.dev
Prompt: Create a Solidity contract that mimics the community-driven aspects of the $PUPS token, emphasizing its zero utility and meme culture.
Generated: DETERMINISTIC_755c2478f81b2e73
Batch ID: 20250612_162203
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

/**
 * @title $PUPS Token Contract
 * @notice A purely meme-based token with zero utility, celebrating internet culture
 * @dev Implements a standard ERC-20 token with additional meme features
 */
contract PupsToken {
    // Token metadata
    string public constant name = "$PUPS";
    string public constant symbol = "PUPS";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // Token balances and allowances
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Meme events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Bark(address indexed sender, string message);
    event MemeShared(address indexed sharer, string memeUri);

    // Community messages
    string[] public communityBarks;
    string[] public memeGallery;

    /**
     * @dev Constructor that mints initial supply to creator
     * @param initialSupply The initial token supply (in smallest units)
     */
    constructor(uint256 initialSupply) {
        totalSupply = initialSupply;
        _balances[msg.sender] = initialSupply;
        emit Transfer(address(0), msg.sender, initialSupply);
    }

    /**
     * @notice Get the token balance of an account
     * @param account The address to query
     * @return The balance of the account
     */
    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Transfer tokens to another address
     * @param recipient The address to transfer to
     * @param amount The amount to transfer
     * @return success Whether the transfer was successful
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @notice Get the allowance for a spender
     * @param owner The address that owns the tokens
     * @param spender The address allowed to spend
     * @return The remaining allowance
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @notice Approve a spender to transfer tokens
     * @param spender The address to approve
     * @param amount The amount to approve
     * @return success Whether the approval was successful
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Transfer tokens from one address to another via allowance
     * @param sender The address to transfer from
     * @param recipient The address to transfer to
     * @param amount The amount to transfer
     * @return success Whether the transfer was successful
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        _transfer(sender, recipient, amount);

        uint256 currentAllowance = _allowances[sender][msg.sender];
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        unchecked {
            _approve(sender, msg.sender, currentAllowance - amount);
        }

        return true;
    }

    /**
     * @notice Internal transfer function
     * @param sender The address to transfer from
     * @param recipient The address to transfer to
     * @param amount The amount to transfer
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        uint256 senderBalance = _balances[sender];
        require(senderBalance >= amount, "ERC20: transfer amount exceeds balance");
        unchecked {
            _balances[sender] = senderBalance - amount;
        }
        _balances[recipient] += amount;

        emit Transfer(sender, recipient, amount);
    }

    /**
     * @notice Internal approval function
     * @param owner The address that owns the tokens
     * @param spender The address to approve
     * @param amount The amount to approve
     */
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    /**
     * @notice Let token holders "bark" - a purely meme function
     * @param message The bark message
     */
    function bark(string memory message) public {
        require(bytes(message).length > 0, "Cannot bark empty message");
        communityBarks.push(message);
        emit Bark(msg.sender, message);
    }

    /**
     * @notice Share a meme URI with the community
     * @param memeUri The URI of the meme (IPFS, HTTP, etc.)
     */
    function shareMeme(string memory memeUri) public {
        require(bytes(memeUri).length > 0, "Cannot share empty meme URI");
        memeGallery.push(memeUri);
        emit MemeShared(msg.sender, memeUri);
    }

    /**
     * @notice Get the total number of barks
     * @return The count of community barks
     */
    function getBarkCount() public view returns (uint256) {
        return communityBarks.length;
    }

    /**
     * @notice Get the total number of shared memes
     * @return The count of shared memes
     */
    function getMemeCount() public view returns (uint256) {
        return memeGallery.length;
    }

    /**
     * @notice Get a specific bark by index
     * @param index The index of the bark
     * @return The bark message
     */
    function getBark(uint256 index) public view returns (string memory) {
        require(index < communityBarks.length, "Index out of bounds");
        return communityBarks[index];
    }

    /**
     * @notice Get a specific meme URI by index
     * @param index The index of the meme
     * @return The meme URI
     */
    function getMeme(uint256 index) public view returns (string memory) {
        require(index < memeGallery.length, "Index out of bounds");
        return memeGallery[index];
    }
}
```
