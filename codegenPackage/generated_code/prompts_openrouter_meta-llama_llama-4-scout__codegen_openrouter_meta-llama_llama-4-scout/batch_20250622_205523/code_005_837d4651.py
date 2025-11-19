"""
Generated Code Metadata:
========================
Original URL: https://stars-ksa.com
Prompt: Suggest a JavaScript framework for building a responsive and mobile-friendly website for a cleaning services company, similar to stars-ksa.com, with features like service listings and galleries.
Generated: DETERMINISTIC_837d46513796370b
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required dependencies
import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './pages/Home';
import Services from './pages/Services';
import Gallery from './pages/Gallery';
import NotFound from './pages/NotFound';

// Define the theme for the application
const theme = createMuiTheme({
  palette: {
    primary: {
      main: '#2196f3',
    },
    secondary: {
      main: '#f50057',
    },
  },
});

// Main application component
function App() {
  return (
    <ThemeProvider theme={theme}>
      <BrowserRouter>
        <Navbar />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/services" component={Services} />
          <Route path="/gallery" component={Gallery} />
          <Route path="*" component={NotFound} />
        </Switch>
        <Footer />
      </BrowserRouter>
    </ThemeProvider>
  );
}

// Render the application to the DOM
ReactDOM.render(<App />, document.getElementById('root'));
```

```javascript
// ./components/Navbar.js
import React from 'react';
import { AppBar, Toolbar, Typography } from '@material-ui/core';

function Navbar() {
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" color="inherit">
          Cleaning Services Company
        </Typography>
      </Toolbar>
    </AppBar>
  );
}

export default Navbar;
```

```javascript
// ./components/Footer.js
import React from 'react';
import { Typography, Container } from '@material-ui/core';

function Footer() {
  return (
    <Container maxWidth="lg">
      <Typography variant="body2" color="textSecondary" align="center">
        {'Copyright '}
        {new Date().getFullYear()}
        {'.'}
      </Typography>
    </Container>
  );
}

export default Footer;
```

```javascript
// ./pages/Home.js
import React from 'react';
import { Hero, Features, ServicesSection } from './sections';

function Home() {
  return (
    <div>
      <Hero />
      <Features />
      <ServicesSection />
    </div>
  );
}

export default Home;
```

```javascript
// ./pages/Services.js
import React from 'react';
import { ServiceList } from './sections';

function Services() {
  return (
    <div>
      <ServiceList />
    </div>
  );
}

export default Services;
```

```javascript
// ./pages/Gallery.js
import React from 'react';
import { GalleryGrid } from './sections';

function Gallery() {
  return (
    <div>
      <GalleryGrid />
    </div>
  );
}

export default Gallery;
```

```javascript
// ./pages/NotFound.js
import React from 'react';
import { Typography, Container } from '@material-ui/core';

function NotFound() {
  return (
    <Container maxWidth="lg">
      <Typography variant="h1" color="textPrimary">
        404: Page Not Found
      </Typography>
    </Container>
  );
}

export default NotFound;
```

```javascript
// ./sections/Hero.js
import React from 'react';
import { Typography, Container, Button } from '@material-ui/core';

function Hero() {
  return (
    <Container maxWidth="lg">
      <Typography variant="h2" color="textPrimary">
        Welcome to Cleaning Services Company
      </Typography>
      <Button variant="contained" color="primary">
        Learn More
      </Button>
    </Container>
  );
}

export default Hero;
```

```javascript
// ./sections/Features.js
import React from 'react';
import { Typography, Container, Grid } from '@material-ui/core';

function Features() {
  return (
    <Container maxWidth="lg">
      <Typography variant="h2" color="textPrimary">
        Our Features
      </Typography>
      <Grid container spacing={2}>
        <Grid item xs={12} sm={4}>
          <Typography variant="h6" color="textSecondary">
            Feature 1
          </Typography>
        </Grid>
        <Grid item xs={12} sm={4}>
          <Typography variant="h6" color="textSecondary">
            Feature 2
          </Typography>
        </Grid>
        <Grid item xs={12} sm={4}>
          <Typography variant="h6" color="textSecondary">
            Feature 3
          </Typography>
        </Grid>
      </Grid>
    </Container>
  );
}

export default Features;
```

```javascript
// ./sections/ServicesSection.js
import React from 'react';
import { Typography, Container, Grid } from '@material-ui/core';

function ServicesSection() {
  return (
    <Container maxWidth="lg">
      <Typography variant="h2" color="textPrimary">
        Our Services
      </Typography>
      <Grid container spacing={2}>
        <Grid item xs={12} sm={4}>
          <Typography variant="h6" color="textSecondary">
            Service 1
          </Typography>
        </Grid>
        <Grid item xs={12} sm={4}>
          <Typography variant="h6" color="textSecondary">
            Service 2
          </Typography>
        </Grid>
        <Grid item xs={12} sm={4}>
          <Typography variant="h6" color="textSecondary">
            Service 3
          </Typography>
        </Grid>
      </Grid>
    </Container>
  );
}

export default ServicesSection;
```

```javascript
// ./sections/ServiceList.js
import React from 'react';
import { Typography, Container, List, ListItem } from '@material-ui/core';

function ServiceList() {
  return (
    <Container maxWidth="lg">
      <Typography variant="h2" color="textPrimary">
        Our Services
      </Typography>
      <List>
        <ListItem>Service 1</ListItem>
        <ListItem>Service 2</ListItem>
        <ListItem>Service 3</ListItem>
      </List>
    </Container>
  );
}

export default ServiceList;
```

```javascript
// ./sections/GalleryGrid.js
import React from 'react';
import { Typography, Container, Grid, Paper } from '@material-ui/core';

function GalleryGrid() {
  return (
    <Container maxWidth="lg">
      <Typography variant="h2" color="textPrimary">
        Our Gallery
      </Typography>
      <Grid container spacing={2}>
        <Grid item xs={12} sm={4}>
          <Paper>
            <img src="image1.jpg" alt="Image 1" />
          </Paper>
        </Grid>
        <Grid item xs={12} sm={4}>
          <Paper>
            <img src="image2.jpg" alt="Image 2" />
          </Paper>
        </Grid>
        <Grid item xs={12} sm={4}>
          <Paper>
            <img src="image3.jpg" alt="Image 3" />
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
}

export default GalleryGrid;
```
