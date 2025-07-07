from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
import yaml

script_dir = Path(__file__).parent if "__file__" in globals() else Path.cwd()

yaml_file_path = script_dir / "plant.yaml"

@dataclass
class Plant:
    name: str
    frequency_days: int
    next_due_date: date

today = date.today()

def water_plant(name: str):
    print(f" watering {name}")


with open(yaml_file_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

plant_config = yaml.safe_load(raw_text)

for plant_name, plant_data in plant_config.items():
    # parse next_due_date into a date object if it came in as a string
    raw_due = plant_data["next_due_date"]
    if isinstance(raw_due, str):
        next_due = datetime.fromisoformat(raw_due).date()
    else:
        next_due = raw_due  # assume it's already a date

    # check if it's due or overdue
    if next_due <= today:
        water_plant(plant_name)

        # compute new due date
        freq = plant_data["frequency_days"]
        new_due = today + timedelta(days=freq)

        # write it back into our in-memory dict
        plant_data["next_due_date"] = new_due

      

with open(yaml_file_path, "w", encoding="utf-8") as f:
      yaml.safe_dump(
          plant_config,
          f,
          sort_keys=False,
          default_flow_style=False  
      )  