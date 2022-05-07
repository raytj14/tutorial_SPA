from django.db import models

# Create your models here.
class Idea(models.Model):
    """モデル"""

    class Meta:
        db_table = 'idea'
    
    RANDOM = 'RND'
    PRESET = 'PRE'
    CUSTOM = 'CST'
    
    REMIND_FREQUENCY_CHOICES = [
        (RANDOM, 'おまかせ'),
        (PRESET, 'デフォルト設定'),
        (CUSTOM, 'カスタム'),
    ]

    ACTIVE = 'ACT'
    HIATUS = 'HIA'

    ACTIVITY_STATUS = [
        (ACTIVE, 'アクティブ'),
        (HIATUS, '待機中')
    ]


    idea = models.TextField(verbose_name='アイデア')
    remind = models.CharField(
        verbose_name = '再通知する頻度',
        choices = REMIND_FREQUENCY_CHOICES,
        default = RANDOM,
        max_length = 3,
    )
    status = models.CharField(
        verbose_name = 'ステータス',
        choices = ACTIVITY_STATUS,
        default = ACTIVE,
        max_length = 3,
    )

    def __str__(self):
        return self.idea
