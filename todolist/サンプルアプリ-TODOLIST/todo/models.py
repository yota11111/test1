from django.db import models  # 最初はこれだけ

# Create your models here.
class Todo(models.Model):
    # ここを自分で記載
    title = models.CharField("タスク", max_length=30)
    content   = models.CharField("内容", max_length=500, null=True)
    term  = models.DateField("期限",null=True)

    # ここを自分で記載
    def __str__(self):
        return self.title
