import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class CalculatorApp(toga.App):
    def startup(self):
        # Creating the main window
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Display box
        self.display = toga.TextInput(readonly=True, style=Pack(flex=1, padding=(0, 5), font_size=20))

        main_box.add(self.display)

        # Buttons
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row in buttons:
            row_box = toga.Box(style=Pack(direction=ROW, padding=5))
            for text in row:
                button = toga.Button(
                    text,
                    on_press=self.on_button_press,
                    style=Pack(flex=1, padding=5, font_size=18)
                )
                row_box.add(button)
            main_box.add(row_box)

        # Set the main window content
        self.main_window = toga.MainWindow(title=self.name)
        self.main_window.content = main_box
        self.main_window.show()

    def on_button_press(self, widget):
        current_text = self.display.value
        text = widget.text  # اصلاح: استفاده از `text` به جای `label`

        if text == '=':
            try:
                # Calculate the expression and update the display
                result = str(eval(current_text))
                self.display.value = result
            except Exception:
                self.display.value = "Error"
        elif text in ['+', '-', '*', '/']:
            if current_text and current_text[-1] not in ['+', '-', '*', '/']:
                self.display.value += text
        else:
            self.display.value += text

def main():
    return CalculatorApp("calculator", 'org.beeware.calculator')
