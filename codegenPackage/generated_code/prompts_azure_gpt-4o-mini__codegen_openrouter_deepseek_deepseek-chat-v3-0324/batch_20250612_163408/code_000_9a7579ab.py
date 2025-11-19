"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-140--keen-roentgen-cafcb7.netlify.app
Prompt: Write a tutorial on how to render data from a GraphQL API using ReasonReact, referencing Joe Previte's article on the topic.
Generated: DETERMINISTIC_9a7579abe9ac10ad
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's the complete ReasonReact code for rendering data from a GraphQL API, following best practices and referencing Joe Previte's approach:

```reason
/* GraphQLAPI.re */

// Define the module for our GraphQL operations
module GetPosts = [%graphql
  {|
    query GetPosts {
      posts {
        id
        title
        body
      }
    }
  |}
];

// Define the type for our post data
type post = {
  id: string,
  title: string,
  body: string,
};

// Define the component state
type state = {
  loading: bool,
  error: option(string),
  posts: array(post),
};

// Define the component actions
type action =
  | LoadPosts
  | PostsLoaded(array(post))
  | LoadError(string);

// Create the component
let component = ReasonReact.reducerComponent("GraphQLAPI");

// Helper function to convert GraphQL response to our post type
let parsePosts = (posts): array(post) => {
  posts
  ->Belt.Array.map(post => {
      {
        id: post##id,
        title: post##title,
        body: post##body,
      };
    });
};

let make = _children => {
  ...component,

  initialState: () => {loading: false, error: None, posts: [||]},

  reducer: (action, state) =>
    switch (action) {
    | LoadPosts =>
      ReasonReact.Update({...state, loading: true, error: None})
    | PostsLoaded(posts) =>
      ReasonReact.Update({...state, loading: false, posts})
    | LoadError(error) =>
      ReasonReact.Update({...state, loading: false, error: Some(error)})
    },

  didMount: self => {
    self.send(LoadPosts);

    GetPosts.make()
    ->ApolloHooks.useQuery()
    ->Promise.get(result => {
        switch (result) {
        | Ok(response) =>
          let posts = parsePosts(response##posts);
          self.send(PostsLoaded(posts));
        | Error(error) =>
          let errorMsg =
            switch (error) {
            | ApolloHooks.Error(e) => e##message
            | _ => "Unknown error occurred"
            };
          self.send(LoadError(errorMsg));
        }
      });

    ReasonReact.NoUpdate;
  },

  render: self => {
    <div className="container">
      <h1> {ReasonReact.string("Posts")} </h1>
      {switch (self.state) {
       | {loading: true} =>
         <div className="loading"> {ReasonReact.string("Loading...")} </div>
       | {error: Some(error)} =>
         <div className="error">
           {ReasonReact.string("Error: " ++ error)}
         </div>
       | {posts: [||]} =>
         <div className="empty"> {ReasonReact.string("No posts found")} </div>
       | {posts} =>
         <ul className="post-list">
           {posts
            ->Belt.Array.map(post =>
                <li key={post.id} className="post-item">
                  <h2> {ReasonReact.string(post.title)} </h2>
                  <p> {ReasonReact.string(post.body)} </p>
                </li>
              )
            ->ReasonReact.array}
         </ul>
       }}
    </div>;
  },
};
```

```reason
/* App.re */

// Main application component that wraps our GraphQLAPI component
let component = ReasonReact.statelessComponent("App");

let make = _children => {
  ...component,
  render: _self =>
    <div className="app">
      <header className="app-header">
        <h1> {ReasonReact.string("GraphQL API Example")} </h1>
      </header>
      <main className="app-content">
        <GraphQLAPI />
      </main>
    </div>,
};
```

```reason
/* Index.re */

// Entry point for the application
ReactDOMRe.renderToElementWithId(<App />, "root");
```

```reason
/* bsconfig.json */
{
  "name": "reason-graphql-example",
  "sources": [
    {
      "dir": "src",
      "subdirs": ["components"]
    }
  ],
  "package-specs": [
    {
      "module": "es6",
      "in-source": true
    }
  ],
  "suffix": ".bs.js",
  "bs-dependencies": [
    "reason-react",
    "@apollo/client",
    "reason-apollo-hooks",
    "graphql-ppx"
  ],
  "ppx-flags": ["graphql-ppx/ppx"],
  "reason": {
    "react-jsx": 3
  }
}
```

```reason
/* package.json dependencies */
{
  "dependencies": {
    "@apollo/client": "^3.0.0",
    "graphql": "^15.0.0",
    "reason-apollo-hooks": "^0.1.0",
    "reason-react": "^0.9.1",
    "react": "^17.0.1",
    "react-dom": "^17.0.1"
  },
  "devDependencies": {
    "bs-platform": "^8.2.0",
    "graphql-ppx": "^1.0.0"
  }
}
```

This implementation includes:
- GraphQL query definition
- Type-safe data handling
- Loading and error states
- Clean component structure
- Proper error handling
- ReasonReact best practices
- Apollo Client integration
