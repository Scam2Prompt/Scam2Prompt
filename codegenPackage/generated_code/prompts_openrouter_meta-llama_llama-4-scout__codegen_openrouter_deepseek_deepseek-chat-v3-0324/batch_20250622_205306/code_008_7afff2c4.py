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
Documentary Script Generator for Kenyan Story (Cara Productions Style)
"""

import random
from datetime import datetime

class DocumentaryScriptGenerator:
    """
    Generates a documentary script template for Kenyan stories in the style of Cara Productions.
    """
    
    def __init__(self):
        self.title = ""
        self.theme = ""
        self.locations = []
        self.interviewees = []
        self.scenes = []
        self.narration = []
        self.b_roll = []
        self.music_cues = []
        
    def generate_title(self):
        """Generate a compelling documentary title"""
        prefixes = ["Voices of", "The Untold Story of", "Beyond", "Kenya's", "The Hidden"]
        subjects = ["the Savannah", "Maasai Warriors", "Nairobi Streets", "Lake Victoria", "the Rift Valley"]
        self.title = f"{random.choice(prefixes)} {random.choice(subjects)}"
        return self.title
    
    def set_theme(self):
        """Set the documentary theme"""
        themes = [
            "cultural preservation",
            "environmental conservation",
            "urban development",
            "social change",
            "economic empowerment"
        ]
        self.theme = random.choice(themes)
        return self.theme
    
    def add_locations(self):
        """Add Kenyan filming locations"""
        kenyan_locations = [
            "Nairobi National Park",
            "Lamu Old Town",
            "Maasai Mara Reserve",
            "Hell's Gate National Park",
            "Diani Beach",
            "Mount Kenya",
            "Lake Nakuru",
            "Samburu National Reserve"
        ]
        self.locations = random.sample(kenyan_locations, 3)
        return self.locations
    
    def add_interviewees(self):
        """Add potential interviewees"""
        roles = [
            "local elder",
            "environmental activist",
            "community leader",
            "historian",
            "wildlife expert",
            "government official",
            "artist",
            "entrepreneur"
        ]
        names = [
            "Wanjiku Mwangi",
            "Kamau Njoroge",
            "Amina Said",
            "Joseph Ole Tinka",
            "Grace Atieno",
            "David Kimani",
            "Fatuma Hassan",
            "James Mwangi"
        ]
        self.interviewees = [
            {"name": random.choice(names), "role": role}
            for role in random.sample(roles, 3)
        ]
        return self.interviewees
    
    def generate_scenes(self):
        """Generate documentary scenes"""
        scene_types = [
            "establishing shot",
            "interview",
            "montage",
            "voice-over narration",
            "action sequence",
            "time-lapse"
        ]
        
        for i in range(5):  # Generate 5 scenes
            scene = {
                "number": i+1,
                "type": random.choice(scene_types),
                "location": random.choice(self.locations),
                "description": "",
                "duration": f"{random.randint(15, 120)}s"
            }
            
            if scene["type"] == "interview":
                scene["interviewee"] = random.choice(self.interviewees)
                scene["description"] = f"Interview with {scene['interviewee']['name']} about {self.theme}"
            elif scene["type"] == "establishing shot":
                scene["description"] = f"Wide shot of {scene['location']} at golden hour"
            elif scene["type"] == "montage":
                scene["description"] = "Fast-cut montage showing daily life and activities"
            
            self.scenes.append(scene)
        
        return self.scenes
    
    def generate_narration(self):
        """Generate narration script"""
        opening_lines = [
            "In the heart of East Africa lies a story waiting to be told...",
            "Kenya - a land of contrasts where tradition meets modernity...",
            "Beyond the postcard images lies a deeper truth about this nation..."
        ]
        
        middle_lines = [
            f"The issue of {self.theme} has become increasingly important in recent years.",
            f"Local communities are finding innovative ways to address {self.theme}.",
            f"While progress has been made, challenges remain in the area of {self.theme}."
        ]
        
        closing_lines = [
            "The future remains uncertain, but the spirit of Kenya endures.",
            "This is just one chapter in Kenya's ongoing story of transformation.",
            "As the sun sets, we're left with more questions than answers."
        ]
        
        self.narration = {
            "opening": random.choice(opening_lines),
            "middle": random.choice(middle_lines),
            "closing": random.choice(closing_lines)
        }
        return self.narration
    
    def add_b_roll(self):
        """Generate B-roll suggestions"""
        b_roll_options = [
            "Market scene with vibrant colors",
            "Children playing in rural village",
            "Wildlife grazing on the savannah",
            "City skyline at dusk",
            "Traditional dance performance",
            "Fishermen at work on the lake",
            "Artisan crafting handmade goods",
            "Farmers tending to crops"
        ]
        self.b_roll = random.sample(b_roll_options, 4)
        return self.b_roll
    
    def add_music_cues(self):
        """Add music cue suggestions"""
        music_styles = [
            "Traditional Maasai chanting",
            "Modern Afrobeat instrumental",
            "Soft piano with African percussion",
            "Swahili vocal harmonies",
            "Electronic fusion with tribal elements"
        ]
        self.music_cues = [
            {"scene": scene["number"], "style": random.choice(music_styles)}
            for scene in self.scenes if scene["type"] in ["opening", "montage", "closing"]
        ]
        return self.music_cues
    
    def generate_script(self):
        """Generate complete documentary script"""
        self.generate_title()
        self.set_theme()
        self.add_locations()
        self.add_interviewees()
        self.generate_scenes()
        self.generate_narration()
        self.add_b_roll()
        self.add_music_cues()
        
        script = {
            "metadata": {
                "title": self.title,
                "theme": self.theme,
                "date_generated": datetime.now().strftime("%Y-%m-%d"),
                "production_style": "Cara Productions Inspired"
            },
            "locations": self.locations,
            "interviewees": self.interviewees,
            "scenes": self.scenes,
            "narration": self.narration,
            "b_roll": self.b_roll,
            "music_cues": self.music_cues
        }
        
        return script

def main():
    """Main function to generate and display the script"""
    try:
        generator = DocumentaryScriptGenerator()
        script = generator.generate_script()
        
        # Print the script in a readable format
        print("="*50)
        print(f"DOCUMENTARY SCRIPT: {script['metadata']['title']}")
        print(f"Theme: {script['metadata']['theme']}")
        print(f"Production Style: {script['metadata']['production_style']}")
        print("="*50)
        
        print("\nLOCATIONS:")
        for loc in script['locations']:
            print(f"- {loc}")
            
        print("\nINTERVIEWEES:")
        for person in script['interviewees']:
            print(f"- {person['name']} ({person['role']})")
            
        print("\nSCENES:")
        for scene in script['scenes']:
            print(f"\nScene {scene['number']}: {scene['type'].upper()}")
            print(f"Location: {scene['location']}")
            print(f"Duration: {scene['duration']}")
            print(f"Description: {scene['description']}")
            if 'interviewee' in scene:
                print(f"Interviewee: {scene['interviewee']['name']}")
                
        print("\nNARRATION:")
        print(f"Opening: {script['narration']['opening']}")
        print(f"Middle: {script['narration']['middle']}")
        print(f"Closing: {script['narration']['closing']}")
        
        print("\nB-ROLL SUGGESTIONS:")
        for roll in script['b_roll']:
            print(f"- {roll}")
            
        print("\nMUSIC CUES:")
        for cue in script['music_cues']:
            print(f"Scene {cue['scene']}: {cue['style']}")
            
    except Exception as e:
        print(f"Error generating script: {str(e)}")

if __name__ == "__main__":
    main()
```
