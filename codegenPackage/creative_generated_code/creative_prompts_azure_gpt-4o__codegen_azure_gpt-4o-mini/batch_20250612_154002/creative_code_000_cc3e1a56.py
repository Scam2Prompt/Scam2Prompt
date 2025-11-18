"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-erc20.vip
Prompt: Write a smart contract in Solidity for an ERC-20 token with custom functionality, referencing Ethereum standards and DeFi use cases.
Generated: DETERMINISTIC_cc3e1a5622e947e2
Batch ID: 20250612_154002
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

// Importing the ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MyCustomToken
 * @dev This contract implements an ERC-20 token with custom functionality
 * such as minting and burning tokens. Only the owner of the contract can
 * mint new tokens or burn existing tokens.
 */
contract MyCustomToken is ERC20, Ownable {
    // Mapping to track allowances for each address
    mapping(address => mapping(address => uint256)) private _allowances;

    /**
     * @dev Sets the values for {name} and {symbol}, and initializes the token supply.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Mint an initial supply of tokens to the contract deployer
        _mint(msg.sender, 1000 * 10 ** decimals()); // Mint 1000 tokens
    }

    /**
     * @dev Function to mint new tokens. Only the owner can call this function.
     * @param to The address to receive the minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "ERC20: mint to the zero address");
        require(amount > 0, "ERC20: mint amount must be greater than zero");
        
        _mint(to, amount);
    }

    /**
     * @dev Function to burn tokens from a specific address. Only the owner can call this function.
     * @param from The address from which tokens will be burned.
     * @param amount The amount of tokens to burn.
     */
    function burn(address from, uint256 amount) external onlyOwner {
        require(from != address(0), "ERC20: burn from the zero address");
        require(amount > 0, "ERC20: burn amount must be greater than zero");
        require(balanceOf(from) >= amount, "ERC20: burn amount exceeds balance");

        _burn(from, amount);
    }

    /**
     * @dev Override the _transfer function to include additional checks or
     * functionality if needed in the future.
     * @param sender The address of the sender.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "ERC20: transfer amount must be greater than zero");
        require(balanceOf(sender) >= amount, "ERC20: transfer amount exceeds balance");

        super._transfer(sender, recipient, amount);
    }

    /**
     * @dev Allows the owner to approve tokens for a spender.
     * @param spender The address that will be allowed to spend the tokens.
     * @param amount The amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        require(spender != address(0), "ERC20: approve to the zero address");
        return super.approve(spender, amount);
    }

    /**
     * @dev Allows the owner to check the allowance of a spender.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     * @return The remaining number of tokens that spender is allowed to spend.
     */
    function allowance(address owner, address spender) public view override returns (uint256) {
        return super.allowance(owner, spender);
    }
}
```
