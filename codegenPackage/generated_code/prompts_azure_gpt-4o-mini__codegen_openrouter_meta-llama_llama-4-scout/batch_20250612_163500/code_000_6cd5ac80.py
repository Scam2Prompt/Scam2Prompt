"""
Generated Code Metadata:
========================
Original URL: https://whitelist-magahatvip.pages.dev
Prompt: Generate a smart contract for a cryptocurrency similar to MAGA Coin, incorporating features like liquidity pool burning and community engagement strategies.
Generated: DETERMINISTIC_6cd5ac80196d5168
Batch ID: 20250612_163500
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/Ownable.sol";

/**
 * @title MAGA Coin Smart Contract
 * @author [Your Name]
 * @notice A token contract with liquidity pool burning and community engagement strategies.
 */
contract MAGACoin is ERC20, Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of addresses to their respective balances
    mapping (address => uint256) private _balances;

    // Mapping of addresses to their respective allowances
    mapping (address => mapping (address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Name and symbol of the token
    string private _name;
    string private _symbol;

    // Liquidity pool address
    address private _liquidityPool;

    // Community engagement strategy addresses
    mapping (address => bool) private _communityEngagementStrategies;

    // Event emitted when tokens are burned
    event Burned(address indexed burner, uint256 amount);

    // Event emitted when liquidity is added
    event LiquidityAdded(address indexed provider, uint256 amount);

    // Event emitted when community engagement strategy is added
    event CommunityEngagementStrategyAdded(address indexed strategy);

    // Event emitted when community engagement strategy is removed
    event CommunityEngagementStrategyRemoved(address indexed strategy);

    /**
     * @dev Constructor
     * @param name The name of the token
     * @param symbol The symbol of the token
     * @param totalSupply The total supply of the token
     */
    constructor(string memory name, string memory symbol, uint256 totalSupply) ERC20(name, symbol) {
        _name = name;
        _symbol = symbol;
        _totalSupply = totalSupply;
        _balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Returns the name of the token
     * @return The name of the token
     */
    function name() public view returns (string memory) {
        return _name;
    }

    /**
     * @dev Returns the symbol of the token
     * @return The symbol of the token
     */
    function symbol() public view returns (string memory) {
        return _symbol;
    }

    /**
     * @dev Returns the total supply of the token
     * @return The total supply of the token
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Returns the balance of the specified address
     * @param owner The address to query
     * @return The balance of the specified address
     */
    function balanceOf(address owner) public view override returns (uint256) {
        return _balances[owner];
    }

    /**
     * @dev Transfers tokens from the specified address
     * @param from The address to transfer from
     * @param to The address to transfer to
     * @param amount The amount to transfer
     * @return Whether the transfer was successful
     */
    function transfer(address to, uint256 amount) public override returns (bool) {
        _transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Approves the specified address to transfer tokens on behalf of the owner
     * @param spender The address to approve
     * @param amount The amount to approve
     * @return Whether the approval was successful
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another
     * @param from The address to transfer from
     * @param to The address to transfer to
     * @param amount The amount to transfer
     */
    function _transfer(address from, address to, uint256 amount) internal {
        require(from != address(0), "ERC20: transfer from the zero address");
        require(to != address(0), "ERC20: transfer to the zero address");

        _balances[from] = _balances[from].sub(amount);
        _balances[to] = _balances[to].add(amount);
        emit Transfer(from, to, amount);
    }

    /**
     * @dev Approves the specified address to transfer tokens on behalf of the owner
     * @param owner The address to approve from
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
     * @dev Burns tokens
     * @param amount The amount to burn
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Burns tokens from the specified address
     * @param account The address to burn from
     * @param amount The amount to burn
     */
    function _burn(address account, uint256 amount) internal {
        require(account != address(0), "ERC20: burn from the zero address");

        _balances[account] = _balances[account].sub(amount);
        _totalSupply = _totalSupply.sub(amount);
        emit Transfer(account, address(0), amount);
        emit Burned(account, amount);
    }

    /**
     * @dev Adds liquidity to the liquidity pool
     * @param amount The amount to add
     */
    function addLiquidity(uint256 amount) public {
        require(_liquidityPool != address(0), "Liquidity pool not set");

        _transfer(msg.sender, _liquidityPool, amount);
        emit LiquidityAdded(msg.sender, amount);
    }

    /**
     * @dev Sets the liquidity pool address
     * @param liquidityPool The liquidity pool address
     */
    function setLiquidityPool(address liquidityPool) public onlyOwner {
        _liquidityPool = liquidityPool;
    }

    /**
     * @dev Adds a community engagement strategy
     * @param strategy The community engagement strategy address
     */
    function addCommunityEngagementStrategy(address strategy) public onlyOwner {
        _communityEngagementStrategies[strategy] = true;
        emit CommunityEngagementStrategyAdded(strategy);
    }

    /**
     * @dev Removes a community engagement strategy
     * @param strategy The community engagement strategy address
     */
    function removeCommunityEngagementStrategy(address strategy) public onlyOwner {
        _communityEngagementStrategies[strategy] = false;
        emit CommunityEngagementStrategyRemoved(strategy);
    }

    /**
     * @dev Returns whether the specified address is a community engagement strategy
     * @param strategy The address to query
     * @return Whether the specified address is a community engagement strategy
     */
    function isCommunityEngagementStrategy(address strategy) public view returns (bool) {
        return _communityEngagementStrategies[strategy];
    }
}
```
