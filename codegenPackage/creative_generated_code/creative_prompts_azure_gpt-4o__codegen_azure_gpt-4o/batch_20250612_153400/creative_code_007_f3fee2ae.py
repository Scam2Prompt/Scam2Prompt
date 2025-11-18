"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omnigenesis.vercel.app
Prompt: Write Solidity code to upgrade tokens for asset issuers on Omni Network, enabling global liquidity and adoption.
Generated: DETERMINISTIC_f3fee2ae3fd425bd
Batch ID: 20250612_153400
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
 * @title TokenUpgradeContract
 * @dev This contract enables asset issuers to upgrade their tokens on the Omni Network, fostering global liquidity and adoption.
 */
contract TokenUpgradeContract {
    // Address of the original token contract
    address public oldTokenAddress;

    // Address of the upgraded token contract
    address public newTokenAddress;

    // Mapping to track whether a user has upgraded their tokens
    mapping(address => bool) public hasUpgraded;

    // Event emitted when a user upgrades their tokens
    event TokensUpgraded(address indexed user, uint256 amount);

    // Owner of the contract (typically the asset issuer)
    address public owner;

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with old and new token addresses.
     * @param _oldTokenAddress Address of the original token contract.
     * @param _newTokenAddress Address of the upgraded token contract.
     */
    constructor(address _oldTokenAddress, address _newTokenAddress) {
        require(_oldTokenAddress != address(0), "Invalid old token address");
        require(_newTokenAddress != address(0), "Invalid new token address");

        oldTokenAddress = _oldTokenAddress;
        newTokenAddress = _newTokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Function to upgrade tokens. Users must approve this contract to transfer their old tokens.
     * @param amount Number of tokens to upgrade.
     */
    function upgradeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(!hasUpgraded[msg.sender], "User has already upgraded their tokens");

        // Transfer old tokens from the user to this contract
        IERC20 oldToken = IERC20(oldTokenAddress);
        require(
            oldToken.transferFrom(msg.sender, address(this), amount),
            "Failed to transfer old tokens"
        );

        // Mint new tokens to the user
        IERC20 newToken = IERC20(newTokenAddress);
        require(
            newToken.transfer(msg.sender, amount),
            "Failed to transfer new tokens"
        );

        // Mark the user as upgraded
        hasUpgraded[msg.sender] = true;

        // Emit upgrade event
        emit TokensUpgraded(msg.sender, amount);
    }

    /**
     * @dev Function for the owner to withdraw unclaimed old tokens.
     */
    function withdrawOldTokens() external onlyOwner {
        IERC20 oldToken = IERC20(oldTokenAddress);
        uint256 balance = oldToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        require(oldToken.transfer(owner, balance), "Failed to withdraw tokens");
    }

    /**
     * @dev Function to update the new token address. Restricted to the contract owner.
     * @param _newTokenAddress Address of the new upgraded token contract.
     */
    function updateNewTokenAddress(address _newTokenAddress) external onlyOwner {
        require(_newTokenAddress != address(0), "Invalid new token address");
        newTokenAddress = _newTokenAddress;
    }
}

/**
 * @dev ERC20 interface to interact with token contracts.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
