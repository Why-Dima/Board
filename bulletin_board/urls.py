from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import AdsList, AdsCreate, AdsUpdate, AdsDetail, ReactionsList, ReactionsAdd, ReactionsDelete


urlpatterns = [
    path('', AdsList.as_view(), name=''),
    path('create/', AdsCreate.as_view(), name='ads_create'),
    path('create/<int:pk>/', AdsUpdate.as_view(), name='ads_update'),
    path('detail/<int:pk>', AdsDetail.as_view(), name='ads_detail'),
    path('reaction/', ReactionsList.as_view(), name='reactions_list'),
    path('reaction_add/<int:pk>', ReactionsAdd.as_view(), name='reactions_add'),
    path('reaction_delete/<int:pk>', ReactionsDelete.as_view(), name='reactions_delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

