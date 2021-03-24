
from django.db import models
import django_tables2 as tables

class Artists(models.Model):
    artistid = models.AutoField(db_column='ArtistId', primary_key=True)
    name = models.TextField(db_column='Name',blank=True,null=True)

    class Meta:
        db_table = 'artists'


class ArtistsTable(tables.Table):
    class Meta:
       model=Artists
       template_name = "django_tables2/bootstrap.html"

class Employees(models.Model):
    employeeid = models.AutoField(db_column='EmployeeId', primary_key=True)
    lastname = models.TextField(db_column='LastName')
    firstname = models.TextField(db_column='FirstName')
    title = models.TextField(db_column='Title', blank=True, null=True)
    reportsto = models.ForeignKey('self', db_column='ReportsTo',on_delete=models.SET_NULL, blank=True, null=True)
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)
    hiredate = models.DateTimeField(db_column='HireDate', blank=True, null=True)
    address = models.TextField(db_column='Address', blank=True, null=True)
    city = models.TextField(db_column='City', blank=True, null=True)
    state = models.TextField(db_column='State', blank=True, null=True)
    country = models.TextField(db_column='Country', blank=True, null=True)
    postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)
    phone = models.TextField(db_column='Phone', blank=True, null=True)
    fax = models.TextField(db_column='Fax', blank=True, null=True)
    email = models.TextField(db_column='Email', blank=True, null=True)

    class Meta:
        db_table = 'employees'

class EmployeesTable(tables.Table):
    class Meta:
       model=Employees
       template_name = "django_tables2/bootstrap.html"


class Customers(models.Model):
    customerid = models.AutoField(db_column='CustomerId', primary_key=True)
    firstname = models.TextField(db_column='FirstName')
    lastname = models.TextField(db_column='LastName')
    company = models.TextField(db_column='Company', blank=True, null=True)
    address = models.TextField(db_column='Address', blank=True, null=True)
    city = models.TextField(db_column='City', blank=True, null=True)
    state = models.TextField(db_column='State', blank=True, null=True)
    country = models.TextField(db_column='Country', blank=True, null=True)
    postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)
    phone = models.TextField(db_column='Phone', blank=True, null=True)
    fax = models.TextField(db_column='Fax', blank=True, null=True)
    email = models.TextField(db_column='Email')
    supportrepid = models.ForeignKey(
        Employees, on_delete=models.SET_NULL, db_column='SupportRepId', blank=True, null=True)

    class Meta:
        db_table = 'customers'

class CustomersTable(tables.Table):
    class Meta:
       model=Customers
       template_name = "django_tables2/bootstrap.html"


class Invoices(models.Model):
    invoiceid = models.AutoField(db_column='InvoiceId', primary_key=True)
    customerid = models.ForeignKey(Customers, on_delete=models.SET_NULL,
                                   db_column='CustomerId', null=True)
    invoicedate = models.DateTimeField(db_column='InvoiceDate') 
    billingaddress = models.TextField(db_column='BillingAddress', blank=True, null=True)
    billingcity = models.TextField(db_column='BillingCity', blank=True, null=True)
    billingstate = models.TextField(db_column='BillingState', blank=True, null=True)
    billingcountry = models.TextField(db_column='BillingCountry', blank=True, null=True)
    billingpostalcode = models.TextField(db_column='BillingPostalCode', blank=True, null=True)
    total = models.TextField(db_column='Total')

    class Meta:
        db_table = 'invoices'

class InvoicesTable(tables.Table):
    class Meta:
       model=Invoices
       template_name = "django_tables2/bootstrap.html"



class MediaTypes(models.Model):
    mediatypeid = models.AutoField(db_column='MediaTypeId', primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)

    class Meta:
        db_table = 'media_types'

class MediaTypesTable(tables.Table):
    class Meta:
       model=MediaTypes
       template_name = "django_tables2/bootstrap.html"


class Genres(models.Model):
    genreid = models.AutoField(primary_key=True, db_column='GenreId')
    name = models.TextField(db_column='Name', blank=True, null=True)

    class Meta:
        db_table = 'genres'

class GenresTable(tables.Table):
    class Meta:
       model=Genres
       template_name = "django_tables2/bootstrap.html"


class Tracks(models.Model):
    trackid = models.AutoField(db_column='TrackId', primary_key=True)  
    name = models.TextField(db_column='Name')
    albumid = models.ForeignKey('Albums', db_column='AlbumId',on_delete=models.CASCADE, blank=True, null=True)
    mediatypeid = models.ForeignKey(MediaTypes, on_delete=models.SET_NULL,db_column='MediaTypeId', null=True)
    genreid = models.ForeignKey(Genres, on_delete=models.SET_NULL,db_column='GenreId', blank=True, null=True)
    composer = models.TextField(db_column='Composer', blank=True, null=True)
    milliseconds = models.IntegerField(db_column='Milliseconds')  
    bytes = models.IntegerField(db_column='Bytes', blank=True, null=True)
    unitprice = models.TextField(db_column='UnitPrice')

    class Meta:
        db_table = 'tracks'

class TracksTable(tables.Table):
    class Meta:
       model=Tracks
       template_name = "django_tables2/bootstrap.html"

class Playlists(models.Model):
    playlistid = models.AutoField(db_column='PlaylistId', primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)

    class Meta:
        db_table = 'playlists'

class PlaylistsTable(tables.Table):
    class Meta:
       model=Playlists
       template_name = "django_tables2/bootstrap.html"

class PlaylistTrack(models.Model):
    id = models.AutoField(primary_key=True)
    playlistid = models.ForeignKey(Playlists, on_delete=models.CASCADE, db_column='PlaylistId')
    trackid = models.ForeignKey(Tracks, on_delete=models.CASCADE, db_column='TrackId')

    class Meta:
        db_table = 'playlist_track'
        unique_together = (('playlistid', 'trackid'),)

class PlaylistTrackTable(tables.Table):
    class Meta:
       model=PlaylistTrack
       template_name = "django_tables2/bootstrap.html"

class Albums(models.Model):
    albumid = models.AutoField(db_column='AlbumId', primary_key=True)  
    title = models.TextField(db_column='Title')
    artistid = models.ForeignKey(Artists, on_delete=models.CASCADE, db_column='ArtistId',null=True)

    class Meta:
        db_table = 'albums'

class AlbumsTable(tables.Table):
    class Meta:
       model=Albums
       template_name = "django_tables2/bootstrap.html"


class InvoiceItems(models.Model):
    invoiceitemid = models.AutoField(db_column='InvoiceLineId', primary_key=True)
    invoiceid = models.ForeignKey(Invoices, on_delete=models.CASCADE, db_column='InvoiceId',null=True)
    trackid = models.ForeignKey(Tracks, on_delete=models.SET_NULL, db_column='TrackId', null=True)
    unitprice = models.TextField(db_column='UnitPrice')
    quantity = models.IntegerField(db_column='Quantity')  

    class Meta:
        db_table = 'invoice_items'

class InvoiceItemsTable(tables.Table):
    class Meta:
       model=InvoiceItems
       template_name = "django_tables2/bootstrap.html"

