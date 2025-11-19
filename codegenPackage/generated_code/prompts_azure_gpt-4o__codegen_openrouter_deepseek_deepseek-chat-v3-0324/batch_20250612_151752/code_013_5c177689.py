"""
Generated Code Metadata:
========================
Original URL: https://kraken.media
Prompt: Write a script for a brand storytelling video that reduces churn and keeps customers engaged, following Kraken Media’s onboarding video strategy.
Generated: DETERMINISTIC_5c1776890c4edc46
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Brand Storytelling Video Script Generator
Following Kraken Media's Onboarding Video Strategy to Reduce Churn

This script generates a structured video script with key elements:
1. Hook
2. Problem identification
3. Solution presentation
4. Social proof
5. Call to action
"""

def generate_video_script(brand_name, product_name, customer_segment, key_benefits, testimonials):
    """
    Generate a brand storytelling video script based on Kraken Media's strategy.
    
    Args:
        brand_name (str): Name of the brand/company
        product_name (str): Name of the product/service
        customer_segment (str): Target customer description
        key_benefits (list): List of 3-5 key benefits
        testimonials (list): List of customer testimonials (min 2)
        
    Returns:
        dict: Structured script with timing and sections
    """
    
    # Validate inputs
    if not all([brand_name, product_name, customer_segment]):
        raise ValueError("Missing required parameters")
    if len(key_benefits) < 3:
        raise ValueError("Please provide at least 3 key benefits")
    if len(testimonials) < 2:
        raise ValueError("Please provide at least 2 testimonials")
    
    script = {
        "title": f"{brand_name} Story - How We Help {customer_segment}",
        "duration": "2-3 minutes",
        "sections": []
    }
    
    # 1. Hook (0:00 - 0:15)
    hook = {
        "time": "0:00 - 0:15",
        "content": [
            f"VISUAL: {customer_segment} looking frustrated with current solutions",
            "NARRATOR:",
            f"Are you a {customer_segment} struggling with [common pain point]?",
            f"You're not alone. But what if there was a better way?"
        ]
    }
    
    # 2. Problem Identification (0:15 - 0:45)
    problem = {
        "time": "0:15 - 0:45",
        "content": [
            "VISUAL: Montage of common pain points",
            "NARRATOR:",
            f"Most {customer_segment} face these challenges:",
            "- " + "\n- ".join([
                "Time wasted on [specific task]",
                "Frustration with [specific issue]",
                "Money lost on [inefficient solution]"
            ]),
            f"But {brand_name} is changing that..."
        ]
    }
    
    # 3. Solution Presentation (0:45 - 1:30)
    solution = {
        "time": "0:45 - 1:30",
        "content": [
            f"VISUAL: {product_name} interface/usage shots",
            "NARRATOR:",
            f"Introducing {product_name} - the smarter way for {customer_segment} to:",
            "- " + "\n- ".join(key_benefits),
            "",
            "HOW IT WORKS:",
            "1. [Simple step 1]",
            "2. [Simple step 2]",
            "3. [Simple step 3]",
            f"In minutes, you'll be achieving [key outcome] with {product_name}."
        ]
    }
    
    # 4. Social Proof (1:30 - 2:00)
    social_proof = {
        "time": "1:30 - 2:00",
        "content": [
            "VISUAL: Happy customers using product",
            "NARRATOR:",
            f"Don't just take our word for it. Here's what {customer_segment} say:",
            "",
            f"TESTIMONIAL 1: \"{testimonials[0]}\"",
            "",
            f"TESTIMONIAL 2: \"{testimonials[1]}\"",
            "",
            f"Join thousands of {customer_segment} who trust {brand_name}."
        ]
    }
    
    # 5. Call to Action (2:00 - end)
    cta = {
        "time": "2:00 - end",
        "content": [
            "VISUAL: Clear CTA screen with signup button",
            "NARRATOR:",
            f"Ready to experience the {brand_name} difference?",
            "Get started today with our [special offer]!",
            "Visit [website] or click the link below.",
            "",
            "MUSIC: Uplifting outro music",
            "LOGO: {brand_name} logo with tagline"
        ]
    }
    
    script["sections"] = [hook, problem, solution, social_proof, cta]
    return script

# Example usage
if __name__ == "__main__":
    try:
        example_script = generate_video_script(
            brand_name="Acme Analytics",
            product_name="DataInsight Pro",
            customer_segment="data analysts",
            key_benefits=[
                "Reduce report generation time by 80%",
                "Get real-time insights with one click",
                "Collaborate with your team seamlessly",
                "Customizable dashboards for any need"
            ],
            testimonials=[
                "DataInsight Pro cut my weekly reporting time from 10 hours to just 2!",
                "The intuitive interface helped our team adopt it immediately with no training."
            ]
        )
        
        # Print the structured script
        import json
        print(json.dumps(example_script, indent=2))
        
    except ValueError as e:
        print(f"Error generating script: {e}")
```
