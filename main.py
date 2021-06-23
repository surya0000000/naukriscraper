import psycopg2
from flask import Flask, request
from flask import render_template

app=Flask("Job site")

dbconnect=psycopg2.connect("dbname=naukri")

@app.route("/")
def initial():
    cursor=dbconnect.cursor()
    cursor.execute("select count(*) from openings")
    data=cursor.fetchall()
    
    return f"{data}"
    


@app.route("/jobs") #decorator
def jobs():
    cursor=dbconnect.cursor()
    cursor.execute("select title,company_name,jd_text from openings")
    jobs_list=cursor.fetchall()
    ret=[]
    for title,company_name,jd_text in jobs_list:
     item=f"{title}  :::  {company_name}   :::   {jd_text}"
     ret.append(item)
    l="<hr/>".join(ret) 
    return f"{l}"
    
if __name__=="__main__":
    app.run()
