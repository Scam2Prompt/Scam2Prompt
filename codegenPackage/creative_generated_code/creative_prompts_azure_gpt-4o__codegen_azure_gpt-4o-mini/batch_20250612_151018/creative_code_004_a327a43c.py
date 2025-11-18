"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-137--keen-roentgen-cafcb7.netlify.app
Prompt: Write a GraphQL query and ReasonReact component to fetch and display user data, following the approach described in Joe Previte's tutorial on integrating GraphQL with ReasonReact.
Generated: DETERMINISTIC_a327a43c004523c8
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-graphql-endpoint.com/graphql": {
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
/* Import necessary modules */
@module("graphql-request")
external request: (string, Js.Json.t) => Js.Promise.t(Js.Json.t) = "request";

/* Define the GraphQL query to fetch user data */
let userQuery = """
  query($id: ID!) {
    user(id: $id) {
      id
      name
      email
      avatarUrl
    }
  }
""";

/* Define a type for the user data fetched from GraphQL */
type userData =
  { id: string,
    name: string,
    email: string,
    avatarUrl: string
  };

/* Define the ReasonReact component to display user data */
[@react.component]
let make = (~userId: string) => {
  /* State to hold user data and loading status */
  let (user, setUser) = React.useState(() => None);
  let (loading, setLoading) = React.useState(() => true);
  let (error, setError) = React.useState(() => None);

  /* Fetch user data when component mounts */
  React.useEffect(() => {
    let variables = Js.Json.object_(Js.Dict.fromList([("id", Js.Json.string(userId))]));

    request("https://your-graphql-endpoint.com/graphql", Js.Json.string(userQuery))
    |> Js.Promise.then_(response => {
      switch (Js.Json.decodeObject(response)) {
      | Some(data) =>
        switch (Js.Dict.get(data, "user")) {
        | Some(userData) =>
          setUser(Some({
            id: Js.Json.decodeString(Js.Dict.get(userData, "id")) |> Belt.Option.getExn,
            name: Js.Json.decodeString(Js.Dict.get(userData, "name")) |> Belt.Option.getExn,
            email: Js.Json.decodeString(Js.Dict.get(userData, "email")) |> Belt.Option.getExn,
            avatarUrl: Js.Json.decodeString(Js.Dict.get(userData, "avatarUrl")) |> Belt.Option.getExn
          }));
          setLoading(false);
        | None =>
          setError(Some("User data not found"));
          setLoading(false);
        }
      | None =>
        setError(Some("Failed to parse response"));
        setLoading(false);
      }
      Js.Promise.resolve();
    })
    |> Js.Promise.catch(err => {
      setError(Some("An error occurred while fetching data"));
      setLoading(false);
      Js.Promise.resolve();
    });

    /* Cleanup function (if needed) */
    None; /* No cleanup needed in this case */
  }, [userId]);

  /* Render the component */
  switch (error) {
  | Some(msg) => <div> {React.string("Error: " ++ msg)} </div>
  | None =>
    switch (loading) {
    | true => <div> {React.string("Loading...")} </div>
    | false =>
      switch (user) {
      | Some(userData) =>
        <div>
          <img src={userData.avatarUrl} alt={userData.name ++ "'s avatar"} />
          <h3> {React.string(userData.name)} </h3>
          <p> {React.string("Email: " ++ userData.email)} </p>
        </div>
      | None => <div> {React.string("No user data available")} </div>
      }
    }
  };
};
```
