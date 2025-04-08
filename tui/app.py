from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Container
from tui.screens.home import HomeScreen

class SugarTUI(App):
    CSS_PATH = None

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(HomeScreen())
        yield Footer()
