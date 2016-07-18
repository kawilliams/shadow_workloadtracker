#!/usr/bin/python2.6
import cgi
import cgitb
from modelDB import *
import csv

# Committee


def write_csv(filename):
    with open(filename, 'wb') as csvfile:
        writ = csv.writer(csvfile)
        info = get_committee_info()
        for row in info:
            writ.writerow(row)
    return

def get_committee_info():
    s = Session()
    committees = s.query(Committee).all() 
    print len(committees)
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

    write_csv('CurrentCommitteesStatus.csv')
    
if __name__ == "__main__":
    main()