
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the music database
db=connection.music
images = db.images
albums = db.albums


#Note: This pgm shoudl run once only
#In case you want to run it again, reload mongodb
#
#mongoimport --host localhost --db music --collection albums --type json --file albums.json --drop
#mongoimport --host localhost --db music --collection images --type json --file images.json --drop
#
def find_and_remove():

    print "find, reporting for duty"

    try:
        iter = images.find().sort([('_id', pymongo.ASCENDING)])
 
    except:
        print "ahhhh - Unexpected error:", sys.exc_info()[0]

    sanity_good_image = 0
    sanity_orphan_image = 0
    for doc in iter:

        last_id = doc['_id']

        #Query albums to confirm the image is being used 
        query = {'images' : {'$all' : [last_id]}}
        #print "\nQuery: " , query

        album = albums.find_one(query)
        if album:
            sanity_good_image += 1
            #print "Image good: ", last_id
        else:
            #Orphan needs to be deleted
            sanity_orphan_image += 1
            print "Image orphan: ", last_id
            images.remove({'_id': last_id})


        #if (sanity_orphan_image > 3) or (sanity_good_image > 3):
        #    break

    print "\n\ntotal good documents: ", sanity_good_image, ", total orphans", sanity_orphan_image


find_and_remove()

