import tkinter as tk
from tkinter import messagebox
import sqlite3
import pandas as pd
from collections import deque
import heapq


# =========================================================
# LOAD DATASET
# =========================================================

df = pd.read_csv("hospital data analysis.csv")

print("Dataset loaded successfully!")
print("Total patients:", len(df))

# Remove duplicates
df.drop_duplicates(inplace=True)


# =========================================================
# DATABASE
# =========================================================

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER PRIMARY KEY,
    age INTEGER,
    gender TEXT,
    condition TEXT,
    procedure TEXT,
    cost REAL,
    length_of_stay INTEGER,
    readmission TEXT,
    outcome TEXT,
    satisfaction REAL
)
""")

conn.commit()


# =========================================================
# IMPORT CSV DATA INTO DATABASE
# =========================================================

cursor.execute("SELECT COUNT(*) FROM patients")
count = cursor.fetchone()[0]

if count == 0:

    for _, row in df.iterrows():

        cursor.execute("""
        INSERT OR IGNORE INTO patients
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row["Patient_ID"],
            row["Age"],
            row["Gender"],
            row["Condition"],
            row["Procedure"],
            row["Cost"],
            row["Length_of_Stay"],
            row["Readmission"],
            row["Outcome"],
            row["Satisfaction"]
        ))

    conn.commit()


# =========================================================
# DSA
# =========================================================

# Array / List
patient_array = list(df["Patient_ID"])


# Queue
patient_queue = deque(patient_array)


# Stack
patient_stack = []


# Priority Queue
priority_queue = []

for _, row in df.iterrows():

    heapq.heappush(
        priority_queue,
        (-row["Cost"], row["Patient_ID"])
    )


# =========================================================
# FUNCTIONS
# =========================================================

def add_patient():

    try:

        patient_id = int(id_entry.get())
        age = int(age_entry.get())
        gender = gender_entry.get()
        condition = condition_entry.get()
        procedure = procedure_entry.get()
        cost = float(cost_entry.get())
        stay = int(stay_entry.get())
        readmission = readmission_entry.get()
        outcome = outcome_entry.get()
        satisfaction = float(satisfaction_entry.get())

    except ValueError:

        messagebox.showerror(
            "Error",
            "Please enter valid values"
        )
        return

    if gender == "" or condition == "":
        messagebox.showerror(
            "Error",
            "Please enter patient details"
        )
        return

    try:

        cursor.execute("""
        INSERT INTO patients
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            patient_id,
            age,
            gender,
            condition,
            procedure,
            cost,
            stay,
            readmission,
            outcome,
            satisfaction
        ))

        conn.commit()

        messagebox.showinfo(
            "Success",
            "Patient added successfully"
        )

        clear_fields()
        view_patients()

    except sqlite3.IntegrityError:

        messagebox.showerror(
            "Error",
            "Patient ID already exists"
        )


def view_patients():

    listbox.delete(0, tk.END)

    cursor.execute(
        "SELECT * FROM patients"
    )

    patients = cursor.fetchall()

    for patient in patients:

        listbox.insert(
            tk.END,
            f"ID: {patient[0]} | "
            f"Age: {patient[1]} | "
            f"Gender: {patient[2]} | "
            f"Condition: {patient[3]} | "
            f"Procedure: {patient[4]} | "
            f"Cost: {patient[5]} | "
            f"Stay: {patient[6]} | "
            f"Readmission: {patient[7]} | "
            f"Outcome: {patient[8]} | "
            f"Satisfaction: {patient[9]}"
        )


def search_patient():

    patient_id = search_entry.get()

    if patient_id == "":
        messagebox.showerror(
            "Error",
            "Enter Patient ID"
        )
        return

    cursor.execute(
        "SELECT * FROM patients WHERE patient_id=?",
        (patient_id,)
    )

    patient = cursor.fetchone()

    listbox.delete(0, tk.END)

    if patient:

        listbox.insert(
            tk.END,
            f"ID: {patient[0]} | "
            f"Age: {patient[1]} | "
            f"Gender: {patient[2]} | "
            f"Condition: {patient[3]} | "
            f"Procedure: {patient[4]} | "
            f"Cost: {patient[5]} | "
            f"Stay: {patient[6]} | "
            f"Readmission: {patient[7]} | "
            f"Outcome: {patient[8]} | "
            f"Satisfaction: {patient[9]}"
        )

    else:

        messagebox.showinfo(
            "Result",
            "Patient not found"
        )


def delete_patient():

    patient_id = search_entry.get()

    if patient_id == "":
        messagebox.showerror(
            "Error",
            "Enter Patient ID"
        )
        return

    cursor.execute(
        "DELETE FROM patients WHERE patient_id=?",
        (patient_id,)
    )

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Patient deleted"
    )

    search_entry.delete(0, tk.END)

    view_patients()


def update_patient():

    patient_id = search_entry.get()

    if patient_id == "":
        messagebox.showerror(
            "Error",
            "Enter Patient ID"
        )
        return

    try:

        cursor.execute("""
        UPDATE patients
        SET age=?,
            gender=?,
            condition=?,
            procedure=?,
            cost=?,
            length_of_stay=?,
            readmission=?,
            outcome=?,
            satisfaction=?
        WHERE patient_id=?
        """, (
            int(age_entry.get()),
            gender_entry.get(),
            condition_entry.get(),
            procedure_entry.get(),
            float(cost_entry.get()),
            int(stay_entry.get()),
            readmission_entry.get(),
            outcome_entry.get(),
            float(satisfaction_entry.get()),
            patient_id
        ))

        conn.commit()

        messagebox.showinfo(
            "Success",
            "Patient updated"
        )

        clear_fields()
        search_entry.delete(0, tk.END)

        view_patients()

    except ValueError:

        messagebox.showerror(
            "Error",
            "Enter valid values"
        )


def clear_fields():

    id_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    condition_entry.delete(0, tk.END)
    procedure_entry.delete(0, tk.END)
    cost_entry.delete(0, tk.END)
    stay_entry.delete(0, tk.END)
    readmission_entry.delete(0, tk.END)
    outcome_entry.delete(0, tk.END)
    satisfaction_entry.delete(0, tk.END)


# =========================================================
# STATISTICS
# =========================================================

def show_statistics():

    total = len(df)

    average_age = df["Age"].mean()
    average_cost = df["Cost"].mean()
    average_stay = df["Length_of_Stay"].mean()
    average_satisfaction = df["Satisfaction"].mean()

    condition = df["Condition"].mode()[0]

    messagebox.showinfo(
        "Hospital Statistics",
        f"Total Patients: {total}\n\n"
        f"Average Age: {average_age:.2f}\n"
        f"Average Cost: {average_cost:.2f}\n"
        f"Average Stay: {average_stay:.2f}\n"
        f"Average Satisfaction: {average_satisfaction:.2f}\n\n"
        f"Most Common Condition: {condition}"
    )


# =========================================================
# SORT PATIENTS BY AGE
# =========================================================

def sort_by_age():

    listbox.delete(0, tk.END)

    cursor.execute("""
    SELECT * FROM patients
    ORDER BY age
    """)

    patients = cursor.fetchall()

    for patient in patients:

        listbox.insert(
            tk.END,
            f"ID: {patient[0]} | "
            f"Age: {patient[1]} | "
            f"Gender: {patient[2]} | "
            f"Condition: {patient[3]} | "
            f"Procedure: {patient[4]} | "
            f"Cost: {patient[5]}"
        )


# =========================================================
# GUI
# =========================================================

root = tk.Tk()

root.title(
    "Hospital Patient Management System"
)

root.geometry("1200x700")


title = tk.Label(
    root,
    text="HOSPITAL PATIENT MANAGEMENT SYSTEM",
    font=("Arial", 20, "bold")
)

title.pack(pady=10)


# =========================================================
# PATIENT DETAILS
# =========================================================

frame = tk.Frame(root)

frame.pack(pady=5)


tk.Label(
    frame,
    text="Patient ID"
).grid(row=0, column=0, padx=5, pady=5)

id_entry = tk.Entry(frame)

id_entry.grid(row=0, column=1)


tk.Label(
    frame,
    text="Age"
).grid(row=0, column=2, padx=5)

age_entry = tk.Entry(frame)

age_entry.grid(row=0, column=3)


tk.Label(
    frame,
    text="Gender"
).grid(row=0, column=4, padx=5)

gender_entry = tk.Entry(frame)

gender_entry.grid(row=0, column=5)


tk.Label(
    frame,
    text="Condition"
).grid(row=1, column=0, padx=5)

condition_entry = tk.Entry(frame)

condition_entry.grid(row=1, column=1)


tk.Label(
    frame,
    text="Procedure"
).grid(row=1, column=2, padx=5)

procedure_entry = tk.Entry(frame)

procedure_entry.grid(row=1, column=3)


tk.Label(
    frame,
    text="Cost"
).grid(row=1, column=4, padx=5)

cost_entry = tk.Entry(frame)

cost_entry.grid(row=1, column=5)


tk.Label(
    frame,
    text="Length of Stay"
).grid(row=2, column=0, padx=5)

stay_entry = tk.Entry(frame)

stay_entry.grid(row=2, column=1)


tk.Label(
    frame,
    text="Readmission"
).grid(row=2, column=2, padx=5)

readmission_entry = tk.Entry(frame)

readmission_entry.grid(row=2, column=3)


tk.Label(
    frame,
    text="Outcome"
).grid(row=2, column=4, padx=5)

outcome_entry = tk.Entry(frame)

outcome_entry.grid(row=2, column=5)


tk.Label(
    frame,
    text="Satisfaction"
).grid(row=3, column=0, padx=5)

satisfaction_entry = tk.Entry(frame)

satisfaction_entry.grid(row=3, column=1)


# =========================================================
# BUTTONS
# =========================================================

button_frame = tk.Frame(root)

button_frame.pack(pady=10)


tk.Button(
    button_frame,
    text="Add Patient",
    command=add_patient,
    width=15
).grid(row=0, column=0, padx=5)


tk.Button(
    button_frame,
    text="View Patients",
    command=view_patients,
    width=15
).grid(row=0, column=1, padx=5)


tk.Button(
    button_frame,
    text="Update",
    command=update_patient,
    width=15
).grid(row=0, column=2, padx=5)


tk.Button(
    button_frame,
    text="Delete",
    command=delete_patient,
    width=15
).grid(row=0, column=3, padx=5)


tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    width=15
).grid(row=0, column=4, padx=5)


tk.Button(
    button_frame,
    text="Statistics",
    command=show_statistics,
    width=15
).grid(row=0, column=5, padx=5)


tk.Button(
    button_frame,
    text="Sort by Age",
    command=sort_by_age,
    width=15
).grid(row=0, column=6, padx=5)


# =========================================================
# SEARCH
# =========================================================

search_frame = tk.Frame(root)

search_frame.pack(pady=5)


tk.Label(
    search_frame,
    text="Search Patient ID:"
).grid(row=0, column=0, padx=5)


search_entry = tk.Entry(search_frame)

search_entry.grid(row=0, column=1, padx=5)


tk.Button(
    search_frame,
    text="Search",
    command=search_patient,
    width=12
).grid(row=0, column=2, padx=5)


# =========================================================
# PATIENT LIST
# =========================================================

listbox = tk.Listbox(
    root,
    width=180,
    height=18
)

listbox.pack(pady=10)


# =========================================================
# START
# =========================================================

view_patients()

root.mainloop()