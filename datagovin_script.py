import psycopg2
import pandas as pd
from database_functions import insert_values, get_cursor, create_database, create_tables
xls_filepath ='teaching_staff.xls'

def xls_to_sql(xls_filepath):
    xls = pd.ExcelFile(xls_filepath)
    df_teaching_staff = pd.read_excel(xls, 'teaching_staff')
    df_profqual = pd.read_excel(xls, 'professional_qualification')
    df_schoolmgmt = pd.read_excel(xls, 'school_management')
    df_schoolcat = pd.read_excel(xls, 'school_category')
    df_acadqual = pd.read_excel(xls, 'academic_qualification')
    df_block = pd.read_excel(xls, 'block')
    df_district = pd.read_excel(xls, 'district')
    df_state = pd.read_excel(xls, 'state')
    
    cur,conn = get_cursor()
    cur = create_database(cur, conn, "teachingstaff_datagovin")
    create_tables(cur)    
    insert_statements=insert_values()

    for i,row in df_state.iterrows():
        cur.execute((insert_statements['state_insert']),list(row))
    for i,row in df_district.iterrows():
        cur.execute((insert_statements['district_insert']),list(row))
    for i,row in df_block.iterrows():
        cur.execute((insert_statements['block_insert']),list(row))
    for i,row in df_schoolmgmt.iterrows():
        cur.execute((insert_statements['school_management_insert']),list(row))
    for i,row in df_schoolcat.iterrows():
        cur.execute((insert_statements['school_category_insert']),list(row))
    for i,row in df_profqual.iterrows():
        cur.execute((insert_statements['prof_qual_insert']),list(row))
    for i,row in df_acadqual.iterrows():
        cur.execute((insert_statements['acad_qual_insert']),list(row))
    for i,row in df_teaching_staff.iterrows():
        cur.execute((insert_statements['teaching_staff_insert']),list(row))
    print("inserted values to db")

xls_to_sql(xls_filepath)
