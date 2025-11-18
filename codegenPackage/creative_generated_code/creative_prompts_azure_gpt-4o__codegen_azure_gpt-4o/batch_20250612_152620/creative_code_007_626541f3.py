"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-31k.pages.dev
Prompt: Write code in Solidity to implement the burning of non-transferable ERC-20 mining credits in exchange for cloud mining power, as outlined in the Bitcoin Minetrix whitepaper.
Generated: DETERMINISTIC_626541f34a897aeb
Batch ID: 20250612_152620
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
 * @title MiningCreditsToken
 * @notice Non-transferable ERC-20 token for mining credits.
 * Users can burn these tokens in exchange for cloud mining power.
 */
contract MiningCreditsToken {
    // Token metadata
    string public constant name = "MiningCreditsToken";
    string public constant symbol = "MCT";
    uint8 public constant decimals = 18;

    // Total supply of tokens
    uint256 public totalSupply;

    // Mapping to track balances of each address
    mapping(address => uint256) private balances;

    // Address of the owner (contract deployer)
    address public owner;

    // Event emitted when tokens are burned
    event TokensBurned(address indexed user, uint256 amount, uint256 miningPowerGranted);

    // Modifier to restrict functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Modifier to check non-transferability
    modifier nonTransferable() {
        revert("Token is non-transferable");
        _;
    }

    /**
     * @dev Constructor sets the initial owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Mint new mining credits to a user.
     * @param recipient The address of the user to receive the tokens.
     * @param amount The amount of tokens to mint (in wei).
     *
     * Only callable by the contract owner.
     */
    function mint(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        balances[recipient] += amount;
        totalSupply += amount;
    }

    /**
     * @dev Burn mining credits in exchange for cloud mining power.
     * @param amount The amount of tokens to burn (in wei).
     *
     * Emits a `TokensBurned` event with the mining power granted.
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance to burn");

        // Calculate mining power based on the burning algorithm.
        uint256 miningPowerGranted = calculateMiningPower(amount);

        // Reduce user's balance and total supply
        balances[msg.sender] -= amount;
        totalSupply -= amount;

        // Emit the TokensBurned event
        emit TokensBurned(msg.sender, amount, miningPowerGranted);
    }

    /**
     * @dev Calculate mining power from burned tokens.
     * @param burnedAmount The amount of tokens burned.
     * @return miningPower The calculated mining power.
     *
     * This function can implement any custom algorithm for mapping burned tokens to mining power.
     */
    function calculateMiningPower(uint256 burnedAmount) public pure returns (uint256 miningPower) {
        // Example: Simple 1-to-1 mapping (customize as per the whitepaper)
        return burnedAmount;
    }

    /**
     * @dev Get the balance of a specific address.
     * @param account The address to query the balance of.
     * @return The balance of the given address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Prevent token transfers. Non-transferable tokens behavior.
     */
    function transfer(address, uint256) external nonTransferable returns (bool) {
        return false; // Function disabled by nonTransferable modifier
    }

    function transferFrom(address, address, uint256) external nonTransferable returns (bool) {
        return false; // Function disabled by nonTransferable modifier
    }
}
```
