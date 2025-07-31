stack = []
stack.append("Halo")
stack.append("Selamat")
stack.append("Siang!")

kalimat = " ".join(stack)
print("Kalimat setelah ngetik 3 kata:", kalimat)

stack.pop()  
stack.pop()  

kalimat_tersisa = " ".join(stack)
print("Kalimat setelah undo 2x:", kalimat_tersisa)