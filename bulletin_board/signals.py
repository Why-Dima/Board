from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User

from .models import Reactions, Ads


@receiver(post_save, sender=Reactions)
def sending_responses(sender, instance, created, **kwargs):

    if created:
        pk = instance.ads_id
        pk_r = instance.id
        user_id = Ads.objects.get(pk=pk).authors_id
        header = Ads.objects.get(pk=pk).header
        reaction = Reactions.objects.get(pk=pk_r)

        title = f'Новый отклик'
        msg = f'На объявление: {header} '\
            f'Содержание: {reaction}'
        email = 'newspost1@yandex.ru'
        user_email = User.objects.get(pk=user_id).email

        send_mail(subject=title, message=msg, from_email=email, recipient_list=[user_email, ])
        print(msg)


