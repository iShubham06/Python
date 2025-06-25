import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
import os


# Load/Save Data Functions
def load_data():
    try:
        return pd.read_csv("students.csv")
    except FileNotFoundError:
        # If file doesn't exist, return a DataFrame with the correct structure
        return pd.DataFrame(columns=["Roll Number", "Name", "Class", "Marks"])

def save_data(df):
    # Save the DataFrame to the CSV file
    df.to_csv("students.csv", index=False)

# Add Student Function
def add_student():
    roll = roll_var.get()
    name = name_var.get()
    cls = class_var.get()
    marks = marks_var.get()

    # Check for empty fields
    if roll and name and cls and marks:
        try:
            # Validate marks as a number
            marks = float(marks)

            # Load existing data
            df = load_data()

            # Check for duplicate Roll Numbers
            if roll in df["Roll Number"].values:
                messagebox.showwarning("Error", "Roll Number already exists!")
                return

            # Add new student data
            new_row = pd.DataFrame([[roll, name, cls, marks]], columns=df.columns)
            df = pd.concat([df, new_row], ignore_index=True)

            # Save updated data to CSV
            save_data(df)

            messagebox.showinfo("Success", "Student added successfully!")
            # Clear input fields
            roll_var.set("")
            name_var.set("")
            class_var.set("")
            marks_var.set("")
        except ValueError:
            messagebox.showwarning("Error", "Marks must be a valid number!")
    else:
        messagebox.showwarning("Error", "Please fill all fields!")

# GUI Setup
root = tk.Tk()
root.title("Student Management System")

# Input Fields
roll_var = tk.StringVar()
name_var = tk.StringVar()
class_var = tk.StringVar()
marks_var = tk.StringVar()

tk.Label(root, text="Roll Number").grid(row=0, column=0)
tk.Entry(root, textvariable=roll_var).grid(row=0, column=1)

tk.Label(root, text="Name").grid(row=1, column=0)
tk.Entry(root, textvariable=name_var).grid(row=1, column=1)

tk.Label(root, text="Class").grid(row=2, column=0)
tk.Entry(root, textvariable=class_var).grid(row=2, column=1)

tk.Label(root, text="Marks").grid(row=3, column=0)
tk.Entry(root, textvariable=marks_var).grid(row=3, column=1)

# Buttons
tk.Button(root, text="Add Student", command=add_student).grid(row=4, column=0, columnspan=2)

root.mainloop()

def generate_report():
    df = load_data()
    if df.empty:
        print("No data to analyze!")
        return

    df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
    class_avg = df.groupby("Class")["Marks"].mean()

    class_avg.plot(kind="bar", color="skyblue")
    plt.title("Class-wise Average Marks")
    plt.xlabel("Class")
    plt.ylabel("Average Marks")
    plt.show()


# Welcome message
print("Welcome to the Class 12 Project Script!")

# Function to load the CSV file
def load_csv(file_path):
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Load the data
        data = pd.read_csv(file_path)

        # Display the first few rows of the dataset
        print("\nCSV file loaded successfully! Here are the first few rows:")
        print(data.head())
        return data

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except pd.errors.EmptyDataError:
        print("Error: The file is empty. Please provide a valid CSV file.")
    except pd.errors.ParserError:
        print("Error: The file could not be parsed. Ensure it's in a valid CSV format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Function to display a menu
def menu():
    print("\n--- Menu ---")
    print("1. Load CSV File")
    print("2. generate report")
    print("0. Exit")

# Main function
def main():
    while True:
        menu()
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            file_path = input("Enter the path to your CSV file: ")
            load_csv(file_path)
        elif choice == '2':
            print("Generating Report!")
            generate_report()
        else:
            print("Invalid choice. Please try again.")
            

# Run the main function
if __name__ == "__main__":
    main()
