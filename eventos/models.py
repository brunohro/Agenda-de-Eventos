from django.db import models

class Local(models.Model):
    nome = models.CharField(max_length=100)
    endereço = models.CharField(max_length=100)
    capacidade = models.IntegerField()

class Categoria(models.Model):
    nome = models.CharField(max_length=100)


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    criado_em = models.DateTimeField(auto_now_add=True)
    local = models.ForeignKey(Local, on_delete=models.PROTECT)
    categoria = models.ManyToManyField(Categoria, null=True, blank=True)

    def vagas_restantes(self):
        vagas = self.local.capacidade - self.inscricoes.count()
        return max(0, vagas)

class Atividade(models.Model):
    titulo = models.CharField(max_length=100)
    palestrante = models.CharField(max_length=100)
    horario = models.DateTimeField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='atividades')


class Inscricoes(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    inscrito_em = models.DateTimeField(auto_now_add=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='inscricoes')


class Relatorio(models.Model):
    presentes = models.IntegerField()
    obs = models.TextField(null=True, blank=True)
    evento = models.OneToOneField(Evento, on_delete=models.CASCADE)

