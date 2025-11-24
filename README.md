#  Doctor Appointment System

This repository contains the source code for a simple **Doctor Appointment Management System** implemented in Python.

##  Project Details

| Field | Value |
| :--- | :--- |
| **Project Name** | Doctor Appointment System |
| **Course** | Introduction to Problem Solving and Programming |
| **Submitted By** | N Nishchay Reddy |
| **Registration Number** | 25BAS10058 |
| **Submitted To** | Dr. Adayasha Sahu |
| **Institute** | VIT Bhopal University |
| **Language** | Python 3 |

---

##  Features

The system provides a basic console-based interface for managing patients, doctors, and appointments.

* **Patient Management:** Add new patient records (Name, Phone, Age, Sex).
* **Doctor Management:** Add new doctor records (Name, Specialization, Qualification).
* **Appointment Booking:** Book an appointment by selecting an existing patient and doctor.
* **Appointment Viewing:** Display a list of all scheduled appointments.
* **Appointment Cancellation:** Cancel an existing appointment by its index.

---

##  Psuedocode

1.  **Prerequisites:** Ensure you have **Python 3** installed on your system.
2.  **Save the Code:** Save the provided Python script (e.g., `DoctorAppointmentSystem.py`).
3.  **Execute:** Open your terminal or command prompt, navigate to the directory where you saved the file, and run the command:

    ```bash
    python DoctorAppointmentSystem.py
    ```

4.  **Interact:** Follow the corrected menu prompts:
    * 1: Add Patient
    * 2: Add Doctor
    * 3: Book Appointment
    * 4: View All Appointments
    * **5: Cancel Appointment** (The corrected menu option)
    * **6: Exit** (The corrected menu option)

---

##  Project Structure

The code is organized into three global lists and several functions, all managed by a main loop.

| Component | Description |
| :--- | :--- |
| `patients` (List) | Stores all patient dictionaries. |
| `doctors` (List) | Stores all doctor dictionaries. |
| `appointments` (List) | Stores all appointment dictionaries. |
| `add_patient()` | Function to collect and save new patient data. |
| `add_doctor()` | Function to collect and save new doctor data. |
| `book_appointment()` | Function to create an appointment by linking patient and doctor IDs. |
| `view_appointments()` | Function to display all existing appointments. |
| `cancel_appointment()` | Function to remove an appointment from the list by index. |
| `while True` loop | The main program loop displaying the menu and handling user choice. |

##  Flowchart

+------------------------------------+
|      Doctor Appointment System     |
+-----------------------+------------+
                        |
                        v
              +------------------+
              |   Show Menu      |
              +------------------+
                        |
        -------------------------------------------------
        |          |            |            |          |
        v          v            v            v          v
 +-------------+ +-------------+ +----------------+ +-----------------+ +--------------------+
 | Add Patient | | Add Doctor  | | Book Appointment | View Appointments | Cancel Appointment |
 +------+------+ +------+------+ +---------+--------+ +---------+-------+ +---------+--------+
        |               |                  |                    |                   |
        v               v                  v                    v                   v
+----------------+ +----------------+  +--------------------+ +------------------+ +------------------+
| Input patient  | | Input doctor   |  | Patients list empty? | | Print all        | | Show all        |
| details        | | details        |  +----------+---------+ | appointments      | | appointments     |
+-------+--------+ +-------+--------+             |           +----------+---------+ +---------+--------+
        |                  |                      |                      |                    |
        v                  v                      v                      v                    v
+-------------------+ +--------------------+  +--------------------+ +------------------+ +------------------+
| Save to patients  | | Save to doctors    |  | Doctors list empty? | | Back to Menu     | | Delete selected |
| list              | | list               |  +----------+---------+ +------------------+ | appointment      |
+---------+---------+ +----------+---------+            |                               +---------+--------+
          |                    |                       |                                         |
          v                    v                       v                                         v
   +--------------+    +--------------+   +---------------------------+                   +-------------+
   | Back to Menu |    | Back to Menu |   | Select patient & doctor  |                   | Back to Menu|
   +--------------+    +--------------+   | Enter date, time, reason |                   +-------------+
                                           +------------+--------------+
                                                        |
                                                        v
                                            +--------------------------+
                                            | Save appointment         |
                                            +------------+-------------+
                                                         |
                                                         v
                                                 +--------------+
                                                 | Back to Menu |
                                                 +--------------+

                     +--------------------------------+
                     | If choice = Exit (option 5)    |
                     +--------------------------------+
                                      |
                                      v
                               +--------------+
                               |     End      |
                               +--------------+
