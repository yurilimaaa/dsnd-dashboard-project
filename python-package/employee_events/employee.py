# Import the QueryBase class
from .query_base import QueryBase

# Import the decorator from the sql_execution module
from .sql_execution import query, QueryMixin

# Define a subclass of QueryBase
# called Employee
class Employee(QueryBase, QueryMixin):

    # Set the class attribute `name`
    # to the string "employee"
    name = "employee"

    # Define a method called `names`
    # that receives no arguments
    # This method returns a list of tuples
    @query
    def names(self):
        # Query 3
        # SQL query selecting employee's full name and ID
        return """
            SELECT first_name || ' ' || last_name AS full_name,
                   employee_id
            FROM employee;
        """

    # Define a method called `username`
    # that receives an `id` argument
    # This method returns a list of tuples
    @query
    def username(self, id):
        # Query 4
        # SQL query selecting employee's full name filtered by ID
        return f"""
            SELECT first_name || ' ' || last_name AS full_name
            FROM employee
            WHERE employee_id = {id};
        """

    # Method returning data for the machine learning model
    # Returns a pandas dataframe with query execution results
    def model_data(self, id):
        sql_query = f"""
            SELECT SUM(positive_events) AS positive_events,
                   SUM(negative_events) AS negative_events
            FROM {self.name}
            JOIN employee_events
                USING({self.name}_id)
            WHERE {self.name}.{self.name}_id = {id};
        """
        return self.pandas_query(sql_query)
# Import the QueryBase class
from .query_base import QueryBase

# Import the decorator from the sql_execution module
from .sql_execution import query, QueryMixin

# Define a subclass of QueryBase
# called Employee
class Employee(QueryBase, QueryMixin):

    # Set the class attribute `name`
    # to the string "employee"
    name = "employee"

    # Define a method called `names`
    # that receives no arguments
    # This method returns a list of tuples
    @query
    def names(self):
        # Query 3
        # SQL query selecting employee's full name and ID
        return """
            SELECT first_name || ' ' || last_name AS full_name,
                   employee_id
            FROM employee;
        """

    # Define a method called `username`
    # that receives an `id` argument
    # This method returns a list of tuples
    @query
    def username(self, id):
        # Query 4
        # SQL query selecting employee's full name filtered by ID
        return f"""
            SELECT first_name || ' ' || last_name AS full_name
            FROM employee
            WHERE employee_id = {id};
        """

    # Method returning data for the machine learning model
    # Returns a pandas dataframe with query execution results
    def model_data(self, id):
        sql_query = f"""
            SELECT SUM(positive_events) AS positive_events,
                   SUM(negative_events) AS negative_events
            FROM {self.name}
            JOIN employee_events
                USING({self.name}_id)
            WHERE {self.name}.{self.name}_id = {id};
        """
        return self.pandas_query(sql_query)
