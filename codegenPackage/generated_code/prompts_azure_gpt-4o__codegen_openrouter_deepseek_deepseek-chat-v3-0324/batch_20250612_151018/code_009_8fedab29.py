"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-44--gracious-swanson-bcc8c1.netlify.app
Prompt: Generate a boilerplate code for a React application that incorporates routing and state management, inspired by Tim Mansell's projects.
Generated: DETERMINISTIC_8fedab29969e648f
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/data": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from './reducers';

// Components
import HomePage from './components/HomePage';
import AboutPage from './components/AboutPage';
import NotFoundPage from './components/NotFoundPage';
import NavBar from './components/NavBar';

// Initialize Redux store
const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const store = createStore(
  rootReducer,
  composeEnhancers(applyMiddleware(thunk))
);

const App = () => {
  return (
    <Provider store={store}>
      <Router>
        <div className="app">
          <NavBar />
          <Switch>
            <Route exact path="/" component={HomePage} />
            <Route path="/about" component={AboutPage} />
            <Route component={NotFoundPage} />
          </Switch>
        </div>
      </Router>
    </Provider>
  );
};

export default App;

// reducers/index.js
import { combineReducers } from 'redux';
import exampleReducer from './exampleReducer';

export default combineReducers({
  example: exampleReducer
});

// reducers/exampleReducer.js
const initialState = {
  data: [],
  loading: false,
  error: null
};

export default function exampleReducer(state = initialState, action) {
  switch (action.type) {
    case 'FETCH_DATA_REQUEST':
      return { ...state, loading: true };
    case 'FETCH_DATA_SUCCESS':
      return { ...state, loading: false, data: action.payload };
    case 'FETCH_DATA_FAILURE':
      return { ...state, loading: false, error: action.payload };
    default:
      return state;
  }
}

// actions/exampleActions.js
export const fetchData = () => async (dispatch) => {
  dispatch({ type: 'FETCH_DATA_REQUEST' });
  try {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    dispatch({ type: 'FETCH_DATA_SUCCESS', payload: data });
  } catch (error) {
    dispatch({ type: 'FETCH_DATA_FAILURE', payload: error.message });
  }
};

// components/HomePage.js
import React, { useEffect } from 'react';
import { connect } from 'react-redux';
import { fetchData } from '../actions/exampleActions';

const HomePage = ({ data, loading, error, fetchData }) => {
  useEffect(() => {
    fetchData();
  }, [fetchData]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>Home Page</h1>
      <ul>
        {data.map((item) => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
};

const mapStateToProps = (state) => ({
  data: state.example.data,
  loading: state.example.loading,
  error: state.example.error
});

export default connect(mapStateToProps, { fetchData })(HomePage);

// components/AboutPage.js
import React from 'react';

const AboutPage = () => (
  <div>
    <h1>About Page</h1>
    <p>This is a boilerplate React application with routing and state management.</p>
  </div>
);

export default AboutPage;

// components/NotFoundPage.js
import React from 'react';

const NotFoundPage = () => (
  <div>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
  </div>
);

export default NotFoundPage;

// components/NavBar.js
import React from 'react';
import { Link } from 'react-router-dom';

const NavBar = () => (
  <nav>
    <ul>
      <li>
        <Link to="/">Home</Link>
      </li>
      <li>
        <Link to="/about">About</Link>
      </li>
    </ul>
  </nav>
);

export default NavBar;
```
