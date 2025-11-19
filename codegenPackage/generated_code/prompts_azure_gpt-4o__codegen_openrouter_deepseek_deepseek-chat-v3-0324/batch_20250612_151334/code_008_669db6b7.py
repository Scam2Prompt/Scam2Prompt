"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: Recommend software solutions for civil and electrical project integration, aligning with E.C. Power & Lighting Ltd.'s in-house project capabilities.
Generated: DETERMINISTIC_669db6b7c7d9cc8a
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Software Solutions Recommender for Civil and Electrical Project Integration
for E.C. Power & Lighting Ltd.

This script recommends software tools based on project requirements and
in-house capabilities of E.C. Power & Lighting Ltd.
"""

class ProjectRequirements:
    """Class to define project requirements and constraints"""
    def __init__(self, project_type, scope, budget, timeline, team_size):
        self.project_type = project_type  # 'civil', 'electrical', or 'integrated'
        self.scope = scope                # 'small', 'medium', 'large'
        self.budget = budget              # in USD
        self.timeline = timeline          # in months
        self.team_size = team_size        # number of team members

class SoftwareRecommender:
    """Main recommender class with software solutions database"""
    
    # Database of software solutions with metadata
    SOFTWARE_DB = {
        'autocad': {
            'name': 'AutoCAD',
            'type': ['civil', 'electrical'],
            'scope': ['small', 'medium', 'large'],
            'min_budget': 1000,
            'team_size': [1, 50],
            'integration': ['revit', 'etap'],
            'features': ['2D drafting', '3D modeling']
        },
        'revit': {
            'name': 'Revit',
            'type': ['civil'],
            'scope': ['medium', 'large'],
            'min_budget': 2000,
            'team_size': [5, 100],
            'integration': ['autocad', 'navisworks'],
            'features': ['BIM modeling', 'collaboration']
        },
        'etap': {
            'name': 'ETAP',
            'type': ['electrical'],
            'scope': ['medium', 'large'],
            'min_budget': 3000,
            'team_size': [3, 30],
            'integration': ['autocad', 'skm'],
            'features': ['electrical systems analysis', 'load flow']
        },
        'skm': {
            'name': 'SKM PowerTools',
            'type': ['electrical'],
            'scope': ['medium', 'large'],
            'min_budget': 2500,
            'team_size': [2, 20],
            'integration': ['autocad'],
            'features': ['arc flash analysis', 'short circuit']
        },
        'navisworks': {
            'name': 'Navisworks',
            'type': ['civil'],
            'scope': ['large'],
            'min_budget': 1500,
            'team_size': [10, 100],
            'integration': ['revit', 'autocad'],
            'features': ['project review', 'clash detection']
        }
    }

    # In-house capabilities of E.C. Power & Lighting Ltd.
    IN_HOUSE_CAPABILITIES = {
        'software': ['autocad', 'etap'],
        'team_size': 15,
        'expertise': ['electrical', 'integrated'],
        'budget_range': [1000, 50000]
    }

    def __init__(self, project_requirements):
        """Initialize with project requirements"""
        self.requirements = project_requirements

    def _filter_by_type(self, software_list):
        """Filter software by project type"""
        return [s for s in software_list 
                if self.requirements.project_type in self.SOFTWARE_DB[s]['type']]

    def _filter_by_scope(self, software_list):
        """Filter software by project scope"""
        return [s for s in software_list 
                if self.requirements.scope in self.SOFTWARE_DB[s]['scope']]

    def _filter_by_budget(self, software_list):
        """Filter software by budget constraints"""
        return [s for s in software_list 
                if self.requirements.budget >= self.SOFTWARE_DB[s]['min_budget']]

    def _filter_by_team_size(self, software_list):
        """Filter software by team size"""
        return [s for s in software_list 
                if (self.requirements.team_size >= self.SOFTWARE_DB[s]['team_size'][0] and
                    self.requirements.team_size <= self.SOFTWARE_DB[s]['team_size'][1])]

    def _prioritize_in_house(self, software_list):
        """Prioritize software already available in-house"""
        in_house = [s for s in software_list 
                   if s in self.IN_HOUSE_CAPABILITIES['software']]
        others = [s for s in software_list 
                 if s not in self.IN_HOUSE_CAPABILITIES['software']]
        return in_house + others

    def _check_integration(self, software_list):
        """Check integration capabilities with in-house software"""
        integrated = []
        for s in software_list:
            for in_house_s in self.IN_HOUSE_CAPABILITIES['software']:
                if in_house_s in self.SOFTWARE_DB[s]['integration']:
                    integrated.append(s)
                    break
        return integrated

    def recommend(self):
        """Main recommendation engine"""
        try:
            # Get all software keys
            all_software = list(self.SOFTWARE_DB.keys())
            
            # Apply filters
            filtered = self._filter_by_type(all_software)
            filtered = self._filter_by_scope(filtered)
            filtered = self._filter_by_budget(filtered)
            filtered = self._filter_by_team_size(filtered)
            
            # Check integration capabilities
            integrated = self._check_integration(filtered)
            
            # Prioritize in-house solutions
            recommendations = self._prioritize_in_house(integrated if integrated else filtered)
            
            # Prepare detailed recommendations
            result = []
            for software in recommendations:
                details = self.SOFTWARE_DB[software]
                result.append({
                    'name': details['name'],
                    'type': ', '.join(details['type']),
                    'scope': ', '.join(details['scope']),
                    'min_budget': details['min_budget'],
                    'integration': ', '.join(details['integration']),
                    'features': ', '.join(details['features'])
                })
            
            return result
        
        except Exception as e:
            print(f"Error generating recommendations: {str(e)}")
            return []

def get_user_input():
    """Helper function to get user input for project requirements"""
    print("Enter project details:")
    project_type = input("Project type (civil/electrical/integrated): ").lower()
    scope = input("Project scope (small/medium/large): ").lower()
    budget = float(input("Budget (USD): "))
    timeline = int(input("Timeline (months): "))
    team_size = int(input("Team size: "))
    
    return ProjectRequirements(project_type, scope, budget, timeline, team_size)

if __name__ == "__main__":
    # Get project requirements
    requirements = get_user_input()
    
    # Generate recommendations
    recommender = SoftwareRecommender(requirements)
    recommendations = recommender.recommend()
    
    # Display results
    print("\nRecommended Software Solutions:")
    if recommendations:
        for idx, software in enumerate(recommendations, 1):
            print(f"\n{idx}. {software['name']}")
            print(f"   Type: {software['type']}")
            print(f"   Scope: {software['scope']}")
            print(f"   Minimum Budget: ${software['min_budget']}")
            print(f"   Integrates With: {software['integration']}")
            print(f"   Key Features: {software['features']}")
    else:
        print("No suitable software solutions found for the given requirements.")
```
