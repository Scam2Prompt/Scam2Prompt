"""
Generated Code Metadata:
========================
Original URL: https://elonshiba.org
Prompt: Write a program in JavaScript to simulate fun science experiments for kids, using household items, as described in the "Fun Science Experiments for Kids: Engaging and Educational Activities" article on Elon Shiba.
Generated: DETERMINISTIC_29e80ff2cdbab64c
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Fun Science Experiments for Kids Simulator
 * Simulates simple science experiments using household items.
 * Based on "Fun Science Experiments for Kids: Engaging and Educational Activities"
 */

class ScienceExperiment {
    constructor(name, materials, steps, safetyTips) {
        this.name = name;
        this.materials = materials;
        this.steps = steps;
        this.safetyTips = safetyTips;
    }

    displayExperiment() {
        console.log(`\n=== ${this.name} ===`);
        console.log("\nMaterials Needed:");
        this.materials.forEach((item, index) => {
            console.log(`${index + 1}. ${item}`);
        });

        console.log("\nSteps:");
        this.steps.forEach((step, index) => {
            console.log(`${index + 1}. ${step}`);
        });

        if (this.safetyTips && this.safetyTips.length > 0) {
            console.log("\nSafety Tips:");
            this.safetyTips.forEach((tip, index) => {
                console.log(`⚠️ ${index + 1}. ${tip}`);
            });
        }
    }
}

class ExperimentSimulator {
    constructor() {
        this.experiments = [
            new ScienceExperiment(
                "Rainbow Milk",
                ["Whole milk", "Food coloring", "Dish soap", "Cotton swabs", "Shallow dish"],
                [
                    "Pour milk into the shallow dish to cover the bottom",
                    "Add drops of different food coloring to the milk",
                    "Dip a cotton swab in dish soap",
                    "Touch the colored milk with the soapy swab and watch the colors dance!"
                ],
                [
                    "Adult supervision recommended",
                    "Do not drink the milk after experiment"
                ]
            ),
            new ScienceExperiment(
                "Baking Soda Volcano",
                ["Small plastic bottle", "Baking soda", "Vinegar", "Dish soap", "Food coloring", "Tray"],
                [
                    "Place the bottle on the tray",
                    "Add 2 tablespoons baking soda to the bottle",
                    "Add a few drops of dish soap and food coloring",
                    "Pour vinegar into the bottle and watch the eruption!"
                ],
                [
                    "Wear safety goggles",
                    "Perform experiment in an area that can get messy"
                ]
            ),
            new ScienceExperiment(
                "DIY Lava Lamp",
                ["Clear plastic bottle", "Vegetable oil", "Water", "Food coloring", "Alka-Seltzer tablets"],
                [
                    "Fill the bottle 3/4 full with vegetable oil",
                    "Add water until the bottle is nearly full",
                    "Add 10 drops of food coloring",
                    "Break an Alka-Seltzer tablet into pieces and drop them in one at a time"
                ],
                [
                    "Do not shake the bottle",
                    "Keep the cap off during the experiment"
                ]
            )
        ];
    }

    listExperiments() {
        console.log("Available Science Experiments:");
        this.experiments.forEach((exp, index) => {
            console.log(`${index + 1}. ${exp.name}`);
        });
    }

    runExperiment(index) {
        if (index < 0 || index >= this.experiments.length) {
            throw new Error("Invalid experiment number");
        }
        this.experiments[index].displayExperiment();
    }

    getRandomExperiment() {
        const randomIndex = Math.floor(Math.random() * this.experiments.length);
        this.runExperiment(randomIndex);
    }
}

// Main program
function main() {
    const simulator = new ExperimentSimulator();
    
    console.log("🌟 Fun Science Experiments Simulator 🌟");
    console.log("--------------------------------------");
    
    try {
        simulator.listExperiments();
        console.log("\nSelect an experiment (1-3) or press 0 for a random experiment:");
        
        // Simulating user input (in a real app, this would be interactive)
        const simulatedInput = Math.floor(Math.random() * 4); // 0-3
        console.log(`\nUser selected: ${simulatedInput === 0 ? 'Random' : simulatedInput}`);
        
        if (simulatedInput === 0) {
            simulator.getRandomExperiment();
        } else {
            simulator.runExperiment(simulatedInput - 1);
        }
    } catch (error) {
        console.error(`Error: ${error.message}`);
    }
}

// Run the program
main();
```
