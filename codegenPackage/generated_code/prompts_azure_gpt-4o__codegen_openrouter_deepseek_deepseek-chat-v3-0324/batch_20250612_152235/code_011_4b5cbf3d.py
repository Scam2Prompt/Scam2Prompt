"""
Generated Code Metadata:
========================
Original URL: https://lopecoin-presale.pages.dev
Prompt: Write a Solidity contract for distributing tokens based on ecosystem allocation percentages (e.g., 30% for ecosystem, 10% for airdrops), as outlined in LopeCoin's tokenomics.
Generated: DETERMINISTIC_4b5cbf3dd8d8b65a
Batch ID: 20250612_152235
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract LopeCoinDistribution is Ownable {
    using SafeMath for uint256;

    IERC20 public token;

    // Allocation percentages (in basis points, where 10000 = 100%)
    uint256 public constant ECOSYSTEM_ALLOCATION = 3000; // 30%
    uint256 public constant AIRDROP_ALLOCATION = 1000;   // 10%
    uint256 public constant TEAM_ALLOCATION = 1500;      // 15%
    uint256 public constant ADVISORS_ALLOCATION = 500;   // 5%
    uint256 public constant RESERVES_ALLOCATION = 4000;  // 40%

    // Total allocations must sum to 10000 (100%)
    uint256 public constant TOTAL_ALLOCATION = 10000;

    // Addresses for each allocation
    address public ecosystemWallet;
    address public airdropWallet;
    address public teamWallet;
    address public advisorsWallet;
    address public reservesWallet;

    // Track distributed amounts
    uint256 public ecosystemDistributed;
    uint256 public airdropDistributed;
    uint256 public teamDistributed;
    uint256 public advisorsDistributed;
    uint256 public reservesDistributed;

    // Events
    event TokensDistributed(
        address indexed wallet,
        uint256 amount,
        string allocationType
    );

    constructor(
        address _tokenAddress,
        address _ecosystemWallet,
        address _airdropWallet,
        address _teamWallet,
        address _advisorsWallet,
        address _reservesWallet
    ) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        require(_ecosystemWallet != address(0), "Ecosystem wallet cannot be zero");
        require(_airdropWallet != address(0), "Airdrop wallet cannot be zero");
        require(_teamWallet != address(0), "Team wallet cannot be zero");
        require(_advisorsWallet != address(0), "Advisors wallet cannot be zero");
        require(_reservesWallet != address(0), "Reserves wallet cannot be zero");

        token = IERC20(_tokenAddress);
        ecosystemWallet = _ecosystemWallet;
        airdropWallet = _airdropWallet;
        teamWallet = _teamWallet;
        advisorsWallet = _advisorsWallet;
        reservesWallet = _reservesWallet;
    }

    /**
     * @dev Distribute tokens based on allocation percentages
     * @param totalSupply The total token supply to calculate allocations from
     */
    function distributeTokens(uint256 totalSupply) external onlyOwner {
        require(totalSupply > 0, "Total supply must be greater than zero");

        uint256 ecosystemAmount = totalSupply.mul(ECOSYSTEM_ALLOCATION).div(TOTAL_ALLOCATION);
        uint256 airdropAmount = totalSupply.mul(AIRDROP_ALLOCATION).div(TOTAL_ALLOCATION);
        uint256 teamAmount = totalSupply.mul(TEAM_ALLOCATION).div(TOTAL_ALLOCATION);
        uint256 advisorsAmount = totalSupply.mul(ADVISORS_ALLOCATION).div(TOTAL_ALLOCATION);
        uint256 reservesAmount = totalSupply.mul(RESERVES_ALLOCATION).div(TOTAL_ALLOCATION);

        _distribute(ecosystemWallet, ecosystemAmount, "Ecosystem");
        _distribute(airdropWallet, airdropAmount, "Airdrop");
        _distribute(teamWallet, teamAmount, "Team");
        _distribute(advisorsWallet, advisorsAmount, "Advisors");
        _distribute(reservesWallet, reservesAmount, "Reserves");
    }

    /**
     * @dev Internal function to handle token distribution
     */
    function _distribute(address wallet, uint256 amount, string memory allocationType) internal {
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        bool success = token.transfer(wallet, amount);
        require(success, "Token transfer failed");

        if (keccak256(bytes(allocationType)) == keccak256(bytes("Ecosystem"))) {
            ecosystemDistributed = ecosystemDistributed.add(amount);
        } else if (keccak256(bytes(allocationType)) == keccak256(bytes("Airdrop"))) {
            airdropDistributed = airdropDistributed.add(amount);
        } else if (keccak256(bytes(allocationType)) == keccak256(bytes("Team"))) {
            teamDistributed = teamDistributed.add(amount);
        } else if (keccak256(bytes(allocationType)) == keccak256(bytes("Advisors"))) {
            advisorsDistributed = advisorsDistributed.add(amount);
        } else if (keccak256(bytes(allocationType)) == keccak256(bytes("Reserves"))) {
            reservesDistributed = reservesDistributed.add(amount);
        }

        emit TokensDistributed(wallet, amount, allocationType);
    }

    /**
     * @dev Update wallet addresses (onlyOwner)
     */
    function updateEcosystemWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "New wallet cannot be zero");
        ecosystemWallet = _newWallet;
    }

    function updateAirdropWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "New wallet cannot be zero");
        airdropWallet = _newWallet;
    }

    function updateTeamWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "New wallet cannot be zero");
        teamWallet = _newWallet;
    }

    function updateAdvisorsWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "New wallet cannot be zero");
        advisorsWallet = _newWallet;
    }

    function updateReservesWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "New wallet cannot be zero");
        reservesWallet = _newWallet;
    }

    /**
     * @dev Recover any ERC20 tokens sent to this contract by mistake
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(token), "Cannot recover the main token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
