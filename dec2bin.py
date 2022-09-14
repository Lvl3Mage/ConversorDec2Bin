def dec2bin(numero_decimal, numero_bits):
	numero_binario = bin(numero_decimal)
	
	if numero_decimal >= 0
		numero_binario = numero_binario[2:len(numero_binario)]
		while len(numero_binario) < numero_bits:
			numero_binario = "0" + numero_binario
	else:
		numero_binario = numero_binario[3:len(numero_binario)]
		while len(numero_binario) < numero_bits:
			numero_binario = "1" + numero_binario
	return numero_binario
if __name__ == "__main__":
	numero_decimal = int(input("Escribe el numero en decimal que quieres convertir: "))
	minLength = len(bin(numero_decimal))-2
	print(minLength)
	numero_bits = int(input("Cuantos bits tendra el numero binario (min to fit is " + str(minLength) +"): " ))
	numero_binario = dec2bin(numero_decimal, numero_bits)
	print(numero_binario)
