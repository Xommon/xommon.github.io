function ListGroup() {
  let items = ["Chicago", "Berlin", "Montreal", "Vancouver", "Barcelona"];
  items = [];

  return (
    <>
      <h1>List</h1>
      {items.length === 0 && <p>No items found</p>}
      <ul className="list-group">
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </>
  );
}

export default ListGroup;
