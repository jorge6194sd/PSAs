from dataclasses import dataclass
from datetime import date
from pathlib import Path
import yaml

script_dir = Path(__file__).parent if "__file__" in globals() else Path.cwd()

yaml_file_path = script_dir / "plant.yaml"

@dataclass
class Plant:
    name: str
    frequency_days: int
    next_due_date: date


with open(yaml_file_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

plant_config = yaml.safe_load(raw_text)

for object_key, plant in plant_config.items():
      
      print(f"Key: {object_key}")
