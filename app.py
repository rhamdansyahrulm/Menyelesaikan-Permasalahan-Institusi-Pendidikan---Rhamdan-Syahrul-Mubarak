import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import streamlit as st
from dict_label import dict_label

from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

st.set_page_config(layout="wide")

st.title('Submission Akhir: Menyelesaikan Permasalahan Institusi Pendidikan')
st.markdown('### Rhamdan Syahrul Mubarak')

#############################################################################################################################
## MACHINE LEARNING
#############################################################################################################################
def predict_student(df):
    preprocessor = joblib.load('feature_scaler.pkl')
    best_rf_classifier = joblib.load('model.sav')
    
    scaled_data = preprocessor.transform(df)
    scaled_df = pd.DataFrame(scaled_data, columns=df.columns).iloc[:, 1:-1]
    
    data_predict = scaled_df.copy()
    result = "Dropout" if best_rf_classifier.predict(data_predict) else "Graduate"
    
    if result == "Dropout" :
        return st.warning("Mahasiswa tersebut berpotensi akan : " +  str(result))
    else :
        return st.success("Mahasiswa tersebut berpotensi akan : " +  str(result))

form_ext = st.expander("Predict Student Condition (Graduate or Dropout)")
form_ext.markdown("#### Student Parameter")

with form_ext.form(key='form_data'):
    # Membagi layout menjadi 2 kolom
    col1, col2 = st.columns(2)

    # Kolom pertama (col1)
    with col1:
        gender = st.selectbox('Gender', dict_label("Gender").values())
        marital_status = st.selectbox('Marital Status', dict_label("Marital_status").values())
        course = st.selectbox('Course', dict_label("Course").values())
        previous_qualification = st.selectbox('Previous Qualification', dict_label("Previous_qualification").values())
        nationality = st.selectbox('Nationality', dict_label("Nacionality").values())
        application_order = st.number_input('Application Order', min_value=1)

    # Kolom kedua (col2)
    with col2:
        daytime_evening_attendance = st.radio('Attendance', dict_label("Daytime_evening_attendance").values())
        debtor_status = st.radio('Debtor Status', ['Yes', 'No'])
        tuition_fees_up_to_date = st.radio('Tuition Fees Up to Date', ['Yes', 'No'])
        scholarship_holder = st.radio('Scholarship Holder', ['Yes', 'No'])
    
    father_col, mother_col = st.columns(2)
    fathers_occupation = father_col.selectbox('Father\'s Occupation', dict_label("occupation").values())
    mothers_occupation = mother_col.selectbox('Mother\'s Occupation', dict_label("occupation").values())
    
    # 1st Semester
    sem_1_col1, sem_1_col2, sem_1_col3 = st.columns(3)
    curricular_units_1st_sem_enrolled = sem_1_col1.number_input('1st Semester Units Enrolled', min_value=0)
    curricular_units_1st_sem_approved = sem_1_col2.number_input('1st Semester Units Approved', min_value=0)
    curricular_units_1st_sem_grade = sem_1_col3.number_input('1st Semester Grade', min_value=0)
    
    # 2nd Semester
    sem_2_col1, sem_2_col2, sem_2_col3 = st.columns(3)
    curricular_units_2nd_sem_enrolled = sem_2_col1.number_input('2nd Semester Units Enrolled', min_value=0)
    curricular_units_2nd_sem_approved = sem_2_col2.number_input('2nd Semester Units Approved', min_value=0)
    curricular_units_2nd_sem_grade = sem_2_col3.number_input('2nd Semester Grade', min_value=0)

    # Tombol untuk submit form
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        predict_form_dict = {
            'Marital_status': dict_label("Marital_status", True)[marital_status],
            'Course': dict_label("Course", True)[course],
            'Previous_qualification': dict_label("Previous_qualification", True)[previous_qualification],
            'Nacionality': dict_label("Nacionality", True)[nationality],
            'Mothers_occupation': dict_label("occupation", True)[mothers_occupation],
            'Fathers_occupation': dict_label("occupation", True)[fathers_occupation],
            'Daytime_evening_attendance': dict_label("Daytime_evening_attendance", True)[daytime_evening_attendance],
            'Gender': dict_label("Gender", True)[gender],
            'Debtor': dict_label("yes_no", True)[debtor_status],
            'Tuition_fees_up_to_date': dict_label("yes_no", True)[tuition_fees_up_to_date],
            'Scholarship_holder': dict_label("yes_no", True)[scholarship_holder],
            'Curricular_units_1st_sem_enrolled': curricular_units_1st_sem_enrolled,
            'Curricular_units_1st_sem_approved': curricular_units_1st_sem_approved,
            'Curricular_units_1st_sem_grade': curricular_units_1st_sem_grade,
            'Curricular_units_2nd_sem_enrolled': curricular_units_2nd_sem_enrolled,
            'Curricular_units_2nd_sem_approved': curricular_units_2nd_sem_approved,
            'Curricular_units_2nd_sem_grade': curricular_units_2nd_sem_grade,
            'Application_order': application_order,
            'Status' : float('NaN')
        }

        predict_form_df = pd.DataFrame([predict_form_dict])
        predict_student(predict_form_df)

#############################################################################################################################
## DATA PREPARE
#############################################################################################################################

data = pd.read_csv("clean_data.csv")

data_actual = data.copy()
data_actual["Status"] = data_actual.apply(lambda row: row["Status"] if row["Enrolled"] else "Enrolled", axis=1)

data_predicted = data[data["Enrolled"]].copy()

#############################################################################################################################
## ACTUAL DATA
#############################################################################################################################

actual_ext = st.expander("Actual Student Condition")
actual_ext.markdown("#### Actual Student Condition")

tabs_name = ["Active", "Graduated", "Dropout"]
active_tabs, graduated_tabs, dropout_tabs = actual_ext.tabs(tabs_name)
active_tabs.dataframe(data_actual[data_actual["Status"] == "Enrolled"].iloc[:, :-2].style)
graduated_tabs.dataframe(data_actual[data_actual["Status"] == "Graduate"].iloc[:, :-2].style)
dropout_tabs.dataframe(data_actual[data_actual["Status"] == "Dropout"].iloc[:, :-2].style)

#############################################################################################################################
## PREDICTED DATA
#############################################################################################################################

predicted_ext = st.expander("Predicted Student Condition")
predicted_ext.markdown("#### Predicted Student Condition")

tabs_name = ["Graduated", "Dropout"]
graduated_tabs, dropout_tabs = predicted_ext.tabs(tabs_name)
graduated_tabs.dataframe(data_predicted[data_predicted["Status"] == "Graduate"].iloc[:, :-2].style)
dropout_tabs.dataframe(data_predicted[data_predicted["Status"] == "Dropout"].iloc[:, :-2].style)