import customtkinter as ctk

# Set your appearance and color theme (you can tweak these if you want)
ctk.set_appearance_mode("System")  # "Dark", "Light", or "System"
ctk.set_default_color_theme("blue")  # or "green", "dark-blue", etc.

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("N.S.")

        # Configure grid: sidebar (col 0) and main container (col 1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar frame (left column)
        self.sidebar = ctk.CTkFrame(self, width=200)
        self.sidebar.grid(row=0, column=0, sticky="ns")
        self.sidebar.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # Sidebar buttons
        self.btn_interp = ctk.CTkButton(self.sidebar, text="Interpolation", command=self.show_interp)
        self.btn_interp.grid(row=0, column=0, pady=10, padx=20, sticky="ew")

        self.btn_curve = ctk.CTkButton(self.sidebar, text="Curve Fitting", command=self.show_curve)
        self.btn_curve.grid(row=1, column=0, pady=10, padx=20, sticky="ew")

        self.btn_integr = ctk.CTkButton(self.sidebar, text="Integration", command=self.show_integr)
        self.btn_integr.grid(row=2, column=0, pady=10, padx=20, sticky="ew")

        # Main container for pages (right column)
        self.main_container = ctk.CTkFrame(self)
        self.main_container.grid(row=0, column=1, sticky="nsew")
        self.main_container.grid_rowconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)

        # Initialize pages
        self.page_interp = InterpolationPage(self.main_container)
        self.page_curve = CurveFittingPage(self.main_container)
        self.page_integr = IntegrationPage(self.main_container)

        # Stack pages on top of each other
        for page in (self.page_interp, self.page_curve, self.page_integr):
            page.grid(row=0, column=0, sticky="nsew")

        # Start with the interpolation page
        self.show_interp()

    def show_interp(self):
        self.page_interp.tkraise()

    def show_curve(self):
        self.page_curve.tkraise()

    def show_integr(self):
        self.page_integr.tkraise()

class InterpolationPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="Interpolation Page", font=("Roboto", 20))
        label.pack(pady=20, padx=20)

class CurveFittingPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="Curve Fitting Page", font=("Roboto", 20))
        label.pack(pady=20, padx=20)

class IntegrationPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="Integration Page", font=("Roboto", 20))
        label.pack(pady=20, padx=20)

