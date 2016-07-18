#!/usr/bin/python2.6
import cgi
import cgitb
cgitb.enable()

from modelDB import *
import csv
import jinja2


def write_csv(filename):
    with open(filename, 'wb') as csvfile:
        writ = csv.writer(csvfile)
        info = get_committee_info()
        for row in info:
            writ.writerow(row)
    return

def display_results(display):
    
    # we need an environment and file loding system to load file and
    # work with the templating engine
    templateLoader = jinja2.FileSystemLoader( searchpath="./" )
    templateEnv = jinja2.Environment( loader=templateLoader )

    TEMPLATE_FILE = "./edit_faculty.html"
    template = templateEnv.get_template( TEMPLATE_FILE )
    
    outputText = template.render(updated=display)

    return outputText

def get_committee_info():
    s = Session()
    committees = s.query(Committee).all() 
    
    com_info = []
    for c in committees:
        com_info.append([c.name])
        com_info.append(["Chair: "+c.chair])
        com_info.append(["Contact info: "+c.contactInfo])
        com_info.append(["Type: "+c.committeeType])
        com_info.append(["Description: "+c.description])
        com_info.append(["Member", "Division", "Rank", "Leave Plans", 
                         "Rotation Date"])
        for m in c.members:
            com_info.append([m.faculty.fullname, m.faculty.division, 
                             m.faculty.rank, m.faculty.upcomingLeave, 
                             m.rotationDate])
        com_info.append([""])
    return com_info

def main():
    print "Content-Type: text/html"
    print
 
    outputText = display_results("Katy")
    form = cgi.FieldStorage()
    if form:
        
        com_file = write_csv('CurrentCommitteesStatus.csv')    
        outputText = display_results("Updated")

    else:
        outputText = display_results("")
    print outputText
    
if __name__ == "__main__":
    main()