
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.school
students = db.students


#Note: This pgm shoudl run once only
#In case you want to run it again, reload mongodb
#mongoimport -d school -c students < students.js
#
#So be smart, save before you do anything:
#db.students.find().forEach(function(doc){db.students_bkp.insert(doc);});
#
#db.students_bkp.find().forEach(function(doc){db.students.insert(doc);});
#
def find_and_remove():

    print "find, reporting for duty"

    try:
        iter = students.find().sort([('_id', pymongo.ASCENDING)])
 
    except:
        print "ahhhh - Unexpected error:", sys.exc_info()[0]

    sanity = 0
    last_id = -1
    for doc in iter:

        last_id = doc['_id']
        last_score = doc['scores']

        new_score = []
        score = -1
        score_counter = 0
        for item in last_score:
            if item['type'] == 'homework':
                if score == -1:
                    score  = item['score']
                    new_score.append(item)
                elif score < item['score']:
                    new_score[score_counter - 1]['score'] = item['score']
            else:
                new_score.append(item)

            score_counter += 1

        #print "\nupdated id: ", last_id, new_score
        #update document
        students.update({'_id' : last_id}, {'scores': new_score})

        sanity += 1
        #if (sanity > 3):
        #    break

    print "\n\ntotal documents: ", sanity


find_and_remove()

