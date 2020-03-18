"""my_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from HR_app import views
urlpatterns = [
        path('admin/', admin.site.urls),
        path('',views.home,name='home'),
        path('candidate_List_delivery/', views.candidate_List_delivery, name='candidate_List_delivery'),
        path('candidate_List1_HR/', views.candidate_List1_HR, name='candidate_List1_HR'),
        path('candidate_List2_BU/', views.candidate_List2_BU, name='candidate_List2_BU'),
        path('candidate_List1_Finance/', views.candidate_List1_Finance, name='candidate_List1_Finance'),

        path('view/<int:id>', views.candidate_view_Delivery, name='candidate_view_Delivery'),
        path('view2/<int:id>', views.candidate_view_HR, name='candidate_view_HR'),
        path('view3/<int:id>', views.candidate_view_BU, name='candidate_view_BU'),
        path('view4/<int:id>', views.candidate_view_Finance, name='candidate_view_Finance'),
        #path('view4/<int:id>', views.candidate_view_Finance, name='candidate_view_Finance'),
        #path('edit/<int:id>', views.edit,name='candidate_edit'),
        path('candidate_update_delivery/<int:id>', views.candidate_update_delivery, name='candidate_update_delivery'),
        path('candidate_update_BU/<int:id>', views.candidate_update_BU, name='candidate_update_BU'),
        path('candidate_update_HR/<int:id>', views.candidate_update_HR, name='candidate_update_HR'),
        path('candidate_update_finance/<int:id>', views.candidate_update_finance, name='candidate_update_finance'),

        path('approve/',views.approve,name='approve'),
        path('disapprove/',views.disapprove,name='disapprove'),

        path('user_logout/',views.user_logout,name='user_logout'),

        path('Login/',views.Login,name='Login'),


        path('password/',views.change_password,name='change_password')


    ]
