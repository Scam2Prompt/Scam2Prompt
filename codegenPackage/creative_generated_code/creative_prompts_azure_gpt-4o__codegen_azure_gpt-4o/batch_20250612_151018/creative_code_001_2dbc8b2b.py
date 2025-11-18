"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-134--keen-roentgen-cafcb7.netlify.app
Prompt: Generate ReasonReact code for rendering data fetched from a GraphQL API, following the techniques outlined by Joe Previte.
Generated: DETERMINISTIC_2dbc8b2b83451357
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
// App.re
/* 
  ReasonReact component to fetch and render data from a GraphQL API.
  This code adheres to best practices and includes error handling.
*/

open ReasonReact;
open Js.Promise;

[@react.component]
let make = () => {
  // Define a state with type: {data: option(string), error: option(string), loading: bool}
  let (state, setState) = React.useState(() => {
    {data: None, error: None, loading: true};
  });

  // GraphQL query string
  let query = "
    query {
      allPosts {
        id
        title
      }
    }
  ";

  // Fetch data using GraphQL API
  React.useEffect0(() => {
    let fetchData = () =>
      fetch("https://example.com/graphql", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({"query": query}),
      })
      |> then(response => response.json())
      |> then(json => {
        let result = json##data##allPosts;
        setState({...state, loading: false, data: Some(result)});
        resolve();
      })
      |> catch(error => {
        setState({...state, loading: false, error: Some(error##message)});
        resolve();
      });
    fetchData();
    None;
  });

  // Render the result
  switch (state) {
  | {loading: true, _, _} => <div>Loading...</div>
   debugging!
