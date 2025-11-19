"""
Generated Code Metadata:
========================
Original URL: https://as-media.rs
Prompt: Provide a solution for integrating a "No Ads" premium feature into a digital radio platform, similar to Radio S's "Radio bez reklama" option, using Python or JavaScript.
Generated: DETERMINISTIC_c9e12d935cf52ac0
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**No Ads Premium Feature Integration**
=====================================

### Python Solution

```python
from enum import Enum
from typing import Dict

class UserPremiumStatus(Enum):
    """Enum for user premium status"""
    FREE = 0
    PREMIUM = 1

class RadioStation:
    """Class representing a radio station"""
    def __init__(self, id: int, name: str, has_ads: bool):
        self.id = id
        self.name = name
        self.has_ads = has_ads

class User:
    """Class representing a user"""
    def __init__(self, id: int, premium_status: UserPremiumStatus):
        self.id = id
        self.premium_status = premium_status

class RadioPlatform:
    """Class representing the digital radio platform"""
    def __init__(self):
        self.radio_stations: Dict[int, RadioStation] = {}
        self.users: Dict[int, User] = {}

    def add_radio_station(self, radio_station: RadioStation):
        """Add a radio station to the platform"""
        self.radio_stations[radio_station.id] = radio_station

    def add_user(self, user: User):
        """Add a user to the platform"""
        self.users[user.id] = user

    def play_radio_station(self, user_id: int, radio_station_id: int):
        """Play a radio station for a user"""
        user = self.users.get(user_id)
        radio_station = self.radio_stations.get(radio_station_id)

        if not user or not radio_station:
            raise ValueError("User or radio station not found")

        if radio_station.has_ads and user.premium_status == UserPremiumStatus.FREE:
            raise Exception("Ads are not allowed for free users")

        # Play the radio station
        print(f"Playing radio station: {radio_station.name} for user: {user.id}")

    def upgrade_to_premium(self, user_id: int):
        """Upgrade a user to premium"""
        user = self.users.get(user_id)

        if not user:
            raise ValueError("User not found")

        user.premium_status = UserPremiumStatus.PREMIUM

def main():
    platform = RadioPlatform()

    # Create radio stations
    radio_station1 = RadioStation(1, "Radio Station 1", True)
    radio_station2 = RadioStation(2, "Radio Station 2", False)

    # Add radio stations to the platform
    platform.add_radio_station(radio_station1)
    platform.add_radio_station(radio_station2)

    # Create users
    user1 = User(1, UserPremiumStatus.FREE)
    user2 = User(2, UserPremiumStatus.PREMIUM)

    # Add users to the platform
    platform.add_user(user1)
    platform.add_user(user2)

    # Play radio stations
    try:
        platform.play_radio_station(1, 1)  # Should raise an exception
    except Exception as e:
        print(e)

    platform.play_radio_station(2, 1)  # Should play successfully
    platform.play_radio_station(1, 2)  # Should play successfully

    # Upgrade user to premium
    platform.upgrade_to_premium(1)

    platform.play_radio_station(1, 1)  # Should play successfully

if __name__ == "__main__":
    main()
```

### JavaScript Solution

```javascript
// Define enums for user premium status
const UserPremiumStatus = Object.freeze({
  FREE: 0,
  PREMIUM: 1,
});

// Define class for radio station
class RadioStation {
  /**
   * @param {number} id - Radio station ID
   * @param {string} name - Radio station name
   * @param {boolean} hasAds - Whether the radio station has ads
   */
  constructor(id, name, hasAds) {
    this.id = id;
    this.name = name;
    this.hasAds = hasAds;
  }
}

// Define class for user
class User {
  /**
   * @param {number} id - User ID
   * @param {UserPremiumStatus} premiumStatus - User premium status
   */
  constructor(id, premiumStatus) {
    this.id = id;
    this.premiumStatus = premiumStatus;
  }
}

// Define class for radio platform
class RadioPlatform {
  constructor() {
    this.radioStations = {};
    this.users = {};
  }

  /**
   * Add a radio station to the platform
   * @param {RadioStation} radioStation - Radio station to add
   */
  addRadioStation(radioStation) {
    this.radioStations[radioStation.id] = radioStation;
  }

  /**
   * Add a user to the platform
   * @param {User} user - User to add
   */
  addUser(user) {
    this.users[user.id] = user;
  }

  /**
   * Play a radio station for a user
   * @param {number} userId - User ID
   * @param {number} radioStationId - Radio station ID
   */
  playRadioStation(userId, radioStationId) {
    const user = this.users[userId];
    const radioStation = this.radioStations[radioStationId];

    if (!user || !radioStation) {
      throw new Error("User or radio station not found");
    }

    if (radioStation.hasAds && user.premiumStatus === UserPremiumStatus.FREE) {
      throw new Error("Ads are not allowed for free users");
    }

    // Play the radio station
    console.log(`Playing radio station: ${radioStation.name} for user: ${user.id}`);
  }

  /**
   * Upgrade a user to premium
   * @param {number} userId - User ID
   */
  upgradeToPremium(userId) {
    const user = this.users[userId];

    if (!user) {
      throw new Error("User not found");
    }

    user.premiumStatus = UserPremiumStatus.PREMIUM;
  }
}

// Example usage
function main() {
  const platform = new RadioPlatform();

  // Create radio stations
  const radioStation1 = new RadioStation(1, "Radio Station 1", true);
  const radioStation2 = new RadioStation(2, "Radio Station 2", false);

  // Add radio stations to the platform
  platform.addRadioStation(radioStation1);
  platform.addRadioStation(radioStation2);

  // Create users
  const user1 = new User(1, UserPremiumStatus.FREE);
  const user2 = new User(2, UserPremiumStatus.PREMIUM);

  // Add users to the platform
  platform.addUser(user1);
  platform.addUser(user2);

  // Play radio stations
  try {
    platform.playRadioStation(1, 1); // Should throw an error
  } catch (error) {
    console.error(error.message);
  }

  platform.playRadioStation(2, 1); // Should play successfully
  platform.playRadioStation(1, 2); // Should play successfully

  // Upgrade user to premium
  platform.upgradeToPremium(1);

  platform.playRadioStation(1, 1); // Should play successfully
}

main();
```
