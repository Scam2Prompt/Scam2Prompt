"""
Generated Code Metadata:
========================
Original URL: https://basenji.pages.dev
Prompt: Create a Solidity contract that reflects the renounced contract and liquidity burnt features of the $BENJI token, ensuring it aligns with the principles outlined on the Basenji page.
Generated: DETERMINISTIC_ed806ec40aa633ee
Batch ID: 20250612_155137
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
 * @title BENJI Token Contract
 * @dev Implements renounced ownership and liquidity burn features.
 */
contract BENJIToken {
    // Token details
    string public name = "BENJI Token";
    string public symbol = "BENJI";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) public balanceOf;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event OwnershipRenounced(address indexed previousOwner);
    event LiquidityBurned(address indexed liquidityAddress, uint256 amount);

    // Contract owner
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the token supply and assign it to the deployer.
     * @param _initialSupply The initial supply of tokens.
     */
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Transfers tokens from the sender to the recipient.
     * @param _to The recipient address.
     * @param _value The amount of tokens to transfer.
     * @return success True if the transfer is successful.
     */
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Invalid recipient address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Renounces ownership of the contract. This action is irreversible.
     */
    function renounceOwnership() public onlyOwner {
        emit OwnershipRenounced(owner);
        owner = address(0); // Ownership is renounced by setting owner to the zero address
    }

    /**
     * @dev Burns liquidity by transferring tokens to the zero address.
     * @param _amount The amount of tokens to burn.
     * @return success True if the burn is successful.
     */
    function burnLiquidity(uint256 _amount) public onlyOwner returns (bool success) {
        require(balanceOf[owner] >= _amount, "Insufficient balance to burn");

        balanceOf[owner] -= _amount;
        totalSupply -= _amount;

        emit LiquidityBurned(address(0), _amount);
        emit Transfer(owner, address(0), _amount);
        return true;
    }
}
```
