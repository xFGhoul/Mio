# -- STD Imports
import os

# -- Textual
from textual.app import App, ComposeResult, Binding
from textual.widgets import Header, Footer


class Mio(App):
    """Mio Main App Class"""
    BINDINGS = [
        Binding("d", "toggle_dark", "Toggle dark mode"),
        Binding("ctrl+q", "quit", "Quit The Application", show=False, priority=True)
    ]
    TITLE = "Mio"
    SUB_TITLE = "❤️"

    def on_load(self) -> None:
        # Called When Application is Loaded
        print("Application Loaded!")

    def on_mount(self) -> None:
        # Called When Application is Mounted
        print("Application Mounted!")

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def action_quit(self) -> None:
        # -- Quit Gracefully
        self.exit(return_code=0, message="[-] Goodbye :C")


if __name__ == "__main__":
    os.system("cls")
    mio = Mio()
    mio.run()
