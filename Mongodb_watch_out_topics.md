
=========== Mongodb Watch Out Topics ==============

Listed below the topics any developer must be aware when using mogodb

1) 50% of the work is in the driver

	1.1) Mongo servers - All about visibility, so You will tell the driver what mongo servers should be accessed, passing the seed list

	1.2) Reading mode order - This is important because you can leave the primary as the last option

	1.3) Timeouts - Don't leave your application hanging 60 seconds (the default) before (when) it fails

	1.4) W the write confirmation and J the Journalism - W means a write operation was completed (or not) at some level (i.e.: wait by N nodes or majority) and Journalism means the data was written into mongo's journal list (what garantee the data is saved somewhere)

	1.5) Connection pooling is managed by the driver, so don't even try to manage this in the application side

	1.6) If programming language's driver is supported (found) @ api.mongodb.org, the programming language doesn't really matter because all have the same features

2) Queries might take longer if you are not writing them in the mongo's way

	2.1) Count operation is bad. Count operation with criteria is a shot in your application heart
	2.2) Use sorting carefully - Use the right index to sort or mongo will skip the indexes (doing a full collection scan)
	2.3) Don't ever use skip. This is extremally expesive to mongo
	2.4) Limit is your friend
	2.5) When you specify the fields you want (aka the keys) in the query criteria, your queries are faster

3) Manipule data cautiously

	3.1) Upsert - Update or insert is cool. You can even specify indexes-keys!
	3.2) Update or delete always using the indexes or your application will pay the price. 
	3.3) If you want to remove all, use drop colletion instead of collection-> Delete without criteria
	3.4) Insert
	3.5) If you want to make sure your data was stored, look at the W and J responses (Aka Write Concern)

4) You have big data, think about Replication and Sharding

