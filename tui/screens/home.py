from textual.widgets import Static, Button, DataTable
from textual.containers import Vertical
from textual.screen import Screen
import json
import os

class HomeScreen(Screen):
    def compose(self):
        yield Static("Sugar TUI - Group Overview", id="title")
        data = self.load_mock_data()
        dt = DataTable()
        dt.add_columns("Group", "Service", "Status", "IP")
        for group in data["groups"]:
            for service in group["services"]:
                dt.add_row(
                    group["name"],
                    service["name"],
                    service["status"],
                    service.get("ip", "N/A")
                )
        yield Vertical(dt)

    def load_mock_data(self):
        path = os.path.join(os.path.dirname(__file__), "../data/mock_config.json")
        with open(path) as f:
            return json.load(f)
