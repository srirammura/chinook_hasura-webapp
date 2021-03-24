from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
import django_tables2 as tables

router = DefaultRouter()
router.register(r'Artists', views.ArtistsViewSet)
router.register(r'Employees', views.EmployeesViewSet)
router.register(r'Customers', views.CustomersViewSet)
router.register(r'Invoices', views.InvoicesViewSet)
router.register(r'Mediatypes', views.MediaTypesViewSet)
router.register(r'Genres', views.GenresViewSet)
router.register(r'Tracks', views.TracksViewSet)
router.register(r'Playlists', views.PlaylistsViewSet)
router.register(r'Playlisttrack', views.PlaylistTrackViewSet)
router.register(r'Albums', views.AlbumsViewSet)
router.register(r'Invoiceitems', views.InvoiceItemsViewSet)

urlpatterns = [
    path('artists_table/', views.ArtistsTableView.as_view(), name="artists_table"),
    path('employees_table/', views.EmployeesTableView.as_view(), name="employees_table"),
    path('customers_table/', views.CustomersTableView.as_view(), name="customers_table"),
    path('invoices_table/', views.InvoicesTableView.as_view(), name="invoices_table"),
    path('mediatypes_table/', views.MediaTypesTableView.as_view(), name="mediatypes_table"),
    path('genres_table/', views.GenresTableView.as_view(), name="genres_table"),
    path('tracks_table/', views.TracksTableView.as_view(), name="tracks_table"),
    path('playlists_table/', views.PlaylistsTableView.as_view(), name="playlists_table"),
    path('playlisttrack_table/', views.PlaylistTrackTableView.as_view(), name="playlisttrack_table"),
    path('albums_table/', views.AlbumsTableView.as_view(), name="albums_table"),
    path('invoiceitems_table/', views.InvoiceItemsTableView.as_view(), name="invoiceitems_table"),
    path('', include(router.urls))
    ]
