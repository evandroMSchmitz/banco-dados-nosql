# Atividade Prática – HBase

## Setup
O para executar os comandos empresentados na resposta siga as instruções da seção **Inicializado e acessando oHBase** apresentada no documento que pode ser acessado via este [link](https://www.dropbox.com/sh/45stbqgbj2nzuy5/AAB8T7F3gEjLzIzKc8Uqh6g2a/Atividades?dl=0&preview=4.+Exercicios+-+HBase.pdf).

## Aquecendo com alguns dados
### Preparando a base
1.Crie a tabela com 2 famílias de colunas:  
  - a. personal-data  
  - b. professional-data
```terminal
create'italians', 'personal-data', 'professional-data'
```
---
2.Importe o arquivo via linha de comando:
Feito download e importação do arquivo _italians.txt_ para a imagem docker para a pasta _/tmp/italians.txt_ e depois executado o comando:
```terminal
hbase shell /tmp/italians.txt
```

### Executando Comandos
1.Adicione mais 2 italianos mantendo adicionando informações como data de nascimento nas informações pessoais e um atributo de anos de experiência nas informações profissionais:
```terminal
put 'italians', '11', 'personal-data:name',  'Genaro Sorrentino'
put 'italians', '11', 'personal-data:city',  'Venesa'
put 'italians', '11', 'personal-data:birthday',  '10/10/1987'
put 'italians', '11', 'professional-data:role',  'Gestao Comercial'
put 'italians', '11', 'professional-data:salary',  '2394'
put 'italians', '12', 'professional-data:experience',  '3'
put 'italians', '12', 'personal-data:name',  'Lorenzo Sorrentino'
put 'italians', '12', 'personal-data:city',  'Pisa'
put 'italians', '12', 'personal-data:birthday',  '14/11/1989'
put 'italians', '12', 'professional-data:role',  'Enfermeiro'
put 'italians', '12', 'professional-data:salary',  '4567'
put 'italians', '12', 'professional-data:experience',  '4'
```
---
2.Adicione o controle de 5 versões na tabela de dados pessoais.
```terminal
alter 'italians', NAME => 'personal-data', VERSIONS => 5
```
---
3.Faça 5 alterações em um dos italianos.
```terminal
put 'italians', '11', 'personal-data:city',  'Pisa'
put 'italians', '11', 'personal-data:city',  'Urbino'
put 'italians', '11', 'personal-data:city',  'Roma'
put 'italians', '11', 'professional-data:salary',  '5000'
put 'italians', '11', 'professional-data:salary',  '6000'
```
---
4.Com o operador get, verifique como o HBase armazenou o histórico.
```terminal
get 'italians', '11', {COLUMN => 'personal-data:city', VERSIONS => 5}
```
---
5.Utilize o scan para mostrar apenas o nome e profissão dos italianos.
```terminal
scan 'italians', {COLUMNS => ['personal-data:name', 'professional-data:role']}
```
---
6.Apague os italianos com row id ímpar.
```terminal
deleteall 'italians', ['1', '3', '5', '7', '9', '11']
```
---
7.Crie um contador de idade 55 para o italiano de row id 5.
```terminal
incr 'italians', '5', 'personal-data:age', 55
```
---
8.Incremente a idade do italiano em 1.
```terminal
incr 'italians', '5', 'personal-data:age'
```
