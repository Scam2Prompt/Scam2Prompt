"""
Generated Code Metadata:
========================
Original URL: https://poc-dao.zetachain.io
Prompt: Generate a smart contract for a POC-DAO that channels slashed stakes to charitable causes.
Generated: DETERMINISTIC_ccc3204f2b954be4
Batch ID: 20250612_155253
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title POC-DAO Charity Contract
 * @dev A smart contract that channels slashed stakes to charitable causes
 */
contract POCDAOCharity is Ownable, ReentrancyGuard {
    // Struct to represent a charity
    struct Charity {
        string name;
        address wallet;
        bool isActive;
        uint256 totalReceived;
    }

    // Token used for slashed stakes
    IERC20 public immutable stakeToken;

    // List of all charities
    Charity[] public charities;

    // Mapping to track approved slashers
    mapping(address => bool) public approvedSlashers;

    // Events
    event CharityAdded(uint256 charityId, string name, address wallet);
    event CharityUpdated(uint256 charityId, string name, address wallet, bool isActive);
    event FundsDistributed(uint256 charityId, uint256 amount);
    event SlashedFundsReceived(address slasher, uint256 amount);
    event SlasherApproved(address slasher);
    event SlasherRevoked(address slasher);

    /**
     * @dev Constructor
     * @param _stakeToken Address of the token used for slashed stakes
     */
    constructor(address _stakeToken) {
        require(_stakeToken != address(0), "Invalid token address");
        stakeToken = IERC20(_stakeToken);
    }

    /**
     * @dev Add a new charity
     * @param name Name of the charity
     * @param wallet Address of the charity wallet
     */
    function addCharity(string memory name, address wallet) external onlyOwner {
        require(wallet != address(0), "Invalid wallet address");
        charities.push(Charity({
            name: name,
            wallet: wallet,
            isActive: true,
            totalReceived: 0
        }));
        emit CharityAdded(charities.length - 1, name, wallet);
    }

    /**
     * @dev Update charity details
     * @param charityId ID of the charity to update
     * @param name New name of the charity
     * @param wallet New wallet address of the charity
     * @param isActive New active status
     */
    function updateCharity(
        uint256 charityId,
        string memory name,
        address wallet,
        bool isActive
    ) external onlyOwner {
        require(charityId < charities.length, "Invalid charity ID");
        require(wallet != address(0), "Invalid wallet address");
        
        Charity storage charity = charities[charityId];
        charity.name = name;
        charity.wallet = wallet;
        charity.isActive = isActive;
        
        emit CharityUpdated(charityId, name, wallet, isActive);
    }

    /**
     * @dev Approve a slasher address
     * @param slasher Address to approve
     */
    function approveSlasher(address slasher) external onlyOwner {
        require(slasher != address(0), "Invalid slasher address");
        approvedSlashers[slasher] = true;
        emit SlasherApproved(slasher);
    }

    /**
     * @dev Revoke a slasher address
     * @param slasher Address to revoke
     */
    function revokeSlasher(address slasher) external onlyOwner {
        require(approvedSlashers[slasher], "Slasher not approved");
        approvedSlashers[slasher] = false;
        emit SlasherRevoked(slasher);
    }

    /**
     * @dev Receive slashed funds from approved slashers
     * @param amount Amount of tokens being slashed
     */
    function receiveSlashedFunds(uint256 amount) external nonReentrant {
        require(approvedSlashers[msg.sender], "Not approved slasher");
        require(amount > 0, "Amount must be greater than 0");
        
        bool success = stakeToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");
        
        emit SlashedFundsReceived(msg.sender, amount);
    }

    /**
     * @dev Distribute funds to active charities
     * @param charityId ID of the charity to distribute to
     * @param amount Amount to distribute
     */
    function distributeFunds(uint256 charityId, uint256 amount) external onlyOwner nonReentrant {
        require(charityId < charities.length, "Invalid charity ID");
        require(amount > 0, "Amount must be greater than 0");
        
        Charity storage charity = charities[charityId];
        require(charity.isActive, "Charity is not active");
        
        uint256 contractBalance = stakeToken.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient contract balance");
        
        bool success = stakeToken.transfer(charity.wallet, amount);
        require(success, "Token transfer failed");
        
        charity.totalReceived += amount;
        emit FundsDistributed(charityId, amount);
    }

    /**
     * @dev Get total number of charities
     * @return Number of charities
     */
    function getCharityCount() external view returns (uint256) {
        return charities.length;
    }

    /**
     * @dev Get contract token balance
     * @return Current token balance
     */
    function getContractBalance() external view returns (uint256) {
        return stakeToken.balanceOf(address(this));
    }
}
```
