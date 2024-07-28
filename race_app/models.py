from django.db import models

class Race(models.Model):
    date = models.DateField()  # 日付
    location = models.CharField(max_length=100)  # 場所

class Horse(models.Model):
    name = models.CharField(max_length=100)  # 馬名
    age = models.IntegerField()  # 年齢
    weight = models.FloatField()  # 斤量
    odds = models.FloatField()  # オッズ
    popularity = models.IntegerField()  # 人気
    race = models.ForeignKey(Race, on_delete=models.CASCADE)  # レース
    jockey = models.CharField(max_length=100)  # 騎手
    trainer = models.CharField(max_length=100)  # 厩舎
    body_weight = models.IntegerField()  # 馬体重
    body_weight_change = models.IntegerField()  # 馬体重の増減
    