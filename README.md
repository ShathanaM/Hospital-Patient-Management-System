# **Team 3 Project: Hospital Patient Management System using Data Structures and Algorithms**

## **Project Title**

**Hospital Patient Management System using Python, Data Structures, and Kaggle Dataset**

### **Dataset**

**Hospital / Healthcare Dataset (Kaggle)**

**Suggested Datasets:**

* Hospital Patient Records Dataset
* Healthcare Dataset
* Medical Appointment No Shows Dataset

**Sample Columns:**

* Patient ID
* Patient Name
* Age
* Gender
* Disease
* Doctor
* Department
* Admission Date
* Discharge Date
* Priority Level
* Status

---

# Step 1: Problem Statement

Hospitals handle hundreds of patient records daily. Managing patient registration, emergency cases, appointments, treatment history, and discharge records requires efficient data structures and algorithms.

Develop a **Hospital Patient Management System** using **DSA concepts** to efficiently manage patient information and hospital operations.

---

# Step 2: Objective

* Load and clean the hospital dataset.
* Manage patient records.
* Handle emergency and regular patient queues.
* Search and sort patient records.
* Display hospital statistics.
* Compare algorithm performance.

---

# Step 3: Download Dataset

1. Open **Kaggle**.
2. Search for **Hospital Patient Dataset** or **Healthcare Dataset**.
3. Download the CSV file.
4. Upload it into Google Colab.

Example file:

```text
hospital_patients.csv
```

---

# Step 4: Import Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import heapq
import time
```

---

# Step 5: Load Dataset

```python
df = pd.read_csv("hospital_patients.csv")
```

Display the first few records.

```python
df.head()
```

---

# Step 6: Explore Dataset

Display:

* Total Patients
* Number of Departments
* Data Types
* Summary Statistics

```python
df.info()
df.describe()
```

---

# Step 7: Data Cleaning

Check missing values.

```python
df.isnull().sum()
```

Fill missing values.

```python
df.fillna("Unknown", inplace=True)
```

Remove duplicate patient records.

```python
df.drop_duplicates(inplace=True)
```

Convert admission/discharge dates to datetime format if needed.

---

# Step 8: Exploratory Data Analysis (EDA)

Analyze:

* Number of Patients
* Patients by Department
* Patients by Disease
* Gender Distribution
* Age Distribution
* Emergency vs Regular Patients

Visualizations:

* Bar Chart
* Pie Chart
* Histogram
* Line Chart

---

# Step 9: Implement Array

Store patient names.

```python
patients = list(df["Patient Name"])
```

Perform:

* Insert Patient
* Delete Patient
* Update Patient
* Display Patients

**Real-world Application:** Patient registration list.

---

# Step 10: Implement Stack

Maintain recently discharged patients.

Operations:

* Push
* Pop
* Peek
* IsEmpty
* Size

Example:

```text
Recently Discharged

Patient C

↓

Patient B

↓

Patient A
```

---

# Step 11: Implement Queue

Manage normal patient registration.

Operations:

* Enqueue Patient
* Dequeue Patient
* Display Queue

Example:

```text
Patient A

↓

Patient B

↓

Patient C
```

---

# Step 12: Implement Circular Queue

Manage appointment slots.

Operations:

* Enqueue
* Dequeue
* Display Queue

**Real-world Application:** Appointment scheduling where completed slots become available again.

---

# Step 13: Implement Priority Queue

Manage emergency patients.

Priority:

```text
Critical

↓

Serious

↓

Normal
```

Operations:

* Add Emergency Patient
* Treat Highest Priority Patient
* Display Priority Queue

---

# Step 14: Implement Deque

Manage ambulance arrivals and departures.

Operations:

* Insert Front
* Insert Rear
* Delete Front
* Delete Rear

---

# Step 15: Implement Singly Linked List

Maintain patient visit history.

Operations:

* Insert Beginning
* Insert End
* Delete Record
* Display History

---

# Step 16: Implement Doubly Linked List

Navigate medical records.

Operations:

* Previous Visit
* Next Visit

Display:

```text
Visit 1 ⇄ Visit 2 ⇄ Visit 3
```

---

# Step 17: Implement Circular Linked List

Create a doctor duty rotation.

```text
Doctor A

↓

Doctor B

↓

Doctor C

↓

Doctor A
```

---

# Step 18: Implement Searching Algorithms

### Linear Search

Search patient by:

* Patient Name
* Patient ID

Display:

* Age
* Disease
* Doctor
* Department

---

### Binary Search

Sort patient IDs.

Search using Binary Search.

Compare execution time with Linear Search.

---

# Step 19: Implement Sorting Algorithms

Sort by:

* Age
* Admission Date
* Patient Name
* Priority Level

Algorithms:

* Bubble Sort
* Selection Sort
* Insertion Sort
* Merge Sort
* Quick Sort

Compare execution times.

---

# Step 20: Implement Hash Table

Store:

```text
Patient ID → Patient Details
```

Example:

```text
P1001

↓

John Kumar
```

Allow instant lookup using Patient ID.

---

# Step 21: Implement Heap

Display:

* Top 10 oldest patients
* Top 10 longest admitted patients
* Top 10 highest priority emergency patients

Use a heap for efficient retrieval.

---

# Step 22: Implement Set

Extract unique:

* Diseases
* Departments
* Doctors

Demonstrate removal of duplicate values.

---

# Step 23: Implement Tree

Represent hospital hierarchy.

```text
Hospital

├── Cardiology

│   ├── Doctor A

│   ├── Doctor B

├── Neurology

│   ├── Doctor C

│   ├── Doctor D

└── Orthopedics

    ├── Doctor E

    └── Doctor F
```

Display the hierarchy using traversal.

---

# Step 24: Implement Graph

Represent referrals between departments.

Example:

```text
Emergency

│

├── Cardiology

├── Neurology

└── ICU
```

Or connect doctors who frequently collaborate.

Visualize using `networkx`.

---

# Step 25: Performance Analysis

Measure execution time for:

* Linear Search
* Binary Search
* Bubble Sort
* Merge Sort
* Quick Sort

Use:

```python
import time
```

Compare algorithm performance.

---

# Step 26: Create Visualizations

Generate:

* Bar Chart → Patients by Department
* Pie Chart → Disease Distribution
* Histogram → Age Distribution
* Line Chart → Monthly Admissions
* Scatter Plot → Age vs Length of Stay

---

# Step 27: Build a Menu-Driven Application

Example:

```text
===== Hospital Patient Management System =====

1. Display Dataset
2. Register Patient
3. Search Patient
4. Sort Patients
5. Patient Registration Queue
6. Appointment Circular Queue
7. Emergency Priority Queue
8. Ambulance Deque
9. Patient History (Linked List)
10. Patient Lookup (Hash Table)
11. Hospital Hierarchy (Tree)
12. Department Graph
13. Top Priority Patients (Heap)
14. Hospital Dashboard
15. Performance Analysis
16. Exit
```

Use a `while True` loop to keep the application running until the user exits.

---

# Step 28: Results

Display:

* Total Patients
* Total Departments
* Most Common Disease
* Average Patient Age
* Highest Priority Patient
* Fastest Searching Algorithm
* Fastest Sorting Algorithm

---

# Step 29: Conclusion

Discuss:

* How DSA improved hospital record management.
* Benefits of queues for patient registration.
* Importance of priority queues in emergency care.
* Fast patient lookup using hash tables.
* Efficient retrieval of critical cases using heaps.
* Insights obtained from the hospital dataset.
* Future enhancements such as online appointment booking, doctor availability prediction, electronic health records (EHR), and AI-assisted patient prioritization.

---

# **DSA Concepts Covered**

| Data Structure / Algorithm                      | Application in the Project                     |
| ----------------------------------------------- | ---------------------------------------------- |
| Array                                           | Patient registration list                      |
| Stack                                           | Recently discharged patients                   |
| Queue                                           | Patient registration                           |
| Circular Queue                                  | Appointment scheduling                         |
| Priority Queue                                  | Emergency patient management                   |
| Deque                                           | Ambulance arrivals/departures                  |
| Singly Linked List                              | Patient visit history                          |
| Doubly Linked List                              | Medical record navigation                      |
| Circular Linked List                            | Doctor duty rotation                           |
| Hash Table                                      | Patient ID lookup                              |
| Set                                             | Unique diseases, doctors, departments          |
| Heap                                            | Highest priority and longest-admitted patients |
| Tree                                            | Hospital department hierarchy                  |
| Graph                                           | Department referrals and doctor collaboration  |
| Linear Search                                   | Search patient records                         |
| Binary Search                                   | Efficient patient ID lookup                    |
| Bubble, Selection, Insertion, Merge, Quick Sort | Sort patient records by age, date, or priority |

This project demonstrates a practical **Hospital Patient Management System** using a real Kaggle healthcare dataset while applying major **Data Structures and Algorithms** in Google Colab.