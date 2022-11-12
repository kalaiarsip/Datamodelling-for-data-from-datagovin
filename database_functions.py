import psycopg2


def create_database(cur, conn, dbname):
    command = "drop database if exists "+dbname
    cur.execute(command)
    command = "create database "+dbname
    cur.execute(command)
    conn.close()
    conn = psycopg2.connect("host=127.0.0.1 dbname="+dbname+" user=postgres password=root")
    conn.set_session(autocommit=True) #----------------------------------
    cur = conn.cursor()
    print("Connected to db: ", conn.info.dbname)
    return cur

def drop_database(cur, dbname):
    command = "drop database if exists "+dbname
    cur.execute(command)

def get_cursor():
    conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=root")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    return cur, conn

def get_all_databases(cur):
    sqlQuery = "SELECT datname FROM pg_database WHERE datistemplate = false;";
    # Execute the query statement
    cur.execute(sqlQuery);
    rows = cur.fetchall();
    print("---List of databases:---");
    for row in rows:
        print('%s' %(row[0]));

def create_tables(cur):
    state = """create table if not exists state(
        id int primary key,
        name varchar(30) )"""
    cur.execute(state)

    district = """create table if not exists district(
        id int primary key,
        name varchar(30),
        state_id int references state(id))"""
    cur.execute(district)

    block = """create table if not exists block(
        id int primary key, 
        name varchar(30), 
        district_id int references district(id))""" #foreign key
    cur.execute(block)

    prof_qual = """create table if not exists professional_qualification(
        id int primary key,
        name varchar(100) )"""
    cur.execute(prof_qual)

    acad_qual = """create table if not exists academic_qualification(
        id int primary key,
        name varchar(30) )"""
    cur.execute(acad_qual)

    school_mgmt = """create table if not exists school_management(
        id int primary key,
        name varchar(50) )"""
    cur.execute(school_mgmt)

    school_cat = """create table if not exists school_category(
        id int primary key,
        name varchar(30) )"""
    cur.execute(school_cat)

    teaching_staff = """create table if not exists teaching_staff(
        id serial primary key,
        block_id int references block(id),
        professional_qualification int references professional_qualification(id),
        academic_year char(9),
        school_management int references school_management(id),
        school_category int references school_category(id),
        academic_qualification int references academic_qualification(id),
        total_male_teachers int,
        total_female_teachers int)"""
    cur.execute(teaching_staff)

def insert_values():
    dict={}
    dict['teaching_staff_insert'] = """insert into teaching_staff(block_id, professional_qualification,\
    academic_year, school_management, school_category, academic_qualification, \
    total_male_teachers, total_female_teachers) values(%s,%s,%s,%s,%s,%s,%s,%s)"""
    dict['block_insert'] = """insert into block(id, name, district_id) values(%s, %s, %s)"""
    dict['district_insert'] = """insert into district(id, name, state_id) values(%s,%s,%s)"""
    dict['state_insert'] = """insert into state(id,name) values(%s, %s)"""
    dict['school_management_insert'] = """insert into school_management(id,name) values(%s, %s)"""
    dict['school_category_insert'] = """insert into school_category(id,name) values(%s, %s)"""
    dict['prof_qual_insert'] = """insert into professional_qualification(id,name) values(%s, %s)"""
    dict['acad_qual_insert'] = """insert into academic_qualification(id,name) values(%s, %s)"""
    #print(dict)
    return dict

cur,conn = get_cursor()
cur = create_database(cur, conn, "test_db")
create_tables(cur)
insert_statements=insert_values()

#drop_database(cur, "testing")
#get_all_databases(cur)
#conn.commit()