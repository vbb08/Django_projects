import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, State, Iso, Region, Site


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader=csv.reader(fhand)
    next(reader)
# Advance past the header

#Empty out the database
    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()

#Format:
#Year 3
#Lon 4
#lat 5
#area
#Category 7
#state 8
#iso 10
#region 9

    for row in reader:
        print(row)
        cat, created = Category.objects.get_or_create(name=row[7])
        sta, created = State.objects.get_or_create(name=row[8])
        i, created = Iso.objects.get_or_create(name=row[10])
        reg, created = Region.objects.get_or_create(name=row[9])

        try:
            y = int(row[3])
        except:
            y = None

        try:
            lon = float(row[4])
        except:
            lon = None

        try:
            lat = float(row[5])
        except:
            lat = None

        try:
            are = float(row[6])
        except:
            are = None
        site = Site(name=row[0], description=row[1], year=y, longitude = lon, latitude = lat, area_hectares = are, category = cat, state = sta, region = reg, iso = i)
        site.save()