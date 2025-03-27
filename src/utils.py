from pathlib import Path

# Path to project root
project_root = Path(__file__).resolve().parent.parent 

# Path to the Python package
package_path = project_root / 'python-package' / 'employee_events'

# Path to the trained machine learning model (model.pkl)
model_path = project_root / 'assets' / 'model.pkl'

# CLI colors for feedback
event_color = '\033[96m'
complete_color = '\033[92m'
color_end = '\033[0m'