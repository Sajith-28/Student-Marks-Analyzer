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
