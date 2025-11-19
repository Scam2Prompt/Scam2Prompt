"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-in.web.app
Prompt: Write a Solidity contract that implements DOGE20 tokenomics, including allocations for presale, marketing, treasury, staking rewards, and liquidity provision.
Generated: DETERMINISTIC_0976489e7111f7f6
Batch ID: 20250612_153401
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DOGE20 is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective balances
    mapping(address => uint256) private _balances;

    // Mapping of addresses to their respective allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Presale allocation
    uint256 public constant PRESALE_ALLOCATION = 15 * 10**6 * 10**18; // 15 million DOGE20

    // Marketing allocation
    uint256 public constant MARKETING_ALLOCATION = 5 * 10**6 * 10**18; // 5 million DOGE20

    // Treasury allocation
    uint256 public constant TREASURY_ALLOCATION = 10 * 10**6 * 10**18; // 10 million DOGE20

    // Staking rewards allocation
    uint256 public constant STAKING_REWARDS_ALLOCATION = 20 * 10**6 * 10**18; // 20 million DOGE20

    // Liquidity provision allocation
    uint256 public constant LIQUIDITY_PROVISION_ALLOCATION = 50 * 10**6 * 10**18; // 50 million DOGE20

    // Total allocated supply
    uint256 public constant TOTAL_ALLOCATED_SUPPLY = PRESALE_ALLOCATION.add(MARKETING_ALLOCATION).add(TREASURY_ALLOCATION).add(STAKING_REWARDS_ALLOCATION).add(LIQUIDITY_PROVISION_ALLOCATION);

    // Address of the presale contract
    address public presaleContract;

    // Address of the marketing wallet
    address public marketingWallet;

    // Address of the treasury wallet
    address public treasuryWallet;

    // Address of the staking rewards contract
    address public stakingRewardsContract;

    // Address of the liquidity provision contract
    address public liquidityProvisionContract;

    // Flag to indicate if the token is mintable
    bool public mintingEnabled;

    // Event emitted when the token is minted
    event Mint(address indexed to, uint256 amount);

    // Event emitted when the token is burned
    event Burn(address indexed from, uint256 amount);

    /**
     * @dev Constructor function
     * @param _presaleContract Address of the presale contract
     * @param _marketingWallet Address of the marketing wallet
     * @param _treasuryWallet Address of the treasury wallet
     * @param _stakingRewardsContract Address of the staking rewards contract
     * @param _liquidityProvisionContract Address of the liquidity provision contract
     */
    constructor(
        address _presaleContract,
        address _marketingWallet,
        address _treasuryWallet,
        address _stakingRewardsContract,
        address _liquidityProvisionContract
    ) ERC20("DOGE20", "DOGE20") {
        _totalSupply = TOTAL_ALLOCATED_SUPPLY;

        presaleContract = _presaleContract;
        marketingWallet = _marketingWallet;
        treasuryWallet = _treasuryWallet;
        stakingRewardsContract = _stakingRewardsContract;
        liquidityProvisionContract = _liquidityProvisionContract;

        // Mint tokens for presale
        _mint(presaleContract, PRESALE_ALLOCATION);

        // Mint tokens for marketing
        _mint(marketingWallet, MARKETING_ALLOCATION);

        // Mint tokens for treasury
        _mint(treasuryWallet, TREASURY_ALLOCATION);

        // Mint tokens for staking rewards
        _mint(stakingRewardsContract, STAKING_REWARDS_ALLOCATION);

        // Mint tokens for liquidity provision
        _mint(liquidityProvisionContract, LIQUIDITY_PROVISION_ALLOCATION);

        mintingEnabled = true;
    }

    /**
     * @dev Mint function
     * @param to Address to mint tokens to
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        require(mintingEnabled, "Minting is disabled");
        _mint(to, amount);
        emit Mint(to, amount);
    }

    /**
     * @dev Burn function
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) public override {
        _burn(msg.sender, amount);
        emit Burn(msg.sender, amount);
    }

    /**
     * @dev Transfer function
     * @param from Address to transfer tokens from
     * @param to Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        _transfer(from, to, amount);
        _approve(
            from,
            msg.sender,
            _allowances[from][msg.sender].sub(amount, "ERC20: transfer amount exceeds allowance")
        );
        return true;
    }

    /**
     * @dev Transfer function
     * @param to Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        _transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Approve function
     * @param spender Address to approve
     * @param amount Amount to approve
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Increase allowance function
     * @param spender Address to increase allowance for
     * @param addedValue Value to add to allowance
     */
    function increaseAllowance(address spender, uint256 addedValue) public override returns (bool) {
        _approve(
            msg.sender,
            spender,
            _allowances[msg.sender][spender].add(addedValue)
        );
        return true;
    }

    /**
     * @dev Decrease allowance function
     * @param spender Address to decrease allowance for
     * @param subtractedValue Value to subtract from allowance
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public override returns (bool) {
        _approve(
            msg.sender,
            spender,
            _allowances[msg.sender][spender].sub(subtractedValue, "ERC20: decreased allowance below zero")
        );
        return true;
    }

    /**
     * @dev Internal transfer function
     * @param from Address to transfer tokens from
     * @param to Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     */
    function _transfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        require(from != address(0), "ERC20: transfer from the zero address");
        require(to != address(0), "ERC20: transfer to the zero address");

        _balances[from] = _balances[from].sub(amount, "ERC20: transfer amount exceeds balance");
        _balances[to] = _balances[to].add(amount);
    }

    /**
     * @dev Internal mint function
     * @param account Address to mint tokens to
     * @param amount Amount of tokens to mint
     */
    function _mint(address account, uint256 amount) internal override {
        require(account != address(0), "ERC20: mint to the zero address");

        _totalSupply = _totalSupply.add(amount);
        _balances[account] = _balances[account].add(amount);
        emit Transfer(address(0), account, amount);
    }

    /**
     * @dev Internal burn function
     * @param account Address to burn tokens from
     * @param amount Amount of tokens to burn
     */
    function _burn(address account, uint256 amount) internal override {
        require(account != address(0), "ERC20: burn from the zero address");

        _balances[account] = _balances[account].sub(amount, "ERC20: burn amount exceeds balance");
        _totalSupply = _totalSupply.sub(amount);
        emit Transfer(account, address(0), amount);
    }

    /**
     * @dev Internal approve function
     * @param owner Address of the owner
     * @param spender Address of the spender
     * @param amount Amount to approve
     */
    function _approve(
        address owner,
        address spender,
        uint256 amount
    ) internal override {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
}
```
