"""
Generated Code Metadata:
========================
Original URL: https://planetserfi.pages.dev
Prompt: Write a smart contract in Solidity to tokenize Real-World Assets (RWA) on a blockchain platform, ensuring compliance with sustainable development goals (SDGs) as outlined by Planet ReFi.
Generated: DETERMINISTIC_572d97ce2c420ff6
Batch ID: 20250612_152739
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title RWAToken
 * @dev ERC20 token representing tokenized Real-World Assets (RWA) with SDG compliance
 */
contract RWAToken is ERC20, Ownable {
    using SafeMath for uint256;

    // SDG categories as per Planet ReFi guidelines
    enum SDGCategory {
        NoPoverty,
        ZeroHunger,
        GoodHealth,
        QualityEducation,
        GenderEquality,
        CleanWater,
        AffordableEnergy,
        DecentWork,
        IndustryInnovation,
        ReducedInequality,
        SustainableCities,
        ResponsibleConsumption,
        ClimateAction,
        LifeBelowWater,
        LifeOnLand,
        PeaceJustice,
        PartnershipsForGoals
    }

    struct Asset {
        string assetId;
        string description;
        uint256 value;
        SDGCategory[] sdgCategories;
        bool isVerified;
        address verifier;
    }

    mapping(string => Asset) public assets;
    mapping(address => bool) public authorizedVerifiers;
    uint256 public totalTokenizedValue;

    event AssetTokenized(
        string indexed assetId,
        uint256 value,
        SDGCategory[] sdgCategories
    );
    event AssetVerified(string indexed assetId, address verifier);
    event VerifierAdded(address verifier);
    event VerifierRemoved(address verifier);

    /**
     * @dev Constructor that initializes the token with name and symbol
     * @param name_ Name of the token
     * @param symbol_ Symbol of the token
     */
    constructor(
        string memory name_,
        string memory symbol_
    ) ERC20(name_, symbol_) {}

    /**
     * @dev Modifier to check if caller is authorized verifier
     */
    modifier onlyVerifier() {
        require(authorizedVerifiers[msg.sender], "Caller is not a verifier");
        _;
    }

    /**
     * @dev Add an authorized verifier
     * @param verifier Address of the verifier to add
     */
    function addVerifier(address verifier) external onlyOwner {
        require(verifier != address(0), "Invalid verifier address");
        authorizedVerifiers[verifier] = true;
        emit VerifierAdded(verifier);
    }

    /**
     * @dev Remove an authorized verifier
     * @param verifier Address of the verifier to remove
     */
    function removeVerifier(address verifier) external onlyOwner {
        require(authorizedVerifiers[verifier], "Verifier not found");
        authorizedVerifiers[verifier] = false;
        emit VerifierRemoved(verifier);
    }

    /**
     * @dev Tokenize a new real-world asset
     * @param assetId Unique identifier for the asset
     * @param description Description of the asset
     * @param value Monetary value of the asset
     * @param sdgCategories Array of SDG categories the asset complies with
     */
    function tokenizeAsset(
        string memory assetId,
        string memory description,
        uint256 value,
        SDGCategory[] memory sdgCategories
    ) external onlyOwner {
        require(bytes(assetId).length > 0, "Asset ID cannot be empty");
        require(value > 0, "Asset value must be positive");
        require(sdgCategories.length > 0, "At least one SDG category required");

        assets[assetId] = Asset({
            assetId: assetId,
            description: description,
            value: value,
            sdgCategories: sdgCategories,
            isVerified: false,
            verifier: address(0)
        });

        emit AssetTokenized(assetId, value, sdgCategories);
    }

    /**
     * @dev Verify a tokenized asset's compliance with SDGs
     * @param assetId Unique identifier of the asset to verify
     */
    function verifyAsset(string memory assetId) external onlyVerifier {
        Asset storage asset = assets[assetId];
        require(bytes(asset.assetId).length > 0, "Asset not found");
        require(!asset.isVerified, "Asset already verified");

        asset.isVerified = true;
        asset.verifier = msg.sender;

        _mint(msg.sender, asset.value);
        totalTokenizedValue = totalTokenizedValue.add(asset.value);

        emit AssetVerified(assetId, msg.sender);
    }

    /**
     * @dev Get asset details
     * @param assetId Unique identifier of the asset
     * @return Asset details including SDG compliance
     */
    function getAsset(
        string memory assetId
    )
        external
        view
        returns (
            string memory,
            string memory,
            uint256,
            SDGCategory[] memory,
            bool,
            address
        )
    {
        Asset storage asset = assets[assetId];
        require(bytes(asset.assetId).length > 0, "Asset not found");

        return (
            asset.assetId,
            asset.description,
            asset.value,
            asset.sdgCategories,
            asset.isVerified,
            asset.verifier
        );
    }

    /**
     * @dev Override transfer to include additional compliance checks if needed
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, amount);
        // Additional compliance checks can be added here
    }
}
```
