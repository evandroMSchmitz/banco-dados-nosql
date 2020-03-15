<h1>Atividade Prática – Neo4j</h1>

<h2>Setup:</h2>
Este exercício foi feito sobre a base movies do Neo4j. 
Para instalar esta base siga os comandos deste [link](https://neo4j.com/developer/example-project/) na seção de **Data Setup**.

<h2>Exercício 1: Retrieving Nodes</h2>

Exercise 1.1: Retrieve all nodes from the database
```terminal
MATCH (n) RETURN n
```
* * *
Exercise 1.2: Examine the schema of your database
```terminal
CALL db.schema.visualization()
```
* * *
Exercise 1.3: Retrieve all Person nodes
```terminal
MATCH (p:Person) RETURN p
```
* * *
Exercise 1.4: Retrieve all Movie nodes
```terminal
MATCH (m:Movie) RETURN m
```

<h2>Exercício 2: Filtering queries using property values</h2>

Exercise 2.1: Retrieve all movies that were released in a specific year
```terminal
MATCH (m:Movie {released:2003}) RETURN m
```
***
Exercise 2.2: View the retrieved results as a table imagem
__Colocar imagem__
***
Exercise 2.3: Query the database for all property keys
```terminal
CALL db.propertyKeys
```
***
Exercise 2.4: Retrieve all Movies released in a specific year, returning their titles
```terminal
MATCH (m:Movie {released:2006}) RETURN m.title
```
***
Exercise 2.5: Display title, released, and tagline values for every Movie node in the graph
```terminal
MATCH (m:Movie) RETURN m.title, m.released, m.tagline
```
***
Exercise 2.6: Display more user-friendly headers in the table
```terminal
MATCH (m:Movie) RETURN m.title AS `movie title`, m.released AS released, m.tagline AS tagLine
```

<h2>Exercício 3: Filtering queries using relationships</h2>

Exercise 3.1: Display the schema of the database
```terminal
CALL db.schema.visualization()
```
***
Exercise 3.2: Retrieve all people who wrote the movie Speed Racer
```terminal
MATCH (p:Person)-[rel:WROTE]->(:Movie {title: 'Speed Racer'}) RETURN p.name
```
***
Exercise 3.3: Retrieve all movies that are connected to the person, Tom Hanks
```terminal
MATCH (m:Movie)<--(:Person {name: 'Tom Hanks'}) RETURN m
```
***
Exercise 3.4: Retrieve information about the relationships Tom Hanks has with the set of movies retrieved earlier
```terminal
MATCH (m:Movie)-[rel]-(:Person {name: 'Tom Hanks'}) RETURN m.title, type(rel)
```
***
Exercise 3.5: Retrieve information about the roles that Tom Hanks acted in
```terminal
MATCH (m:Movie)-[rel:ACTED_IN]-(:Person {name: 'Tom Hanks'}) RETURN m.title, rel.roles
```

<h2>Exercício 4: Filtering queries using the WHERE clause</h2>

Exercise 4.1: Retrieve all movies that Tom Cruise acted in
```terminal
MATCH (p:Person)-[rel:ACTED_IN]->(m:Movie) WHERE p.name = 'Tom Cruise' RETURN m.title
```
***
Exercise 4.2: Retrieve all people that were born in the 70’s
```terminal
MATCH (p:Person) WHERE p.born >= 1970 AND p.born <= 1979 RETURN p.name
```
***
Exercise 4.3: Retrieve the actors who acted in the movie The Matrix who were born after 1960
```terminal
MATCH (p:Person)-[rel:ACTED_IN]->(m:Movie) WHERE p.born > 1960 AND m.title = 'The Matrix' RETURN p.name, p.born AS year
```
***
Exercise 4.4: Retrieve all movies by testing the node label and a property
```terminal
MATCH (m) WHERE m:Movie AND m.released = 2000 RETURN m
```
***
Exercise 4.5: Retrieve all people that wrote movies by testing the relationship between two nodes
```terminal
MATCH (p)-[rel]->(m) WHERE m:Movie AND type(rel) = 'WROTE' AND p:Person RETURN p
```
***
Exercise 4.6: Retrieve all people in the graph that do not have a property
```terminal
MATCH (p) WHERE p:Person AND p.born IS NULL RETURN p.name, p.born
```
***
Exercise 4.7: Retrieve all people related to movies where the relationship has a property
```terminal
MATCH (p)-[rel]->(m) WHERE m:Movie AND rel.rating IS NOT NULL AND p:Person RETURN p.name, m.title, rel.rating
```
***
Exercise 4.8: Retrieve all actors whose name begins with James (Instructions)
```terminal
MATCH (p)-[rel]->(m) WHERE m:Movie AND type(rel) = 'ACTED_IN' AND p:Person AND p.name STARTS WITH 'James' RETURN p.name
```
***
Exercise 4.9: Retrieve all REVIEWED relationships from the graph with filtered results
```terminal
MATCH (:Person)-[rel:REVIEWED]->(m) WHERE m:Movie AND toLower(rel.summary) CONTAINS 'fun' RETURN m.title, rel.rating, rel.summary
```
***
Exercise 4.10: Retrieve all people who have produced a movie, but have not directed a movie
```terminal
MATCH (p:Person)-[:PRODUCED]->(m:Movie) WHERE NOT((p)-[:DIRECTED]->(:Movie)) RETURN p.name, m.title
```
***
Exercise 4.11: Retrieve the movies and their actors where one of the actors also directed the movie
```terminal
MATCH (p1:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(p2:Person) WHERE EXISTS((p2)-[:DIRECTED]->(m)) RETURN  p1.name as Actor, p2.name as `Actor/Director`, m.title as Movie
```
***
Exercise 4.12: Retrieve all movies that were released in a set of years
```terminal
MATCH (m:Movie) WHERE m.released IN [2000, 2004, 2008] RETURN m.title
```
***
Exercise 4.13: Retrieve the movies that have an actor’s role that is the name of the movie
```terminal
MATCH (p:Person)-[rel:ACTED_IN]->(m:Movie) WHERE  m.title in rel.roles RETURN  p.name as Actor, rel.roles as Role, m.title as Movie
```

<h2>Exercício 5: Controlling query processing</h2>

Exercise 5.1: Retrieve data using multiple MATCH patterns.
```terminal
MATCH (p1:Person)-[:ACTED_IN]->(m:Movie)<-[:DIRECTED]-(d:Person), (p2:Person)-[:ACTED_IN]->(m) WHERE p1.name = 'Gene Hackman' RETURN  m.title AS Movie, d.name AS Director, p2.name AS `Co-Actors`
```
***
Exercise 5.2: Retrieve particular nodes that have a relationship.
```terminal
MATCH (follower:Person)-[:FOLLOWS]-(p:Person) WHERE follower.name='James Thompson' RETURN follower, p
```
***
Exercise 5.3: Modify the query to retrieve nodes that are exactly three hops away.
```terminal
MATCH (follower:Person)-[:FOLLOWS*3]-(p:Person) WHERE follower.name='James Thompson' RETURN follower, p
```
***
Exercise 5.4: Modify the query to retrieve nodes that are one and two hops away.
```terminal
MATCH (follower:Person)-[:FOLLOWS*1..2]-(p:Person) WHERE follower.name='James Thompson' RETURN follower, p
```
***
Exercise 5.5: Modify the query to retrieve particular nodes that are connected no matter how many hops are required.
```terminal
MATCH (follower:Person)-[:FOLLOWS*]-(p:Person) WHERE follower.name='James Thompson' RETURN follower, p
```
***
Exercise 5.6: Specify optional data to be retrieved during the query.
```terminal
MATCH (p:Person) WHERE p.name STARTS WITH 'Tom' OPTIONAL MATCH (p)-[:DIRECTED]->(m:Movie) RETURN p
```
***
Exercise 5.7: Retrieve nodes by collecting a list.
```terminal
MATCH (p:Person)-[:ACTED_IN]->(m:Movie) RETURN p.name AS `Actor`, collect(m.title) AS `Movies`
```
***
Exercise 5.8: Retrieve all movies that Tom Cruise has acted in and the co-actors that acted in the same movie by collecting a list
```terminal
MATCH (p1:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]- (p2:Person) WHERE p1.name = 'Tom Cruise' RETURN  m.title AS Movie, collect(p2.name) AS `Co-Actors`
```
***
Exercise 5.9: Retrieve nodes as lists and return data associated with the corresponding lists.
```terminal
MATCH (p:Person)-[:REVIEWED]->(m:Movie) RETURN m.title as movie, count(p) as numReviews, collect(p.name) as reviewers
```
***
Exercise 5.10: Retrieve nodes and their relationships as lists.
```terminal
MATCH (p:Person)-[:DIRECTED]->(m:Movie)<-[:ACTED_IN]-(p2:Person) RETURN p.name as Director, count(p2) as `Actors Number`, collect(p2.name) as `Actors`
```
***
Exercise 5.11: Retrieve the actors who have acted in exactly five movies.
```terminal
MATCH (p:Person)-[:ACTED_IN]->(m:Movie) WITH p, count(p) AS numMovies, collect(m.title) AS movies WHERE numMovies = 5 RETURN p.name as Actor, movies
```
***
Exercise 5.12: Retrieve the movies that have at least 2 directors with other optional data.
```terminal
MATCH (m:Movie) WITH m, size((:Person)-[:DIRECTED]->(m)) AS directors WHERE directors >= 2 OPTIONAL MATCH (p:Person)-[:REVIEWED]->(m) RETURN m.title, p.name
```

<h2>Exercício 6: Controlling results returned</h2>

Exercise 6.1: Execute a query that returns duplicate records.
```terminal
MATCH (m:Movie)<-[:ACTED_IN]-(a:Person) WHERE m.released >=1990 AND m.released < 2000 RETURN m.released, m.title, collect(a.name) AS `Actors`
```
***
Exercise 6.2: Modify the query to eliminate duplication.
```terminal
MATCH (m:Movie)<-[:ACTED_IN]-(a:Person) WHERE m.released >= 1990 AND m.released < 2000 RETURN DISTINCT m.released, collect(m.title), collect(a.name)
```
***
Exercise 6.3: Modify the query to eliminate more duplication.
```terminal
MATCH (m:Movie)<-[:ACTED_IN]-(a:Person) WHERE m.released >= 1990 AND m.released < 2000 RETURN  m.released, collect(DISTINCT m.title), collect(a.name)
```
***
Exercise 6.4: Sort results returned.
```terminal
MATCH (m:Movie)<-[:ACTED_IN]-(a:Person) WHERE m.released >= 1990 AND m.released < 2000 RETURN  m.released, collect(DISTINCT m.title), collect(a.name) ORDER BY m.released DESC
```
***
Exercise 6.5: Retrieve the top 5 ratings and their associated movies.
```terminal
MATCH (m:Movie)<-[rel:REVIEWED]-(a:Person) RETURN  m.title, rel.rating ORDER BY rel.rating DESC LIMIT 5
```
***
Exercise 6.6: Retrieve all actors that have not appeared in more than 3 movies.
```terminal
MATCH (p:Person)-[:ACTED_IN]->(m:Movie) WITH p, count(p) AS numMovies, collect(m.title) AS movies WHERE numMovies <= 3 RETURN p.name as Actor, movies
```

<h2>Exercício 7: Working with Cypher data</h2>

Exercise 7.1: Collect and use lists.
```terminal
MATCH (a:Person)-[:ACTED_IN]->(m:Movie)<-[:PRODUCED]-(p:Person) WITH m, collect(DISTINCT a.name) AS actors, collect(DISTINCT p.name) as producers RETURN m.title, actors, producers ORDER BY size(actors)
```
***
Exercise 7.2: Collect a list.
```terminal
MATCH (a:Person)-[:ACTED_IN]->(m:Movie) WITH  a, collect(m.title) AS movies WHERE size(movies) > 5 RETURN a.name, movies
```
***
Exercise 7.3: Unwind a list.
```terminal
MATCH (a:Person)-[:ACTED_IN]->(m:Movie) WITH  a, collect(m.title) AS movies WHERE size(movies) > 5 WITH a, movies UNWIND movies AS movie RETURN a.name, movie
```
***
Exercise 7.4: Perform a calculation with the date type.
```terminal
MATCH (m:Movie)<-[:ACTED_IN]-(actor:Person {name: 'Tom Hanks'}) WHERE exists(actor.born) AND exists(m.released) WITH m, date().year - m.released as yearsPassed, m.released - actor.born as ageTom RETURN m.title, m.released, yearsPassed, ageTom ORDER BY yearsPassed
```

<h2>Exercício 8 – Creating nodes</h2>

Exercise 8.1: Create a Movie node.
```terminal
CREATE(:Movie{title: 'Forrest Gump'})
```
***
Exercise 8.2: Retrieve the newly-created node.
```terminal
MATCH (m:Movie {title: 'Forrest Gump'}) RETURN m
```
***
Exercise 8.3: Create a Person node.
```terminal
CREATE(:Person{name: 'Robin Wright'})
```
***
Exercise 8.4: Retrieve the newly-created node.
```terminal
MATCH (p:Person) WHERE p.name = 'Robin Wright' RETURN p
```
***
Exercise 8.5: Add a label to a node.
```terminal
MATCH (m:Movie) WHERE m.released < 2010 SET m:OlderMovie RETURN m
```
***
Exercise 8.6: Retrieve the node using the new label.
```terminal
MATCH (m:OlderMovie) RETURN m.title, m.released
```
***
Exercise 8.7: Add the Female label to selected nodes.
```terminal
MATCH (p:Person) WHERE p.name STARTS WITH 'Robin' SET p:Female RETURN DISTINCT labels(p)
```
***
Exercise 8.8: Retrieve all Female nodes.
```terminal
MATCH (p:Female) RETURN p
```
***
Exercise 8.9: Remove the Female label from the nodes that have this label.
```terminal
MATCH (p:Person) WHERE p.name STARTS WITH 'Robin' REMOVE p:Female RETURN DISTINCT labels(p)
```
***
Exercise 8.10: View the current schema of the graph.
```terminal
CALL db.schema.visualization()
```
***
Exercise 8.11: Add properties to a movie.
```terminal
MATCH(m:Movie) 
WHERE m.title = 'Forrest Gump' 
SET m.released = 1994, m.lengthInMinutes = 142, m.tagline = 'Life is like a box of chocolates…​you never know what you’re gonna get.',
m:OlderMovie
RETURN m
```
***
Exercise 8.12: Retrieve an OlderMovie node to confirm the label and properties.
```terminal
MATCH(m:OlderMovie) WHERE m.title = 'Forrest Gump' RETURN m
```
***
Exercise 8.13: Add properties to the person, Robin Wright.
```terminal
MATCH(p:Person) WHERE p.name = 'Robin Wright'  SET p.born = 1966, p.birthPlace = 'Dallas' RETURN p
```
***
Exercise 8.14: Retrieve an updated Person node.
```terminal
MATCH(p:Person) WHERE p.name = 'Robin Wright' RETURN p
```
***
Exercise 8.15: Remove a property from a Movie node.
```terminal
MATCH(m:Movie) WHERE m.title = 'Forrest Gump' REMOVE m.lengthInMinutes RETURN m
```
***
Exercise 8.16: Retrieve the node to confirm that the property has been removed.
```terminal
MATCH(m:Movie) WHERE m.title = 'Forrest Gump' RETURN m
```
***
Exercise 8.17: Remove a property from a Person node.
```terminal
MATCH(p:Person) WHERE p.name = 'Robin Wright' REMOVE p.birthPlace RETURN p
```
***
Exercise 8.18: Retrieve the node to confirm that the property has been removed.
```terminal
MATCH(p:Person) WHERE p.name = 'Robin Wright' RETURN p
```

<h2>Exercício 9 – Creating relationships</h2>

Exercise 9.1: Create ACTED_IN relationships.
```terminal
MATCH (m:Movie) WHERE m.title='Forrest Gump' MATCH (a:Person) WHERE a.name='Robin Wright' OR a.name='Tom Hanks' OR a.name='Gary Sinise' CREATE(a)-[rel:ACTED_IN]->(m) RETURN a, m
```
***
Exercise 9.2: Create DIRECTED relationships.
```terminal
MATCH (m:Movie)
WHERE m.title='Forrest Gump'
MATCH (a:Person)
WHERE a.name='Robert Zemeckis'
CREATE(a)-[rel:DIRECTED]->(m)
RETURN a, m
```
***
Exercise 9.3: Create a HELPED relationship.
```terminal
MATCH (a:Person)
WHERE a.name='Tom Hanks'
MATCH (p:Person)
WHERE p.name='Gary Sinise'
CREATE(a)-[rel:HELPED ]->(p)
RETURN a, p
```
***
Exercise 9.4: Query nodes and new relationships.
```terminal
MATCH (p:Person)-[rel]-(m:Movie)
WHERE m.title = 'Forrest Gump'
RETURN p, rel, m
```
***
Exercise 9.5: Add properties to relationships.
```terminal
MATCH (p:Person)-[rel:ACTED_IN]->(m:Movie)
WHERE m.title = 'Forrest Gump'
SET rel.roles =
CASE p.name
	WHEN 'Tom Hanks' THEN ['Forrest Gump']
    WHEN 'Robin Wright' THEN ['Jenny Curran']
    WHEN 'Gary Sinise' THEN ['Lieutenant Dan Taylor']
END
RETURN p, m, rel
```
***
Exercise 9.6: Add a property to the HELPED relationship.
```terminal
MATCH (p:Person)-[rel:HELPED]->(p2:Person)
WHERE p.name = 'Tom Hanks' AND p2.name = 'Gary Sinise'
SET rel.research = 'war history'
RETURN p, p2, rel
```
***
Exercise 9.7: View the current list of property keys in the graph.
```terminal
CALL db.propertyKeys
```
***
Exercise 9.8: View the current schema of the graph.
```terminal
CALL db.schema.visualization
```
***
Exercise 9.9: Retrieve the names and roles for actors.
```terminal
MATCH (p:Person)-[rel:ACTED_IN]->(m:Movie)
WHERE m.title = 'Forrest Gump'
RETURN p.name, rel.roles
```
***
Exercise 9.10: Retrieve information about any specific relationships.
```terminal
MATCH (p:Person)-[rel:HELPED]->(p2:Person)
RETURN p, rel, p2
```
***
Exercise 9.11: Modify a property of a relationship.
```terminal
MATCH (p:Person)-[rel:ACTED_IN]->(m:Movie)
WHERE m.title = 'Forrest Gump' AND p.name = 'Gary Sinise'
SET rel.roles = ['Lt. Dan Taylor']
RETURN p, m, rel
```
***
Exercise 9.12: Remove a property from a relationship.
```terminal
MATCH (p:Person)-[rel:HELPED]->(p2:Person)
WHERE p.name = 'Tom Hanks' AND p2.name = 'Gary Sinise'
REMOVE rel.research
RETURN p, p2, rel
```
***
Exercise 9.13: Confirm that your modifications were made to the graph.
```terminal
MATCH (p:Person)-[rel:HELPED]->(p2:Person)
RETURN p, p2, rel
```

<h2>Exercício 10 – Deleting nodes and relationships</h2>

Exercise 10.1: Delete a relationship.
```terminal
```
***
Exercise 10.2: Confirm that the relationship has been deleted.
```terminal
```
***
Exercise 10.3: Retrieve a movie and all of its relationships.
```terminal
```
***
Exercise 10.4: Try deleting a node without detaching its relationships.
```terminal
```
***
Exercise 10.5: Delete a Movie node, along with its relationships.
```terminal
```
***
Exercise 10.6: Confirm that the Movie node has been deleted.
```terminal
```
