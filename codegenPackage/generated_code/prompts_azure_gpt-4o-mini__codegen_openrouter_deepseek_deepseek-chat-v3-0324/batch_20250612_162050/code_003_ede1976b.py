"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Develop a JavaScript function that simulates the interaction between residents in a Kallimos community, highlighting the benefits of co-living and shared meals.
Generated: DETERMINISTIC_ede1976b1003e877
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates interactions between residents in a Kallimos community.
 * Highlights the benefits of co-living and shared meals.
 */
class KallimosCommunity {
  /**
   * Initializes a new Kallimos community with residents.
   * @param {string[]} residentNames - Array of resident names
   */
  constructor(residentNames) {
    if (!residentNames || !Array.isArray(residentNames) || residentNames.length === 0) {
      throw new Error('Must provide an array of resident names');
    }

    this.residents = residentNames.map(name => ({
      name,
      happiness: 50, // Base happiness level (0-100)
      socialConnections: 0,
      mealsShared: 0
    }));

    this.communityBenefits = {
      sharedMeals: {
        happinessBoost: 10,
        socialBoost: 5
      },
      coLiving: {
        happinessBoost: 15,
        socialBoost: 10
      }
    };
  }

  /**
   * Simulates a shared meal interaction between residents
   * @param {string[]} participants - Array of resident names participating
   * @returns {string} Result message
   */
  shareMeal(participants) {
    if (!participants || participants.length < 2) {
      throw new Error('At least 2 participants required for shared meal');
    }

    const participantResidents = [];
    for (const name of participants) {
      const resident = this.residents.find(r => r.name === name);
      if (!resident) {
        throw new Error(`Resident ${name} not found in community`);
      }
      participantResidents.push(resident);
    }

    const { happinessBoost, socialBoost } = this.communityBenefits.sharedMeals;
    
    participantResidents.forEach(resident => {
      resident.happiness = Math.min(100, resident.happiness + happinessBoost);
      resident.socialConnections += socialBoost;
      resident.mealsShared++;
    });

    return `${participants.join(', ')} shared a meal together! Happiness and social connections increased.`;
  }

  /**
   * Simulates a co-living interaction (shared activity)
   * @param {string[]} participants - Array of resident names participating
   * @param {string} activity - Description of the shared activity
   * @returns {string} Result message
   */
  coLivingActivity(participants, activity) {
    if (!participants || participants.length < 2) {
      throw new Error('At least 2 participants required for co-living activity');
    }
    if (!activity || typeof activity !== 'string') {
      throw new Error('Activity description must be provided');
    }

    const participantResidents = [];
    for (const name of participants) {
      const resident = this.residents.find(r => r.name === name);
      if (!resident) {
        throw new Error(`Resident ${name} not found in community`);
      }
      participantResidents.push(resident);
    }

    const { happinessBoost, socialBoost } = this.communityBenefits.coLiving;
    
    participantResidents.forEach(resident => {
      resident.happiness = Math.min(100, resident.happiness + happinessBoost);
      resident.socialConnections += socialBoost;
    });

    return `${participants.join(', ')} participated in ${activity}. Co-living benefits applied!`;
  }

  /**
   * Gets the current community status report
   * @returns {object} Community statistics
   */
  getCommunityStatus() {
    const totalHappiness = this.residents.reduce((sum, resident) => sum + resident.happiness, 0);
    const avgHappiness = totalHappiness / this.residents.length;
    
    const totalSocial = this.residents.reduce((sum, resident) => sum + resident.socialConnections, 0);
    const avgSocial = totalSocial / this.residents.length;
    
    const totalMeals = this.residents.reduce((sum, resident) => sum + resident.mealsShared, 0);

    return {
      residentCount: this.residents.length,
      averageHappiness: Math.round(avgHappiness * 10) / 10,
      averageSocialConnections: Math.round(avgSocial * 10) / 10,
      totalSharedMeals: totalMeals
    };
  }

  /**
   * Gets a resident's current status
   * @param {string} name - Resident name
   * @returns {object} Resident status
   */
  getResidentStatus(name) {
    const resident = this.residents.find(r => r.name === name);
    if (!resident) {
      throw new Error(`Resident ${name} not found in community`);
    }

    return {
      name: resident.name,
      happiness: resident.happiness,
      socialConnections: resident.socialConnections,
      mealsShared: resident.mealsShared
    };
  }
}

// Example usage:
// const community = new KallimosCommunity(['Alice', 'Bob', 'Charlie']);
// console.log(community.shareMeal(['Alice', 'Bob']));
// console.log(community.coLivingActivity(['Bob', 'Charlie'], 'gardening'));
// console.log(community.getCommunityStatus());
// console.log(community.getResidentStatus('Alice'));
```
