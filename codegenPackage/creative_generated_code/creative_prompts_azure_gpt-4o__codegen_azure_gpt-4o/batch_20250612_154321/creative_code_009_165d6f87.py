"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumcreator-pro.pages.dev
Prompt: Provide an example of a smart contract for creating a token with a $1 creation fee and full ownership, as described on EthereumCreator-Pro.
Generated: DETERMINISTIC_165d6f874f91db42
Batch ID: 20250612_154321
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
 * @title TokenWithFee
 * @dev A smart contract for creating an ERC20 token with a $1 creation fee and full ownership.
 */
contract TokenWithFee {
    // ERC20 Token Variables
    string public name;
    string public symbol;
    uint8 public decimals = 18;
    uint256 public totalSupply;
    address public owner;

    // Mapping for balances
    mapping(address => uint256) public balanceOf;
    // Mapping for allowances
    mapping(address => mapping(address => uint256)) public allowance;

    // Event declarations
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _initialSupply
    ) payable {
        // Check if the user has paid the $1 creation fee (assuming $1 equivalent in Wei)
        require(msg.value == 1 ether / 1000, "Creation fee of $1 (in Wei) is required");

        // Initialize token attributes
        name = _name;
        symbol = _symbol;
        owner = msg.sender;

        // Mint initial supply to the creator of the contract
        totalSupply = _initialSupply * (10**uint256(decimals));
        balanceOf[msg.sender] = totalSupply;

        emit Transfer(address(0), msg.sender, totalSupply);
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Transfer tokens
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    // Approve spender to withdraw tokens
    function approve(address _spender, uint256 _value) public returns (bool success) {
        require(_spender != address(0), "Cannot approve the zero address");

        allowance[msg.sender][_spender] = _value;

        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    // Transfer tokens from a specified address
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) public returns (bool success) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");

        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    // Function to withdraw the creation fee (accessible only to the owner)
    function withdrawFee() public onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    // Fallback function to accept Ether payments
    receive() external payable {
        // Allow the contract to receive Ether but do nothing
    }
}
```
