from rest_framework import viewsets
import django_tables2 as tables
from . import models
from . import serializers

class ArtistsViewSet(viewsets.ModelViewSet):
    queryset = models.Artists.objects.none()
    serializer_class = serializers.ArtistsSerializer
 
class ArtistsTableView(tables.SingleTableView):
    table_class = models.ArtistsTable
    queryset = models.Artists.objects.all()
    template_name="index.html"

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = models.Employees.objects.none()
    serializer_class = serializers.EmployeesSerializer

class EmployeesTableView(tables.SingleTableView):
    table_class = models.EmployeesTable
    queryset = models.Employees.objects.all()
    template_name="index.html"

class CustomersViewSet(viewsets.ModelViewSet):
    queryset = models.Customers.objects.none()
    serializer_class = serializers.CustomersSerializer

class CustomersTableView(tables.SingleTableView):
    table_class = models.CustomersTable
    queryset = models.Customers.objects.all()
    template_name="index.html"


class InvoicesViewSet(viewsets.ModelViewSet):
    queryset = models.Invoices.objects.none()
    serializer_class = serializers.InvoicesSerializer

class InvoicesTableView(tables.SingleTableView):
    table_class = models.InvoicesTable
    queryset = models.Invoices.objects.all()
    template_name="index.html"


class MediaTypesViewSet(viewsets.ModelViewSet):
    queryset = models.MediaTypes.objects.none()
    serializer_class = serializers.MediaTypesSerializer

class MediaTypesTableView(tables.SingleTableView):
    table_class = models.MediaTypesTable
    queryset = models.MediaTypes.objects.all()
    template_name="index.html"

class GenresViewSet(viewsets.ModelViewSet):
    queryset = models.Genres.objects.none()
    serializer_class = serializers.GenresSerializer

class GenresTableView(tables.SingleTableView):
    table_class = models.GenresTable
    queryset = models.Genres.objects.all()
    template_name="index.html"


class TracksViewSet(viewsets.ModelViewSet):
    queryset = models.Tracks.objects.none()
    serializer_class = serializers.TracksSerializer

class TracksTableView(tables.SingleTableView):
    table_class = models.TracksTable
    queryset = models.Tracks.objects.all()
    template_name="index.html"

class PlaylistsViewSet(viewsets.ModelViewSet):
    queryset = models.Playlists.objects.none()
    serializer_class = serializers.PlaylistsSerializer

class PlaylistsTableView(tables.SingleTableView):
    table_class = models.PlaylistsTable
    queryset = models.Playlists.objects.all()
    template_name="index.html"

class PlaylistTrackViewSet(viewsets.ModelViewSet):
    queryset = models.PlaylistTrack.objects.none()
    serializer_class = serializers.PlaylistTrackSerializer

class PlaylistTrackTableView(tables.SingleTableView):
    table_class = models.PlaylistTrackTable
    queryset = models.PlaylistTrack.objects.all()
    template_name="index.html"


class AlbumsViewSet(viewsets.ModelViewSet):
    queryset = models.Albums.objects.none()
    serializer_class = serializers.AlbumsSerializer

class AlbumsTableView(tables.SingleTableView):
    table_class = models.AlbumsTable
    queryset = models.Albums.objects.all()
    template_name="index.html"


class InvoiceItemsViewSet(viewsets.ModelViewSet):
    queryset = models.InvoiceItems.objects.none()
    serializer_class = serializers.InvoiceItemsSerializer

class InvoiceItemsTableView(tables.SingleTableView):
    table_class = models.InvoiceItemsTable
    queryset = models.InvoiceItems.objects.all()
    template_name="index.html"
