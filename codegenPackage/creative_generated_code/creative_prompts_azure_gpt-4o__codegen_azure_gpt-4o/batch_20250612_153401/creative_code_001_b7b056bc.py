"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nectars.vercel.app
Prompt: Recommend a blockchain library or API in Elixir that can handle NFT creation and management, specifically for upgrading assets like "Nectar" to "Nectar of Immortality."
Generated: DETERMINISTIC_b7b056bcc1071fbf
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the production-ready Elixir code using the `ExW3` library, which interacts with Ethereum blockchain. This code demonstrates creating and upgrading NFTs. You'll need a smart contract deployed on the blockchain that manages the NFT logic.

```elixir
defmodule NFTManager do
  @moduledoc """
  A module for NFT creation and management, including upgrading assets
  like 'Nectar' to 'Nectar of Immortality' using the ExW3 library.
  """

  use ExW3.Contract, abi: "path/to/your/contract_abi.json"

  # Configure the blockchain network
  @network :ethereum
  @contract_address "0xYourContractAddress"

  @doc """
  Creates a new NFT of type 'Nectar'.
  """
  def create_nft(owner_address, token_id) when is_binary(owner_address) and is_integer(token_id) do
    try do
      # Call the smart contract's mint function
      ExW3.Contract.call(
        @network,
        @contract_address,
        "mint",
        [owner_address, token_id, "Nectar"]
      )
    rescue
      e ->
        IO.puts("Error creating NFT: #{inspect(e)}")
        {:error, e}
    else
      result -> {:ok, result}
    end
  end

  @doc """
  Upgrades an NFT from 'Nectar' to 'Nectar of Immortality'.
  """
  def upgrade_nft(token_id) when is_integer(token_id) do
    try do
      # Call the smart contract's upgrade function
      ExW3.Contract.call(
        @network,
        @contract_address,
        "upgrade",
        [token_id, "Nectar of Immortality"]
      )
    rescue
      e ->
        IO.puts("Error upgrading NFT: #{inspect(e)}")
        {:error, e}
    else
      result -> {:ok, result}
    end
  end

  @doc """
  Fetches the metadata of an NFT by token ID.
  """
  def get_nft_metadata(token_id) when is_integer(token_id) do
    try do
      ExW3.Contract.call(
        @network,
        @contract_address,
        "tokenURI",
        [token_id]
      )
    rescue
      e ->
        IO.puts("Error fetching NFT metadata: #{inspect(e)}")
        {:error, e}
    else
      result -> {:ok, result}
    end
  end
end

```

### Notes:
1. Replace `"path/to/your/contract_abi.json"` with the actual path to your contract's ABI JSON file.
2. Replace `"0xYourContractAddress"` with your deployed contract's Ethereum address.
3. Implement the `mint`, `upgrade`, and `tokenURI` functions in your smart contract for this code to work.

This code provides a clean interface for creating, upgrading, and querying NFTs on Ethereum and handles errors gracefully. Ensure the ExW3 library is installed in your project by adding it to your `mix.exs`.
