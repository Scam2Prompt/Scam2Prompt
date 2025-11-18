"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Write a Solidity smart contract to create a token that complies with the ERC-20 standard, as described in Ethereum's documentation.
Generated: DETERMINISTIC_28829d645b2f0b36
Batch ID: 20250612_151948
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

// Importing the OpenZeppelin ERC20 contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MyToken
 * @dev Implementation of the ERC20 token standard with minting capability
 */
contract MyToken is ERC20, Ownable {
    // Mapping from account addresses to their allowed spenders
    mapping(address => mapping(address => uint256)) private _allowances;

    // Event emitted when tokens are minted
    event TokensMinted(address indexed to, uint256 amount);

    /**
     * @dev Constructor that gives the creator all initial tokens.
     */
    constructor(uint256 initialSupply) ERC20("MyToken", "MTK") {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Minting initial supply to the contract deployer
    }

    /**
     * @dev Function to mint new tokens. Only callable by the owner.
     * @param to The address that will receive the minted tokens.
     * @param amount The number of tokens to mint.
     */
    function mint(address to, uint256 amount) public onlyOwner {
        require(to != address(0), "Mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");
        _mint(to, amount);
        emit TokensMinted(to, amount); // Emitting an event after minting
    }

    /**
     * @dev Function to transfer tokens. Overrides the ERC20 transfer function
     * to add custom logic if necessary in the future.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(amount <= balanceOf(msg.sender), "Transfer amount exceeds balance");

        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Function to approve another address to spend tokens on behalf of the msg.sender.
     * @param spender The address that will spend the tokens.
     * @param amount The amount of tokens to be spent.
     * @return A boolean indicating success.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        require(spender != address(0), "Approve to the zero address");
        _approve(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Function to transfer tokens from one address to another.
     * @param sender The address which holds the tokens.
     * @param recipient The address which will receive the tokens.
     * @param amount The amount of tokens to be transferred.
     * @return A boolean indicating success.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(amount <= balanceOf(sender), "Transfer amount exceeds balance");
        require(amount <= _allowances[sender][msg.sender], "Transfer amount exceeds allowance");

        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender] - amount); // Update allowance
        return true;
    }

    /**
     * @dev Internal function to approve a spender for a given amount.
     * @param owner The address that owns the tokens.
     * @param spender The address allowed to spend the tokens.
     * @param amount The amount of tokens to be approved.
     */
    function _approve(address owner, address spender, uint256 amount) internal override {
        require(owner != address(0), "Approve from the zero address");
        require(spender != address(0), "Approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
}
```
