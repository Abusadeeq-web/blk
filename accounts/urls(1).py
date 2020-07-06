from	django.urls	import	path


from	django.contrib.auth	import	views	as	auth_views
from .views import index_view, profile_view, signup_view, activation_sent_view, activate

urlpatterns	=	[


				path('login/',	auth_views.LoginView.as_view(),	name='login'),


				path('logout/',	auth_views.LogoutView.as_view(),	name='logout'),
				
    path('index/', index_view, name="index"),
    path('profile/', profile_view, name="profile"),
    path('signup/', signup_view, name="signup"),
    path('sent/', activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),

]