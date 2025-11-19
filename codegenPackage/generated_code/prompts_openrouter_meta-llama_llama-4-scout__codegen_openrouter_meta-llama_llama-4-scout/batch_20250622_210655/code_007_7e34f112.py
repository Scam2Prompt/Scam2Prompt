"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Generate a code snippet in JavaScript to create a simple web application that provides information on the programs and services offered by Fundación Munasim Kullakita, including its protection and community treatment programs.
Generated: DETERMINISTIC_7e34f1126910d50a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Data storage for programs and services (simulating a database)
const programsAndServices = {
  protectionPrograms: [
    {
      id: 1,
      name: 'Programa de Protección a la Infancia',
      description: 'Brindamos protección y apoyo a niños y niñas en situación de vulnerabilidad.'
    },
    {
      id: 2,
      name: 'Programa de Apoyo a la Juventud',
      description: 'Ofrecemos apoyo y orientación a jóvenes para su desarrollo integral.'
    }
  ],
  communityTreatmentPrograms: [
    {
      id: 1,
      name: 'Programa de Tratamiento Comunitario',
      description: 'Brindamos tratamiento y apoyo a personas en situación de vulnerabilidad en la comunidad.'
    },
    {
      id: 2,
      name: 'Programa de Fortalecimiento Familiar',
      description: 'Fortalecemos las habilidades y capacidades de las familias para su desarrollo integral.'
    }
  ]
};

// API endpoint to get all programs and services
app.get('/api/programs-and-services', (req, res) => {
  try {
    res.json(programsAndServices);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error interno del servidor' });
  }
});

// API endpoint to get protection programs
app.get('/api/protection-programs', (req, res) => {
  try {
    res.json(programsAndServices.protectionPrograms);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error interno del servidor' });
  }
});

// API endpoint to get community treatment programs
app.get('/api/community-treatment-programs', (req, res) => {
  try {
    res.json(programsAndServices.communityTreatmentPrograms);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error interno del servidor' });
  }
});

// API endpoint to get program or service by id
app.get('/api/programs-and-services/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const program = programsAndServices.protectionPrograms.find(p => p.id === id) 
                  || programsAndServices.communityTreatmentPrograms.find(p => p.id === id);
    if (!program) {
      res.status(404).json({ message: 'Programa o servicio no encontrado' });
    } else {
      res.json(program);
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error interno del servidor' });
  }
});

// Start server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
