"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://graph-protocol.vercel.app
Prompt: Write a script in JavaScript to interact with a smart contract for a random winner selection game, ensuring compatibility with the Graph Protocol.
Generated: DETERMINISTIC_5dd3d7a8bb4b6ae4
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from "ethers";
import { useEffect, useState } from "react";
import { gql, useQuery } from "@apollo/client";

// Smart contract ABI and address
const CONTRACT_ABI = [
    // Replace with the actual ABI of your smart contract
    "function enterGame() public payable",
    "function selectWinner() public",
    "event WinnerSelected(address winner)"
];
const CONTRACT_ADDRESS = "0xYourContractAddressHere"; // Replace with your contract's address

// GraphQL query to get the latest winner from The Graph
const GET_LATEST_WINNER = gql`
    query {
        winners(first: 1, orderBy: timestamp, orderDirection: desc) {
            id
            winner
            timestamp
        }
    }
`;

// Main component
const RandomWinnerGame = () => {
    const [provider, setProvider] = useState(null);
    const [contract, setContract] = useState(null);
    const [error, setError] = useState(null);
    const { data, loading, error: queryError } = useQuery(GET_LATEST_WINNER);

    // Initialize Ethereum provider and contract
    useEffect(() => {
        const initProvider = async () => {
            try {
                // Connect to MetaMask or any Ethereum wallet
                const { ethereum } = window;
                if (!ethereum) throw new Error("Ethereum provider not found");

                const newProvider = new ethers.providers.Web3Provider(ethereum);
                const newContract = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, newProvider);
                
                setProvider(newProvider);
                setContract(newContract);
            } catch (err) {
                setError(err.message);
                console.error("Error initializing provider:", err);
            }
        };

        initProvider();
    }, []);

    // Function to enter the game
    const enterGame = async () => {
        if (!contract) return;

        try {
            const signer = provider.getSigner();
            const tx = await contract.connect(signer).enterGame({ value: ethers.utils.parseEther("0.01") });
            await tx.wait();
            console.log("Successfully entered the game:", tx);
        } catch (err) {
            setError(err.message);
            console.error("Error entering game:", err);
        }
    };

    // Function to select a winner
    const selectWinner = async () => {
        if (!contract) return;

        try {
            const signer = provider.getSigner();
            const tx = await contract.connect(signer).selectWinner();
            await tx.wait();
            console.log("Winner selected:", tx);
        } catch (err) {
            setError(err.message);
            console.error("Error selecting winner:", err);
        }
    };

    // Display content
    return (
        <div>
            <h1>Random Winner Selection Game</h1>
            {error && <p style={{ color: "red" }}>{error}</p>}
            {loading && <p>Loading latest winner...</p>}
            {queryError && <p style={{ color: "red" }}>{queryError.message}</p>}
            {data && (
                <div>
                    <h2>Latest Winner:</h2>
                    <p>Winner Address: {data.winners[0].winner}</p>
                    <p>Timestamp: {new Date(data.winners[0].timestamp * 1000).toLocaleString()}</p>
                </div>
            )}
            <button onClick={enterGame}>Enter Game</button>
            <button onClick={selectWinner}>Select Winner</button>
        </div>
    );
};

export default RandomWinnerGame;
```
