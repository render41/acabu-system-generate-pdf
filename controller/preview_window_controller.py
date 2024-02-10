import tkinter as tk


class PreviewWindowController(tk.Toplevel):
    def __init__(self, parent, title, subtitle, description):
        super().__init__(parent)
        self.title("Preview")
        self.geometry(newGeometry="400x300")

        self.canvas = tk.Canvas(self, width=400, height=300)
        self.canvas.pack()

        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.draw_preview()

    def draw_preview(self):
        self.canvas.create_text(200, 50, text="Preview", font=(
            "Helvetica", 24, "bold"), justify='center')
        self.canvas.create_text(100, 100, text="{}".format(self.title), font=(
            "Helvetica", 18, "bold"), anchor="w", justify='left')
        self.canvas.create_text(100, 130, text="{}".format(self.subtitle), font=(
            "Helvetica", 12, "normal"), anchor="w", justify='left')
        self.canvas.create_text(100, 160, text="{}".format(self.description), font=(
            "Helvetica", 12, "normal"), anchor="w", justify='left')
