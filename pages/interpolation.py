import customtkinter as ctk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from src.interpolation.newton import Newton
from src.interpolation.lagrange import Lagrange


class InterpolationPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="Interpolation Page", font=("Roboto", 20))
        label.pack(pady=20, padx=20)
