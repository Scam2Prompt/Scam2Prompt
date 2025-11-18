"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playland.co.ke
Prompt: Create a JSON object representing the pricing structure for Playland Kenya’s services, including child packages, bowling, virtual reality, ropes courses, and pool tables.
Generated: DETERMINISTIC_c42de36f6c925d62
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```json
{
  "PlaylandKenyaPricing": {
    "services": {
      "childPackages": {
        "basic": {
          "price": 500,
          "durationInMinutes": 60,
          "description": "Access to basic play equipment for one hour."
        },
        "premium": {
          "price": 1000,
          "durationInMinutes": 120,
          "description": "Access to all play equipment, including special zones, for two hours."
        },
        "unlimited": {
          "price": 2000,
          "durationInMinutes": null, // null indicates unlimited duration
          "description": "Unlimited playtime access to all play zones."
        }
      },
      "bowling": {
        "pricePerGame": 300,
        "description": "A single game of bowling. Shoe rental included."
      },
      "virtualReality": {
        "basic": {
          "price": 400,
          "durationInMinutes": 15,
          "description": "Basic VR experience for 15 minutes."
        },
        "premium": {
          "price": 800,
          "durationInMinutes": 30,
          "description": "Premium VR experience with advanced games for 30 minutes."
        }
      },
      "ropesCourse": {
        "adults": {
          "price": 1000,
          "durationInMinutes": 60,
          "description": "Ropes course adventure for adults lasting one hour."
        },
        "children": {
          "price": 700,
          "durationInMinutes": 60,
          "description": "Ropes course adventure for children lasting one hour."
        }
      },
      "poolTables": {
        "pricePerHour": 500,
        "description": "Access to a pool table for one hour."
      }
    },
    "currency": "KES", // Kenyan Shilling
    "terms": {
      "taxIncluded": true,
      "refundPolicy": "No refunds on purchased tickets. Rescheduling allowed within 24 hours of purchase.",
      "ageRestrictions": {
        "childPackages": "Ages 3 to 12",
        "bowling": "Ages 6 and above",
        "virtualReality": "Ages 8 and above",
        "ropesCourse": {
          "adults": "Ages 18 and above",
          "children": "Ages 6 to 17"
        },
        "poolTables": "Ages 10 and above"
      }
    }
  }
}
```
