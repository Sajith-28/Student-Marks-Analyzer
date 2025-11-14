# 📊 Student Marks Analyzer

A simple and interactive Streamlit web app that allows users to input student marks, calculate the average, and identify students who scored above average.

## 🚀 Features

- Dynamic input fields based on the number of students
- Calculates the average mark
- Highlights students who scored above the average
- Clean and intuitive user interface

## 🛠️ Technologies Used

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)

## 📦 Installation

1. **Clone the repository:**

```bash
   git clone https://github.com/your-username/student-marks-analyzer.git
   cd student-marks-analyzer
```
## Create a virtual environment 
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## - Install Streamlit
```
pip install streamlit
```

## Run the app using Streamlit:
```
streamlit run app.py
```

## Project Structurestudent-marks-analyzer/
```
│
├── app.py              # Main Streamlit application
├── README.md           # Project documentation
└── requirements.txt    # Optional: list of dependencies
📸 ScreenshotsApp Screenshot✍️ Author- Your Name – your-website.com  GitHub
📄 LicenseThis project is licensed under the MIT License - see the LICENSE file for details.
Let me know if you'd like help generating the `requirements.txt` file or customizing the author section!
```
## Program :
```
import streamlit as st

st.title("Student Marks Analyzer")

st.write("Enter the marks of students (minimum 1 student).")

# Number of students input
num_students = st.number_input("How many students?", min_value=1, step=1)

marks = []

# Dynamically generate input fields
for i in range(int(num_students)):
    mark = st.number_input(f"Enter mark of student {i+1}:", min_value=0.0, step=1.0)
    marks.append(mark)

# Calculate when button is clicked
if st.button("Calculate"):
    average = sum(marks) / len(marks)
    
    st.subheader(f"Average Mark = {average}")

    st.write("### Students with marks above average:")
    found = False
    
    for i, m in enumerate(marks):
        if m > average:
            st.write(f"Student {i+1}: {m}")
            found = True

    if not found:
        st.write("No student scored above average.")
```
## Screenshots:

<img width="575" height="685" alt="image" src="https://github.com/user-attachments/assets/7bed86a5-5f75-4876-acb5-6e7cef38e251" />


## 
Author Name: SAJITH AHAMED F



