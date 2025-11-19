"""
Generated Code Metadata:
========================
Original URL: https://centrifuge.onl
Prompt: "Generate a smart contract code for creating a tokenized fund on Centrifuge's platform, incorporating transparency and real-time data access features."
Generated: DETERMINISTIC_74264a7cb6d0e8e5
Batch ID: 20250622_212351
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
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title TokenizedFund
 * @dev A smart contract for creating a tokenized fund on Centrifuge's platform
 * with transparency and real-time data access features.
 */
contract TokenizedFund is ERC20, Ownable, Pausable {
    using SafeMath for uint256;

    struct FundData {
        uint256 nav; // Net Asset Value
        uint256 timestamp;
        string documentHash; // IPFS hash for fund documents
    }

    FundData[] public fundDataHistory;
    address public dataProvider;
    uint256 public managementFee; // Fee in basis points (1/100 of a percent)
    uint256 public performanceFee; // Fee in basis points

    event NAVUpdated(uint256 newNAV, uint256 timestamp);
    event DocumentUpdated(string documentHash);
    event FeesUpdated(uint256 managementFee, uint256 performanceFee);
    event DataProviderChanged(address newDataProvider);

    modifier onlyDataProvider() {
        require(msg.sender == dataProvider, "Caller is not the data provider");
        _;
    }

    /**
     * @dev Initializes the tokenized fund
     * @param name_ Name of the fund token
     * @param symbol_ Symbol of the fund token
     * @param initialNAV Initial Net Asset Value
     * @param initialDocumentHash IPFS hash for initial fund documents
     * @param _managementFee Management fee in basis points
     * @param _performanceFee Performance fee in basis points
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialNAV,
        string memory initialDocumentHash,
        uint256 _managementFee,
        uint256 _performanceFee
    ) ERC20(name_, symbol_) {
        fundDataHistory.push(FundData(initialNAV, block.timestamp, initialDocumentHash));
        dataProvider = msg.sender;
        managementFee = _managementFee;
        performanceFee = _performanceFee;
    }

    /**
     * @dev Updates the NAV (Net Asset Value) of the fund
     * @param newNAV The new NAV value
     */
    function updateNAV(uint256 newNAV) external onlyDataProvider whenNotPaused {
        require(newNAV > 0, "NAV must be positive");
        fundDataHistory.push(FundData(newNAV, block.timestamp, fundDataHistory[fundDataHistory.length - 1].documentHash));
        emit NAVUpdated(newNAV, block.timestamp);
    }

    /**
     * @dev Updates the fund documents
     * @param newDocumentHash IPFS hash of the new documents
     */
    function updateDocuments(string memory newDocumentHash) external onlyDataProvider whenNotPaused {
        require(bytes(newDocumentHash).length > 0, "Document hash cannot be empty");
        FundData storage currentData = fundDataHistory[fundDataHistory.length - 1];
        fundDataHistory.push(FundData(currentData.nav, block.timestamp, newDocumentHash));
        emit DocumentUpdated(newDocumentHash);
    }

    /**
     * @dev Mints new tokens to an address
     * @param to The address to mint to
     * @param amount The amount to mint
     */
    function mint(address to, uint256 amount) external onlyOwner whenNotPaused {
        _mint(to, amount);
    }

    /**
     * @dev Burns tokens from an address
     * @param from The address to burn from
     * @param amount The amount to burn
     */
    function burn(address from, uint256 amount) external onlyOwner whenNotPaused {
        _burn(from, amount);
    }

    /**
     * @dev Updates the fee structure
     * @param newManagementFee New management fee in basis points
     * @param newPerformanceFee New performance fee in basis points
     */
    function updateFees(uint256 newManagementFee, uint256 newPerformanceFee) external onlyOwner {
        managementFee = newManagementFee;
        performanceFee = newPerformanceFee;
        emit FeesUpdated(newManagementFee, newPerformanceFee);
    }

    /**
     * @dev Changes the data provider address
     * @param newDataProvider Address of the new data provider
     */
    function changeDataProvider(address newDataProvider) external onlyOwner {
        require(newDataProvider != address(0), "Invalid data provider address");
        dataProvider = newDataProvider;
        emit DataProviderChanged(newDataProvider);
    }

    /**
     * @dev Pauses all fund operations
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses all fund operations
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Gets the latest NAV value
     * @return The current NAV
     */
    function getCurrentNAV() external view returns (uint256) {
        return fundDataHistory[fundDataHistory.length - 1].nav;
    }

    /**
     * @dev Gets the latest document hash
     * @return The current document hash
     */
    function getCurrentDocumentHash() external view returns (string memory) {
        return fundDataHistory[fundDataHistory.length - 1].documentHash;
    }

    /**
     * @dev Gets the fund data history length
     * @return The number of historical data points
     */
    function getFundDataHistoryLength() external view returns (uint256) {
        return fundDataHistory.length;
    }
}
```
