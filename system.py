import tkinter as tk
from tkinter import messagebox, filedialog
import os
import logging

# Set up logging
logging.basicConfig(filename='file_management.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Dummy user credentials
USER_CREDENTIALS = {
    "admin": "password123"
}

class FileManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("File Management System")
        
        self.username = None
        
        self.login_frame = tk.Frame(self.master)
        self.login_frame.pack(pady=20)

        self.label_username = tk.Label(self.login_frame, text="Username:")
        self.label_username.grid(row=0, column=0)
        self.entry_username = tk.Entry(self.login_frame)
        self.entry_username.grid(row=0, column=1)

        self.label_password = tk.Label(self.login_frame, text="Password:")
        self.label_password.grid(row=1, column=0)
        self.entry_password = tk.Entry(self.login_frame, show='*')
        self.entry_password.grid(row=1, column=1)

        self.button_login = tk.Button(self.login_frame, text="Login", command=self.login)
        self.button_login.grid(row=2, columnspan=2)

        self.file_frame = None

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            self.username = username
            logging.info(f"{username} logged in.")
            self.show_file_management()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def show_file_management(self):
        self.login_frame.pack_forget()
        
        self.file_frame = tk.Frame(self.master)
        self.file_frame.pack(pady=20)

        self.button_create = tk.Button(self.file_frame, text="Create File", command=self.create_file)
        self.button_create.pack(pady=5)

        self.button_delete = tk.Button(self.file_frame, text="Delete File", command=self.delete_file)
        self.button_delete.pack(pady=5)

        self.button_open = tk.Button(self.file_frame, text="Open File", command=self.open_file)
        self.button_open.pack(pady=5)

        self.button_logout = tk.Button(self.file_frame, text="Logout", command=self.logout)
        self.button_logout.pack(pady=5)

    def create_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as f:
                f.write("")  # Create an empty file
            logging.info(f"{self.username} created file: {file_path}")
            messagebox.showinfo("File Created", f"File created: {file_path}")

    def delete_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            if os.path.exists(file_path):
                os.remove(file_path)
                logging.info(f"{self.username} deleted file: {file_path}")
                messagebox.showinfo("File Deleted", f"File deleted: {file_path}")
            else:
                messagebox.showerror("Error", "File does not exist.")

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            if os.path.exists(file_path):
                os.startfile(file_path)  # This will open the file with the default application
                logging.info(f"{self.username} opened file: {file_path}")
            else:
                messagebox.showerror("Error", "File does not exist.")

    def logout(self):
        logging.info(f"{self.username} logged out.")
        self.file_frame.pack_forget()
        self.login_frame.pack(pady=20)
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.username = None

if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()
