import streamlit as st

# Streamlit app to display and interact with the student database
st.title("Student Database Viewer")

# Load the student database
import pandas as pd
import numpy as np

# Generate the student database (reusing the function from the first cell)
def generate_student_database(num_records=100000):
	np.random.seed(42)
	student_ids = np.arange(1, num_records + 1)
	names = [f"Student_{i}" for i in student_ids]
	ages = np.random.randint(18, 25, size=num_records)
	departments = np.random.choice(['CSE', 'ECE', 'ME', 'CE', 'EE'], size=num_records)
	cgpas = np.round(np.random.uniform(5.0, 10.0, size=num_records), 2)
	graduation_years = np.random.choice([2022, 2023, 2024, 2025], size=num_records)
	data = {
		'StudentID': student_ids,
		'Name': names,
		'Age': ages,
		'Department': departments,
		'CGPA': cgpas,
		'GraduationYear': graduation_years
	}
	return pd.DataFrame(data)

student_db = generate_student_database()

# Display the first 100 rows of the dataset
st.subheader("Student Dataset")
st.write(student_db.head(100))

# Filter students by department
st.subheader("Filter by Department")
department = st.selectbox("Select Department", student_db['Department'].unique())
filtered_data = student_db[student_db['Department'] == department]
st.write(filtered_data)

# Display statistics
st.subheader("Statistics")
st.write(f"Average CGPA in {department} department: {filtered_data['CGPA'].mean():.2f}")
st.write(f"Number of students in {department} department: {filtered_data.shape[0]}")
