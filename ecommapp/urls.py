from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns=[
    path("",views.home),
    path("register/",views.registration),
    path("login/",views.user_login),
    path("logout/",views.user_logout),
    path('catfilter/<cid>',views.catfilter),
    path('sort/<s>',views.sort),
    path('range',views.range),
    path('productdetail/<pid>',views.productdetail),
    path('addtocart/<pid>',views.addToCart),
    path('viewcart/',views.viewcart),
    path('remove/<cid>',views.removefromcart),
    path('updateqty/<qv>/<cid>',views.updateqty),
    path('placeorder',views.placeorder),
    path('makepayment',views.makepayment)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

