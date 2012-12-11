Quiz: HW 6.1

Which of the following statements are true about MongoDB replication. Check all that apply.

True = The minimum sensible number of voting nodes to a replica set is three.

K False = MongoDB replication is synchronous.

K False = The Mongo shell is capable of attaching to a replica set and automatically failing over.

K False = By default, using the new MongoClient connection class, w=1 and j=1.

K True = The oplog utilizes a capped collection.

>>> Quiz: HW 6.2 - DONE

Let's suppose you have a five member replica set and want to assure that writes are committed to the journal and are acknowledged by at least 3 nodes before you proceed forward. What would be the appropriate settings for w and j?


w=1, j=1

X - w="majority", j=1

w=3, j=0

w=5, j=1

w=1,j=3

>>> Quiz: HW 6.3

Which of the following statements are true about choosing and using a shard key:

False - There must be a index on the collection that starts with the shard key.

K True - Mongo can not enforce unique indexes on a sharded collection other than the shard key itself.

K True - Any update that does not contain the shard key will be sent to all shards.

K False - You can change the shard key on a collection if you desire. <- Changed

>>> Quiz: HW 6.4 - DONE

You have a sharded system with three shards and have sharded the collections "grades" in the "test" database across those shards. The output of sh.status() when connected to mongos looks like this:
mongos> sh.status()
--- Sharding Status --- 
  sharding version: { "_id" : 1, "version" : 3 }
  shards:
	{  "_id" : "s0",  "host" : "s0/localhost:37017,localhost:37018,localhost:37019" }
	{  "_id" : "s1",  "host" : "s1/localhost:47017,localhost:47018,localhost:47019" }
	{  "_id" : "s2",  "host" : "s2/localhost:57017,localhost:57018,localhost:57019" }
  databases:
	{  "_id" : "admin",  "partitioned" : false,  "primary" : "config" }
	{  "_id" : "test",  "partitioned" : true,  "primary" : "s0" }
		test.grades chunks:
				s1	4
				s0	4
				s2	4
			{ "student_id" : { $minKey : 1 } } -->> { "student_id" : 0 } on : s1 Timestamp(12000, 0) 
			{ "student_id" : 0 } -->> { "student_id" : 2640 } on : s0 Timestamp(11000, 1) 
			{ "student_id" : 2640 } -->> { "student_id" : 91918 } on : s1 Timestamp(10000, 1) 
			{ "student_id" : 91918 } -->> { "student_id" : 176201 } on : s0 Timestamp(4000, 2) 
			{ "student_id" : 176201 } -->> { "student_id" : 256639 } on : s2 Timestamp(12000, 1) 
			{ "student_id" : 256639 } -->> { "student_id" : 344351 } on : s2 Timestamp(6000, 2) 
			{ "student_id" : 344351 } -->> { "student_id" : 424983 } on : s0 Timestamp(7000, 2) 
			{ "student_id" : 424983 } -->> { "student_id" : 509266 } on : s1 Timestamp(8000, 2) 
		{ "student_id" : 509266 } -->> { "student_id" : 596849 } on : s1 Timestamp(9000, 2) 
			{ "student_id" : 596849 } -->> { "student_id" : 772260 } on : s0 Timestamp(10000, 2) 
			{ "student_id" : 772260 } -->> { "student_id" : 945802 } on : s2 Timestamp(11000, 2) 
			{ "student_id" : 945802 } -->> { "student_id" : { $maxKey : 1 } } on : s2 Timestamp(11000, 3) 
If you ran the query
use test
db.grades.find({'student_id':530289})
Which shards would be involved in answering the query?


s0,s1 and s2

s0

X - s1

s2
