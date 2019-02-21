1. The task was clear and easy to follow along.

2. I spent about 25% of time understanding. Once I got an understanding, I spent 40% designing (choosing programming language, libraries, database, architecture), 20% of time coding, and the remaining 15% testing endpoints and database activity.

3. I chose python because I was familiar with python's handy liibrary for unzipping gzip files. Flask makes setting up endpoints and routes, fun and easy. SQLite requires minimal configuration compared to other SQL oriented databases for setting up a non front-end CRUD application in my honest opinion.  I've also built endpoints with this stack before and it was the most familiar to me although I didn't manage the database before.

4.Yes! the fetchall method provides a large bottleneck in the sense that with large datasets, performance time is very slow. This is more of a bottleneck with SQLite itself. Switching to a heavier SQL-oriented database would most likely mitigate this. Along with this, using a data manipulation like numpy or pandas (or combination of both) would probably help mitigate this bottleneck too rather than strictly iterating with a for loop.

5.This would work with a billion rows but increase the threat of the bottleneck.

6. If I had more time, connfigure this program with a heavier database, create helper/util files to store logic (as opposed to keeping it in the server file), decrease the complexity of a few get methods, write unittests, write more in depth error handling, and switch to a different VM mirroring software.

7. I am confident that under the proper environment, this solution will do exactly what it's supposed to do. I've accounted for all of the methods. Without configuration issues, I'd say I'm confident in the solution.

8. I've sent this in an email to Devon, but I was having some issues getting ubuntu to play nicely with my directories in my VM. I am wrong to assume that you have python and pip installed but ./script.bash will be the one command that get's it running. Other than that, this has been a fun assessment on my part and I hope it's been that way for you!

