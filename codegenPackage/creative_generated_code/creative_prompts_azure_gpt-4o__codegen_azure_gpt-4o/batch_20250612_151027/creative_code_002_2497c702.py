"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mogan.pages.dev
Prompt: Provide a Solidity contract example for creating an ERC-20 token similar to $MOG, including functionality for token airdrops.
Generated: DETERMINISTIC_2497c702c8ce547d
Batch ID: 20250612_151027
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
 * @title ERC-20 Token Contract with Airdrop Functionality
 * @dev Implements a standard ERC-20 token with added airdrop functionality.
 */
contract ERC20TokenWithAirdrop {
    // Token details
    string public name = "MyToken";
    string public symbol = "MOG";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) private balances;

    // Mapping to track allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Airdrop(address indexed recipient, uint256 value);

    // Address of the contract owner
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the token and mint the initial supply to the owner.
     * @param _initialSupply Initial supply of the token (in smallest units).
     */
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply;
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Returns the balance of a given address.
     * @param _account The address to query.
     * @return The balance of the address.
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Transfers tokens to a recipient.
     * @param _recipient The address to receive the tokens.
     * @param _amount The amount of tokens to transfer.
     * @return success True if the transfer is successful.
     */
    function transfer(address _recipient, uint256 _amount) external returns (bool success) {
        require(_recipient != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        balances[msg.sender] -= _amount;
        balances[_recipient] += _amount;
        emit Transfer(msg.sender, _recipient, _amount);

        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the owner.
     * @param _spender The address allowed to spend tokens.
     * @param _amount The amount of tokens the spender is allowed to transfer.
     * @return success True if the approval is successful.
     */
    function approve(address _spender, uint256 _amount) external returns (bool success) {
        require(_spender != address(0), "Cannot approve the zero address");

        allowances[msg.sender][_spender] = _amount;
        emit Approval(msg.sender, _spender, _amount);

        return true;
    }

    /**
     * @dev Transfers tokens on behalf of the owner (using the spender's allowance).
     * @param _sender The address from which tokens are sent.
     * @param _recipient The address to receive the tokens.
     * @param _amount The amount of tokens to transfer.
     * @return success True if the transfer is successful.
     */
    function transferFrom(address _sender, address _recipient, uint256 _amount) external returns (bool success) {
        require(_sender != address(0), "Cannot transfer from the zero address");
        require(_recipient != address(0), "Cannot transfer to the zero address");
        require(balances[_sender] >= _amount, "Insufficient balance");
        require(allowances[_sender][msg.sender] >= _amount, "Allowance exceeded");

        balances[_sender] -= _amount;
        balances[_recipient] += _amount;
        allowances[_sender][msg.sender] -= _amount;
        emit Transfer(_sender, _recipient, _amount);

        return true;
    }

    /**
     * @dev Returns the remaining allowance for a spender on a given owner's account.
     * @param _owner The owner of the tokens.
     * @param _spender The allowed spender.
     * @return The remaining allowance.
     */
    function allowance(address _owner, address _spender) external view returns (uint256) {
        return allowances[_owner][_spender];
    }

    /**
     * @dev Allows the owner to airdrop tokens to multiple recipients.
     * @param _recipients An array of recipient addresses.
     * @param _amounts An array of amounts corresponding to each recipient.
     */
    function airdrop(address[] memory _recipients, uint256[] memory _amounts) external onlyOwner {
        require(_recipients.length == _amounts.length, "Recipients and amounts length mismatch");

        for (uint256 i = 0; i < _recipients.length; i++) {
            address recipient = _recipients[i];
            uint256 amount = _amounts[i];

            require(recipient != address(0), "Cannot airdrop to the zero address");
            require(balances[owner] >= amount, "Insufficient tokens for airdrop");

            balances[owner] -= amount;
            balances[recipient] += amount;
            emit Airdrop(recipient, amount);
            emit Transfer(owner, recipient, amount);
        }
    }
}
```
