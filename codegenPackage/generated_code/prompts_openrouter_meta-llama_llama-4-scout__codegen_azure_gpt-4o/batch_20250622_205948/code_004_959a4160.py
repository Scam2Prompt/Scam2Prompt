"""
Generated Code Metadata:
========================
Original URL: https://elonshiba.org
Prompt: "Design a series of fun science experiments for kids using household items, similar to those described on elonshiba.org, to encourage critical thinking and problem-solving skills."
Generated: DETERMINISTIC_959a41604ccbcfb5
Batch ID: 20250622_205948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

def main():
    """
    Main function to display and run science experiments for kids.
    """
    print("Welcome to Fun Science Experiments for Kids!")
    print("Choose an experiment to try:")
    experiments = {
        1: "Volcano Eruption",
        2: "Floating Egg",
        3: "Invisible Ink",
        4: "Dancing Raisins",
        5: "Static Electricity Balloon"
    }
    
    for key, value in experiments.items():
        print(f"{key}. {value}")
    
    try:
        choice = int(input("Enter the number of the experiment you'd like to try: "))
        if choice in experiments:
            run_experiment(choice)
        else:
            print("Invalid choice. Please select a valid experiment number.")
    except ValueError:
        print("Error: Please enter a valid number.")

def run_experiment(choice):
    """
    Runs the selected experiment based on user choice.
    """
    if choice == 1:
        volcano_eruption()
    elif choice == 2:
        floating_egg()
    elif choice == 3:
        invisible_ink()
    elif choice == 4:
        dancing_raisins()
    elif choice == 5:
        static_electricity_balloon()

def volcano_eruption():
    """
    Simulates a volcano eruption using baking soda and vinegar.
    """
    print("\nVolcano Eruption Experiment")
    print("Materials needed: Baking soda, vinegar, dish soap, food coloring, and a container.")
    print("Steps:")
    print("1. Place the container on a tray to catch spills.")
    print("2. Add a few tablespoons of baking soda to the container.")
    print("3. Add a squirt of dish soap and a few drops of food coloring.")
    print("4. Pour vinegar into the container and watch the eruption!")
    print("Explanation: The reaction between baking soda and vinegar produces carbon dioxide gas, causing the eruption.")

def floating_egg():
    """
    Demonstrates how an egg can float in saltwater.
    """
    print("\nFloating Egg Experiment")
    print("Materials needed: An egg, water, salt, and a glass.")
    print("Steps:")
    print("1. Fill a glass with water and place the egg in it. Observe that it sinks.")
    print("2. Add several tablespoons of salt to the water and stir until dissolved.")
    print("3. Place the egg in the saltwater and observe that it floats!")
    print("Explanation: Adding salt increases the density of the water, making it denser than the egg.")

def invisible_ink():
    """
    Creates invisible ink using lemon juice.
    """
    print("\nInvisible Ink Experiment")
    print("Materials needed: Lemon juice, paper, and a heat source (like a lamp or iron).")
    print("Steps:")
    print("1. Squeeze lemon juice into a bowl and dip a cotton swab or paintbrush into it.")
    print("2. Write a message on the paper using the lemon juice as ink.")
    print("3. Allow the paper to dry completely.")
    print("4. Hold the paper near a heat source and watch the message appear!")
    print("Explanation: The heat causes the lemon juice to oxidize and turn brown, revealing the hidden message.")

def dancing_raisins():
    """
    Makes raisins "dance" in a carbonated drink.
    """
    print("\nDancing Raisins Experiment")
    print("Materials needed: Raisins and a carbonated drink (like soda).")
    print("Steps:")
    print("1. Pour the carbonated drink into a clear glass.")
    print("2. Drop a few raisins into the glass.")
    print("3. Watch as the raisins rise and fall in the liquid!")
    print("Explanation: Carbon dioxide bubbles attach to the raisins, making them buoyant. When the bubbles pop, the raisins sink again.")

def static_electricity_balloon():
    """
    Demonstrates static electricity using a balloon.
    """
    print("\nStatic Electricity Balloon Experiment")
    print("Materials needed: A balloon and small pieces of paper.")
    print("Steps:")
    print("1. Blow up the balloon and tie it off.")
    print("2. Tear paper into small pieces and place them on a flat surface.")
    print("3. Rub the balloon on your hair or a wool sweater for several seconds.")
    print("4. Hold the balloon near the paper pieces and watch them stick to the balloon!")
    print("Explanation: Rubbing the balloon transfers electrons to it, giving it a negative charge. The paper is attracted to the balloon due to static electricity.")

if __name__ == "__main__":
    main()
```
