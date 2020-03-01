<h1>Atividade Prática – MongoDB</h1>

<h2>Exercício 1 - Aquecendo com os pets</h2>

1. Adicione outro Peixe e um Hamster com nome Frodo:
- Comando:
```javascript
db.pets.insert([{name: "Frodo", species: "Peixe"}, {name: "Frodo", species:"Hamster"}])
```
- Resultado:
```javascript
BulkWriteResult({
        "writeErrors" : [ ],
        "writeConcernErrors" : [ ],
        "nInserted" : 2,
        "nUpserted" : 0,
        "nMatched" : 0,
        "nModified" : 0,
        "nRemoved" : 0,
        "upserted" : [ ]
})
```
* * *
2. Faça uma contagem dos pets na coleção:
- Comando:
```javascript
db.pets.count()
```
- Resultado:
```javascript
8
```
* * *
3. Retorne apenas um elemento o método prático possível:
- Comando:
```javascript
db.pets.findOne()
```
- Resultado:
```javascript
{
        "_id" : ObjectId("5e5b9dcb63fad5d4dacd1db1"),
        "name" : "Mike",
        "species" : "Hamster"
}
```
* * *
4. Identifique o ID para o Gato Kilha:
- Comando:
```javascript
db.pets.find({"name": "Kilha", "species": "Gato"}, {_id: 1})
```
- Resultado:
```javascript
{ "_id" : ObjectId("5e5b9de663fad5d4dacd1db3") }
```
* * *
5. Faça uma busca pelo ID e traga o Hamster Mike: Fazer
- Comando:
```javascript
db.pets.find({"_id": ObjectId("5e5b9dcb63fad5d4dacd1db1")})
```
- Resultado:
```javascript
{ "_id" : ObjectId("5e5b9dcb63fad5d4dacd1db1"), "name" : "Mike", "species" : "Hamster" }
```
* * *
6. Use o find para trazer todos os Hamsters:
- Comando:
```javascript
db.pets.find({"species": "Hamster"})
```
- Resultado:
```javascript
{ "_id" : ObjectId("5e5b9dcb63fad5d4dacd1db1"), "name" : "Mike", "species" : "Hamster" }
{ "_id" : ObjectId("5e5ba3d663fad5d4dacd1dba"), "name" : "Frodo", "species" : "Hamster" }
```
* * *
7. Use o find para listar todos os pets com nome Mike:
- Comando:
```javascript
db.pets.find({"name": "Mike"})
```
- Resultado:
```javascript
{ "_id" : ObjectId("5e5b9dcb63fad5d4dacd1db1"), "name" : "Mike", "species" : "Hamster" }
{ "_id" : ObjectId("5e5b9df763fad5d4dacd1db4"), "name" : "Mike", "species" : "Cachorro" }
```
* * *
8. Liste apenas o documento que é um Cachorro chamado Mike:
- Comando:
```javascript
db.pets.find({"name": "Mike", "species": "Cachorro"})
```
- Resultado:
```javascript
{ "_id" : ObjectId("5e5b9df763fad5d4dacd1db4"), "name" : "Mike", "species" : "Cachorro" }
```
