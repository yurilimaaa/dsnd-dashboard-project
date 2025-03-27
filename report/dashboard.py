from fasthtml.common import *
import matplotlib.pyplot as plt
import pickle

# ✅ Import QueryBase, Employee, Team from employee_events
from employee_events.query_base import QueryBase
from employee_events.employee import Employee
from employee_events.team import Team

# ✅ Import the model loader from utils.py
from utils import model_path

def load_model():
    with open(model_path, 'rb') as f:
        return pickle.load(f)

"""
Below, we import the parent classes
you will use for subclassing
"""
from base_components import (
    Dropdown,
    BaseComponent,
    Radio,
    MatplotlibViz,
    DataTable
)

from combined_components import FormGroup, CombinedComponent

# ReportDropdown
class ReportDropdown(Dropdown):

    def build_component(self, model, id, name):
        self.label = model.name
        return super().build_component(model, id, name)

    def component_data(self, model):
        return model.names()

# Header
class Header(BaseComponent):

    def build_component(self, model, id, name):
        return H1(model.name.title())

# LineChart subclass of MatplotlibViz
class LineChart(MatplotlibViz):

    def visualization(self, model, asset_id):
        # Get event data
        df = model.event_counts(asset_id)

        # Fill missing values with 0
        df = df.fillna(0)

        # Set event_date as index
        df = df.set_index("event_date")

        # Sort the index
        df = df.sort_index()

        # Calculate cumulative sums
        df = df.cumsum()

        # Rename columns
        df.columns = ["Positive", "Negative"]

        # Create subplot
        fig, ax = plt.subplots(figsize=(7, 2.5))

        # Plot the data
        df.plot(ax=ax)

        # Apply styling
        self.set_axis_styling(ax, border_color="black", font_color="black")

        # Add labels
        ax.set_title("Event Activity Over Time")
        ax.set_xlabel("Day")
        ax.set_ylabel("Cumulative Events")

        return fig