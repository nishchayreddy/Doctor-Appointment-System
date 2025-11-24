# 5.2 statement.md: Project Statement for Doctor Appointment System

---

## 1.  Problem Statement

The management of appointments in a small clinic or doctor's office often relies on manual processes (e.g., paper records, simple spreadsheets), which are prone to errors such as **double-booking**, **missing patient records**, and **inefficient tracking** of patient-doctor pairings. There is a need for a **simple, reliable, and accessible digital system** to manage the fundamental entities—**Patients**, **Doctors**, and **Appointments**—to ensure smooth administrative operations.

---

## 2. Scope of the Project

The scope of this project is to develop a **console-based application** using **Python** that demonstrates the core functionality of a basic medical appointment management system.

The project will focus on:

* **In-Memory Data Storage:** Data will be stored in Python lists and dictionaries for the duration of the program session (no persistent database).
* **Core CRUD Operations:** Implementing functions for Creating (Add), Reading (View), and Deleting (Cancel) records.
* **Simple User Interface:** Providing a numbered menu for user interaction via the command line.

**The scope explicitly excludes:** User authentication, complex scheduling algorithms, external database integration (SQL/NoSQL), advanced reporting, and graphical user interfaces (GUI).

---

## 3. Target Users

The primary users of this system are the individuals responsible for administrative and scheduling tasks within a medical setting, specifically:

* **Clinic Receptionists / Administrative Staff:** Individuals responsible for registering new patients, updating doctor details, and booking/canceling appointments daily.
* **System Developers/Students:** The project serves as a foundational demonstration of object management and procedural programming logic.

---

## 4. High-Level Features

The application offers the following key capabilities:

| Category | Feature | Description |
| :--- | :--- | :--- |
| **User Management** | Add Patient | Allows administrators to register a new patient with details (Name, Phone, Age, Sex). |
| | Add Doctor | Allows administrators to register a new doctor with professional details (Name, Specialization, Qualification). |
| **Scheduling** | Book Appointment | Facilitates scheduling by requiring the selection of an existing Patient ID and Doctor ID, along with the Date, Time, and Reason for the visit. |
| **Data Retrieval** | View All Appointments | Displays a comprehensive, enumerated list of all currently scheduled appointments, showing the Patient-to-Doctor linkage. |
| **Maintenance** | Cancel Appointment | Allows the cancellation of an appointment by selecting its corresponding number/index from the viewed list. |