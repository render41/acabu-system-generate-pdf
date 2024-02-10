import tkinter as tk


class FormView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.title("Formulário para PDF")
        self.geometry("800x500")

        self.controller = controller

        self.label_title = tk.Label(self, text='Título:')
        self.label_title.pack()
        self.entry_title = tk.Entry(self)
        self.entry_title.pack()

        self.label_subtitle = tk.Label(self, text="Subtítulo:")
        self.label_subtitle.pack()
        self.entry_subtitle = tk.Entry(self)
        self.entry_subtitle.pack()

        self.label_description = tk.Label(self, text="Descrição:")
        self.label_description.pack()
        self.text_description = tk.Text(self)
        self.text_description.pack()

        self.btn_preview = tk.Button(
            self, text="Visualizar", command=self.controller.show_preview)
        self.btn_preview.pack()

        self.btn_submit = tk.Button(
            self, text="Gerar PDF", command=self.controller.generate_pdf)
        self.btn_submit.pack()
