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
5. Faça uma busca pelo ID e traga o Hamster Mike:
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

<h2>Exercício 2 – Mama mia!</h2>

1. Liste/Conte todas as pessoas que tem exatamente 99 anos. Você pode usar um count para indicar a quantidade:
- Comando:
```javascript
db.italians.find({"age": 99}).count()
```
- Resultado:
```javascript
0
```
* * *
2. Identifique quantas pessoas são elegíveis atendimento prioritário (pessoas com mais de 65 anos):
- Comando:
```javascript
db.italians.find({"age": {$gt: 65}}).count()
```
- Resultado:
```javascript
1736
```
* * *
3. Identifique todos os jovens (pessoas entre 12 a 18 anos):
- Comando:
```javascript
db.italians.find({"age": {"$gt": 12, "$lt": 18}}).count()
```
- Resultado:
```javascript
649
```
* * *
4. Identifique quantas pessoas tem gatos, quantas tem cachorro e quantas não tem nenhum dos dois:
- Comando (cada linha responde a uma parte da pergunta, respectivamente):
```javascript
db.italians.find({"cat": {"$exists": true,}}).count()
db.italians.find({"dog": {"$exists": true,}}).count()
db.italians.find({"$and": [{"dog": {"$exists": false}}, {"cat": {"$exists": false}}]}).count()
```
- Resultado:
```javascript
5909
3980
2419
```
* * *
5. Liste/Conte todas as pessoas acima de 60 anos que tenham gato:
- Comando:
```javascript
db.italians.find({"$and": [{"age": {"$gt": 60}}, {"cat": {"$exists": true}}]}).count()
```
- Resultado:
```javascript
1449
```
* * *
6. Liste/Conte todos os jovens com cachorro:
- Comando:
```javascript
db.italians.find({"$and": [{"age": {"$gt": 12, "$lt": 18}}, {"dog": {"$exists": true}}]}).count()
```
- Resultado:
```javascript
251
```
* * *
7. Utilizando o $where, liste todas as pessoas que tem gato e cachorro:
- Comando:
```javascript
db.italians.find({$where: "this.dog && this.cat"}).count()
```
- Resultado:
```javascript
2308
```
* * *
8. Liste todas as pessoas mais novas que seus respectivos gatos:
- Comando:
```javascript
 db.italians.find({$where: "this.cat && this.age > this.cat.age"}).count()
```
- Resultado:
```javascript
5218
```
* * *
9. Liste as pessoas que tem o mesmo nome que seu bichano (gatou ou cachorro):
- Comando:
```javascript
db.italians.find({$where: "(this.cat && this.firstname == this.cat.name) || (this.dog && this.firstname == this.dog.name)"}).count()
```
- Resultado:
```javascript
96
```
* * *
10. Projete apenas o nome e sobrenome das pessoas com tipo de sangue de fator RH negativo:
- Comando:
```javascript
db.italians.find({"bloodType": {"$regex": /\w{1,2}-/i}}).count()
```
- Resultado:
```javascript
4908
```
