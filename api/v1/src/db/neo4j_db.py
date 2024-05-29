from neo4j import GraphDatabase, Transaction
from src.utils.parsing import format_dict_for_cypher
from src.utils.handlers import handle_db_operations


class Neo4jDB:
    """
    A class to manage the database operations for Neo4j.
    """

    def __init__(self, uri, username, password):
        """
        Initialize the database driver.
        """
        self._driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        """
        Close the database connection.
        """
        self._driver.close()

    def execute_write(self, func, **kwargs):
        with self._driver.session() as session:
            return session.execute_write(func, **kwargs)

    def execute_read(self, func, **kwargs):
        with self._driver.session() as session:
            return session.execute_read(func, **kwargs)

    @handle_db_operations
    def drop(self, label=None):
        """
        Delete all or certains nodes and relationships.

        Args:
            tx (Transaction): Neo4j transaction.
            label (str): Label for the node.

        Returns:
            dict: The result of the operation.
        """

        def delete_all(tx: Transaction):
            query = f"MATCH (n) DETACH DELETE n"
            result = tx.run(query)
            return result.consume().counters

        def delete_label(tx: Transaction, label: str):
            query = f"MATCH (n:{label}) DETACH DELETE n"
            result = tx.run(query)
            return result.consume().counters

        if label:
            result = self.execute_write(delete_label, label=label)
            return result
        else:
            result = self.execute_write(delete_all)
            return result

    @handle_db_operations
    def create_index(self, node_label: str, property_name: str) -> dict:
        """
        Create a unique index on a node.

        Args:
            tx (Transaction): Neo4j transaction.
            node_label (str): Label for the node.
            property_name (str): Property to index.

        Returns:
            dict: The result of the operation.
        """

        def create_node_index(tx: Transaction, node_label: str, property_name: str):
            query = f"CREATE CONSTRAINT FOR (a:{node_label}) REQUIRE a.{property_name} IS UNIQUE"
            result = tx.run(query)
            return result.consume().counters

        index = self.execute_write(
            create_node_index, node_label=node_label, property_name=property_name
        )
        return index

    def create_node(
        self, tx: Transaction, node_label: str, properties: dict, identifier: str = "id"
    ) -> dict:
        """
        Create a node with given label and properties.

        Args:
            tx (Transaction): Neo4j transaction.
            node_label (str): Label for the node.
            properties (dict): Properties for the node.

        Returns:
            dict: The result of the operation.
        """
        # TODO: Student: Create node
        # (fixme, neo4j): Build a Cypher query to create a node with a specific label and properties.
        # The identifier is the property that will be used to identify the node.
        # The method format_dict_for_cypher is used to format the properties.
        # Example: format_dict_for_cypher({"name": "John Doe"}) -> "{name: 'John Doe'}"

        identifier_value = properties.get(identifier)
        properties = format_dict_for_cypher(properties)
        query = f"""
        CYPHER QUERY
        """
        result = tx.run(query, properties=properties)
        return result.single()

    def read_node(
        self,
        tx: Transaction,
        node_label: str,
        properties: dict,
        many: bool = False,
        limit: int = None,
        sort: tuple = None,
    ) -> dict:
        """
        Read nodes with the given label and properties, with optional sorting and limiting.

        Args:
            tx (Transaction): Neo4j transaction.
            node_label (str): Label for the node.
            properties (dict): Properties for the node.
            many (bool): Whether to return many nodes or not.
            limit (int, optional): The maximum number of nodes to return.
            sort (tuple, optional): A tuple of the field to sort by and the sort direction ('asc' or 'desc').

        Returns:
            dict: The result of the operation.
        """
        # TODO: Read Node
        # (fixme, neo4j): Build a Cypher query to read nodes with a specific label and properties.
        # We should be able(optionally) to sort the nodes by a specific field and limit the number of nodes returned.
        # Make sure to manage the case where we want to return many nodes or just one node.

        properties = format_dict_for_cypher(properties)
        query = f"""
        CYPHER QUERY
        """
        # Adding sort functionality
        if sort is not None:
            pass
        # Adding limit functionality
        if limit is not None:
            pass

        result = tx.run(query)
        result_data = result.data()
        if many:
            result_to_return = []
        else:
            result_to_return = {}

        return result_to_return

    def update_node(
        self,
        tx: Transaction,
        node_label: str,
        match_properties: dict,
        set_properties: dict,
    ) -> dict:
        """
        Update nodes with the given label and matching properties.

        Args:
            tx (Transaction): Neo4j transaction.
            node_label (str): Label for the node.
            match_properties (dict): Properties to match.
            set_properties (dict): Properties to set.

        Returns:
            dict: The result of the operation.
        """
        # TODO: Update Node
        # (fixme, neo4j): Build a Cypher query to update nodes with a specific label and matching properties.
        # You can use the `format_dict_for_cypher` method to format the properties.
        match_properties = format_dict_for_cypher(match_properties)
        set_properties = format_dict_for_cypher(set_properties)
        query = query = f"""
        CYPHER QUERY
        """
        result = tx.run(query)
        return result.data()

    def delete_node(self, tx: Transaction, node_label: str, properties: dict) -> dict:
        """
        Delete nodes with the given label and properties.

        Args:
            tx (Transaction): Neo4j transaction.
            node_label (str): Label for the node.
            properties (dict): Properties for the node.

        Returns:
            dict: The result of the operation.
        """
        # TODO: Delete Node
        # (fixme, neo4j): Build a Cypher query to delete nodes with a specific label and properties.
        # Keep in mind nodes can have relationships with other nodes.
        properties = format_dict_for_cypher(properties)

        query = query = f"""
        CYPHER QUERY
        """
        result = tx.run(query)
        counters_dict = result.consume().counters
        return counters_dict

    def create_relationship(
        self,
        tx: Transaction,
        start_node_label,
        start_node_properties,
        end_node_label,
        end_node_properties,
        relation_type,
    ) -> dict:
        """
        Create a relationship between two nodes.

        Args:
            tx (Transaction): Neo4j transaction.
            start_node_label (str): Label for the starting node.
            start_node_properties (dict): Properties for the starting node.
            end_node_label (str): Label for the ending node.
            end_node_properties (dict): Properties for the ending node.
            relation_type (str): Type of relationship.

        Returns:
            dict: The relationship created.
        """
        # TODO: Create Relationship
        # (fixme, neo4j): Build a Cypher query to create a relationship between two nodes.
        # You can use the `format_dict_for_cypher` method to format the properties.
        # Keep in mind that we can specify the properties of the nodes.

        start_node_properties = format_dict_for_cypher(start_node_properties)
        end_node_properties = format_dict_for_cypher(end_node_properties)
        # Create the query string
        query = f"""
        CYPHER QUERY
        """
        result = tx.run(query)
        result_data = result.data()
        relation_data = result_data[0]["r"]
        return relation_data

    def read_relationship(
        self,
        tx: Transaction,
        start_node_label,
        start_node_properties,
        end_node_label,
        end_node_properties,
        relation_type,
        many=False,
    ) -> dict:
        """
        Read a relationship between two nodes.

        Args:
            tx (Transaction): Neo4j transaction.
            start_node_label (str): Label for the starting node.
            start_node_properties (dict): Properties for the starting node.
            end_node_label (str): Label for the ending node.
            end_node_properties (dict): Properties for the ending node.
            relation_type (str): Type of relationship.

        Returns:
            dict: The relationship read.
        """
        # TODO: Read Relationship
        # (fixme, neo4j): Build a Cypher query to read a relationship between two nodes.
        # You can use the `format_dict_for_cypher` method to format the properties.
        # Make sure to manage the case where we want to return many relationships or just one relationship.
        start_node_properties = format_dict_for_cypher(start_node_properties)
        end_node_properties = format_dict_for_cypher(end_node_properties)
        query = f"""
        CYPHER QUERY
        """

        result = tx.run(query)
        result_data = result.data()
        if many:
            relation_data = []
        else:
            relation_data = ()

        return relation_data

    def update_relationship(
        self,
        tx: Transaction,
        start_node_label,
        start_node_properties,
        end_node_label,
        end_node_properties,
        relation_type,
        new_properties,
    ) -> dict:
        """
        Update a relationship between two nodes.

        Args:
            tx (Transaction): Neo4j transaction.
            start_node (dict): Starting node properties.
            end_node (dict): Ending node properties.
            relationship_type (str): Type of relationship.
            properties (dict): New properties for the relationship.

        Returns:
            dict: The relationship updated.
        """
        # TODO: Update Relationship
        # (fixme, neo4j): Build a Cypher query to update a relationship between two nodes.
        # You can use the `format_dict_for_cypher` method to format the properties.
        new_properties = format_dict_for_cypher(new_properties)
        start_node_properties = format_dict_for_cypher(start_node_properties)
        end_node_properties = format_dict_for_cypher(end_node_properties)
        query = f"""
        CYPHER QUERY
        """

        result = tx.run(query)
        counters_dict = result.consume().counters
        return counters_dict

    def delete_relationship(
        self,
        tx: Transaction,
        start_node_label,
        start_node_properties,
        end_node_label,
        end_node_properties,
        relation_type,
    ) -> dict:
        """
        Delete a relationship between two nodes.

        Args:
            tx (Transaction): Neo4j transaction.
            start_node (dict): Starting node properties.
            end_node (dict): Ending node properties.
            relationship_type (str): Type of relationship.

        Returns:
            dict: The result of the operation.
        """
        # TODO: Delete Relationship
        # (fixme, neo4j): Build a Cypher query to delete a relationship between two nodes.
        query = f"""
        CYPHER QUERY
        """
        result = tx.run(query)
        counters_dict = result.consume().counters
        return counters_dict

    @handle_db_operations
    def create(self, tx_type: str, **kwargs):
        """
        Create a node with the given label and properties.

        Args:
            tx (Transaction): Neo4j transaction.
            node_label (str): Label for the node.
            properties (dict): Properties for the node.

        Returns:
            dict: The result of the operation.
        """
        if tx_type == "node":
            return self.execute_write(
                self.create_node,
                node_label=kwargs["node_label"],
                properties=kwargs["properties"],
                identifier=kwargs["identifier"],
            )
        if tx_type == "relationship":
            return self.execute_write(
                self.create_relationship,
                start_node_label=kwargs["start_node_label"],
                start_node_properties=kwargs["start_node_properties"],
                end_node_label=kwargs["end_node_label"],
                end_node_properties=kwargs["end_node_properties"],
                relation_type=kwargs["relation_type"],
            )

    @handle_db_operations
    def read(self, tx_type: str, **kwargs):
        """
        Read nodes with the given label and properties.

        Args:
            tx (Transaction): Neo4j transaction.
            node_label (str): Label for the node.
            properties (dict): Properties for the node.

        Returns:
            dict: The result of the operation.
        """
        if tx_type == "node":
            return self.execute_read(
                self.read_node,
                node_label=kwargs["node_label"],
                properties=kwargs["properties"],
                many=kwargs.get("many", False),
                limit=kwargs.get("limit", None),
                sort=kwargs.get("sort", None),
            )
        if tx_type == "relationship":
            return self.execute_read(
                self.read_relationship,
                start_node_label=kwargs["start_node_label"],
                start_node_properties=kwargs["start_node_properties"],
                end_node_label=kwargs["end_node_label"],
                end_node_properties=kwargs["end_node_properties"],
                relation_type=kwargs["relation_type"],
                many=kwargs.get("many", False),
            )

    @handle_db_operations
    def update(self, tx_type: str, **kwargs):
        """
        Update nodes with the given label and matching properties.

        Args:
            tx (Transaction): Neo4j transaction.
            node_label (str): Label for the node.
            match_properties (dict): Properties to match.
            set_properties (dict): Properties to set.

        Returns:
            dict: The result of the operation.
        """
        if tx_type == "node":
            return self.execute_write(
                self.update_node,
                node_label=kwargs["node_label"],
                match_properties=kwargs["match_properties"],
                set_properties=kwargs["set_properties"],
            )
        if tx_type == "relationship":
            return self.execute_write(
                self.update_relationship,
                start_node_label=kwargs["start_node_label"],
                start_node_properties=kwargs["start_node_properties"],
                end_node_label=kwargs["end_node_label"],
                end_node_properties=kwargs["end_node_properties"],
                relation_type=kwargs["relation_type"],
                new_properties=kwargs["new_properties"],
            )

    @handle_db_operations
    def delete(self, tx_type: str, **kwargs):
        """
        Delete nodes with the given label and properties.

        Args:
            tx (Transaction): Neo4j transaction.
            node_label (str): Label for the node.
            properties (dict): Properties for the node.

        Returns:
            dict: The result of the operation.
        """
        if tx_type == "node":
            return self.execute_write(
                self.delete_node,
                node_label=kwargs["node_label"],
                properties=kwargs["properties"],
            )
        if tx_type == "relationship":
            return self.execute_write(
                self.delete_relationship,
                start_node_label=kwargs["start_node_label"],
                start_node_properties=kwargs["start_node_properties"],
                end_node_label=kwargs["end_node_label"],
                end_node_properties=kwargs["end_node_properties"],
                relation_type=kwargs["relation_type"],
            )
