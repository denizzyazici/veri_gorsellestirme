import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import  mplot3d   # 3D grafif için

x = np.random.rand(3, 3) * 10
x = x.round()
print(x)

col = ["A", "B", "C"]
idx = ["X", "Y", "Z"]

x2 = pd.DataFrame(data=x, index=idx, columns=col)
print(x2)

x2 = x2.set_index("A")
print(x2)

x2 = x2.reset_index()
print(x2)

x2.index = idx
print(x2)

print("##########")
###MATPLOTLİB####

veri = np.random.rand(12,1)*10
veri = veri.round()   # tam sayıya yuvarlar
print(veri)

grafik = plt.plot(veri, "red")
plt.title("Başlık")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")
plt.show()

print("#########")


liste1 = [10, 15, 20, 25, 30, 35, 40, 45, 50]
liste2 = [330, 270, 85, 60, 530, 15, 750, 305, 320]

arr1 = np.array(liste1)
arr2 = np.array(liste2)

plt.plot(arr1, arr2, "g")
plt.title("Bu grafiğin başlığı")
plt.xlabel("X Verisi")
plt.ylabel("Y Verisi")
plt.show()


#######


dizi1 = np.linspace(0,100,11) # başlangıç,bitiş,eleman sayısı
print(dizi1)

dizi2 = dizi1 ** 2
print(dizi2)

plt.plot(dizi1, dizi2, "r*-")
plt.show()

print("#########")

#SUBPLOT###

plt.subplot(1, 1, 1)
plt.show()


plt.subplot(2, 1, 1)
plt.show()

diz1 = range(10)
diz2 = range(5, 15)


plt.subplot(1, 2, 1)
plt.plot(diz1, diz2, "b*-")
plt.subplot(1, 2, 2)
plt.plot(diz2, diz1, "y--")
plt.show()

#######
## Figure oluşturmak ve PNG olarak kaydetmek ###
dizi3 = np.linspace(1, 10, 10)
print(dizi3)
dizi4 = dizi3 ** 2
print(dizi4)

fig1 = plt.figure()
ax = fig1.add_axes([0.2,0.2,1,1]) # başka grafiğe göre yatay konum,düşey konum,genişlik.yükseklik
ax.plot(dizi3, dizi4, "r")
plt.show()


fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.7,0.7])
ax2 = fig.add_axes([0.3,0.3,0.3,0.3])

ax1.plot(dizi3,dizi4, "b")
ax1.set_title("Mavi Başlık")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax2.plot(dizi3,dizi4, "r")
ax2.set_title("Kırmızı Başlık")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
plt.show()

#### figure png olarak kaydetme
fig.savefig("Figure.png", dpi=200) # dpi=çözünürlük


##### BAR GRAFİĞİ #####

liste3 = ["X", "Y", "Z", "T"]
liste4 = [10, 20, 15, 5]

plt.bar(liste3,liste4, color="purple", width=0.2)
plt.show()

plt.barh(liste3,liste4, color="purple", height=0.2)
plt.show()

##########
list = [40, 35, 27, 17]
list2 = [10, 20, 15, 5]
x = np.arange(4)  # listenin uzunluğu 4 olduğu için
plt.bar(x, list, color="red", width=0.2)
plt.bar(x, list2, color="purple", width=0.2)
plt.title("BAŞLIK")
plt.xlabel("Yatay Eksen")
plt.ylabel("Düşey Eksen")
plt.show()


x = np.arange(4)  # listenin uzunluğu 4 olduğu için (x = ["X", "Y", "Z", "T"] de yazılabilir)
plt.bar(x, list, color="red", width=0.2)
plt.bar(x, list2, color="purple", width=0.2)
plt.title("BAŞLIK")
plt.xlabel("Yatay Eksen")
plt.ylabel("Düşey Eksen")
plt.xticks(x, ("X", "Y", "Z", "T"))
plt.legend(labels=["kırmızı", "mor"])
plt.show()

plt.bar(x, list, color="red", width=0.2)
plt.bar(x, list2, color="purple", width=0.2)
plt.title("BAŞLIK")
plt.xlabel("Yatay Eksen")
plt.ylabel("Düşey Eksen")
plt.xticks(x, ("X", "Y", "Z", "T"))
plt.yticks(np.arange(0,50,10)) # düey eksenin 0 dan başlayıp 50 ye kadar 10 ar 10 ar gitmesini sağlar
plt.legend(labels=["kırmızı", "mor"])
plt.show()

###### PIE CHART #######

plt.figure(figsize=(8, 8))
x = [15, 35, 35, 15]
y = ["A", "B", "C", "D"]
plt.pie(x, labels=y)
plt.show()


e = [0.2, 0, 0, 0]
plt.pie(x, explode=e, labels=y)
plt.show()


##### HISTOGRAM ####

x = np.random.normal(100, 150, 50) #(merkez,ölçek,sayı miktarı)
x = x.round()
plt.hist(x, color="r")
plt.show()


### SCATTER(DAGILIM GRAFIGI) ####

x = np.random.rand(15, 10)*100
y = np.random.randn(15, 10)*100
plt.scatter(x, y, color="red")

z = np.random.rand(15, 10)*50
t = np.random.randn(15, 10)*50
plt.scatter(z, t, color="black")

plt.show()

#########
x = np.random.rand(15,10)*100
y = np.random.randn(15,10)*100
plt.scatter(x, y, color="red", alpha=0.5)

z = np.random.rand(15, 10)*50
t = np.random.randn(15, 10)*50
plt.scatter(z, t, color="black", alpha=0.5)

plt.show()
#########

arr1 = np.array([1,2,3,5,7])
arr2 = np.array([10,20,30,40,50])

renk = ["black", "red", "pink", "blue", "green"]
boyut = [100,250,500,1000,2000]
plt.scatter(arr1, arr2, color=renk, s=boyut)
plt.colorbar()
plt.show()

####### 3D GRAFİK #####

fig = plt.figure(figsize=(10, 10))   # figsize grafik boyutunu belirler
ax = plt.axes(projection="3d")

z = np.random.rand(10, 3)   # rand 10 a 3 lük bir matris sağlar
x = z * np.random.rand(10, 3)
y = z * np.random.rand(10, 3)

ax.plot_surface(x, y, z, color="red")
plt.title("3 boyutlu grafik")
plt.show()


### satış verisinin analizi ve veri görselleştirme #####

data = pd.read_csv("data.csv")
print(data.head()) # ilk beş veriyi göstermek için
print(data.shape)  # satır, sutün sayısnı gösterir

print(data.isnull().sum()) # not a number ı görmek için

x1 = data["OrderDate"]
y1 = data["Unit Price"]

plt.figure(figsize=(15, 8))
plt.bar(x1, y1)
plt.show()

#######

x1 = range(1, 44)
y1 = data["Unit Price"]

plt.figure(figsize=(15, 8))
plt.bar(x1, y1)
plt.show()

##

x1 = range(1, 44)
y1 = data["Unit Price"]

plt.figure(figsize=(15, 8))
plt.bar(x1, y1, color="purple", width=0.5)
plt.xlabel("Günler")
plt.ylabel("Birim Fiyat")
plt.title("Satışlar")
plt.xticks(np.arange(1, 44, 1))
plt.show()

###

x1 = range(1, 44)
y1 = data["Unit Price"]

plt.figure(figsize=(15, 8))
plt.bar(x1, y1, color="purple", width=0.5)
plt.xlabel("Günler")
plt.ylabel("Birim Fiyat")
plt.title("Satışlar")
plt.xticks(np.arange(1, 44, 1))
plt.plot(x1, y1, color="cyan")
plt.legend(labels="satışlar")
plt.show()

########

satislar = data.groupby("Item")  # item ile unit price arasındaki ilişkiyi gösterir
satislar = satislar.sum()
satislar = satislar.plot()
plt.show()


#######

satislar = data.groupby("Item")  # item ile unit price arasındaki ilişkiyi gösterir
satislar = satislar.sum()
satislar = satislar.plot(kind="bar")
satislar.set_ylabel("Miktar & Birim Fiyat")
plt.show()

