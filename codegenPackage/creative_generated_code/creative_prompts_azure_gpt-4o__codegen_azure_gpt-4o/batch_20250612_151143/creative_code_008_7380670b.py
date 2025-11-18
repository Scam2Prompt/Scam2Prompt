"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buy-dogepreneur.pages.dev
Prompt: Create a Solidity-based smart contract for a fair launch presale model, similar to DogePreneur's approach, ensuring tokens are airdropped to contributors' wallets at launch.
Generated: DETERMINISTIC_7380670b8700293d
Batch ID: 20250612_151143
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
 * @title FairLaunchPresale
 * @dev A smart contract for managing a fair launch presale model with automatic token airdrops.
 */
contract FairLaunchPresale {
    // State variables
    address public owner; // Owner of the contract
    address public tokenAddress; // Address of the token to be distributed
    uint256 public presaleEndTime; // Timestamp when the presale ends
    uint256 public totalContributed; // Total amount of ETH contributed
    bool public tokensAirdropped; // Flag indicating if tokens have been airdropped
    uint256 public tokenRatePerEth; // Number of tokens per ETH contributed

    mapping(address => uint256) public contributions; // Tracks contributions by address
    address[] private contributors; // List of all contributors

    // Events
    event ContributionReceived(address indexed contributor, uint256 amount);
    event TokensAirdropped(uint256 totalTokensDistributed);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier presaleActive() {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        _;
    }

    modifier presaleEnded() {
        require(block.timestamp >= presaleEndTime, "Presale is still active");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _tokenAddress Address of the token to be distributed.
     * @param _presaleDuration Duration of the presale in seconds.
     * @param _tokenRatePerEth Number of tokens per ETH contributed.
     */
    constructor(address _tokenAddress, uint256 _presaleDuration, uint256 _tokenRatePerEth) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_presaleDuration > 0, "Presale duration must be greater than zero");
        require(_tokenRatePerEth > 0, "Token rate per ETH must be greater than zero");

        owner = msg.sender;
        tokenAddress = _tokenAddress;
        presaleEndTime = block.timestamp + _presaleDuration;
        tokenRatePerEth = _tokenRatePerEth;
    }

    /**
     * @dev Function to contribute ETH during the presale.
     * @notice Contributors can call this function to participate in the presale.
     */
    function contribute() external payable presaleActive {
        require(msg.value > 0, "Contribution must be greater than zero");

        if (contributions[msg.sender] == 0) {
            contributors.push(msg.sender);
        }

        contributions[msg.sender] += msg.value;
        totalContributed += msg.value;

        emit ContributionReceived(msg.sender, msg.value);
    }

    /**
     * @dev Function to airdrop tokens to contributors after the presale ends.
     * @notice Only the owner can call this function once the presale has ended.
     */
    function airdropTokens() external onlyOwner presaleEnded {
        require(!tokensAirdropped, "Tokens have already been airdropped");

        uint256 totalTokensToDistribute = totalContributed * tokenRatePerEth;

        for (uint256 i = 0; i < contributors.length; i++) {
            address contributor = contributors[i];
            uint256 contributorEth = contributions[contributor];
            uint256 tokensToAirdrop = contributorEth * tokenRatePerEth;

            require(
                IERC20(tokenAddress).transfer(contributor, tokensToAirdrop),
                "Token transfer failed"
            );
        }

        tokensAirdropped = true;
        emit TokensAirdropped(totalTokensToDistribute);
    }

    /**
     * @dev Function to withdraw any remaining ETH in the contract after the presale.
     * @notice Only the owner can call this function once the presale has ended.
     */
    function withdrawETH() external onlyOwner presaleEnded {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");

        payable(owner).transfer(balance);
    }

    /**
     * @dev Function to set the token rate per ETH.
     * @notice Only the owner can call this function.
     * @param _tokenRatePerEth New token rate per ETH.
     */
    function setTokenRate(uint256 _tokenRatePerEth) external onlyOwner presaleActive {
        require(_tokenRatePerEth > 0, "Token rate must be greater than zero");
        tokenRatePerEth = _tokenRatePerEth;
    }

    // Fallback function to accept ETH
    receive() external payable {
        contribute();
    }
}

/**
 * @dev Interface for ERC20 token interactions.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
