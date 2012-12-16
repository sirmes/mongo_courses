
=========== Mongodb Watch Out Topics ==============

Listed below the topics any developer must be aware when using mogodb

1) 50% of the work is in the driver

	1.1) Mongo servers - All about visibility, so You will tell the driver what mongo servers should be accessed, passing the seed list

	1.2) Reading mode order - This is important because you can aliviate the primary server, since it receives the writes, leaving it as the last option in the seed list

	1.3) Timeouts - Set your application preferences. Btw, there are different timeouts.
		Good source: http://stackoverflow.com/questions/6520439/how-to-configure-mongodb-java-driver-mongooptions-for-production-use

	1.4) W the write confirmation and J the Journalism - W means at what level a write operation was completed (or not). I.e.: Wait by N nodes or majority. And Journalism means the data was written into mongo's journal list (what garantee the data is saved somewhere in disk)

	1.5) Connection pooling is managed by the driver, so don't even try to manage this in the application side

	1.6) If programming language's driver is supported by (found at) api.mongodb.org, the programming language doesn't really matter because all have the same features. If not, you are at your own risk.

	DEMO: Saks Api

2) Queries might take longer if you are not writing them in a mongo way

	2.1) Count operation is bad. Count operation with criteria is a shot in your application heart
	2.2) Use sorting carefully - Use the right index to sort or mongo will skip the indexes (doing a full collection scan)
	2.3) Don't ever use skip. This is extremally expesive to mongoDB
	2.4) Limit is your friend
	2.5) When you specify the fields you want to show/return in/from a query criteria, your queries will be faster
	2.6) Use indexes! Use Explain to make sure your index is being used correct. Even array-fields can have indexes

	DEMO: Enron DB over mongo shell

3) Manipule data cautiously

	3.1) Upsert - Update or insert is cool and works pretty well. You can specify indexes too!
	3.2) Update or delete operations always by the indexes or your application will pay the price. 
	3.3) If you want to remove all, use drop colletion instead of collection-> Delete without criteria. Much faster!
	3.4) Inserts might be slowers when 1) (w=majority, j=1), 2) Heavy I/O indexes are created and 3) Architecture no using sharding
	3.5) If you want to make sure your data was 'stored', look at the W and J settings (Aka Write Concern)

	DEMO: Music DB over Python driver

4) You have big data or high I/O, think (very well) about Replication and Sharding

	4.1) Reads and writes in a smaller chuck of data is always fast. This argument supports the Replication and Sharding
	4.2) Easier to Scale Up and Out as well
	4.3) Shard data by the best index. Not all the time the less granular key is the best index.
		Read Choosing Shard Key: http://docs.mongodb.org/manual/core/sharding-internals/#sharding-internals-shard-keys
	4.4) The developer doesn't need to know about shard keys, sharding locations and any other shard internal
	4.5) The initial setup and the daily operational becomes more complex

	DEMO: TBD

5) Closing thoughts, Questions and Answers

	5.1) MongoDB is a powerful DB, but has its trick things like any other DB in the market
	5.2) If Heavy I/O: Replication && Sharding = true
	5.3) There are other very good NoSQL DBs in the market, like Lucene, Cassandra or if you are in the cloud Dynamo DB.
	5.4) Your turn!