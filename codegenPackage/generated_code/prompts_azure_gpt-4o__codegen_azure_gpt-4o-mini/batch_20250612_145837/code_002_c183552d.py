"""
Generated Code Metadata:
========================
Original URL: https://etuktuk-io-web.pages.dev
Prompt: Develop a feature in a Crazy Taxi-style game where players can use $TUK tokens to upgrade their vehicles and unlock new cities, as described in the eTukTuk ecosystem.
Generated: DETERMINISTIC_c183552d1c8bc947
Batch ID: 20250612_145837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Vehicle:
    """Class representing a vehicle in the Crazy Taxi-style game."""
    
    def __init__(self, name, speed, upgrade_cost):
        """
        Initialize a new vehicle.

        :param name: Name of the vehicle
        :param speed: Speed of the vehicle
        :param upgrade_cost: Cost to upgrade the vehicle
        """
        self.name = name
        self.speed = speed
        self.upgrade_cost = upgrade_cost
        self.upgraded = False

    def upgrade(self, tokens):
        """
        Upgrade the vehicle if enough tokens are available.

        :param tokens: Number of $TUK tokens available
        :return: Success message or error message
        """
        if tokens >= self.upgrade_cost:
            self.upgraded = True
            return f"{self.name} upgraded successfully!"
        else:
            return f"Not enough tokens to upgrade {self.name}. Required: {self.upgrade_cost}, Available: {tokens}"


class City:
    """Class representing a city in the game."""
    
    def __init__(self, name, unlock_cost):
        """
        Initialize a new city.

        :param name: Name of the city
        :param unlock_cost: Cost to unlock the city
        """
        self.name = name
        self.unlock_cost = unlock_cost
        self.unlocked = False

    def unlock(self, tokens):
        """
        Unlock the city if enough tokens are available.

        :param tokens: Number of $TUK tokens available
        :return: Success message or error message
        """
        if tokens >= self.unlock_cost:
            self.unlocked = True
            return f"{self.name} unlocked successfully!"
        else:
            return f"Not enough tokens to unlock {self.name}. Required: {self.unlock_cost}, Available: {tokens}"


class Game:
    """Main class to manage the game state."""
    
    def __init__(self):
        """Initialize the game with vehicles and cities."""
        self.vehicles = []
        self.cities = []
        self.tokens = 0

    def add_vehicle(self, vehicle):
        """Add a vehicle to the game."""
        self.vehicles.append(vehicle)

    def add_city(self, city):
        """Add a city to the game."""
        self.cities.append(city)

    def earn_tokens(self, amount):
        """
        Earn $TUK tokens.

        :param amount: Number of tokens to earn
        """
        if amount < 0:
            raise ValueError("Amount of tokens earned cannot be negative.")
        self.tokens += amount

    def upgrade_vehicle(self, vehicle_name):
        """
        Upgrade a vehicle by name.

        :param vehicle_name: Name of the vehicle to upgrade
        :return: Result of the upgrade attempt
        """
        for vehicle in self.vehicles:
            if vehicle.name == vehicle_name:
                return vehicle.upgrade(self.tokens)
        return f"Vehicle {vehicle_name} not found."

    def unlock_city(self, city_name):
        """
        Unlock a city by name.

        :param city_name: Name of the city to unlock
        :return: Result of the unlock attempt
        """
        for city in self.cities:
            if city.name == city_name:
                return city.unlock(self.tokens)
        return f"City {city_name} not found."


# Example usage
if __name__ == "__main__":
    game = Game()

    # Adding vehicles
    game.add_vehicle(Vehicle("Tuk Tuk", 60, 10))
    game.add_vehicle(Vehicle("Speedy Car", 80, 20))

    # Adding cities
    game.add_city(City("City A", 15))
    game.add_city(City("City B", 25))

    # Earning tokens
    game.earn_tokens(30)

    # Upgrading a vehicle
    print(game.upgrade_vehicle("Tuk Tuk"))  # Should succeed
    print(game.upgrade_vehicle("Speedy Car"))  # Should succeed

    # Unlocking a city
    print(game.unlock_city("City A"))  # Should succeed
    print(game.unlock_city("City B"))  # Should succeed
```
