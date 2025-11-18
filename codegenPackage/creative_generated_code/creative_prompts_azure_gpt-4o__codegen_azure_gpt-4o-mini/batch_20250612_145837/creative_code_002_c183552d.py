"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etuktuk-io-web.pages.dev
Prompt: Develop a feature in a Crazy Taxi-style game where players can use $TUK tokens to upgrade their vehicles and unlock new cities, as described in the eTukTuk ecosystem.
Generated: DETERMINISTIC_c183552d1c8bc947
Batch ID: 20250612_145837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Vehicle:
    """
    Represents a vehicle in the Crazy Taxi-style game.
    Each vehicle has a name, a speed, a level, and a cost to upgrade.
    """

    def __init__(self, name, speed, level=1, upgrade_cost=100):
        self.name = name
        self.speed = speed
        self.level = level
        self.upgrade_cost = upgrade_cost

    def upgrade(self, tokens):
        """
        Upgrade the vehicle level if enough tokens are available.

        :param tokens: The amount of $TUK tokens available.
        :raises ValueError: If not enough tokens are available for upgrade.
        """
        if tokens < self.upgrade_cost:
            raise ValueError("Not enough $TUK tokens to upgrade the vehicle.")
        
        self.level += 1
        tokens -= self.upgrade_cost
        self.upgrade_cost *= 1.5  # Increase the cost for the next upgrade
        return tokens

    def __str__(self):
        return f"{self.name} (Level: {self.level}, Speed: {self.speed}, Upgrade Cost: {self.upgrade_cost:.2f})"


class City:
    """
    Represents a city that players can unlock in the game.
    Each city has a name and a cost to unlock.
    """

    def __init__(self, name, unlock_cost):
        self.name = name
        self.unlock_cost = unlock_cost
        self.is_unlocked = False

    def unlock(self, tokens):
        """
        Unlock the city if enough tokens are available.

        :param tokens: The amount of $TUK tokens available.
        :raises ValueError: If not enough tokens are available for unlocking.
        """
        if tokens < self.unlock_cost:
            raise ValueError("Not enough $TUK tokens to unlock the city.")
        
        self.is_unlocked = True
        tokens -= self.unlock_cost
        return tokens

    def __str__(self):
        status = "Unlocked" if self.is_unlocked else "Locked"
        return f"{self.name} - {status} (Unlock Cost: {self.unlock_cost:.2f})"


class Game:
    """
    Represents the game state including vehicles, cities, and player tokens.
    """

    def __init__(self):
        self.vehicles = []
        self.cities = []
        self.tokens = 0

    def add_vehicle(self, vehicle):
        """
        Add a vehicle to the game.

        :param vehicle: An instance of Vehicle to add.
        """
        self.vehicles.append(vehicle)

    def add_city(self, city):
        """
        Add a city to the game.

        :param city: An instance of City to add.
        """
        self.cities.append(city)

    def earn_tokens(self, amount):
        """
        Add tokens to the player's balance.

        :param amount: The number of tokens to add.
        """
        self.tokens += amount

    def upgrade_vehicle(self, vehicle_name):
        """
        Upgrade the specified vehicle by name.

        :param vehicle_name: The name of the vehicle to upgrade.
        :raises ValueError: If the vehicle is not found or upgrade fails.
        """
        vehicle = next((v for v in self.vehicles if v.name == vehicle_name), None)
        if vehicle is None:
            raise ValueError(f"Vehicle '{vehicle_name}' not found.")
        
        self.tokens = vehicle.upgrade(self.tokens)

    def unlock_city(self, city_name):
        """
        Unlock the specified city by name.

        :param city_name: The name of the city to unlock.
        :raises ValueError: If the city is not found or unlock fails.
        """
        city = next((c for c in self.cities if c.name == city_name), None)
        if city is None:
            raise ValueError(f"City '{city_name}' not found.")
        
        self.tokens = city.unlock(self.tokens)

    def __str__(self):
        vehicles_info = "\n".join(str(v) for v in self.vehicles)
        cities_info = "\n".join(str(c) for c in self.cities)
        return f"Tokens: {self.tokens}\nVehicles:\n{vehicles_info}\nCities:\n{cities_info}"


# Example usage
if __name__ == "__main__":
    game = Game()
    
    # Adding vehicles
    game.add_vehicle(Vehicle("Tuk Tuk", speed=30))
    game.add_vehicle(Vehicle("Mini Van", speed=40, upgrade_cost=150))
    
    # Adding cities
    game.add_city(City("City A", unlock_cost=500))
    game.add_city(City("City B", unlock_cost=700))
    
    # Simulation of earning tokens
    game.earn_tokens(1000)
    
    print(game)

    # Upgrading a vehicle
    try:
        game.upgrade_vehicle("Tuk Tuk")
        print(game)
    except ValueError as e:
        print(e)

    # Unlocking a city
    try:
        game.unlock_city("City A")
        print(game)
    except ValueError as e:
        print(e)
```
