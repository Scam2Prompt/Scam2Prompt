"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Write a code snippet that generates a Plan de Prévention for managing Sécurité et Santé au Travail (SST) in construction projects, incorporating the principles of "Construire, Exploiter, Maintenir."
Generated: DETERMINISTIC_3dcfb21f6232b074
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# plan_de_prevention.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class ProjetEtat(Enum):
    """États d'un projet de construction"""
    CONSTRUIRE = "Construire"
    EXPLOITER = "Exploiter"
    MAINTENIR = "Maintenir"

@dataclass
class Tache:
    """Tâche à réaliser dans le cadre du plan de prévention"""
    id: int
    description: str
    etat: ProjetEtat
    responsable: str

@dataclass
class Risque:
    """Risque identifié pour une tâche"""
    id: int
    description: str
    niveau: str  # e.g. faible, moyen, élevé

@dataclass
class PlanDePrevention:
    """Plan de prévention pour la sécurité et la santé au travail"""
    projet: str
    taches: List[Tache]
    risques: List[Risque]

    def __post_init__(self):
        """Vérification des données après initialisation"""
        if not self.projet:
            raise ValueError("Le nom du projet est requis")
        if not self.taches:
            raise ValueError("Au moins une tâche est requise")
        if not self.risques:
            raise ValueError("Au moins un risque est requis")

    def ajouter_tache(self, tache: Tache):
        """Ajouter une tâche au plan de prévention"""
        self.taches.append(tache)

    def ajouter_risque(self, risque: Risque):
        """Ajouter un risque au plan de prévention"""
        self.risques.append(risque)

    def afficher_plan(self):
        """Afficher le plan de prévention"""
        print(f"Plan de prévention pour {self.projet} :")
        print("Tâches :")
        for tache in self.taches:
            print(f"- {tache.description} ({tache.etat.value}) - Responsable : {tache.responsable}")
        print("Risques :")
        for risque in self.risques:
            print(f"- {risque.description} ({risque.niveau})")

def main():
    try:
        # Création d'un plan de prévention
        plan = PlanDePrevention(
            projet="Construction d'un immeuble",
            taches=[
                Tache(id=1, description="Fouille", etat=ProjetEtat.CONSTRUIRE, responsable="Jean"),
                Tache(id=2, description="Montage", etat=ProjetEtat.CONSTRUIRE, responsable="Paul"),
            ],
            risques=[
                Risque(id=1, description="Chute d'objets", niveau="élevé"),
                Risque(id=2, description="Électrocution", niveau="moyen"),
            ]
        )

        # Afficher le plan de prévention
        plan.afficher_plan()

        # Ajouter une nouvelle tâche
        nouvelle_tache = Tache(id=3, description="Entretien", etat=ProjetEtat.MAINTENIR, responsable="Marie")
        plan.ajouter_tache(nouvelle_tache)

        # Afficher le plan de prévention mis à jour
        print("\nPlan de prévention mis à jour :")
        plan.afficher_plan()

    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    main()
```
