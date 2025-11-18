"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeig2qxervlifeg5gur3hrsbgo6hrco4esjxaz2r6nixoqkc6nhhjbe.ipfs.dweb.link
Prompt: Write a Solidity contract to support exotic options trading as part of the Pencils Protocol Vaults yield strategies.
Generated: DETERMINISTIC_02a8f268dc6aa932
Batch ID: 20250612_150228
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
 * @title Pencils Protocol Exotic Options Vault
 * @notice This contract supports exotic options trading as part of
 *         the Pencils Protocol Vaults yield strategies.
 * @author [Your Name]
 */
contract ExoticOptionsVault {
    // Events
    event OptionCreated(
        uint256 indexed optionId,
        address indexed creator,
        string underlyingAsset,
        uint256 strikePrice,
        uint256 expirationTimestamp,
        uint256 premium
    );
    event OptionExercised(uint256 indexed optionId, address indexed exerciser);
    event OptionExpired(uint256 indexed optionId);

    // Struct for an option
    struct Option {
        address creator; // Address of the option creator
        string underlyingAsset; // The asset being traded
        uint256 strikePrice; // Strike price of the option
        uint256 expirationTimestamp; // Expiration timestamp of the option
        uint256 premium; // Premium paid for the option
        bool isExercised; // Flag to check if the option is exercised
        bool isExpired; // Flag to check if the option is expired
    }

    // State variables
    mapping(uint256 => Option) public options; // Mapping of option ID to Option
    uint256 public nextOptionId; // Incremental ID for options
    address public vaultOwner; // Owner of the vault

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == vaultOwner, "Only owner can perform this action");
        _;
    }

    modifier onlyOptionCreator(uint256 optionId) {
        require(
            msg.sender == options[optionId].creator,
            "Only option creator can perform this action"
        );
        _;
    }

    // Constructor
    constructor() {
        vaultOwner = msg.sender; // Set the vault owner initially
    }

    /**
     * @notice Create a new exotic option
     * @param underlyingAsset The asset being traded
     * @param strikePrice The strike price of the option
     * @param expirationTimestamp The expiration timestamp of the option
     * @param premium The premium for the option
     */
    function createOption(
        string memory underlyingAsset,
        uint256 strikePrice,
        uint256 expirationTimestamp,
        uint256 premium
    ) external returns (uint256) {
        require(
            expirationTimestamp > block.timestamp,
            "Expiration must be in the future"
        );

        uint256 optionId = nextOptionId++;
        options[optionId] = Option({
            creator: msg.sender,
            underlyingAsset: underlyingAsset,
            strikePrice: strikePrice,
            expirationTimestamp: expirationTimestamp,
            premium: premium,
            isExercised: false,
            isExpired: false
        });

        emit OptionCreated(
            optionId,
            msg.sender,
            underlyingAsset,
            strikePrice,
            expirationTimestamp,
            premium
        );

        return optionId;
    }

    /**
     * @notice Exercise an exotic option
     * @param optionId The ID of the option to exercise
     */
    function exerciseOption(uint256 optionId) external onlyOptionCreator(optionId) {
        Option storage option = options[optionId];

        require(!option.isExercised, "Option already exercised");
        require(!option.isExpired, "Option already expired");
        require(
            block.timestamp <= option.expirationTimestamp,
            "Option has expired"
        );

        option.isExercised = true;

        emit OptionExercised(optionId, msg.sender);
    }

    /**
     * @notice Expire an exotic option (can be called by anyone after expiration)
     * @param optionId The ID of the option to expire
     */
    function expireOption(uint256 optionId) external {
        Option storage option = options[optionId];

        require(!option.isExpired, "Option already expired");
        require(
            block.timestamp > option.expirationTimestamp,
            "Option has not expired yet"
        );

        option.isExpired = true;

        emit OptionExpired(optionId);
    }

    /**
     * @notice Get details of an option
     * @param optionId The ID of the option to fetch details for
     * @return Option struct containing the option details
     */
    function getOptionDetails(uint256 optionId)
        external
        view
        returns (Option memory)
    {
        return options[optionId];
    }

    /**
     * @notice Change the vault owner
     * @param newOwner The new owner of the vault
     */
    function changeVaultOwner(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        vaultOwner = newOwner;
    }
}
```
