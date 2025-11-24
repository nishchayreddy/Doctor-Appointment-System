patients = []
doctors = []
appointments = []

def add_patient():
    name = input("Enter patient name: ")
    phone = input("Enter phone number: ")
    age = input("Enter patient age: ")
    sex = input("Enter the sex of the patient: ")

    patients.append({
        "name": name,
        "phone": phone,
        "age": age,
        "sex": sex
    })
    print("Patient added successfully.")

def add_doctor():
    name = input("Enter doctor name: ")
    spec = input("Enter specialization: ")
    qualification = input("Enter the qualification of the doctor: ")

    doctors.append({
        "name": name,
        "spec": spec,
        "qualification": qualification
    })
    print("Doctor added successfully.")

def book_appointment():
    if not patients:
        print("No patients available!")
        return
    if not doctors:
        print("No doctors available!")
        return
    
    print("\n--- Patients ---")
    for i, p in enumerate(patients):
        print(i, "-", p["name"])
        
    pid = int(input("Select patient ID: "))
    
    print("\n--- Doctors ---")
    for i, d in enumerate(doctors):
        print(i, "-", d["name"], "-", d["spec"])

    did = int(input("Select doctor ID: "))
    
    date = input("Enter date: ")
    time = input("Enter time: ")
    reason = input("Enter reason for visiting: ")

    appointments.append({
        "patient": patients[pid]["name"],
        "doctor": doctors[did]["name"],
        "date": date,
        "time": time,
        "reason": reason
    })

    print("Appointment booked successfully!")

def view_appointments():
    if not appointments:
        print("\nNo appointments found.")
        return
    
    print("\n------ APPOINTMENTS ------")
    for i, a in enumerate(appointments):
        print(f"{i}. {a['patient']} -> {a['doctor']} on {a['date']} at {a['time']} | Reason: {a['reason']}")
    print("--------------------------")

def cancel_appointment():
    if not appointments:
        print("\nNo appointments to cancel.")
        return
    
    view_appointments()
    idx = int(input("Enter appointment number to cancel: "))

    if 0 <= idx < len(appointments):
        del appointments[idx]
        print("Appointment cancelled successfully.")
    else:
        print("Invalid appointment selection.")


while True:
    print("""
==== Doctor Appointment System ====
1. Add Patient
2. Add Doctor
3. Book Appointment
4. View All Appointments
5. Cancel Appointment
6. Exit
""")

    ch = input("Enter choice: ")

    if ch == "1":
        add_patient()
    elif ch == "2":
        add_doctor()
    elif ch == "3":
        book_appointment()
    elif ch == "4":
        view_appointments()
    elif ch == "5":
        cancel_appointment()
    elif ch == "6":
        print("Exiting...")
        break
    else:
        print("Invalid option! Try again.")
