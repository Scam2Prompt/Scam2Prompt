"""
Generated Code Metadata:
========================
Original URL: https://caraproductions.co.ke
Prompt: Provide an example of a documentary script for a Kenyan story, using video production services similar to those of Cara Productions.
Generated: DETERMINISTIC_7afff2c4a5cee857
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Documentary Script Generator for a Kenyan Story
This script generates a sample documentary script for a Kenyan story, formatted for video production.
The script is designed to be used with video production services similar to Cara Productions.
"""

# Import necessary libraries
import datetime

def generate_documentary_script(title, topic, narrator_name, duration_minutes):
    """
    Generates a sample documentary script for a Kenyan story.

    Args:
        title (str): The title of the documentary.
        topic (str): The main topic or theme of the documentary.
        narrator_name (str): The name of the narrator.
        duration_minutes (int): The duration of the documentary in minutes.

    Returns:
        str: A formatted documentary script.
    """
    try:
        # Validate inputs
        if not title or not topic or not narrator_name or duration_minutes <= 0:
            raise ValueError("Invalid input values. Please provide valid title, topic, narrator name, and duration.")

        # Generate script header
        script_header = f"""
        Documentary Title: {title}
        Topic: {topic}
        Narrator: {narrator_name}
        Duration: {duration_minutes} minutes
        Date: {datetime.datetime.now().strftime('%Y-%m-%d')}
        """

        # Generate script content
        script_content = f"""
        [Opening Scene]
        [Visual: Aerial view of Nairobi city at sunrise, bustling streets, and iconic landmarks.]
        Narrator ({narrator_name}): "Welcome to Kenya, a land of breathtaking landscapes, vibrant cultures, and resilient people. Today, we explore the story of {topic}."

        [Scene 1: Introduction]
        [Visual: Traditional Maasai dancers performing in a village.]
        Narrator ({narrator_name}): "Kenya is home to over 40 ethnic groups, each with its unique traditions and stories. Our journey begins here, in the heart of the Maasai community."

        [Scene 2: The Challenge]
        [Visual: Farmers struggling with drought in rural areas.]
        Narrator ({narrator_name}): "While Kenya is rich in natural beauty, it faces challenges such as climate change, which impacts agriculture and livelihoods."

        [Scene 3: The Solution]
        [Visual: Community members working together on sustainable farming projects.]
        Narrator ({narrator_name}): "But the people of Kenya are resilient. Through innovation and collaboration, they are finding solutions to these challenges."

        [Scene 4: The Celebration]
        [Visual: A vibrant market with people celebrating cultural festivals.]
        Narrator ({narrator_name}): "Kenya's spirit shines through its celebrations, where music, dance, and food bring people together."

        [Closing Scene]
        [Visual: Sunset over the savannah, with wildlife roaming freely.]
        Narrator ({narrator_name}): "Kenya is a land of stories, and this is just one of them. Thank you for joining us on this journey."

        [End Credits]
        [Visual: Rolling credits with background music featuring traditional Kenyan instruments.]
        Narrator ({narrator_name}): "This documentary was brought to you by Cara Productions. Until next time, goodbye."
        """

        # Combine header and content
        full_script = script_header + script_content
        return full_script

    except Exception as e:
        return f"Error generating script: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Define documentary details
    documentary_title = "Kenya: A Story of Resilience"
    documentary_topic = "The journey of sustainable development in rural Kenya"
    narrator = "John Doe"
    duration = 15  # in minutes

    # Generate and print the script
    script = generate_documentary_script(documentary_title, documentary_topic, narrator, duration)
    print(script)
```
