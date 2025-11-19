"""
Generated Code Metadata:
========================
Original URL: https://nectars.vercel.app
Prompt: Create an Elixir module that validates the upgrade process of Nectar to Nectar of Immortality, ensuring the correct number of NFTs (25 total) are generated.
Generated: DETERMINISTIC_45fadc3de2e2e258
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```elixir
defmodule NectarUpgradeValidator do
  @moduledoc """
  Validates the upgrade process of Nectar to Nectar of Immortality.
  """

  @doc """
  Validates the upgrade process.

  ## Parameters

  - `nectar_nfts`: List of Nectar NFTs.
  - `immortality_nfts`: List of Nectar of Immortality NFTs.

  ## Returns

  - `:ok` if the upgrade is valid.
  - `{:error, reason}` if the upgrade is invalid.

  ## Raises

  - `ArgumentError` if the input parameters are invalid.
  """
  @spec validate_upgrade(list, list) :: :ok | {:error, String.t()}
  def validate_upgrade(nectar_nfts, immortality_nfts) when is_list(nectar_nfts) and is_list(immortality_nfts) do
    total_nfts = length(nectar_nfts) + length(immortality_nfts)

    cond do
      total_nfts != 25 ->
        {:error, "Invalid number of NFTs. Expected 25, got #{total_nfts}"}

      true ->
        :ok
    end
  end

  def validate_upgrade(_, _), do: raise(ArgumentError, "Invalid input parameters")

  @doc """
  Batch validates multiple upgrade processes.

  ## Parameters

  - `upgrades`: List of tuples containing Nectar NFTs and Nectar of Immortality NFTs.

  ## Returns

  - `{:ok, results}` if all upgrades are valid.
  - `{:error, failed_upgrades}` if any upgrade is invalid.

  ## Raises

  - `ArgumentError` if the input parameters are invalid.
  """
  @spec batch_validate_upgrades(list) :: {:ok, list} | {:error, list}
  def batch_validate_upgrades(upgrades) when is_list(upgrades) do
    results =
      Enum.map(upgrades, fn {nectar_nfts, immortality_nfts} ->
        case validate_upgrade(nectar_nfts, immortality_nfts) do
          :ok -> {:ok, {nectar_nfts, immortality_nfts}}
          error -> error
        end
      end)

    case Enum.split_with(results, &match?({:ok, _}, &1)) do
      {[], failed_upgrades} -> {:error, failed_upgrades}
      {successful_upgrades, _} -> {:ok, successful_upgrades}
    end
  end

  def batch_validate_upgrades(_), do: raise(ArgumentError, "Invalid input parameters")
end
```
