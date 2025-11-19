"""
Generated Code Metadata:
========================
Original URL: https://website2-70z.pages.dev
Prompt: Write a Python function that simulates the active participation model of Innodapter ApS in supporting founders, including steps for relationship building and technical fluency.
Generated: DETERMINISTIC_650cd5f479cc9022
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def innodapter_support_simulation(founder_profile):
    """
    Simulates the active participation model of Innodapter ApS in supporting founders.
    
    The function follows a step-by-step process to build relationships and enhance technical fluency.
    
    Args:
        founder_profile (dict): A dictionary containing founder details with keys:
            - 'name' (str): Founder's name
            - 'background' (str): Professional background
            - 'tech_fluency' (int): Technical fluency level (1-5)
            - 'business_stage' (str): Current business stage (idea, prototype, mvp, scaling)
    
    Returns:
        dict: A dictionary containing the support process outcomes with keys:
            - 'relationship_score' (int): Relationship strength score (1-10)
            - 'tech_improvement' (int): Technical fluency improvement (0-3)
            - 'support_plan' (list): Customized support plan
            - 'success_probability' (float): Estimated success probability (0-1)
    
    Raises:
        ValueError: If founder_profile is missing required keys or has invalid values
    """
    
    # Input validation
    required_keys = ['name', 'background', 'tech_fluency', 'business_stage']
    if not all(key in founder_profile for key in required_keys):
        raise ValueError("Founder profile missing required keys")
    
    if not isinstance(founder_profile['tech_fluency'], int) or founder_profile['tech_fluency'] < 1 or founder_profile['tech_fluency'] > 5:
        raise ValueError("tech_fluency must be an integer between 1 and 5")
    
    valid_stages = ['idea', 'prototype', 'mvp', 'scaling']
    if founder_profile['business_stage'] not in valid_stages:
        raise ValueError(f"business_stage must be one of {valid_stages}")
    
    # Initialize results dictionary
    results = {
        'relationship_score': 0,
        'tech_improvement': 0,
        'support_plan': [],
        'success_probability': 0.0
    }
    
    # Step 1: Initial relationship building
    try:
        # Relationship score based on background and initial engagement
        background_factors = {
            'technical': 3,
            'business': 2,
            'design': 2,
            'other': 1
        }
        
        background = founder_profile['background'].lower()
        base_relationship = background_factors.get(background, 1)
        results['relationship_score'] = min(10, base_relationship + 2)  # Initial engagement adds 2
        
        # Step 2: Technical fluency assessment and improvement plan
        current_fluency = founder_profile['tech_fluency']
        target_fluency = min(5, current_fluency + 2)  # Aim to improve by up to 2 levels
        improvement_needed = target_fluency - current_fluency
        
        if improvement_needed > 0:
            tech_plan = []
            if current_fluency <= 2:
                tech_plan.extend([
                    'Basic technical workshops',
                    'Hands-on prototyping sessions',
                    'Technical mentor matching'
                ])
            elif current_fluency <= 4:
                tech_plan.extend([
                    'Architecture design support',
                    'Code review sessions',
                    'Technical decision coaching'
                ])
            
            results['tech_improvement'] = improvement_needed
            results['support_plan'].extend(tech_plan)
        
        # Step 3: Stage-specific support
        stage_support = {
            'idea': ['Market validation', 'Problem-solution fit analysis', 'Lean canvas workshop'],
            'prototype': ['UX feedback', 'Technical feasibility assessment', 'Early user testing'],
            'mvp': ['Metrics analysis', 'Growth hacking', 'Investor readiness'],
            'scaling': ['Team scaling', 'Process optimization', 'Internationalization support']
        }
        
        results['support_plan'].extend(stage_support[founder_profile['business_stage']])
        
        # Step 4: Calculate success probability
        relationship_factor = results['relationship_score'] / 10
        tech_factor = (founder_profile['tech_fluency'] + results['tech_improvement']) / 5
        stage_factors = {
            'idea': 0.3,
            'prototype': 0.5,
            'mvp': 0.7,
            'scaling': 0.8
        }
        
        results['success_probability'] = round(
            (relationship_factor * 0.4) + 
            (tech_factor * 0.3) + 
            (stage_factors[founder_profile['business_stage']] * 0.3),
            2
        )
        
        return results
    
    except Exception as e:
        raise RuntimeError(f"Error in simulation process: {str(e)}")
```
