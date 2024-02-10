from controller import form_controller


def main():
    app = form_controller.FormController()
    app.form_view.mainloop()


if __name__ == "__main__":
    main()
