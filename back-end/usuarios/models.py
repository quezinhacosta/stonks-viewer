from django.db import models

class Transacao(models.Model):
    TIPO_CHOICES = [
        ('expense', 'Gasto fixo'),
        ('extra', 'Gasto extra'),
        ('income', 'Ganho fixo'),
        ('investment', 'Ganho extra'),
        ('other', 'Outro'),
    ]

    data = models.DateField()
    descricao = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.descricao} - {self.valor}"


class MetaFinanceira(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Lembrete(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    data = models.DateField()

    def __str__(self):
        return self.nome
