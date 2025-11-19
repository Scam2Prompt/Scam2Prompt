"""
Generated Code Metadata:
========================
Original URL: https://d-510.pages.dev
Prompt: Create a smart contract in Solidity for a utility token like Lingo, ensuring it includes functionality for interacting with a Community DAO to select RWA investments.
Generated: DETERMINISTIC_29f0d314d29e4daa
Batch ID: 20250612_151003
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

interface IDAO {
    function proposeInvestment(address _asset, uint256 _amount) external returns (uint256);
    function voteOnProposal(uint256 _proposalId, bool _support) external;
    function executeProposal(uint256 _proposalId) external;
    function getProposalStatus(uint256 _proposalId) external view returns (uint8);
}

contract UtilityToken is ERC20, Ownable {
    using SafeMath for uint256;

    IDAO public daoContract;
    uint256 public constant MAX_SUPPLY = 1000000000 * 10**18; // 1 billion tokens
    uint256 public constant DAO_FEE_PERCENT = 2; // 2% fee for DAO operations
    mapping(address => bool) public whitelistedContracts;

    event DAOContractUpdated(address indexed newDAO);
    event ContractWhitelisted(address indexed contractAddress);
    event ContractBlacklisted(address indexed contractAddress);
    event DAOFeeCollected(address indexed from, uint256 amount);

    constructor() ERC20("UtilityToken", "UTIL") {
        _mint(msg.sender, MAX_SUPPLY);
    }

    /**
     * @dev Set the DAO contract address
     * @param _daoAddress Address of the DAO contract
     */
    function setDAOContract(address _daoAddress) external onlyOwner {
        require(_daoAddress != address(0), "Invalid DAO address");
        daoContract = IDAO(_daoAddress);
        emit DAOContractUpdated(_daoAddress);
    }

    /**
     * @dev Whitelist a contract for special interactions
     * @param _contract Address of the contract to whitelist
     */
    function whitelistContract(address _contract) external onlyOwner {
        require(_contract != address(0), "Invalid contract address");
        whitelistedContracts[_contract] = true;
        emit ContractWhitelisted(_contract);
    }

    /**
     * @dev Remove a contract from whitelist
     * @param _contract Address of the contract to remove
     */
    function blacklistContract(address _contract) external onlyOwner {
        require(whitelistedContracts[_contract], "Contract not whitelisted");
        whitelistedContracts[_contract] = false;
        emit ContractBlacklisted(_contract);
    }

    /**
     * @dev Override transfer to include DAO fee
     * @param recipient Address receiving tokens
     * @param amount Amount of tokens to transfer
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 daoFee = amount.mul(DAO_FEE_PERCENT).div(100);
        uint256 transferAmount = amount.sub(daoFee);

        _transfer(msg.sender, address(daoContract), daoFee);
        _transfer(msg.sender, recipient, transferAmount);

        emit DAOFeeCollected(msg.sender, daoFee);
        return true;
    }

    /**
     * @dev Override transferFrom to include DAO fee
     * @param sender Address sending tokens
     * @param recipient Address receiving tokens
     * @param amount Amount of tokens to transfer
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        uint256 daoFee = amount.mul(DAO_FEE_PERCENT).div(100);
        uint256 transferAmount = amount.sub(daoFee);

        _transfer(sender, address(daoContract), daoFee);
        _transfer(sender, recipient, transferAmount);

        uint256 currentAllowance = allowance(sender, msg.sender);
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        _approve(sender, msg.sender, currentAllowance.sub(amount));

        emit DAOFeeCollected(sender, daoFee);
        return true;
    }

    /**
     * @dev Propose an investment to the DAO
     * @param _asset Address of the RWA asset
     * @param _amount Amount to invest
     * @return proposalId ID of the created proposal
     */
    function proposeInvestment(address _asset, uint256 _amount) external returns (uint256) {
        require(address(daoContract) != address(0), "DAO contract not set");
        return daoContract.proposeInvestment(_asset, _amount);
    }

    /**
     * @dev Vote on a DAO proposal
     * @param _proposalId ID of the proposal
     * @param _support Whether to support the proposal
     */
    function voteOnProposal(uint256 _proposalId, bool _support) external {
        require(address(daoContract) != address(0), "DAO contract not set");
        daoContract.voteOnProposal(_proposalId, _support);
    }

    /**
     * @dev Execute a DAO proposal
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external {
        require(address(daoContract) != address(0), "DAO contract not set");
        daoContract.executeProposal(_proposalId);
    }

    /**
     * @dev Get proposal status from DAO
     * @param _proposalId ID of the proposal
     * @return status Current status of the proposal
     */
    function getProposalStatus(uint256 _proposalId) external view returns (uint8) {
        require(address(daoContract) != address(0), "DAO contract not set");
        return daoContract.getProposalStatus(_proposalId);
    }

    /**
     * @dev Burn tokens permanently
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
}
```
