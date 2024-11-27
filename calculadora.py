import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        # Variables
        self.expression = ""
        self.input_text = tk.StringVar()

        # Pantalla de entrada
        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(expand=True, fill="both")

        self.input_field = tk.Entry(
            self.entry_frame,
            textvariable=self.input_text,
            font=("Arial", 20),
            justify="right",
            bd=10,
            insertwidth=2
        )
        self.input_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20)

        # Botones
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(expand=True, fill="both")

        # Configuración de botones
        buttons = [
            '7', '8', '9', 'C',
            '4', '5', '6', '/',
            '1', '2', '3', '*',
            '0', '.', '=', '+',
            '-', '(', ')', ''
        ]

        row_val, col_val = 0, 0
        for button in buttons:
            if button != '':
                b = tk.Button(
                    self.button_frame,
                    text=button,
                    font=("Arial", 18),
                    command=lambda x=button: self.on_button_click(x)
                )
                b.grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configurar dimensiones de los botones
        for i in range(5):
            self.button_frame.grid_rowconfigure(i, weight=1)
            self.button_frame.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button):
        if button == "C":
            self.expression = ""
        elif button == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Error"
        else:
            self.expression += button
        self.input_text.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
