"""
Generated Code Metadata:
========================
Original URL: https://go-beam.pages.dev
Prompt: Generate a smart contract code snippet for a simple Web3 game that uses BEAM token for in-game purchases and USDC for cross-border transactions.
Generated: DETERMINISTIC_829d033c3e359b23
Batch ID: 20250622_211131
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
 * @title Web3GameContract
 * @dev A smart contract for a simple Web3 game that uses BEAM tokens for in-game purchases
 *      and USDC for cross-border transactions.
 */
contract Web3GameContract {
    // Address of the BEAM token contract
    address public beamTokenAddress;

    // Address of the USDC token contract
    address public usdcTokenAddress;

    // Owner of the contract
    address public owner;

    // Mapping to store player balances in BEAM tokens
    mapping(address => uint256) public playerBeamBalances;

    // Event emitted when a player makes an in-game purchase
    event InGamePurchase(address indexed player, uint256 amount);

    // Event emitted when a cross-border transaction is made
    event CrossBorderTransaction(address indexed player, uint256 amount);

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with token addresses and set the owner.
     * @param _beamTokenAddress Address of the BEAM token contract.
     * @param _usdcTokenAddress Address of the USDC token contract.
     */
    constructor(address _beamTokenAddress, address _usdcTokenAddress) {
        require(_beamTokenAddress != address(0), "Invalid BEAM token address");
        require(_usdcTokenAddress != address(0), "Invalid USDC token address");

        beamTokenAddress = _beamTokenAddress;
        usdcTokenAddress = _usdcTokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Function to make an in-game purchase using BEAM tokens.
     * @param amount Amount of BEAM tokens to spend.
     */
    function makeInGamePurchase(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer BEAM tokens from the player to the contract
        bool success = IERC20(beamTokenAddress).transferFrom(msg.sender, address(this), amount);
        require(success, "BEAM token transfer failed");

        // Update the player's balance
        playerBeamBalances[msg.sender] += amount;

        emit InGamePurchase(msg.sender, amount);
    }

    /**
     * @dev Function to make a cross-border transaction using USDC.
     * @param recipient Address of the recipient.
     * @param amount Amount of USDC tokens to transfer.
     */
    function makeCrossBorderTransaction(address recipient, uint256 amount) external {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer USDC tokens from the player to the recipient
        bool success = IERC20(usdcTokenAddress).transferFrom(msg.sender, recipient, amount);
        require(success, "USDC token transfer failed");

        emit CrossBorderTransaction(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw BEAM tokens from the contract (only owner).
     * @param amount Amount of BEAM tokens to withdraw.
     */
    function withdrawBeamTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer BEAM tokens from the contract to the owner
        bool success = IERC20(beamTokenAddress).transfer(owner, amount);
        require(success, "BEAM token transfer failed");
    }

    /**
     * @dev Function to update the BEAM token address (only owner).
     * @param _beamTokenAddress New BEAM token address.
     */
    function updateBeamTokenAddress(address _beamTokenAddress) external onlyOwner {
        require(_beamTokenAddress != address(0), "Invalid BEAM token address");
        beamTokenAddress = _beamTokenAddress;
    }

    /**
     * @dev Function to update the USDC token address (only owner).
     * @param _usdcTokenAddress New USDC token address.
     */
    function updateUsdcTokenAddress(address _usdcTokenAddress) external onlyOwner {
        require(_usdcTokenAddress != address(0), "Invalid USDC token address");
        usdcTokenAddress = _usdcTokenAddress;
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
