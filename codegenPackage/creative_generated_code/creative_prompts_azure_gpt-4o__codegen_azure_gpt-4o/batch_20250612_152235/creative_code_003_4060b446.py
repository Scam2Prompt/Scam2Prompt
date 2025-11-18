"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe-claims.pages.dev
Prompt: Create an example of an ERC-20 token contract similar to $PEPE, including tokenomics features like airdrops.
Generated: DETERMINISTIC_4060b446cb172b02
Batch ID: 20250612_152235
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
 * @title ERC-20 Token Contract with Tokenomics Features
 * @author Expert Programmer
 * @notice This contract creates an ERC-20 token with optional airdrop functionality
 * @dev Follows best practices and includes proper error handling
 */
contract PepeToken {
    // Token details
    string public name = "PepeToken";
    string public symbol = "PEPE";
    uint8 public decimals = 18; // Standard precision
    uint256 public totalSupply;

    // Mapping for balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Owner of the contract (centralized control for tokenomics features)
    address public owner;

    // Events for token activities
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Airdrop(address indexed recipient, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @notice Constructor to initialize the token and mint initial supply
     * @param _initialSupply The initial token supply in wei
     */
    constructor(uint256 _initialSupply) {
        owner = msg.sender; // Set the contract deployer as the owner
        totalSupply = _initialSupply; // Set total supply
        balances[owner] = _initialSupply; // Assign all tokens to the owner
        emit Transfer(address(0), owner, _initialSupply); // Emit the initial transfer event
    }

    /**
     * @notice Check the balance of an account
     * @param _account The address to query the balance of
     * @return The balance of the requested account
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }

    /**
     * @notice Transfer tokens to a recipient
     * @param _recipient The address to transfer tokens to
     * @param _amount The amount of tokens to transfer
     * @return True if the transfer was successful
     */
    function transfer(address _recipient, uint256 _amount) external returns (bool) {
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        require(_recipient != address(0), "Cannot transfer to zero address");

        balances[msg.sender] -= _amount;
        balances[_recipient] += _amount;
        emit Transfer(msg.sender, _recipient, _amount);
        return true;
    }

    /**
     * @notice Approve an address to spend tokens on behalf of msg.sender
     * @param _spender Address allowed to spend the tokens
     * @param _amount Amount of tokens to approve
     * @return True if the approval was successful
     */
    function approve(address _spender, uint256 _amount) external returns (bool) {
        require(_spender != address(0), "Cannot approve zero address");

        allowances[msg.sender][_spender] = _amount;
        emit Approval(msg.sender, _spender, _amount);
        return true;
    }

    /**
     * @notice Transfer tokens from one account to another using allowance
     * @param _sender Address from which tokens are transferred
     * @param _recipient Address to transfer tokens to
     * @param _amount Amount of tokens to transfer
     * @return True if the transfer was successful
     */
    function transferFrom(address _sender, address _recipient, uint256 _amount) external returns (bool) {
        require(balances[_sender] >= _amount, "Insufficient balance");
        require(allowances[_sender][msg.sender] >= _amount, "Allowance exceeded");
        require(_recipient != address(0), "Cannot transfer to zero address");

        balances[_sender] -= _amount;
        balances[_recipient] += _amount;
        allowances[_sender][msg.sender] -= _amount;

        emit Transfer(_sender, _recipient, _amount);
        return true;
    }

    /**
     * @notice Check the allowance for a spender
     * @param _owner Token owner
     * @param _spender Address allowed to spend tokens
     * @return Remaining allowance for the spender
     */
    function allowance(address _owner, address _spender) external view returns (uint256) {
        return allowances[_owner][_spender];
    }

    /**
     * @notice Mint new tokens to an account (owner-only)
     * @param _account Address to mint tokens to
     * @param _amount Amount of tokens to mint
     */
    function mint(address _account, uint256 _amount) external onlyOwner {
        require(_account != address(0), "Cannot mint to zero address");
        totalSupply += _amount;
        balances[_account] += _amount;
        emit Transfer(address(0), _account, _amount);
    }

    /**
     * @notice Airdrop tokens to multiple accounts (owner-only)
     * @param _recipients Array of recipient addresses
     * @param _amounts Array of token amounts for each address
     */
    function airdrop(address[] calldata _recipients, uint256[] calldata _amounts) external onlyOwner {
        require(_recipients.length == _amounts.length, "Recipients and amounts length mismatch");

        for (uint256 i = 0; i < _recipients.length; i++) {
            address recipient = _recipients[i];
            uint256 amount = _amounts[i];

            require(recipient != address(0), "Cannot airdrop to zero address");
            require(balances[owner] >= amount, "Insufficient balance for airdrop");

            balances[owner] -= amount;
            balances[recipient] += amount;
            emit Airdrop(recipient, amount);
            emit Transfer(owner, recipient, amount);
        }
    }

    /**
     * @notice Burn tokens from an account (owner-only)
     * @param _account Address to burn tokens from
     * @param _amount Amount of tokens to burn
     */
    function burn(address _account, uint256 _amount) external onlyOwner {
        require(balances[_account] >= _amount, "Insufficient balance to burn");
        totalSupply -= _amount;
        balances[_account] -= _amount;
        emit Transfer(_account, address(0), _amount);
    }
}
```
