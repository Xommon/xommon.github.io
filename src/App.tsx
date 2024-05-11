import ListGroup from "./components/ListGroup";

function App() {
  let items = ["Chicago", "Berlin", "Montréal", "Vancouver", "Barcelona"];

  return (
    <div>
      <ListGroup items={items} heading="Cities" />
    </div>
  );
}

export default App;
