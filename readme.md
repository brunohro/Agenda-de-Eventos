mensagem exibida:

"Não é possível excluir local
A exclusão do objeto local “UFERSA” exigiria a exclusão dos seguintes objetos relacionados protegidos:

Evento: evt3
Evento: evt4
Evento: evt6"

Isso acontece devido ao on_delete=models.PROTECT, pois ele exige que um local só pode ser excluído se os eventos forem excluídos um à um. Dessa forma, protegendo os eventos.