# Import the QueryBase class
from .query_base import QueryBase

# Import dependencies for SQL execution
from .sql_execution import query, QueryMixin

# Create a subclass of QueryBase called `Team`
class Team(QueryBase, QueryMixin):

    # Set the class attribute `name` to the string "team"
    name = "team"

    # Define a `names` method that receives no arguments
    # This method returns a list of tuples from an SQL execution
    @query
    def names(self):
        # Query 5: Select team_name and team_id from the team table
        return """
            SELECT team_name, team_id
            FROM team;
        """

    # Define a `username` method that receives an ID argument
    # This method returns a list of tuples from an SQL execution
    @query
    def username(self, id):
        # Query 6: Select team_name with a filter on team_id
        return f"""
            SELECT team_name
            FROM team
            WHERE team_id = {id};
        """

    # Method returning data for the machine learning model
    # Returns a pandas dataframe with query execution results
    def model_data(self, id):
        sql_query = f"""
            SELECT positive_events, negative_events FROM (
                SELECT employee_id,
                       SUM(positive_events) AS positive_events,
                       SUM(negative_events) AS negative_events
                FROM {self.name}
                JOIN employee_events
                    USING({self.name}_id)
                WHERE {self.name}.{self.name}_id = {id}
                GROUP BY employee_id
            );
        """
        return self.pandas_query(sql_query)
