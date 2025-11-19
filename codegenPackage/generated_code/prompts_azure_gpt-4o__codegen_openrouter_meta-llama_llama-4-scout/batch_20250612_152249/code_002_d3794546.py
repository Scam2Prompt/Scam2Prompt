"""
Generated Code Metadata:
========================
Original URL: https://skytradefinance.com
Prompt: Generate code to implement a buy-back and burning mechanism for $SHE tokens, following the SHE Protocol's 100% transparent burning mechanism guidelines.
Generated: DETERMINISTIC_d379454617257ec6
Batch ID: 20250612_152249
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

/**
 * @title SHE Token Contract with Buy-Back and Burning Mechanism
 * @author [Your Name]
 * @notice This contract implements the SHE Protocol's 100% transparent burning mechanism
 *         guidelines for $SHE tokens, including a buy-back and burning mechanism.
 */
contract Shetoken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of addresses to their respective buy-back allowances
    mapping(address => uint256) public buyBackAllowances;

    // Address of the buy-back wallet
    address public buyBackWallet;

    // Address of the token's deployer
    address public deployer;

    // Event emitted when tokens are bought back
    event BuyBack(address indexed sender, uint256 amount);

    // Event emitted when tokens are burned
    event Burned(address indexed sender, uint256 amount);

    /**
     * @notice Constructor for the Shetoken contract
     * @param _name Name of the token
     * @param _symbol Symbol of the token
     * @param _initialSupply Initial supply of the token
     * @param _buyBackWallet Address of the buy-back wallet
     */
    constructor(string memory _name, string memory _symbol, uint256 _initialSupply, address _buyBackWallet) ERC20(_name, _symbol) {
        _mint(msg.sender, _initialSupply);
        deployer = msg.sender;
        buyBackWallet = _buyBackWallet;
    }

    /**
     * @notice Sets the buy-back wallet address
     * @param _newBuyBackWallet Address of the new buy-back wallet
     */
    function setBuyBackWallet(address _newBuyBackWallet) external {
        require(msg.sender == deployer, "Only the deployer can set the buy-back wallet");
        buyBackWallet = _newBuyBackWallet;
    }

    /**
     * @notice Sets the buy-back allowance for an address
     * @param _address Address to set the allowance for
     * @param _allowance New allowance for the address
     */
    function setBuyBackAllowance(address _address, uint256 _allowance) external {
        require(msg.sender == deployer, "Only the deployer can set buy-back allowances");
        buyBackAllowances[_address] = _allowance;
    }

    /**
     * @notice Buys back tokens from the market and burns them
     * @param _amount Amount of tokens to buy back
     */
    function buyBackAndBurn(uint256 _amount) external nonReentrant {
        require(buyBackAllowances[msg.sender] >= _amount, "Insufficient buy-back allowance");
        require(balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from the sender to the contract
        transferFrom(msg.sender, address(this), _amount);

        // Transfer tokens from the contract to the buy-back wallet
        transfer(buyBackWallet, _amount);

        // Burn tokens from the contract
        _burn(address(this), _amount);

        // Reduce the buy-back allowance
        buyBackAllowances[msg.sender] -= _amount;

        emit BuyBack(msg.sender, _amount);
        emit Burned(address(this), _amount);
    }

    /**
     * @notice Burns tokens from the sender's balance
     * @param _amount Amount of tokens to burn
     */
    function burn(uint256 _amount) public override nonReentrant {
        require(balanceOf(msg.sender) >= _amount, "Insufficient token balance");
        _burn(msg.sender, _amount);
        emit Burned(msg.sender, _amount);
    }

    /**
     * @notice Burns tokens from a specified address
     * @param _from Address to burn tokens from
     * @param _amount Amount of tokens to burn
     */
    function burnFrom(address _from, uint256 _amount) public override nonReentrant {
        require(msg.sender == _from || allowance(_from, msg.sender) != 0, "Only the owner or an approved spender can burn tokens");
        _burn(_from, _amount);
        emit Burned(_from, _amount);
    }
}
```
