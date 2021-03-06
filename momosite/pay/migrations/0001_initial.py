# Generated by Django 2.1.3 on 2018-11-25 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDormInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('住址', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OrdersInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('订单号', models.CharField(max_length=100, unique=True)),
                ('充值类型', models.CharField(max_length=20)),
                ('充值金额', models.FloatField()),
                ('创建时间', models.DateTimeField(auto_now_add=True)),
                ('支付状态', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderSOWInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('学号', models.CharField(max_length=15)),
                ('姓名', models.CharField(max_length=15)),
                ('订单号', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pay.OrdersInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdorminfo',
            name='订单号',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pay.OrdersInfo'),
        ),
    ]
