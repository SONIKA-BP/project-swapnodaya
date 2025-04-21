import sqlite3

def generate_report():
    conn = sqlite3.connect('db/hireme.db')
    cursor = conn.cursor()

    # Fetching all required data
    jobsdata = cursor.execute('SELECT * FROM jobs').fetchall()
    appliedData = cursor.execute('SELECT * FROM student_applications').fetchall()
    studentData = cursor.execute('SELECT * FROM students').fetchall()

    conn.close()

    report_data = []
    
    # Loop through all applications and match with student and job data
    for app in appliedData:
        student = next((s for s in studentData if s[0] == app[1]), None)
        job = next((j for j in jobsdata if j[0] == app[2]), None)
        
        # If student and job are found, append the data to report
        if student and job:
            report_data.append({
                'student_name': student[1],
                'college': student[3],
                'job_role': job[1],
                'company': job[2],
                'package': job[3],
                'status': app[3]
            })
    
    return report_data
