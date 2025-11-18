"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperswap.tech
Prompt: Generate a smart contract for launching a new token on the HyperEVM Native Dex, incorporating liquidity management features.
Generated: DETERMINISTIC_40e6f76cf8320080
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title TokenWithLiquidityManagement
 * @dev A smart contract for launching a new ERC20 token and managing its liquidity on a HyperEVM Native Dex.
 */
contract TokenWithLiquidityManagement {
    // ERC20 Token variables
    string public name = "MyToken";
    string public symbol = "MTK";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Liquidity variables
    address public owner;
    address public dexRouter; // Address of the Dex Router
    address public liquidityPool; // Address of the liquidity pool

    // Balances mapping
    mapping(address => uint256) public balances;

    // Allowances mapping for ERC20 functionality
    mapping(address => mapping(address => uint256)) public allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event LiquidityAdded(uint256 tokenAmount, uint256 nativeAmount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize token parameters and set the owner.
     * @param _totalSupply The total supply of the token.
     * @param _dexRouter Address of the Dex Router to interact with.
     */
    constructor(uint256 _totalSupply, address _dexRouter) {
        require(_dexRouter != address(0), "Invalid Dex Router address");
        totalSupply = _totalSupply * (10**decimals);
        balances[msg.sender] = totalSupply;
        owner = msg.sender;
        dexRouter = _dexRouter;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param _to The address to transfer tokens to.
     * @param _value The amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Transfer to zero address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approves a spender to spend tokens on behalf of the token owner.
     * @param _spender The address of the spender.
     * @param _value The amount of tokens to approve.
     */
    function approve(address _spender, uint256 _value) external returns (bool) {
        require(_spender != address(0), "Approve to zero address");

        allowances[msg.sender][_spender] = _value;

        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using allowance mechanism.
     * @param _from The address to transfer tokens from.
     * @param _to The address to transfer tokens to.
     * @param _value The amount of tokens to transfer.
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) external returns (bool) {
        require(_to != address(0), "Transfer to zero address");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");

        balances[_from] -= _value;
        balances[_to] += _value;
        allowances[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Adds liquidity to the Dex Router.
     * @param tokenAmount Amount of tokens to add to the liquidity pool.
     * @param nativeAmount Amount of native currency to add to the liquidity pool.
     */
    function addLiquidity(uint256 tokenAmount, uint256 nativeAmount) external onlyOwner {
        require(tokenAmount > 0 && nativeAmount > 0, "Invalid amounts");

        // Transfer tokens from owner to this contract
        balances[owner] -= tokenAmount;
        balances[address(this)] += tokenAmount;

        // Interact with Dex Router to add liquidity
        // Placeholder for Dex Router interaction - Replace with actual Dex functions
        // Example: dexRouter.addLiquidity(tokenAddress, nativeAmount);

        emit LiquidityAdded(tokenAmount, nativeAmount);
    }

    /**
     * @dev Returns the balance of a given address.
     * @param _account The address to query the balance of.
     * @return The balance of the given address.
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Returns the allowance of a spender for a given owner.
     * @param _owner The address of the token owner.
     * @param _spender The address of the spender.
     * @return The amount of tokens the spender is allowed to transfer on behalf of the owner.
     */
    function allowance(address _owner, address _spender) external view returns (uint256) {
        return allowances[_owner][_spender];
    }
}
```
