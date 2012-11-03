
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the students database
db=connection.students
grades = db.grades


#Note: This pgm shoudl run once only
#In case you want to run it again, reload mongodb
#mongoimport -d students -c grades < grades.js
#
#So be smart, save before you do anything:
#db.grades.find().forEach(function(doc){db.grades_bkp.insert(doc);});
#
def find_and_delete():

    print "find, reporting for duty"

    #Adhoc query
    #db.grades.find({"type" : "homework"}).sort({"student_id" : -1, "score" : 1}).limit(10)
    query = {'type':'homework'}

    try:
        iter = grades.find(query).sort([('student_id', pymongo.DESCENDING), ('score', pymongo.ASCENDING)])
 
    except:
        print "ahhhh - Unexpected error:", sys.exc_info()[0]

    sanity = 0
    last_id = -1
    last_student_id = -1
    for doc in iter:
        #print doc

        if doc['student_id'] != last_student_id:
            if last_id != -1:
                #delete lowest grade
                grades.remove({'_id' : last_id})
                print "delete student/id: ", last_student_id, last_id, last_score
            last_id = doc['_id']
            last_student_id = doc['student_id']
            last_score = doc['score']

        sanity += 1
        #if (sanity > 10):
        #    break

    #just to accomodate the last record:
    grades.remove({'_id' : last_id})
    print "delete student/id: ", last_student_id, last_id, last_score

    print "\n\ntotal documents: ", sanity


find_and_delete()

