# Generated by Django 5.1.7 on 2025-03-15 04:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencias',
            name='idUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuarios'),
        ),
        migrations.AlterField(
            model_name='canalservicio',
            name='idUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuarios'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='idUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuarios'),
        ),
        migrations.AlterField(
            model_name='motivotransaccion',
            name='idUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuarios'),
        ),
        migrations.AlterField(
            model_name='tipocliente',
            name='idUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuarios'),
        ),
        migrations.AlterField(
            model_name='tipotransaccion',
            name='idUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuarios'),
        ),
        migrations.AlterField(
            model_name='transacciones',
            name='idUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuarios'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='idUsuarioRegistro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.usuarios'),
        ),
    ]
