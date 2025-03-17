import customtkinter as ctk

class CurveFittingPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="Curve Fitting Page", font=("Roboto", 20))
        label.pack(pady=20, padx=20)
