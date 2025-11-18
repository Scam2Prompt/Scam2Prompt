"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rtt23423.pages.dev
Prompt: Write code for managing treasury assets in a DeFi protocol, including tokenized treasuries and stablecoins, as outlined by the Ondo Foundation.
Generated: DETERMINISTIC_db05a2be2f567f06
Batch ID: 20250612_152000
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
 * @title TreasuryManagement
 * @dev A smart contract for managing treasury assets in a DeFi protocol, including tokenized treasuries and stablecoins.
 */
contract TreasuryManagement {
    // Struct to represent a treasury asset
    struct TreasuryAsset {
        string name; // Name of the tokenized treasury asset
        address tokenAddress; // ERC20 token address
        uint256 balance; // Current balance of the asset in the treasury
    }

    // Mapping to store treasury assets by ID
    mapping(uint256 => TreasuryAsset) public treasuryAssets;

    // Counter for treasury asset IDs
    uint256 private assetCounter;

    // Mapping to store stablecoin balances
    mapping(address => uint256) public stablecoinBalances;

    // Address of the owner of the contract
    address public owner;

    // Events
    event AssetAdded(uint256 indexed assetId, string name, address tokenAddress);
    event AssetUpdated(uint256 indexed assetId, uint256 newBalance);
    event StablecoinDeposited(address indexed stablecoinAddress, uint256 amount);
    event StablecoinWithdrawn(address indexed stablecoinAddress, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Adds a new treasury asset to the management system.
     * @param name The name of the asset.
     * @param tokenAddress The ERC20 token address of the asset.
     */
    function addTreasuryAsset(string memory name, address tokenAddress) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");

        TreasuryAsset memory newAsset = TreasuryAsset({
            name: name,
            tokenAddress: tokenAddress,
            balance: 0
        });

        treasuryAssets[assetCounter] = newAsset;
        emit AssetAdded(assetCounter, name, tokenAddress);

        assetCounter++;
    }

    /**
     * @dev Updates the balance of a specific treasury asset.
     * @param assetId The ID of the asset to update.
     * @param newBalance The new balance of the asset.
     */
    function updateTreasuryAssetBalance(uint256 assetId, uint256 newBalance) external onlyOwner {
        require(assetId < assetCounter, "Asset ID does not exist");

        treasuryAssets[assetId].balance = newBalance;
        emit AssetUpdated(assetId, newBalance);
    }

    /**
     * @dev Deposits stablecoins into the treasury.
     * @param stablecoinAddress The address of the stablecoin being deposited.
     * @param amount The amount of stablecoins to deposit.
     */
    function depositStablecoin(address stablecoinAddress, uint256 amount) external {
        require(stablecoinAddress != address(0), "Invalid stablecoin address");
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer the stablecoin from the sender to the contract
        bool success = IERC20(stablecoinAddress).transferFrom(msg.sender, address(this), amount);
        require(success, "Stablecoin transfer failed");

        stablecoinBalances[stablecoinAddress] += amount;
        emit StablecoinDeposited(stablecoinAddress, amount);
    }

    /**
     * @dev Withdraws stablecoins from the treasury.
     * @param stablecoinAddress The address of the stablecoin being withdrawn.
     * @param amount The amount of stablecoins to withdraw.
     */
    function withdrawStablecoin(address stablecoinAddress, uint256 amount) external onlyOwner {
        require(stablecoinAddress != address(0), "Invalid stablecoin address");
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(stablecoinBalances[stablecoinAddress] >= amount, "Insufficient balance");

        // Transfer the stablecoin from the contract to the owner
        bool success = IERC20(stablecoinAddress).transfer(owner, amount);
        require(success, "Stablecoin transfer failed");

        stablecoinBalances[stablecoinAddress] -= amount;
        emit StablecoinWithdrawn(stablecoinAddress, amount);
    }

    /**
     * @dev Gets the details of a specific treasury asset.
     * @param assetId The ID of the asset.
     * @return name The name of the asset.
     * @return tokenAddress The ERC20 token address of the asset.
     * @return balance The current balance of the asset.
     */
    function getTreasuryAsset(uint256 assetId)
        external
        view
        returns (string memory name, address tokenAddress, uint256 balance)
    {
        require(assetId < assetCounter, "Asset ID does not exist");

        TreasuryAsset memory asset = treasuryAssets[assetId];
        return (asset.name, asset.tokenAddress, asset.balance);
    }
}

/**
 * @dev Interface for ERC20 tokens used for stablecoins.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
