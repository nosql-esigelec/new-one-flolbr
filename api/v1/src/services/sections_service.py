"""
Section Service
"""
# pylint: disable=W0212
from src.db.neo4j_db import Neo4jDB


class SectionService:
    """
    Class to manage project operations.
    """

    def __init__(self, neo4j: Neo4jDB = None):
        self.neo4j = neo4j


    def get_options_for_question(self, question_id: str) -> list:
        """
        Get options for a question.

        Args:
            question_id (str): The question ID.

        Returns:
            List[dict]: The options.
        """
        # hint: This method can inspire you to implement some with relationships.
        options = self.neo4j.read(
            tx_type="relationship",
            start_node_label="Question",
            start_node_properties={"id": question_id},
            end_node_label="Option",
            end_node_properties={},
            relation_type="HAS_OPTION",
            many=True
        ).get("result")
        # the key 2 is the right part of the relationship where 0 is the left part and 1 is the relationship
        options = [option[2] for option in options]
        return options

    def get_sections(self) -> list:
        """
        Get all sections.
        """
        # TODO:(neo4j) Get All Sections
        # Implement this method to get all sections from neo4j.
        # (fixme, neo4j): You can use the `read` method of the Neo4jDB class to get all nodes of Label
        # Section.
        # Make sure to sort the sections by the `order` property in the natural order.
        sections = []  # placeholder

        return sections

    def get_section_by_property(self, property: str, value: str) -> dict:
        """
        Get a section by a specific property.

        Args:

            property (str): The property to be used to get the section.
            value (str): The value of the property.

        Returns:
            dict: The section.
        """
        # TODO:(neo4j) Get Section Info by property
        # Implement this method to get a section from neo4j by a specific property.
        # (fixme, neo4j): You can use the `read` method of the Neo4jDB class to get a node of Label
        # Section by a specific property.
        section = {}  # placeholder

        return section

    def get_next_section(self, section_id: str) -> dict:
        """
        Get the next section.

        Args:
            section_id (str): The section ID.

        Returns:
            dict: The next section.
        """
        # TODO(neo4j): Get Next Section
        # Implement this method to get the next section.
        # (fixme, neo4j): Build a Cypher query to get the next node of Label Section.
        # The next section has an order that is greater than the order of the current section.  
        # You can use the `read` method of the Neo4jDB class to get a node of Label Section by a specific property.

        # Find the current section
        current_section = {} # placeholder
        # Get the order of the current section
        current_section_order = 0 # placeholder
        # Get the next section order
        next_section_order = current_section_order + 1
        # Get the next section
        next_section = {} # placeholder
        return next_section

    def get_questions_for_section(self, section_id: str) -> list:
        """
        Get all questions for a section.

        Args:
            section_id (str): The section ID.

        Returns:
            List[dict]: The questions.
        """
        # TODO(neo4j): Get questions for a section
        # Implement this method to get all questions for a section.
        # (fixme, neo4j): Build a Cypher query to get all nodes of Label Question
        # that are related to the current section.
        # Reminder: A Section node can HAS_QUESTION to multiple Question nodes.
        # You can use the read method of Neo4jDB class.

        # Find the questions for the section
        questions = []  # placeholder
    
        # Get the options for each question
        questions_processed = []
        for question in questions:
            question_dict = dict(question.items())
            # TO COMPLETE

        return questions_processed

    def get_next_questions(self, question_id: str, option_text: str) -> list:
        """
        Get next questions for a question answered.

        Args:
            question_id (str): The question ID.
            option_text (str): The option text.

        Returns:
            List[dict]: The next questions.
        """
        # TODO(neo4j): Get next questions
        # Implement this method to get next questions given the options
        # picked for the current question.
        # Reminder: An Option node can LEADS_TO to multiple Question nodes.
        # The option_text argument is the text of the option picked by the user for
        # the question with the question_id argument.
        # You can use the method read of Neo4jDB class.

       # Find the next questions given the current option picked
        questions = []  # placeholder
        # Get the options for each question
        questions_processed = []
        for question in questions:
            question_dict = dict(question.items())
            # TO COMPLETE

        return questions_processed
