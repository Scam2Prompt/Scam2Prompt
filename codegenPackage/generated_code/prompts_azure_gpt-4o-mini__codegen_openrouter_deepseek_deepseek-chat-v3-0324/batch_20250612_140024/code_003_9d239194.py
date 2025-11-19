"""
Generated Code Metadata:
========================
Original URL: https://kraken.media
Prompt: Develop a tutorial video outline that simplifies a complex topic, following the e-learning video style recommended by Kraken Media.
Generated: DETERMINISTIC_9d23919408077a7e
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Tutorial Video Outline Generator for Kraken Media Style E-Learning Videos

This script generates a structured outline for a tutorial video following Kraken Media's
recommended e-learning video style. The outline simplifies complex topics by breaking them
down into digestible segments with clear learning objectives.

Features:
- Generates a structured outline with timing recommendations
- Includes placeholders for key video elements (intro, modules, summary)
- Follows best practices for e-learning content
"""

def generate_video_outline(topic, complexity_level, target_audience, duration_minutes=10):
    """
    Generate a tutorial video outline in Kraken Media's e-learning style.
    
    Args:
        topic (str): The main topic of the tutorial
        complexity_level (str): 'beginner', 'intermediate', or 'advanced'
        target_audience (str): Description of the intended audience
        duration_minutes (int): Total video duration in minutes
        
    Returns:
        dict: Structured outline with timing and content recommendations
    """
    
    # Validate inputs
    if not topic or not isinstance(topic, str):
        raise ValueError("Topic must be a non-empty string")
    
    valid_complexity = ['beginner', 'intermediate', 'advanced']
    if complexity_level.lower() not in valid_complexity:
        raise ValueError(f"Complexity level must be one of: {', '.join(valid_complexity)}")
    
    if not isinstance(duration_minutes, int) or duration_minutes < 1:
        raise ValueError("Duration must be a positive integer")
    
    # Calculate segment durations (percentage-based)
    segment_ratios = {
        'intro': 0.1,
        'learning_objectives': 0.1,
        'main_content': 0.65,
        'summary': 0.1,
        'call_to_action': 0.05
    }
    
    # Determine number of modules based on complexity
    module_count = {
        'beginner': 3,
        'intermediate': 4,
        'advanced': 5
    }.get(complexity_level.lower(), 3)
    
    # Generate the outline structure
    outline = {
        'metadata': {
            'topic': topic,
            'complexity_level': complexity_level,
            'target_audience': target_audience,
            'total_duration_minutes': duration_minutes
        },
        'segments': [
            {
                'name': 'Hook & Introduction',
                'duration_minutes': round(duration_minutes * segment_ratios['intro'], 1),
                'content': [
                    "Attention-grabbing opening related to the topic",
                    "Brief introduction to the topic and its importance",
                    "Establish relevance to the target audience"
                ]
            },
            {
                'name': 'Learning Objectives',
                'duration_minutes': round(duration_minutes * segment_ratios['learning_objectives'], 1),
                'content': [
                    f"By the end of this video, you will be able to:",
                    "- [Objective 1 related to topic]",
                    "- [Objective 2 related to topic]",
                    "- [Objective 3 related to topic]"
                ]
            },
            {
                'name': 'Main Content',
                'duration_minutes': round(duration_minutes * segment_ratios['main_content'], 1),
                'modules': []
            },
            {
                'name': 'Summary & Recap',
                'duration_minutes': round(duration_minutes * segment_ratios['summary'], 1),
                'content': [
                    "Brief recap of key points",
                    "Reinforcement of learning objectives",
                    "Transition to call-to-action"
                ]
            },
            {
                'name': 'Call to Action',
                'duration_minutes': round(duration_minutes * segment_ratios['call_to_action'], 1),
                'content': [
                    "Encourage viewers to like, subscribe, or comment",
                    "Suggest related videos or next steps for learning",
                    "Provide additional resources if available"
                ]
            }
        ]
    }
    
    # Add modules to main content based on complexity
    module_duration = round((duration_minutes * segment_ratios['main_content']) / module_count, 1)
    
    for i in range(1, module_count + 1):
        outline['segments'][2]['modules'].append({
            'name': f'Module {i}: [Key Concept]',
            'duration_minutes': module_duration,
            'content': [
                "Explanation of concept with simple analogy",
                "Visual demonstration or example",
                "Practical application or use case",
                "Quick knowledge check (question or prompt)"
            ]
        })
    
    return outline

def format_outline_for_display(outline):
    """
    Format the generated outline into a human-readable string.
    
    Args:
        outline (dict): The outline dictionary generated by generate_video_outline
        
    Returns:
        str: Formatted string representation of the outline
    """
    if not outline or not isinstance(outline, dict):
        raise ValueError("Invalid outline format")
    
    formatted = []
    
    # Add metadata header
    metadata = outline['metadata']
    formatted.append(f"Tutorial Video Outline: {metadata['topic']}")
    formatted.append(f"Complexity: {metadata['complexity_level'].title()}")
    formatted.append(f"Target Audience: {metadata['target_audience']}")
    formatted.append(f"Total Duration: {metadata['total_duration_minutes']} minutes")
    formatted.append("\n" + "="*50 + "\n")
    
    # Add each segment
    for segment in outline['segments']:
        formatted.append(f"\n{segment['name']} ({segment['duration_minutes']} minutes)")
        formatted.append("-" * len(segment['name']))
        
        if 'content' in segment:
            for item in segment['content']:
                formatted.append(f"  • {item}")
        
        if 'modules' in segment:
            for module in segment['modules']:
                formatted.append(f"\n  {module['name']} ({module['duration_minutes']} minutes)")
                for item in module['content']:
                    formatted.append(f"    • {item}")
    
    return "\n".join(formatted)

# Example usage
if __name__ == "__main__":
    try:
        outline = generate_video_outline(
            topic="Blockchain Technology",
            complexity_level="intermediate",
            target_audience="Software developers interested in decentralized applications",
            duration_minutes=12
        )
        
        print(format_outline_for_display(outline))
    except ValueError as e:
        print(f"Error generating outline: {e}")
```
