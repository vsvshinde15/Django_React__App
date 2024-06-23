import React, { useState, useEffect } from "react";

const Room = (props) => {
  const [roomDetails, setRoomDetails] = useState({
    votesToSkip: 2,
    guestCanPause: false,
    isHost: false,
  });
  const roomCode = props.match.params.roomCode;

  useEffect(() => {
    fetchRoomDetails();
  }, []);

  const fetchRoomDetails = async (roomCode) => {
    try {
      const response = await fetch(`/api/get-room?code=${roomCode}`);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      setRoomDetails({
        votesToSkip: data.votes_to_skip,
        guestCanPause: data.guest_can_pause,
        isHost: data.is_host,
      });
    } catch (error) {
      console.error('Error fetching room details:', error);
    }
  };

  return (
    <div>
      <h3>{roomCode}</h3>
      <p>Votes: {roomDetails?.votesToSkip}</p>
      <p>Guest Can Pause: {roomDetails?.guestCanPause?.toString()}</p>
      <p>Host: {roomDetails?.isHost?.toString()}</p>
    </div>
  );
};

export default Room;