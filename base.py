#function untuk menyimpan data
def menyimpan_biodata(nama, asal, tanggal):
	file = open("database.txt","a+")
	data = file.write("nama saya adalah: %s\n"%(nama))
	data = file.write("saya berasal dari: %s\n"%(asal))
	data = file.write("saya lahir pada: %s\n"%(tanggal))
	
#function tampilkan semua data
def tampilkan_semua_biodata(nama, asal, tanggal):
	file = open("database.txt","r")
	print("==menampilkan biodata==")
	print(file.read())
	
# fungsi untuk pilihan	
def option():
	print("pilih salah satu dari tiga functionlitas berikut:")
	print("1. menyimpan biodata")
	print("2. tampilkan semua biodata")
	print("3. keluar dari program")
	pilihan = int(input("masukan pilihan anda:"))
	return pilihan
	
nama = str(input("masukan nama: "))
asal = str(input("masukan asal: "))
tanggal = str(input("masukan tanggal: "))


#main program	
pilihan = True
while(pilihan<3):
	pilihan = option()
	if(pilihan==1):
		file=open("database.txt","a+")
		data=file.write("nama: %s\n" %(nama))
		file=open("database.txt","a+")
		data=file.write("asal: %s\n" %(asal))
		file=open("database.txt","a+")
		data=file.write("tanggal: %s\n" %(tanggal))
		print("==menyimpan biodata==")
		
	elif(pilihan==2):
		file=open("database.txt","r")
		print("==menyimpan biodata==")
		print(file.read())
		
	else:
		print("bye bye")