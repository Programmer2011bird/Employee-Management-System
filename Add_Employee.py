#-----------------------------#
#           6/22/2024         #
#-----------------------------#
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class ADD_TAB(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.geometry("400x280")
        self.resizable(False, False)
        self.wm_title("Employee management system: ADD TAB")

        self.LABEL_EMPLOYEE_NAME: ctk.CTkLabel = ctk.CTkLabel(self, text="Employee's Name: ")
        self.ENTRY_EMPLOYEE_NAME: ctk.CTkEntry = ctk.CTkEntry(self, placeholder_text="Name")

        self.LABEL_EMPLOYEE_ID: ctk.CTkLabel = ctk.CTkLabel(self, text="Employee's ID: ")
        self.ENTRY_EMPLOYEE_ID: ctk.CTkEntry = ctk.CTkEntry(self, placeholder_text="ID")

        self.LABEL_EMPLOYEE_PART: ctk.CTkLabel = ctk.CTkLabel(self, text="Employee's PART: ")
        self.ENTRY_EMPLOYEE_PART: ctk.CTkEntry = ctk.CTkEntry(self, placeholder_text="Part")

        self.LABEL_EMPLOYEE_SHIFT: ctk.CTkLabel = ctk.CTkLabel(self, text="Employee's SHIFT: ")
        self.ENTRY_EMPLOYEE_SHIFT: ctk.CTkEntry = ctk.CTkEntry(self, placeholder_text="Shift")

        self.BUTTON_ADD_EMPLOYEE: ctk.CTkButton = ctk.CTkButton(self, text="Add Employee", width=300,
                                                                command=self.add_Employee_to_csv)

        self.LABEL_EMPLOYEE_NAME.grid(row=0, column=0, padx=30, pady=15)
        self.ENTRY_EMPLOYEE_NAME.grid(row=0, column=1, padx=30, pady=15)

        self.LABEL_EMPLOYEE_ID.grid(row=1, column=0, padx=30, pady=15)
        self.ENTRY_EMPLOYEE_ID.grid(row=1, column=1, padx=30, pady=15)

        self.LABEL_EMPLOYEE_PART.grid(row=2, column=0, padx=30, pady=15)
        self.ENTRY_EMPLOYEE_PART.grid(row=2, column=1, padx=30, pady=15)

        self.LABEL_EMPLOYEE_SHIFT.grid(row=3, column=0, padx=30, pady=15)
        self.ENTRY_EMPLOYEE_SHIFT.grid(row=3, column=1, padx=30, pady=15)

        self.BUTTON_ADD_EMPLOYEE.grid(row=4, column=0, padx=30, pady=15, columnspan=2)

    def add_Employee_to_csv(self) -> None:
        EMPLOYEE_NAME: str = str(self.ENTRY_EMPLOYEE_NAME.get())
        EMPLOYEE_ID: int = int(self.ENTRY_EMPLOYEE_ID.get())
        EMPLOYEE_PART: str = str(self.ENTRY_EMPLOYEE_PART.get())
        EMPLOYEE_SHIFT: str = str(self.ENTRY_EMPLOYEE_SHIFT.get())

        with open("DATA/EMPLOYEES.csv", "a") as file:
            file.write(f"{EMPLOYEE_NAME},{EMPLOYEE_ID},{EMPLOYEE_PART},{EMPLOYEE_SHIFT}\n")
