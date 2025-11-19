"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://projectdeksa.pages.dev
Prompt: Develop a smart contract in Solidity for the $MASA token, incorporating features that reflect its utility in the virtual economy of the DEKSA project.
Generated: DETERMINISTIC_758ac069e5cf4f1b
Batch ID: 20250612_163848
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

// Importing the OpenZeppelin ERC20 contract for standard token functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MASAToken
 * @dev Implementation of the $MASA token for the DEKSA project
 */
contract MASAToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Token details
    string private constant _name = "Masa Token";
    string private constant _symbol = "MASA";
    uint8 private constant _decimals = 18;

    // Mapping to track the balances locked in staking
    mapping(address => uint256) private _stakingBalances;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the token with an initial supply
    constructor(uint256 initialSupply) ERC20(_name, _symbol) {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, initialSupply.mul(10 ** uint256(_decimals)));
    }

    /**
     * @dev Stake a specified amount of MASA tokens.
     * @param amount The amount of tokens to be staked.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        // Transfer the tokens to the contract for staking
        _transfer(msg.sender, address(this), amount);
        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].add(amount);
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake a specified amount of MASA tokens.
     * @param amount The amount of tokens to be unstaked.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than 0");
        require(_stakingBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update the staking balance and transfer tokens back to the user
        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].sub(amount);
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Get the staking balance of a specific user.
     * @param user The address of the user to query.
     * @return The staking balance of the user.
     */
    function stakingBalance(address user) external view returns (uint256) {
        return _stakingBalances[user];
    }

    /**
     * @dev Allow the owner to mint new tokens.
     * @param to The address to which the newly minted tokens will be sent.
     * @param amount The amount of tokens to be minted.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(amount > 0, "Mint amount must be greater than 0");
        _mint(to, amount);
    }

    /**
     * @dev Allow the owner to burn tokens from any user's balance.
     * @param from The address from which tokens will be burned.
     * @param amount The amount of tokens to be burned.
     */
    function burn(address from, uint256 amount) external onlyOwner {
        require(amount > 0, "Burn amount must be greater than 0");
        require(balanceOf(from) >= amount, "Insufficient balance to burn");
        
        _burn(from, amount);
    }
}
```
