from shapely.geometry import Point
import geopandas as gpd
from fiona.crs import from_epsg
import matplotlib.pyplot as plt
import pandas as pd

# Učitavanje shapefajla, granica Jagodine

shapefile_path = r'C:\Users\Tijana\Desktop\Programiranje\Ispit\Granica Jagodina.shp'
granica= gpd.read_file(shapefile_path)

# Provera koordinatnog sistema

granica.crs
print(granica.crs)
granica.crs = from_epsg(6316)
granica.crs
print(granica.crs)


# Prkazivanje Granice Jagodine na karti

granica.plot(color='lightgray', edgecolor='black')
plt.title("Jagodina")
plt.show()

#Ubacivanje tacaka-koordinata, svaka tacka predstavlja jedan turistički objekat

t_1 = Point(7521876, 4869199)
t_2 = Point(7521726, 4869262)
t_3 = Point(7521857, 4868856)
t_4 = Point(7521670, 4868871)
t_5 = Point(7521517, 4870827)
t_6 = Point(7511786, 4870175)
t_7 = Point(7522722, 4877492)
t_8 = Point(7521531, 4870205)
t_9 = Point(7521327, 4870598)

#Kreiranje liste

turističke_lokacije = [(t_1, "Akva Park"), (t_2, "Muzej voštanih figura"),( (t_3, "Đurđevo brdo")), ((t_4, "Zoološki vrt")),
                ((t_5, "Muzej nivne i marginalne umetnosti")),((t_6, "Manastir Jošanica")), ((t_7, "Kočin hrast")), ((t_8, "Zavičajni muzej")), ((t_9, "Centar"))]


prostor= gpd.GeoDataFrame()
prostor['geometry'] = None

for ID, (tacka,naziv) in enumerate(turističke_lokacije):
    prostor.loc[ID, 'geometry'] = tacka
    prostor.loc[ID, 'Naziv tacke'] = naziv

# Računanje distance od Centra grada do turističkih lokacija vazdušnom linijom

rastojanjeC_ZM = t_9.distance(t_8)
rastojanjeC_KH = t_9.distance(t_7)
rastojanjeC_MJ = t_9.distance(t_6)
rastojanjeC_MNiMU = t_9.distance(t_5)
rastojanjeC_ZV = t_9.distance(t_4)
rastojanjeC_ĐB = t_9.distance(t_3)
rastojanjeC_MVF = t_9.distance(t_2)
rastojanjeC_AP = t_9.distance(t_1)

print('Udaljenost od Centra grada do Zavičajnog muzeja je', rastojanjeC_ZM,".")
print('Udaljenost od Centra grada do Kočinog Hrasta je', rastojanjeC_KH,"." )
print('Udaljenost od Centra grada do Manastira Jošanice je', rastojanjeC_MJ, ".")
print('Udaljenost od Centra grada do Muzeja naivne i marginalne umetnosti je', rastojanjeC_MNiMU, ".")
print('Udaljenost od Centra grada do Zoološkog Vrta je', rastojanjeC_ZV,".")
print('Udaljenost od Centra grada do Đurđevog brda je', rastojanjeC_ĐB,".")
print('Udaljenost od Centra grada do Muzeja voštanih figura je',      rastojanjeC_MVF,"." )
print('Udaljenost od Centra grada do Akva Parka je', rastojanjeC_AP,".")

#Provera koordinatnog sistema

prostor.crs
print(prostor.crs)
prostor.crs = from_epsg(6316)
print(prostor.crs)

# Prikazivanje turističkih objekata na karti

prostor.plot(facecolor='red')
plt.title("Turističke lokacije")
plt.show()

# Spajanje granice Jagodine i turističkih objekata

spojeno = pd.concat([prostor.geometry,granica.geometry])

print(spojeno.crs)
print(spojeno)


spojeno.plot(cmap="hsv")
plt.title("Turističke lokacije na teritoriji Grada Jagodina")
plt.show()