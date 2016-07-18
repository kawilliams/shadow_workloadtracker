#!/usr/bin/python2.6
import cgi
import cgitb
import os
import jinja2
import log_tb
cgitb.enable()

from modelDB import *
from check import *
from update_faculty import *


# Global variable that will hold the input name of the form we will process and
# some other global variables
PASSWORD_INPUT = "password"
CSV_NAME = "FacultyInformation.csv"
FILE_INPUT = "file"

def main():

    print "Content-Type: text/html"
    print
    
    
    form = cgi.FieldStorage()
    
    password_form = str(form.getvalue(PASSWORD_INPUT)).strip()
    
    if check_password(password_form):
        file_obj = form[FILE_INPUT]
        if file_obj.filename:
            #remove previous file and save the new one
            os.remove(CSV_NAME)
            open(CSV_NAME, 'wb').write(file_obj.file.read())
            
            # update db using the new csv
            new_list = make_faculty_fromCSV(CSV_NAME)
            msg = update_facultyInfo(new_list)
            
            msg += "<br>Upload sucessful"
        else:
            msg = "No file was uploaded!"
            
        
        print "<html><body>"
        print "<h4>",msg,"</h4>"
        
        print'''
        <button type="button" onclick="goback()">Go Back</button>
        <a id="redirect" href="write_com_csv.cgi" hidden>
        <script>
        function goback(){ document.getElementById('redirect').click(); };
        </script>
        </body>
        </html>
        '''        

    else:
        print '''
        <html>

        <body onload="loading()">
        
        <a id="redirect" href="wrong_password.html" hidden>
        
        
        <script>
        function loading(){
           document.getElementById('redirect').click();
        }
        </script>
        </body>
        </html>
        '''
        
    
if __name__ == "__main__":
    try:
        main()
        
    except:
        log_tb.log()
        print '''
        <html>
        <body onload="loading()">
        <a id="redirect" href="error.html" hidden>
        <script>
        function loading(){
           document.getElementById('redirect').click();
        }
        </script>
        </body>
        </html>
        '''              