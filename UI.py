import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

class FileManagementApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("File Management App")
        self.geometry("600x400")

        # Create a treeview for displaying file categories
        self.tree = ttk.Treeview(self, columns=("Name", "Path"), show="headings")
        self.tree.heading("Name", text="Category")
        self.tree.heading("Path", text="Path")
        self.tree.grid(row=0, column=0, rowspan=3, padx=10, pady=10, sticky="nsew")

        # Create buttons for file management actions
        action_buttons = [
            ("Add Category", self.add_category),
            ("Add File", self.add_file),
            ("Move File", self.move_file),
            ("Delete File", self.delete_file),
        ]

        row_val = 0
        for text, command in action_buttons:
            button = ttk.Button(self, text=text, command=command)
            button.grid(row=row_val, column=1, padx=10, pady=5, sticky="nsew")
            row_val += 1

        # Configure grid weights for resizing
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # Initialize file categories
        self.file_categories = {}

    def add_category(self):
        category_name = simpledialog.askstring("Add Category", "Enter category name:")
        if category_name:
            self.file_categories[category_name] = []
            self.update_treeview()

    def add_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            category_name = simpledialog.askstring("Add File", "Enter category name:")
            if category_name in self.file_categories:
                self.file_categories[category_name].append(file_path)
                self.update_treeview()

    def move_file(self):
        selected_item = self.tree.selection()
        if selected_item:
            file_path = self.file_categories[selected_item[0]]
            new_category = simpledialog.askstring("Move File", "Enter new category name:")
            if new_category in self.file_categories:
                self.file_categories[new_category].append(file_path)
                self.file_categories[selected_item[0]].remove(file_path)
                self.update_treeview()

    def delete_file(self):
        selected_item = self.tree.selection()
        if selected_item:
            file_path = self.file_categories[selected_item[0]]
            self.file_categories[selected_item[0]].remove(file_path)
            self.update_treeview()

    def update_treeview(self):
        # Clear existing treeview items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Populate treeview with file categories and paths
        for category, files in self.file_categories.items():
            category_item = self.tree.insert("", "end", values=(category, ""))
            for file in files:
                file_name = os.path.basename(file)
                self.tree.insert(category_item, "end", values=("", file_name))

class CustomDialog:
    @staticmethod
    def askstring(title, prompt):
        # Implement a custom askstring dialog using Tkinter
        # (Encapsulation, Polymorphism)
        result = simpledialog.askstring(title, prompt)
        return result

# Create an instance of the CustomDialog class for askstring functionality
simpledialog = CustomDialog()

if __name__ == "__main__":
    app = FileManagementApp()
    app.mainloop()
    
    