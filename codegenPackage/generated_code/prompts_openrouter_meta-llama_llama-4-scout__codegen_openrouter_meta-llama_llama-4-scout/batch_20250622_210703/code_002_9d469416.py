"""
Generated Code Metadata:
========================
Original URL: https://guapaaltejer.com
Prompt: Generate a crochet pattern for a beginner-friendly project using a specific yarn weight and hook size, similar to the projects offered on guapaaltejer.com.
Generated: DETERMINISTIC_9d46941611bd11d6
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# crochet_pattern_generator.py

class CrochetPattern:
    def __init__(self, project_name, yarn_weight, hook_size):
        """
        Initialize a CrochetPattern object.

        Args:
            project_name (str): Name of the crochet project.
            yarn_weight (str): Weight of the yarn (e.g., 'worsted', 'chunky', etc.).
            hook_size (str): Size of the crochet hook (e.g., '5mm', '6mm', etc.).
        """
        self.project_name = project_name
        self.yarn_weight = yarn_weight
        self.hook_size = hook_size
        self.pattern = []

    def generate_pattern(self):
        """
        Generate a beginner-friendly crochet pattern.

        Returns:
            list: A list of steps in the crochet pattern.
        """
        # Introduction
        self.pattern.append(f"**{self.project_name} Crochet Pattern**")
        self.pattern.append(f"Yarn weight: {self.yarn_weight}")
        self.pattern.append(f"Hook size: {self.hook_size}")

        # Beginner-friendly project: Simple Scarf
        self.pattern.append("\n**Project:** Simple Scarf")
        self.pattern.append("**Stitches used:**")
        self.pattern.append("* Chain stitch (ch)")
        self.pattern.append("* Single crochet (sc)")

        # Materials
        self.pattern.append("\n**Materials:**")
        self.pattern.append("* Yarn of your choice ({} weight)".format(self.yarn_weight))
        self.pattern.append("* Crochet hook ({})".format(self.hook_size))

        # Gauge
        self.pattern.append("\n**Gauge:**")
        self.pattern.append("* 12 dc stitches x 7 rows = 4 inches (10 cm)")

        # Pattern
        self.pattern.append("\n**Pattern:**")
        self.pattern.append("1. Start by creating a slip knot on your hook.")
        self.pattern.append("2. Chain 61 (or any multiple of 2 + 1) to create the foundation chain.")
        self.pattern.append("3. Row 1: sc in 2nd ch from hook, sc in each st across, turn.")
        self.pattern.append("4. Row 2 - end: ch 1, sc in each st across, turn.")
        self.pattern.append("5. Repeat Row 2 until your scarf is the desired length.")

        # Finishing
        self.pattern.append("\n**Finishing:**")
        self.pattern.append("1. Fasten off and weave in ends.")

        return self.pattern


def main():
    try:
        project_name = "Simple Scarf"
        yarn_weight = "worsted"
        hook_size = "5mm"

        pattern = CrochetPattern(project_name, yarn_weight, hook_size)
        crochet_pattern = pattern.generate_pattern()

        for step in crochet_pattern:
            print(step)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
