"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-coin-creator.pages.dev
Prompt: Write a Solidity code snippet for creating a token on the BNB Smart Chain with 100% ownership and a $1 creation fee.
Generated: DETERMINISTIC_93f56198862511d1
Batch ID: 20250612_155911
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
 * @title TokenWithOwnership
 * @dev A simple token contract with 100% ownership reserved for the deployer.
 * Includes a $1 creation fee (payable in BNB).
 */
contract TokenWithOwnership {
    // Token details
    string public name;
    string public symbol;
    uint8 public decimals;
    uint256 public totalSupply;

    // Ownership mapping
    mapping(address => uint256) private balances;

    // Address of the contract owner
    address public owner;

    // $1 creation fee (in BNB)
    uint256 public constant CREATION_FEE = 0.0035 ether; // Approximate value for $1 (subject to market rate fluctuations)

    // Event declarations
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "You are not the owner");
        _;
    }

    /**
     * @dev Constructor for the token contract.
     * Requires a $1 creation fee to be paid during deployment.
     * @param _name Name of the token.
     * @param _symbol Symbol of the token.
     * @param _decimals Number of decimals the token uses.
     * @param _totalSupply Total token supply (allocated to owner).
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint8 _decimals,
        uint256 _totalSupply
    ) payable {
        // Ensure the creation fee is paid
        require(msg.value >= CREATION_FEE, "Insufficient creation fee");

        // Initialize token details
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _totalSupply;

        // Assign all tokens to the deployer
        owner = msg.sender;
        balances[owner] = _totalSupply;

        // Emit a transfer event to reflect token allocation
        emit Transfer(address(0), owner, _totalSupply);
    }

    /**
     * @dev Transfer tokens to a specific address.
     * @param _to Address to transfer tokens to.
     * @param _value Number of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) external returns (bool) {
        // Check for sufficient balance
        require(balances[msg.sender] >= _value, "Insufficient balance");

        // Perform the transfer
        balances[msg.sender] -= _value;
        balances[_to] += _value;

        // Emit a transfer event
        emit Transfer(msg.sender, _to, _value);

        return true;
    }

    /**
     * @dev Get the balance of a specific address.
     * @param _account Address to query the balance for.
     * @return Balance of the specified address.
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Withdraw the creation fee collected during deployment.
     * Restricted to owner.
     */
    function withdrawFee() external onlyOwner {
        // Transfer the fee to the owner's address
        payable(owner).transfer(address(this).balance);
    }
}
```
