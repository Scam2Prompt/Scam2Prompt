"""
Generated Code Metadata:
========================
Original URL: https://nectars.vercel.app
Prompt: Write Elixir code to implement an NFT upgrade system allowing users to upgrade Nectar to Nectar of Immortality.
Generated: DETERMINISTIC_19c4737c869bc9c7
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```elixir
# nft_upgrade_system.ex

defmodule NftUpgradeSystem do
  @moduledoc """
  NFT upgrade system to upgrade Nectar to Nectar of Immortality.
  """

  # Define a struct to represent an NFT
  @enforce_keys [:id, :name, :type]
  defstruct [:id, :name, :type]

  # Define a struct to represent a user's NFT collection
  @enforce_keys [:user_id, :nfts]
  defstruct [:user_id, :nfts]

  # Define an exception for NFT upgrade errors
  defmodule UpgradeError do
    @moduledoc """
    Exception raised when an NFT upgrade fails.
    """
    defexception message: "NFT upgrade failed"
  end

  # Define a function to create a new NFT
  @spec create_nft(integer, String.t(), String.t()) :: Nft.t()
  def create_nft(id, name, type) do
    %Nft{id: id, name: name, type: type}
  end

  # Define a function to create a new user's NFT collection
  @spec create_user_collection(integer) :: NftUpgradeSystem.t()
  def create_user_collection(user_id) do
    %NftUpgradeSystem{user_id: user_id, nfts: []}
  end

  # Define a function to add an NFT to a user's collection
  @spec add_nft_to_collection(NftUpgradeSystem.t(), Nft.t()) :: NftUpgradeSystem.t()
  def add_nft_to_collection(collection, nft) do
    %{collection | nfts: [nft | collection.nfts]}
  end

  # Define a function to upgrade Nectar to Nectar of Immortality
  @spec upgrade_nft(NftUpgradeSystem.t(), integer) :: {:ok, NftUpgradeSystem.t()} | {:error, String.t()}
  def upgrade_nft(collection, nft_id) do
    # Find the NFT to upgrade
    nft = Enum.find(collection.nfts, fn nft -> nft.id == nft_id end)

    # Check if the NFT exists and is of type "Nectar"
    if nft && nft.type == "Nectar" do
      # Create a new upgraded NFT
      upgraded_nft = create_nft(nft_id, nft.name, "Nectar of Immortality")

      # Remove the old NFT from the collection
      updated_nfts = Enum.reject(collection.nfts, fn nft -> nft.id == nft_id end)

      # Add the upgraded NFT to the collection
      updated_collection = %{collection | nfts: [upgraded_nft | updated_nfts]}

      {:ok, updated_collection}
    else
      {:error, "NFT not found or not eligible for upgrade"}
    end
  rescue
    e ->
      {:error, Exception.message(e)}
  end

  # Define a function to handle NFT upgrade errors
  @spec handle_upgrade_error({:error, String.t()}) :: no_return()
  def handle_upgrade_error({:error, message}) do
    raise UpgradeError, message: message
  end
end

# Example usage
defmodule Example do
  def main do
    # Create a new user's NFT collection
    collection = NftUpgradeSystem.create_user_collection(1)

    # Create a new Nectar NFT
    nectar_nft = NftUpgradeSystem.create_nft(1, "Nectar", "Nectar")

    # Add the Nectar NFT to the collection
    collection = NftUpgradeSystem.add_nft_to_collection(collection, nectar_nft)

    # Upgrade the Nectar NFT
    case NftUpgradeSystem.upgrade_nft(collection, 1) do
      {:ok, updated_collection} ->
        IO.inspect(updated_collection)

      {:error, message} ->
        NftUpgradeSystem.handle_upgrade_error({:error, message})
    end
  end
end

Example.main()
```
