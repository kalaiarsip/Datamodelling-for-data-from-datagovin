# datamodelling-for-data-from-datagovin

Datamodelling for Teachers Qualification

Source: 
Collected 3 files from https://data.gov.in/catalog/teachers-gender-academic-qualification-professional-qualification-classes-taught-school?page=2 focused on telengana for 2019-2020 (as xls download)

Downloaded file format (xls), fields:
Academic_Year	State_Code	State_Name	District_Code	District_Name	Block_Code	Block_Name	School_Management_Id	School_Management_Name	School_Category_Id	School_Category_Name	Academic_Qualification_Id	Academic_Qualification_Name	Professional_Qualification_Id	Professional_Qualification_Name	Only_Pre_Primary_Male	Only_Pre_Primary_Female	Pre_Primary_and_Primary_Male	Pre_Primary_and_Primary_Female	Only_Primary_Male	Only_Primary_Female	Primary_and_Upperprimary_Male	Primary_and_Upperprimary_Female	Only_Upperprimary_Male	Only_Upperprimary_Female	Upperprimary_and_Secondary_Male	Upperprimary_and_Secondary_Female	Only_Secondary_Male	Only_Secondary_Female	Secondary_and_Highersecondary_Male	Secondary_and_Highersecondary_Female	Only_Highersecondary_Male	Only_Highersecondary_Female	Total_Teacher	Total_Male	Total_Female

Removed unnecessary data and normalized data structure. see image in folder (datamodel_datagovin_teachers.jpg).

The script takes the clean and combined file (teaching_staff.xls) and pushes it to postgres db. in norm form.
