try:
	a = [0,1,2]
	b = int(input("Masukan nilai : "))
	c = int(input("Masukan index list : "))
	d = a[c]+b
except ValueError:
	print("Masukan bukan integer")
except IndexError:
	print("Index yang dimaksud tidak ada")