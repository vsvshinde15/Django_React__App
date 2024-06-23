import React from "react";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";
import Room from "./Room";

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";

const HomePage = () => {
  return (
    <Router>
      <Switch>
        <Route exact path="/">
          <p>This is the home page</p>
        </Route>
        <Route path="/join" component={RoomJoinPage} />
        <Route path="/create-room" component={CreateRoomPage} />
        <Route path="/room/:roomCode" component={Room} />
      </Switch>
    </Router>
  );
};

export default HomePage;