from view import form_view
from model import form_data_model
from tkinter import filedialog, messagebox
from fpdf import FPDF
import tkinter as tk
import preview_window_controller


class FormController:
    def __init__(self):
        self.form_model = form_data_model.FormDataModel()
        self.form_view = form_view.FormView(self)

    def show_preview(self):
        title = self.form_view.entry_title.get()
        subtitle = self.form_view.entry_subtitle.get()
        description = self.form_view.text_description.get("1.0", tk.END)
        preview_window = preview_window_controller.PreviewWindowController(
            parent=self.form_view, title=title, subtitle=subtitle, description=description)

    def generate_pdf(self):
        try:
            title = self.form_view.entry_title.get()
            subtitle = self.form_view.entry_subtitle.get()
            description = self.form_view.text_description.get("1.0", tk.END)
            save_path = filedialog.asksaveasfilename(
                defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if save_path:
                self._create_pdf(title, subtitle, description, save_path)
        except:
            print("Error convert data.")

    def _create_pdf(self, title, subtitle, description, save_path):
        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Helvetica", style='B', size=18)
            pdf.cell(w=200, h=10, text=title, ln=True)
            pdf.set_font("Helvetica", size=10)
            pdf.cell(w=200, h=10, text=subtitle, ln=True)
            pdf.set_font("Helvetica", size=12)
            pdf.multi_cell(w=200, h=18, text=description)

            pdf.output(save_path)

            messagebox.showinfo("PDF Gerado", "PDF gerado com sucesso!")
        except:
            messagebox.showerror("Erro ao Criar", "Erro na criação do PDF.")
