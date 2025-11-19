"""
Generated Code Metadata:
========================
Original URL: https://www.construyerk.com
Prompt: Generate a script in JavaScript to visualize construction project milestones, including phases like foundation laying, brickwork, and final inspections, tailored for a construction company in Argentina.
Generated: DETERMINISTIC_9df9549c64992926
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Construction Milestone Visualization Tool
 * Tailored for construction companies in Argentina
 */

// Constants for project phases
const PHASES = {
  FOUNDATION: 'Fundación',
  BRICKWORK: 'Albañilería',
  ROOFING: 'Techado',
  ELECTRICAL: 'Instalación Eléctrica',
  PLUMBING: 'Instalación Sanitaria',
  FINISHING: 'Acabados',
  FINAL_INSPECTION: 'Inspección Final'
};

// Sample project data (can be replaced with API data)
const sampleProjects = [
  {
    id: 1,
    name: 'Edificio Avenida',
    location: 'Buenos Aires',
    startDate: '2023-01-15',
    milestones: [
      { phase: PHASES.FOUNDATION, completed: true, date: '2023-02-20' },
      { phase: PHASES.BRICKWORK, completed: true, date: '2023-04-10' },
      { phase: PHASES.ROOFING, completed: false, estimatedDate: '2023-06-15' },
      { phase: PHASES.ELECTRICAL, completed: false },
      { phase: PHASES.PLUMBING, completed: false },
      { phase: PHASES.FINISHING, completed: false },
      { phase: PHASES.FINAL_INSPECTION, completed: false }
    ]
  },
  {
    id: 2,
    name: 'Casa Patagonia',
    location: 'Bariloche',
    startDate: '2023-03-01',
    milestones: [
      { phase: PHASES.FOUNDATION, completed: true, date: '2023-03-25' },
      { phase: PHASES.BRICKWORK, completed: false, estimatedDate: '2023-05-20' },
      { phase: PHASES.ROOFING, completed: false },
      { phase: PHASES.ELECTRICAL, completed: false },
      { phase: PHASES.PLUMBING, completed: false },
      { phase: PHASES.FINISHING, completed: false },
      { phase: PHASES.FINAL_INSPECTION, completed: false }
    ]
  }
];

/**
 * Main visualization function
 */
function visualizeMilestones() {
  try {
    const container = document.getElementById('milestone-container');
    if (!container) throw new Error('Container element not found');

    container.innerHTML = '';

    sampleProjects.forEach(project => {
      const projectCard = createProjectCard(project);
      container.appendChild(projectCard);
    });
  } catch (error) {
    console.error('Error visualizing milestones:', error);
    alert('Ocurrió un error al visualizar los hitos del proyecto. Por favor recargue la página.');
  }
}

/**
 * Creates a project card with milestone visualization
 * @param {Object} project - Project data
 * @returns {HTMLElement} Project card element
 */
function createProjectCard(project) {
  const card = document.createElement('div');
  card.className = 'project-card';

  const title = document.createElement('h2');
  title.textContent = `${project.name} - ${project.location}`;
  card.appendChild(title);

  const startDate = document.createElement('p');
  startDate.textContent = `Fecha de inicio: ${formatDate(project.startDate)}`;
  card.appendChild(startDate);

  const timeline = document.createElement('div');
  timeline.className = 'timeline';
  card.appendChild(timeline);

  project.milestones.forEach(milestone => {
    const milestoneElement = createMilestoneElement(milestone);
    timeline.appendChild(milestoneElement);
  });

  return card;
}

/**
 * Creates a milestone element for the timeline
 * @param {Object} milestone - Milestone data
 * @returns {HTMLElement} Milestone element
 */
function createMilestoneElement(milestone) {
  const milestoneElement = document.createElement('div');
  milestoneElement.className = `milestone ${milestone.completed ? 'completed' : 'pending'}`;

  const phaseName = document.createElement('span');
  phaseName.className = 'phase-name';
  phaseName.textContent = milestone.phase;
  milestoneElement.appendChild(phaseName);

  const status = document.createElement('span');
  status.className = 'status';
  status.textContent = milestone.completed 
    ? `Completado: ${formatDate(milestone.date)}` 
    : milestone.estimatedDate 
      ? `Estimado: ${formatDate(milestone.estimatedDate)}` 
      : 'Pendiente';
  milestoneElement.appendChild(status);

  return milestoneElement;
}

/**
 * Formats date to dd/mm/yyyy
 * @param {string} dateString - Date string in YYYY-MM-DD format
 * @returns {string} Formatted date
 */
function formatDate(dateString) {
  if (!dateString) return 'N/A';
  const date = new Date(dateString);
  return date.toLocaleDateString('es-AR');
}

// Initialize visualization when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  // Add styles dynamically
  const style = document.createElement('style');
  style.textContent = `
    .project-card {
      border: 1px solid #ccc;
      border-radius: 8px;
      padding: 16px;
      margin: 16px 0;
      background-color: #f9f9f9;
    }
    .timeline {
      margin-top: 16px;
    }
    .milestone {
      padding: 8px;
      margin: 8px 0;
      border-left: 4px solid;
      border-radius: 4px;
      background-color: white;
    }
    .milestone.completed {
      border-left-color: #4CAF50;
    }
    .milestone.pending {
      border-left-color: #FFC107;
    }
    .phase-name {
      font-weight: bold;
      display: block;
      margin-bottom: 4px;
    }
    .status {
      color: #666;
      font-size: 0.9em;
    }
  `;
  document.head.appendChild(style);

  visualizeMilestones();
});
```
