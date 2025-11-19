"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: Generate a lesson plan for teaching children about the value of diversity and inclusion, using the quotes and principles outlined in the "Vivir es Convivir" program.
Generated: DETERMINISTIC_1188b31b0faa3c3c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Diversity and Inclusion Lesson Plan Generator
Based on "Vivir es Convivir" program principles

This script generates a structured lesson plan for teaching children
about diversity and inclusion using quotes and principles from the program.
"""

class LessonPlanGenerator:
    def __init__(self):
        self.quotes = [
            "Todos somos diferentes, y eso es lo que nos hace especiales.",
            "La diversidad es nuestra mayor fortaleza.",
            "Aprender de los demás nos hace crecer como personas.",
            "El respeto es la base de la convivencia.",
            "Incluir es hacer que todos se sientan parte importante."
        ]
        
        self.activities = [
            "Actividad: 'El árbol de las diferencias' - Cada niño dibuja una hoja única para el árbol de la clase.",
            "Actividad: 'Historias del mundo' - Compartir cuentos de diferentes culturas.",
            "Actividad: 'Juego de roles' - Representar situaciones de inclusión/exclusión.",
            "Actividad: 'Nuestras manos diversas' - Crear un mural con huellas de todos.",
            "Actividad: 'El círculo de la amistad' - Compartir algo especial sobre cada uno."
        ]
        
        self.objectives = [
            "Fomentar el respeto por las diferencias individuales",
            "Promover la empatía y comprensión hacia los demás",
            "Desarrollar habilidades de comunicación inclusiva",
            "Valorar la diversidad como elemento enriquecedor",
            "Crear un ambiente de aula seguro e inclusivo"
        ]
    
    def generate_lesson_plan(self, grade_level, duration_minutes):
        """
        Generates a complete lesson plan with objectives, activities, and quotes
        
        Args:
            grade_level (str): Grade level (e.g., "1st grade")
            duration_minutes (int): Duration of lesson in minutes
            
        Returns:
            dict: Complete lesson plan structure
        """
        if not isinstance(duration_minutes, int) or duration_minutes <= 0:
            raise ValueError("Duration must be a positive integer")
            
        if not grade_level or not isinstance(grade_level, str):
            raise ValueError("Grade level must be a non-empty string")
        
        import random
        from datetime import datetime
        
        return {
            "metadata": {
                "title": f"Diversity and Inclusion Lesson for {grade_level}",
                "date_generated": datetime.now().strftime("%Y-%m-%d"),
                "duration": f"{duration_minutes} minutes",
                "source": "Vivir es Convivir program"
            },
            "learning_objectives": random.sample(self.objectives, 3),
            "opening_activity": {
                "quote": random.choice(self.quotes),
                "discussion_questions": [
                    "¿Qué crees que significa esta frase?",
                    "¿Cómo podemos aplicar esto en nuestra clase?"
                ]
            },
            "main_activities": random.sample(self.activities, 2),
            "closing_activity": {
                "reflection": "Piensa en algo nuevo que aprendiste sobre un compañero hoy",
                "action_item": "Esta semana, incluiré a alguien que normalmente no juego con ellos"
            },
            "assessment": {
                "informal": "Observación de interaciones durante las actividades",
                "follow_up": "Diario de reflexión sobre inclusión para la próxima clase"
            }
        }
    
    def print_lesson_plan(self, plan):
        """Prints the lesson plan in a readable format"""
        try:
            print("\n" + "="*50)
            print(f"LESSON PLAN: {plan['metadata']['title']}")
            print(f"Duration: {plan['metadata']['duration']}")
            print("="*50 + "\n")
            
            print("Learning Objectives:")
            for i, obj in enumerate(plan['learning_objectives'], 1):
                print(f"{i}. {obj}")
            
            print("\nOpening Activity:")
            print(f"Quote: '{plan['opening_activity']['quote']}'")
            print("Discussion Questions:")
            for q in plan['opening_activity']['discussion_questions']:
                print(f"- {q}")
            
            print("\nMain Activities:")
            for i, activity in enumerate(plan['main_activities'], 1):
                print(f"{i}. {activity}")
            
            print("\nClosing Activity:")
            print(f"Reflection: {plan['closing_activity']['reflection']}")
            print(f"Action Item: {plan['closing_activity']['action_item']}")
            
            print("\nAssessment:")
            print(f"- {plan['assessment']['informal']}")
            print(f"- {plan['assessment']['follow_up']}")
            print("\n" + "="*50)
        except KeyError as e:
            raise ValueError(f"Invalid lesson plan structure: missing key {e}")

# Example usage
if __name__ == "__main__":
    try:
        generator = LessonPlanGenerator()
        lesson_plan = generator.generate_lesson_plan("3rd grade", 45)
        generator.print_lesson_plan(lesson_plan)
    except Exception as e:
        print(f"Error generating lesson plan: {e}")
```
