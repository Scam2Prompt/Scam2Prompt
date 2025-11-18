"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-140--keen-roentgen-cafcb7.netlify.app
Prompt: Implement a ReasonReact component that fetches and renders data from a GraphQL API, as outlined in Joe Previte's article "How to Render Data from a GraphQL API in ReasonReact."
Generated: DETERMINISTIC_eea5f822aeb50b71
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/graphql": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```reason
/* ReasonReact Component to fetch and render data from a GraphQL API */

/* Import necessary modules */
open ReasonReact;
open Js.Promise;
open Fetch;

/* Define GraphQL query as a string */
let query = {|
  query {
    posts {
      id
      title
    }
  }
|};

/* Define types for GraphQL response */
type post = {
  id: string,
  title: string,
};

type responseData = {
  posts: array(post),
};

/* Define the component */
[@react.component]
let make = () => {
  /* State to manage data and loading */
  let (state, setState) = React.useState(() => ({
    data: None,
    isLoading: true,
    error: None,
  }));

  /* Function to fetch data from GraphQL API */
  let fetchData = () => {
    let url = "https://example.com/graphql";
    Fetch.fetch(url, {
      method: #POST,
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({"query": query}),
    })
    |> then_(response =>
         response.json()
         |> then_(json =>
              /* Parse response data */
              switch json##data {
              | Some(data) =>
                let posts = Belt.Array.map(data##posts, post => {
                  id: post##id,
                  title: post##title,
                });
                setState(_ => ({
                  data: Some(posts),
                  isLoading: false,
                  error: None,
                }));
                resolve()
              | None =>
                setState(_ => ({
                  data: None,
                  isLoading: false,
                  error: Some("Failed to load data"),
                }));
                resolve()
              }
          )
         |> catch(_error =>
              /* Handle network or parsing errors */
              setState(_ => ({
                data: None,
                isLoading: false,
                error: Some("Network or parsing error"),
              }));
              resolve()
          )
     );
    resolve();
  };

  /* Fetch data when component mounts */
  React.useEffect(() => {
    fetchData();
    None;
  }, []);

  /* Render logic */
  switch (state) {
  | {data: Some(posts), isLoading: false, error: None} =>
    /* Render list of posts */
    <div>
      <h1>{"Posts"}</h1>
      <ul>
        posts
        |> Belt.Array.map(post => <li key={post.id}>{React.string(post.title)}</li>)
        |> ReasonReact.array
      </ul>
    </div>
  | {data: None, isLoading: true, error: None} =>
    /* Render loading indicator */
    <div>{"Loading..."}</div>
  | {data: None, isLoading: false, error: Some(error)} =>
    /* Render error message */
    <div>{"Error: " ++ error}</div>
  };
};
```
