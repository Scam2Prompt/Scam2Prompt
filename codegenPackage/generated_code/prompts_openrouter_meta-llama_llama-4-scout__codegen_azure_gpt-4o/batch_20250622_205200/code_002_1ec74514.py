"""
Generated Code Metadata:
========================
Original URL: https://ogma.ca
Prompt: Compare the features of the 2025 Spring Golf Tournament at TPC Toronto at Osprey Valley with another golf tournament, highlighting the unique challenges and scoring opportunities of the Hoot course.
Generated: DETERMINISTIC_1ec74514c7a7f5db
Batch ID: 20250622_205200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class GolfTournament:
    """
    A class to represent a golf tournament and its features.
    """
    def __init__(self, name, location, courses, unique_challenges, scoring_opportunities):
        """
        Initialize the GolfTournament object.

        :param name: Name of the tournament
        :param location: Location of the tournament
        :param courses: List of courses in the tournament
        :param unique_challenges: Unique challenges of the tournament
        :param scoring_opportunities: Scoring opportunities in the tournament
        """
        self.name = name
        self.location = location
        self.courses = courses
        self.unique_challenges = unique_challenges
        self.scoring_opportunities = scoring_opportunities

    def to_dict(self):
        """
        Convert the GolfTournament object to a dictionary.

        :return: Dictionary representation of the tournament
        """
        return {
            "name": self.name,
            "location": self.location,
            "courses": self.courses,
            "unique_challenges": self.unique_challenges,
            "scoring_opportunities": self.scoring_opportunities
        }

def compare_tournaments(tournament1, tournament2, course_to_highlight):
    """
    Compare two golf tournaments and highlight the unique challenges and scoring opportunities
    of a specific course.

    :param tournament1: First GolfTournament object
    :param tournament2: Second GolfTournament object
    :param course_to_highlight: Name of the course to highlight
    :return: Comparison result as a dictionary
    """
    try:
        # Extract details for the highlighted course from tournament1
        if course_to_highlight in tournament1.courses:
            t1_challenges = tournament1.unique_challenges.get(course_to_highlight, "No data available")
            t1_scoring = tournament1.scoring_opportunities.get(course_to_highlight, "No data available")
        else:
            t1_challenges = "Course not found in tournament1"
            t1_scoring = "Course not found in tournament1"

        # Extract details for the highlighted course from tournament2
        if course_to_highlight in tournament2.courses:
            t2_challenges = tournament2.unique_challenges.get(course_to_highlight, "No data available")
            t2_scoring = tournament2.scoring_opportunities.get(course_to_highlight, "No data available")
        else:
            t2_challenges = "Course not found in tournament2"
            t2_scoring = "Course not found in tournament2"

        # Prepare comparison result
        comparison_result = {
            "Tournament 1": {
                "Name": tournament1.name,
                "Location": tournament1.location,
                "Highlighted Course": course_to_highlight,
                "Unique Challenges": t1_challenges,
                "Scoring Opportunities": t1_scoring
            },
            "Tournament 2": {
                "Name": tournament2.name,
                "Location": tournament2.location,
                "Highlighted Course": course_to_highlight,
                "Unique Challenges": t2_challenges,
                "Scoring Opportunities": t2_scoring
            }
        }

        return comparison_result

    except Exception as e:
        # Handle unexpected errors
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Define the 2025 Spring Golf Tournament at TPC Toronto at Osprey Valley
    tpc_toronto = GolfTournament(
        name="2025 Spring Golf Tournament",
        location="TPC Toronto at Osprey Valley",
        courses=["Hoot", "North", "Heathlands"],
        unique_challenges={
            "Hoot": "Dense forest areas and narrow fairways",
            "North": "Undulating greens and water hazards",
            "Heathlands": "Links-style layout with strong winds"
        },
        scoring_opportunities={
            "Hoot": "Short par-4s and reachable par-5s",
            "North": "Strategic layups and birdie chances on par-3s",
            "Heathlands": "Aggressive play on downwind holes"
        }
    )

    # Define another golf tournament
    another_tournament = GolfTournament(
        name="2025 Summer Golf Championship",
        location="Pebble Beach Golf Links",
        courses=["Spyglass Hill", "Pebble Beach", "Hoot"],
        unique_challenges={
            "Spyglass Hill": "Steep elevation changes and tight fairways",
            "Pebble Beach": "Cliffside holes and unpredictable winds",
            "Hoot": "Dense forest areas and narrow fairways"
        },
        scoring_opportunities={
            "Spyglass Hill": "Short par-3s and reachable par-5s",
            "Pebble Beach": "Birdie chances on shorter par-4s",
            "Hoot": "Short par-4s and reachable par-5s"
        }
    )

    # Compare the tournaments, highlighting the "Hoot" course
    comparison = compare_tournaments(tpc_toronto, another_tournament, "Hoot")

    # Print the comparison result in a readable format
    print(json.dumps(comparison, indent=4))
```
