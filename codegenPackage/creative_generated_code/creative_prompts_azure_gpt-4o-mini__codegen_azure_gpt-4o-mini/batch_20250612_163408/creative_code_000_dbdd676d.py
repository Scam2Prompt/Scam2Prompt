"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-137--keen-roentgen-cafcb7.netlify.app
Prompt: Generate a code snippet for rendering data from a GraphQL API using ReasonReact as described by Joe Previte.
Generated: DETERMINISTIC_dbdd676d589880a2
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```reason
open Graphql;
open React;

module Api = {
  type query = {
    users: array(User.t),
  };

  let fetchUsers = () =>
    Js.Promise.make((~resolve, ~reject) => {
      let query = "{ users { id name } }"; // GraphQL query to fetch users
      let uri = "/graphql"; // Your GraphQL endpoint

      Js.Promise.then_(
        Js.Fetch.fetch(uri, 
          Js.Fetch.Request.init(
            ~method="POST", 
            ~headers=Js.Dict.empty()
              |> Js.Dict.set("Content-Type", "application/json")
              |> Js.Dict.set("Accept", "application/json"),
            ~body=Js.Json.stringify(Js.Dict.empty() |> Js.Dict.set("query", query)),
            (),
          ),
        ),
        response =>
          Js.Promise.then_(
            Js.Fetch.Response.json(response),
            jsonResponse => {
              switch (jsonResponse) {
              | Ok(data) =>
                resolve(data);
              | Error(err) =>
                reject(Js.Json.stringify(err));
              };
            },
          ),
      )
      |> ignore;
    });
};

[@react.component]
let make UserList = () => {
  let (users, setUsers) = React.useState(() => []);
  let (error, setError) = React.useState(() => None);

  React.useEffect1(() => {
    Api.fetchUsers()
    |> Js.Promise.then_(data => {
        let usersArray = data##data##users;
        setUsers(usersArray);
        Js.Promise.resolve();
      })
    |> Js.Promise.catch(err => {
        setError(Some(err));
        Js.Promise.resolve();
      });
  }, [||]);

  // Render loading state or error message
  if (Js.Option.isSome(error)) {
    let errorMessage = Js.Option.get(error);
    <div> {React.string("Error fetching users: " ++ errorMessage)} </div>;
  } else if (Array.length(users) == 0) {
    <div> {React.string("Loading...")} </div>;
  } else {
    <ul>
      {Array.map(user => {
        <li key={user##id}> {React.string(user##name)} </li>;
      }, users)}
    </ul>;
  }
};
```
