### Singleton

Só um objeto de determinado tipo com referência global. 

### Onde usar?

Logging, bancos de dados, spoolers de impressão...
Depende do problema a se resolver. Resolve principalmente conflitos de uso, sincronização...

### Intenções ao usar o Singleton

Garantir a existência de somente um objeto de determinado tipo, controlar acesso concorrente a recursos compartilhados.

### Caracteristica em código

Construtor privado!
Método público que devolve o objeto já criado. 

