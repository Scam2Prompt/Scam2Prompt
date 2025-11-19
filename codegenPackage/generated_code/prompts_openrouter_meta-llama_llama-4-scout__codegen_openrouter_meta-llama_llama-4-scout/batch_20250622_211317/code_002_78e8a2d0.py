"""
Generated Code Metadata:
========================
Original URL: https://simoncat.pages.dev
Prompt: Generate a smart contract code in Solidity for a token with a similar tokenomics structure to Simon's Cat, including a 30% presale allocation for investors and a 10% allocation for the foundation.
Generated: DETERMINISTIC_78e8a2d06db77432
Batch ID: 20250622_211317
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

/**
 * @title SimCatToken
 * @author [Your Name]
 * @notice Token contract for Simon's Cat-like tokenomics
 */
contract SimCatToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tokenomics
    uint256 public constant TOTAL_SUPPLY = 1 * 10**9 * 10**18; // 1 billion tokens
    uint256 public constant PRESALE_ALLOCATION = TOTAL_SUPPLY * 30 / 100; // 30% for presale
    uint256 public constant FOUNDATION_ALLOCATION = TOTAL_SUPPLY * 10 / 100; // 10% for foundation

    // Mapping of account balances
    mapping(address => uint256) public balances;

    // Mapping of allowances
    mapping(address => mapping(address => uint256)) public allowances;

    // Events
    event Presale(address indexed to, uint256 amount);
    event FoundationAllocation(address indexed to, uint256 amount);

    /**
     * @notice Constructor
     * @param name_ Token name
     * @param symbol_ Token symbol
     */
    constructor(string memory name_, string memory symbol_) ERC20(name_, symbol_) {
        // Mint total supply
        _mint(msg.sender, TOTAL_SUPPLY);

        // Presale allocation
        _presaleAllocation();

        // Foundation allocation
        _foundationAllocation();
    }

    /**
     * @notice Presale allocation
     */
    function _presaleAllocation() internal {
        // Presale investors
        address[] memory presaleInvestors = new address[](1);
        presaleInvestors[0] = 0x...; // Add presale investor addresses

        uint256 presaleAmount = PRESALE_ALLOCATION.div(presaleInvestors.length);

        for (uint256 i = 0; i < presaleInvestors.length; i++) {
            _transfer(msg.sender, presaleInvestors[i], presaleAmount);
            emit Presale(presaleInvestors[i], presaleAmount);
        }
    }

    /**
     * @notice Foundation allocation
     */
    function _foundationAllocation() internal {
        address foundation = 0x...; // Add foundation address
        _transfer(msg.sender, foundation, FOUNDATION_ALLOCATION);
        emit FoundationAllocation(foundation, FOUNDATION_ALLOCATION);
    }

    /**
     * @notice Transfer tokens
     * @param to Recipient address
     * @param amount Amount to transfer
     * @return bool Success
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        return super.transfer(to, amount);
    }

    /**
     * @notice Approve spending
     * @param spender Spender address
     * @param amount Amount to approve
     * @return bool Success
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        return super.approve(spender, amount);
    }

    /**
     * @notice Transfer from
     * @param from Sender address
     * @param to Recipient address
     * @param amount Amount to transfer
     * @return bool Success
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        return super.transferFrom(from, to, amount);
    }

    /**
     * @notice Increase allowance
     * @param spender Spender address
     * @param addedValue Value to add
     * @return bool Success
     */
    function increaseAllowance(address spender, uint256 addedValue) public override returns (bool) {
        return super.increaseAllowance(spender, addedValue);
    }

    /**
     * @notice Decrease allowance
     * @param spender Spender address
     * @param subtractedValue Value to subtract
     * @return bool Success
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public override returns (bool) {
        return super.decreaseAllowance(spender, subtractedValue);
    }

    /**
     * @notice Burn tokens
     * @param amount Amount to burn
     */
    function burn(uint256 amount) public override {
        super.burn(amount);
    }

    /**
     * @notice Burn tokens from
     * @param account Account to burn from
     * @param amount Amount to burn
     */
    function burnFrom(address account, uint256 amount) public override {
        super.burnFrom(account, amount);
    }
}
```
