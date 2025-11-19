"""
Generated Code Metadata:
========================
Original URL: https://nectars.vercel.app
Prompt: Generate a code snippet in Elixir to track and burn old versions of a digital item, such as the old version of Elixir mentioned for Nectars upgrades.
Generated: DETERMINISTIC_81c6cfeb2e078dec
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```elixir
# lib/item_tracker.ex

defmodule ItemTracker do
  @moduledoc """
  Tracks and burns old versions of digital items.

  ## Usage

      iex> ItemTracker.track_item(%ItemTracker.Item{version: 1, id: 1})
      iex> ItemTracker.burn_old_versions(1, 2)
      iex> ItemTracker.get_tracked_items(1)
  """

  @doc """
  Starts the ItemTracker GenServer.
  """
  def start_link(opts \\ []) do
    GenServer.start_link(__MODULE__, opts, name: __MODULE__)
  end

  @doc """
  Tracks a digital item.

  ## Parameters

  * `item` - The item to track.

  ## Returns

  * `:ok` if the item was tracked successfully.
  """
  def track_item(item) do
    GenServer.call(__MODULE__, {:track_item, item})
  end

  @doc """
  Burns old versions of a digital item.

  ## Parameters

  * `item_id` - The ID of the item.
  * `new_version` - The new version of the item.

  ## Returns

  * `:ok` if the old versions were burned successfully.
  """
  def burn_old_versions(item_id, new_version) do
    GenServer.call(__MODULE__, {:burn_old_versions, item_id, new_version})
  end

  @doc """
  Gets the tracked items for a given item ID.

  ## Parameters

  * `item_id` - The ID of the item.

  ## Returns

  * A list of tracked items.
  """
  def get_tracked_items(item_id) do
    GenServer.call(__MODULE__, {:get_tracked_items, item_id})
  end

  use GenServer

  def init(_opts) do
    {:ok, %{items: %{}}}
  end

  def handle_call({:track_item, item}, _from, state) do
    item_id = item.id
    version = item.version

    items =
      case Map.get(state.items, item_id) do
        nil ->
          %{item | burned?: false}

        existing_item ->
          existing_item
          |> Map.put(:version, version)
          |> Map.put(:burned?, false)
      end

    state =
      put_in(state, [:items, item_id], items)

    {:reply, :ok, state}
  end

  def handle_call({:burn_old_versions, item_id, new_version}, _from, state) do
    case Map.get(state.items, item_id) do
      nil ->
        {:reply, {:error, "Item not found"}, state}

      item ->
        if item.version < new_version do
          state =
            put_in(state, [:items, item_id, :burned?], true)

          {:reply, :ok, state}
        else
          {:reply, {:error, "New version must be greater than existing version"}, state}
        end
    end
  end

  def handle_call({:get_tracked_items, item_id}, _from, state) do
    items =
      case Map.get(state.items, item_id) do
        nil -> []
        item -> [item]
      end

    {:reply, items, state}
  end
end

# lib/item.ex

defmodule ItemTracker.Item do
  @enforce_keys [:id, :version]
  defstruct [:id, :version, :burned?]

  @type t() :: %__MODULE__{
          id: integer(),
          version: integer(),
          burned?: boolean()
        }
end

# test/item_tracker_test.exs

defmodule ItemTrackerTest do
  use ExUnit.Case

  setup do
    ItemTracker.start_link()
    :ok
  end

  test "tracks a digital item" do
    item = %ItemTracker.Item{version: 1, id: 1}
    assert :ok == ItemTracker.track_item(item)
  end

  test "burns old versions of a digital item" do
    item = %ItemTracker.Item{version: 1, id: 1}
    ItemTracker.track_item(item)
    assert :ok == ItemTracker.burn_old_versions(1, 2)
  end

  test "gets tracked items" do
    item = %ItemTracker.Item{version: 1, id: 1}
    ItemTracker.track_item(item)
    assert [%ItemTracker.Item{}] = ItemTracker.get_tracked_items(1)
  end
end
```
